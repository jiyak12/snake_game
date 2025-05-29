import random
from collections import deque
import heapq

# Directions (Up, Down, Left, Right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Random movement algorithm (limited moves)
def random_move(start, goal, obstacles, rows, cols):
    path = []
    current = start

    for _ in range(1000):  # Limit to 1000 moves
        direction = random.choice(DIRECTIONS)
        new_pos = (current[0] + direction[0], current[1] + direction[1])

        if (
            0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and
            new_pos not in obstacles
        ):
            path.append(direction)
            current = new_pos

        if current == goal:
            return path

    return []  # If it takes too long, return empty path


# Breadth-First Search (BFS) Algorithm
def bfs(start, goal, obstacles, rows, cols):
    queue = deque([(start, [])])  
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        for direction in DIRECTIONS:
            new_pos = (current[0] + direction[0], current[1] + direction[1])

            if (
                0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and
                new_pos not in visited and new_pos not in obstacles
            ):
                visited.add(new_pos)
                queue.append((new_pos, path + [direction]))

    return []  


# Depth-First Search (DFS) Algorithm
def dfs(start, goal, obstacles, rows, cols):
    stack = [(start, [])]  
    visited = set()
    visited.add(start)

    while stack:
        current, path = stack.pop()

        if current == goal:
            return path

        for direction in DIRECTIONS:
            new_pos = (current[0] + direction[0], current[1] + direction[1])

            if (
                0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and
                new_pos not in visited and new_pos not in obstacles
            ):
                visited.add(new_pos)
                stack.append((new_pos, path + [direction]))

    return []  


# Iterative Deepening Search (IDS) Algorithm
def ids(start, goal, obstacles, rows, cols):
    def depth_limited_search(node, goal, depth, path, visited):
        if node == goal:
            return path
        if depth <= 0:
            return None

        visited.add(node)

        for direction in DIRECTIONS:
            new_pos = (node[0] + direction[0], node[1] + direction[1])

            if (
                0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and
                new_pos not in visited and new_pos not in obstacles
            ):
                result = depth_limited_search(new_pos, goal, depth - 1, path + [direction], visited)
                if result:
                    return result

        return None

    depth = 0
    while True:
        visited = set()
        result = depth_limited_search(start, goal, depth, [], visited)
        if result:
            return result
        depth += 1


# Uniform Cost Search (UCS) Algorithm
def ucs(start, goal, obstacles, rows, cols):
    queue = [(0, start, [])]  
    visited = set()
    visited.add(start)

    while queue:
        cost, current, path = heapq.heappop(queue)

        if current == goal:
            return path

        for direction in DIRECTIONS:
            new_pos = (current[0] + direction[0], current[1] + direction[1])

            if (
                0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and
                new_pos not in visited and new_pos not in obstacles
            ):
                visited.add(new_pos)
                heapq.heappush(queue, (cost + 1, new_pos, path + [direction]))

    return []  

# Greedy Best-First Search Algorithm
def greedy_bfs(start, goal, obstacles, rows, cols):
    def heuristic(node):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    queue = [(heuristic(start), start, [])]  
    visited = set()
    visited.add(start)

    while queue:
        _, current, path = heapq.heappop(queue)

        if current == goal:
            return path

        for direction in DIRECTIONS:
            new_pos = (current[0] + direction[0], current[1] + direction[1])

            if (
                0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and
                new_pos not in visited and new_pos not in obstacles
            ):
                visited.add(new_pos)
                heapq.heappush(queue, (heuristic(new_pos), new_pos, path + [direction]))

    return []  


# A* Search Algorithm
def astar(start, goal, obstacles, rows, cols):
    def heuristic(node):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    queue = [(0, start, [])]  
    visited = set()
    cost = {start: 0}

    while queue:
        total_cost, current, path = heapq.heappop(queue)

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        for direction in DIRECTIONS:
            new_pos = (current[0] + direction[0], current[1] + direction[1])

            if (
                0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and
                new_pos not in visited and new_pos not in obstacles
            ):
                new_cost = cost[current] + 1
                if new_pos not in cost or new_cost < cost[new_pos]:
                    cost[new_pos] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_pos), new_pos, path + [direction]))

    return []
