###################################
# 알고리즘 함수/메서드 부분 구현 시작
###################################

# 출발지와 목적지의 위치 찾기
def find_positions(grid, start_mark, goal_mark):
    rows, cols = len(grid), len(grid[0])
    start = goal = None

    for row in range(rows):
        for col in range(cols):
            cell = grid[row][col]
            if cell == start_mark:
                start = (row, col)
            elif cell == goal_mark:
                goal = (row, col)

    return start, goal

# 매뉴얼 기준: 이동 가능/불가 타일 정의
# - 이동 가능: G(일반), S(모래; 체력 페널티는 시뮬레이터가 처리)
# - 이동 불가: R(바위), W(물), T(나무), F(보급시설), 유닛들(H, M1~M3, E1~E3)
WALKABLE = {"G", "S"}
BLOCK_UNITS = {"H", "M1", "M2", "M3", "E1", "E2", "E3"}
BLOCK_TERRAINS = {"R", "W", "T", "F"}
BLOCKED = BLOCK_TERRAINS | BLOCK_UNITS

def in_bounds(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

def is_walkable_cell(grid, r, c):
    cell = grid[r][c]
    # 목표 X는 별도 처리하므로 여기선 일반 이동성만 본다.
    return (cell in WALKABLE)

def have_normal_bullet():
    me = my_allies.get('M')
    if not me or len(me) < 3:
        return 0
    try:
        return int(me[2])  # [체력, 방향, 일반포탄, 메가포탄]
    except:
        return 0

# 경로 탐색 알고리즘 (BFS)
# - 인접 칸이 X면 사거리/장애물 검사 없이 '인접'만 처리해 즉시 사격
# - 단, 일반 포탄이 1발 이상 있어야 발사 커맨드 반환 (없으면 이동 계속 탐색)
def bfs(grid, start, target, wall_symbol_unused):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        (r, c), actions = queue.popleft()

        # 1) 인접 칸에 목표가 있으면, 탄약이 있는지 확인 후 발사
        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc, rows, cols) and (nr, nc) == target:
                if have_normal_bullet() > 0:
                    return actions + [FIRE_CMDS[d]]
                # 탄약이 없으면 사격 불가 → 이동 경로 탐색 계속

        # 2) 4방 이동 확장
        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc
            if not in_bounds(nr, nc, rows, cols):
                continue

            # 목표(X)는 '들어가는' 칸이 아니라 '맞추는' 대상이므로
            # 이동 확장에서는 제외, 대신 위의 인접-사격 로직이 처리
            if grid[nr][nc] == TARGET_SYMBOL:
                continue

            # 이동 불가 타일/유닛은 스킵
            if grid[nr][nc] in BLOCKED:
                continue

            # 이동 가능 타일만 방문
            if is_walkable_cell(grid, nr, nc) and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), actions + [MOVE_CMDS[d]]))

    # 경로/사격 불가
    return []

# 경로 탐색 변수 정의
DIRS = [(0,1), (1,0), (0,-1), (-1,0)]
MOVE_CMDS = {0: "R A", 1: "D A", 2: "L A", 3: "U A"}
FIRE_CMDS = {0: "R F", 1: "D F", 2: "L F", 3: "U F"}
START_SYMBOL = 'M'
TARGET_SYMBOL = 'X'

# 최초 데이터 파싱
parse_data(game_data)

# 출발지점, 목표지점의 위치 확인
start, target = find_positions(map_data, START_SYMBOL, TARGET_SYMBOL)
if not start or not target:
    print("[ERROR] Start or target not found in map")
    close()
    exit()

# 최초 경로 탐색
actions = bfs(map_data, start, target, None)

###################################
# 알고리즘 함수/메서드 부분 구현 끝
###################################