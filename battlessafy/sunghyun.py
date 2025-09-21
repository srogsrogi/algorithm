def bfs(grid, starts, targets, wall):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(starts, [])])
    visited = {starts}
    while queue:
        (r, c), actions_now = queue.popleft()
        for d, (dr, dc) in enumerate(DIRS):
            for nums in range(1, 4):  # 4번 문제 3별 조건: 사거리 3
                nr, nc = r + dr * nums, c + dc * nums
                if 0 <= nr < rows and 0 <= nc < cols:
		                # 진지/탱크 타격 가능 여부(사로에 방해물 없음)
                    if grid[nr][nc] == 'R':  # or grid[nr][nc] == 'T':  
                    # 포탄이 바위/나무 통과 못한다고 가정
                    # 포탄이 바위를 통과하면 4번까지는 필요 없음
                        break
                    if (nr, nc) == targets:
                        return actions_now + [FIRE_CMDS[d]]

        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc

            if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc] != wall
                    and grid[nr][nc] != 'W'  # 물 지형 고려: 4번까지 통과
                    and (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                queue.append(((nr, nc), actions_now + [MOVE_CMDS[d]]))

    return []