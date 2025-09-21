import sys
import socket
from collections import deque

# ==================================================================================================
# [알고리즘 설명]
# 1. 이 코드는 BFS(너비 우선 탐색)를 기반으로 동작합니다.
#    BFS는 시작점으로부터 거리가 가까운 곳부터 순서대로 탐색하여, 가장 '적은 이동 횟수'로 목표에 도달하는 경로를 찾는데 특화되어 있습니다.
#
# 2. 탐색 전략: "공격 우선, 이후 이동"
#    - BFS 큐에서 현재 위치를 꺼낼 때마다, 가장 먼저 그 위치에서 적 포탑을 공격할 수 있는지 확인합니다.
#    - (핵심) 사거리 3 내에 적 포탑이 있고, 경로상에 다른 장애물(바위, 나무)이 없다면 즉시 '공격' 명령을 내리고 탐색을 종료합니다.
#    - 만약 현재 위치에서 공격할 수 없다면, 상하좌우로 '이동' 가능한 다음 위치를 탐색하여 큐에 추가합니다.
#
# 3. 코드 구조 (woosung.py 기반)
#    - 이동 가능('G', 'S') / 이동 불가('R', 'W', 'T' 등) 타일을 명확하게 세트(set)로 정의하여 코드를 간결하게 만듭니다.
#    - BFS 탐색에 필요한 함수들과 게임 서버와 통신하는 부분으로 나뉘어 있습니다.
# ==================================================================================================


##############################
# 메인 프로그램 통신 변수 정의
##############################
HOST = '127.0.0.1'
PORT = 8747
ARGS = sys.argv[1] if len(sys.argv) > 1 else ''
sock = socket.socket()

##############################
# 메인 프로그램 통신 함수 정의
##############################

# 메인 프로그램 연결 및 초기화
def init(nickname):
    try:
        sock.connect((HOST, PORT))
        init_command = f'INIT {nickname}'
        return submit(init_command)
    except Exception as e:
        print(f'[ERROR] 서버 연결 실패: {e}')
        return None

# 메인 프로그램으로 데이터(명령어) 전송
def submit(string_to_send):
    try:
        send_data = ARGS + string_to_send + ' '
        sock.send(send_data.encode('utf-8'))
        return receive()
    except Exception as e:
        print(f'[ERROR] 데이터 전송 실패: {e}')
        return None

# 메인 프로그램으로부터 데이터 수신
def receive():
    try:
        game_data = (sock.recv(1024)).decode()
        if game_data and game_data[0].isdigit() and int(game_data[0]) > 0:
            return game_data
        close()
        return None
    except Exception as e:
        print(f'[ERROR] 데이터 수신 실패: {e}')
        return None

# 연결 해제
def close():
    try:
        if sock:
            sock.close()
    except Exception as e:
        print(f'[ERROR] 연결 해제 실패: {e}')

##############################
# 입력 데이터 변수 및 파싱 함수
##############################
map_data = [[]]
my_allies = {}
enemies = {}
codes = []

def parse_data(game_data_str):
    game_data_rows = game_data_str.split('\n')
    row_index = 0

    header = game_data_rows[row_index].split(' ')
    map_height, map_width, num_allies, num_enemies, num_codes = map(int, header)
    row_index += 1

    map_data.clear()
    map_data.extend([row.split(' ') for row in game_data_rows[row_index:row_index + map_height]])
    row_index += map_height

    my_allies.clear()
    for i in range(num_allies):
        ally = game_data_rows[row_index + i].split(' ')
        my_allies[ally.pop(0)] = ally
    row_index += num_allies

    enemies.clear()
    for i in range(num_enemies):
        enemy = game_data_rows[row_index + i].split(' ')
        enemies[enemy.pop(0)] = enemy

###################################
# 알고리즘 구현 부분
###################################

# --- 탐색에 필요한 변수 및 함수 정의 ---

# 방향 벡터 (우, 하, 좌, 상) - 인덱스 0:우, 1:하, 2:좌, 3:상
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 각 방향에 맞는 이동/발사 명령어
MOVE_CMDS = {0: "R A", 1: "D A", 2: "L A", 3: "U A"}
FIRE_CMDS = {0: "R F", 1: "D F", 2: "L F", 3: "U F"}

# 맵의 시작('M')과 목표('X') 심볼
START_SYMBOL = 'M'
TARGET_SYMBOL = 'X'

