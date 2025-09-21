import sys
import socket
from collections import deque

# ==================================================================================================
# [PART 2] BFS 함수 (핵심 로직, 원리만 이해하면 쉬움)
# - 역할: 이 코드의 '뇌'. 현재 상태에서 최적의 행동을 계산합니다.
# - 암기법: 딱 두 가지만 기억하세요. "1. 공격 먼저, 2. 없으면 이동"
#
# [PART 3] 메인 실행 부분 (탐색과 명령을 연결하는 부분)
# - 역할: '뇌'가 계산한 결과를 '입'을 통해 서버로 전달하는 실행부입니다.
# - 암기법: "데이터 받고 -> 길 없으면 길 찾고 -> 찾은 길대로 한 칸 행동!" 이 순서를 반복합니다.
# ==================================================================================================

# ==================================================================================================
# [PART 2] BFS 함수 (핵심 암기 파트)
# ==================================================================================================

# --- BFS 탐색에 필요한 간단한 설정 ---
# 방향 벡터: 4방향을 숫자로 다루기 위한 약속. 0:우, 1:하, 2:좌, 3:상
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
# 각 방향 숫자에 맞는 이동/발사 명령어를 미리 만들어 둠
MOVE_CMDS = {0: "R A", 1: "D A", 2: "L A", 3: "U A"}
FIRE_CMDS = {0: "R F", 1: "D F", 2: "L F", 3: "U F"}

# 이동 가능한 땅 종류를 미리 정의. set을 쓰면 탐색 속도가 빠름.
WALKABLE = {"G", "S"}

# --- 포탄 있는지 확인하는 함수 ---
def have_bullet():
    # my_allies 딕셔너리에서 내 정보('M')를 가져와 포탄 수(세 번째 값)가 0보다 큰지 확인
    try: return int(my_allies.get('M')[2]) > 0
    except: return False # 데이터가 이상할 경우에 대비한 안전장치

# --- BFS 함수 본체 (이것만 외우면 끝!) ---
def find_path_bfs(grid, start, target):
    rows, cols = len(grid), len(grid[0])
    # 1. 큐(deque)를 만들고, 시작점 정보를 넣는다.
    # (시작 좌표, 시작점까지의 행동들) -> 시작점이니까 행동은 당연히 빈 리스트 []
    queue = deque([(start, [])])
    # 2. 방문했던 곳을 기록할 set을 만들고, 시작점을 기록한다.
    # (이걸 안하면 갔던 길을 또 가면서 무한루프에 빠질 수 있음)
    visited = {start}

    # 3. 큐에 탐색할 곳이 남아있는 동안 계속 반복
    while queue:
        # 4. 큐의 맨 앞에서 탐색할 대상(현재위치, 행동리스트)을 꺼낸다.
        (r, c), actions = queue.popleft()

        # 5. [공격 로직]: 현재 위치에서, 내 바로 옆(1칸)에 타겟이 있는지 확인
        # enumerate(DIRS)는 방향(dr, dc)과 함께 인덱스(i)도 제공 (0:우, 1:하, ...)
        for i, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc # 다음 좌표 계산
            if (nr, nc) == target: # 다음 좌표가 목표 지점이라면
                if have_bullet(): # 총알이 있는지 확인하고
                    return actions + [FIRE_CMDS[i]] # 있다면, 현재까지의 행동에 발사 명령을 추가해서 반환! (탐색 성공)
                # 총알이 없다면 공격할 수 없으므로, 다른 길을 계속 탐색한다.

        # 6. [이동 로직]: 위에서 쏠 곳을 못찾았다면, 다음 이동할 곳을 찾는다.
        for i, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc # 다음 좌표 계산
            
            # [핵심 조건] 다음 갈 곳이 (1)맵 안이고, (2)갈 수 있는 땅이고, (3)아직 안 가본 곳이라면
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] in WALKABLE and (nr, nc) not in visited:
                # 7. 위 조건을 통과했다면, 그곳은 이제 방문했다고 기록하고
                visited.add((nr, nc))
                # 8. 큐에 다음 탐색 대상으로 추가한다. (현재까지의 행동에 이동 명령을 추가해서)
                queue.append(((nr, nc), actions + [MOVE_CMDS[i]]))
    
    # 9. 큐를 다 비울때까지 길을 못찾았다면, 탐색 실패. 빈 리스트를 반환.
    return []

# ==================================================================================================
# [PART 3] 메인 실행 부분 (BFS 함수를 호출하는 부분)
# ==================================================================================================

NICKNAME = 'EasyCode'
game_data = init(NICKNAME)
actions = [] # 행동 계획을 저장할 리스트 (초기엔 비어있음)

# 게임이 끝날 때까지(game_data가 None이 될 때까지) 계속 반복
while game_data is not None:
    # 1. 서버가 보내준 최신 게임 데이터를 파싱(분석)한다.
    parse_data(game_data)

    # 2. 만약 이전에 세워둔 행동 계획(actions)이 비어있다면, 새로운 계획을 세운다.
    if not actions:
        # 맵 전체를 스캔해서 내 위치(M)와 적 포탑 위치(X)를 찾는다.
        my_pos, target_pos = None, None
        for r, row_data in enumerate(map_data):
            for c, cell in enumerate(row_data):
                if cell == 'M': my_pos = (r, c)
                elif cell == 'X': target_pos = (r, c)
        
        # 내 위치와 적 위치를 둘 다 찾았을 경우에만 BFS 실행!
        if my_pos and target_pos:
            # BFS("뇌")를 호출해서 최적의 행동 계획을 계산하고, 그 결과를 actions 리스트에 저장.
            actions = find_path_bfs(map_data, my_pos, target_pos)

    # 3. 행동 계획에 따라 행동한다.
    output = "S" # 기본 행동은 '대기(Stay)'. 길을 못찾았을 경우를 대비한 안전장치.
    if actions: # 만약 행동 계획이 비어있지 않다면
        # 계획된 행동 중 가장 첫 번째 것을 꺼내서 이번 턴에 할 일(output)로 정한다.
        output = actions.pop(0)
    
    # 4. 결정된 행동(output)을 서버로 전송하고, 다음 턴의 게임 데이터를 받는다.
    game_data = submit(output)

# 게임 종료
close()