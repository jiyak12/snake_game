# SNAKE GAME
The project aims to implement intelligent pathfinding algorithms to navigate a snake through a grid-based environment to locate food while avoiding obstacles.
This repository explores the application of various search algorithms, including Breadth-First Search (BFS), Depth-First Search (DFS), Iterative Deepening Search (IDS), Uniform Cost Search (UCS), Greedy Best-First Search (Greedy BFS), and A* Search. Each algorithm determines the
snake's optimal path based on predefined or heuristic strategies.


The project involves evaluating the performance of these algorithms under varying levels of
difficulty, characterized by increasing obstacle density. Metrics such as time taken to find
food, number of moves, and success rate are analyzed to compare algorithm efficiency. This
implementation provides insights into algorithm behavior in dynamic environments,
showcasing the practical use of artificial intelligence in solving real-world pathfinding
problems.

## PREREQUISITES: 
pip install pygame

## HOW TO RUN GAME:
python snake.py <level> <search_algorithm>

where, <level> can be level0 , level1 , level2 or level3.

<search_algorithm> can be bfs , dfs , ucs , ids , a_star , random or greedy

## IMPLEMENTATION OF ALGORITHMS:
There are four levels in the game with increasing obstacle density:
Level 0 : No obstacles.
Level 1 : Low obstacle density.
Level 2 : Medium obstacle density.
Level 3: High obstacle density.


- RANDOM MOVEMENT(Implemented) : A basic algorithm implemented to give students
an idea about what you need to do. It selects an action randomly out of all possible ones.

![image](https://github.com/user-attachments/assets/fed1e7dc-be00-42af-930f-55a90f975c6e)

- BFS : Uses a queue as the frontier to explore paths level by level, ensuring the shortest path is found.

![image](https://github.com/user-attachments/assets/8a515c35-8c9f-4f87-953f-965951481f41)

-  DFS : Employs a stack as the frontier, diving deep into one path before backtracking, which can result in non-optimal paths.

![image](https://github.com/user-attachments/assets/8173b8d7-66be-422c-8c6b-0213651c5b3c)

- IDS : Combines BFS and DFS by incrementally increasing the depth limit and using a stack for exploration.

![image](https://github.com/user-attachments/assets/da116d7a-dfde-4976-9100-45ada0bc2e24)

- UCS : Uses a priority queue as the frontier to prioritize paths with the lowest cumulative cost.

![image](https://github.com/user-attachments/assets/1d643984-2c69-4fab-9c5f-1742b4dc045b)

-  Greedy BFS : Uses a priority queue and selects paths based solely on the heuristic function, which in this case is the Manhattan distance (the sum of the absolute differences in the x and y coordinates between the snake and the food).

![image](https://github.com/user-attachments/assets/83b79270-2a50-4f0f-9cb3-ccf4cfc4409b)

- A* Search : Uses a priority queue but combines both the actual cost to reach a node and the Manhattan distance as the heuristic to ensure the most efficient path is found. 
![image](https://github.com/user-attachments/assets/2b6d30d2-e92c-4238-b420-061a02cfc9ff)

## COMPARISON BETWEEN DIFFERENT ALGORITHMS

Parameters used for comparison
- Time Taken: How quickly the algorithm finds the food.
- Number of Moves: The number of moves the snake makes to reach the food.
- Failure Rate: How often the algorithm fails in guiding the snake to the food.

![image](https://github.com/user-attachments/assets/a3bc9eba-f590-450a-9c92-e66eef88f4c4)