# 이동 가능한 타일과 불가능한 타일 정의 (woosung.py의 아이디어)
WALKABLE = {"G", "S"}  # 일반 땅, 모래는 이동 가능
# 바위, 물, 나무는 이동 불가. (적 포탑 'X'도 이동은 불가) 
BLOCKED_TERRAINS = {"R", "T", "X"} 

# 맵 범위 확인 함수
def is_in_bounds(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

# 일반 포탄 보유 여부 확인 함수
def have_normal_bullet():
    me = my_allies.get('M')
    try:
        # me[2]가 일반 포탄 개수
        return int(me[2]) > 0
    except:
        return False

# --- 핵심 BFS 함수 ---

def find_best_action_path(grid, start, target):
    """
    BFS를 사용하여 목표(적 포탑)를 공격하기 위한 최적의 행동 순서를 찾습니다.
    """
    rows, cols = len(grid), len(grid[0])
    # 큐에는 ((현재 행, 현재 열), [지금까지의 행동 리스트]) 를 저장
    queue = deque([(start, [])])
    # 방문한 위치를 기록하여 무한 루프 방지
    visited = {start}

    while queue:
        (r, c), actions = queue.popleft()

        # 1. (공격 우선) 현재 위치에서 사거리 3 내의 적을 탐색
        for d_idx, (dr, dc) in enumerate(DIRS):
            # 각 방향으로 1~3칸까지 확인
            for dist in range(1, 4):
                nr, nc = r + dr * dist, c + dc * dist

                # 맵을 벗어나면 이 방향으로는 더 이상 탐색 불필요
                if not is_in_bounds(nr, nc, rows, cols):
                    break
                
                # (핵심) 포탄 경로에 장애물(바위, 나무)이 있으면 공격 불가
                if grid[nr][nc] in {"R", "T"}:
                    break

                # 경로상에 장애물이 없고, 목표를 발견했다면
                if (nr, nc) == target:
                    # 포탄이 있는지 확인 후, 발사 명령을 내리고 결과 반환
                    if have_normal_bullet():
                        return actions + [FIRE_CMDS[d_idx]]
                    # 포탄이 없다면, 이 방향으로 공격은 불가능. 다른 행동을 계속 탐색.
                    break
        
        # 2. (이후 이동) 공격할 대상이 없으면, 다음 이동 위치를 탐색
        for d_idx, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc

            # 다음 위치가 맵 안이고,
            if is_in_bounds(nr, nc, rows, cols):
                # 이동 가능한 땅(G, S)이며, 아직 방문하지 않은 곳이라면
                if grid[nr][nc] in WALKABLE and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    # 새로운 위치와, 지금까지의 행동에 이동 명령을 추가하여 큐에 삽입
                    queue.append(((nr, nc), actions + [MOVE_CMDS[d_idx]]))

    # 큐가 모두 비었는데 길을 못찾았으면 빈 리스트 반환
    return []

##############################
# 메인 실행 부분
##############################

# 닉네임 설정 및 최초 연결
NICKNAME = 'FinalCode'
game_data = init(NICKNAME)
actions = [] # 행동 순서를 저장할 리스트

# 게임이 진행되는 동안 반복
while game_data is not None:
    # 서버로부터 받은 데이터 파싱
    parse_data(game_data)

    # 행동 순서가 비어있다면, 새로운 행동 순서를 탐색
    if not actions:
        # 맵에서 내 위치(M)와 적 포탑 위치(X) 찾기
        my_pos, enemy_turret_pos = None, None
        for r_idx, row in enumerate(map_data):
            for c_idx, cell in enumerate(row):
                if cell == START_SYMBOL:
                    my_pos = (r_idx, c_idx)
                elif cell == TARGET_SYMBOL:
                    enemy_turret_pos = (r_idx, c_idx)
        
        # 내 위치와 적 포탑 위치를 모두 찾았다면, BFS로 최적 행동 탐색
        if my_pos and enemy_turret_pos:
            actions = find_best_action_path(map_data, my_pos, enemy_turret_pos)

    # 결정된 행동 순서에서 가장 첫 번째 행동을 꺼내 서버로 전송
    output = "S" # 기본값은 대기(Stay)
    if actions:
        output = actions.pop(0)
    
    # 서버로 명령 전송 후, 다음 턴의 게임 데이터 수신
    game_data = submit(output)

# 게임 종료 후 연결 해제
close()
