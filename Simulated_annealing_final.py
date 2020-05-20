from copy import deepcopy
import random
import SolveMaze
import cmath

"""def Method():
    method_used = input("Enter the method \
                                            1.DFS  \
                                                2.BFS \
                                                    3.A* with manhatten \
                                                        4.A* with euclidian")
    #print(method_used)
    return method_used"""

"""def parameter():
    para = input("Enter the quantity \
                                     1.Length of shortest Path \
                                     2.Number of Nodes Expaned \
                                     3.Maximum length of fring")
    #print(para)
    return para"""

def Solve_Method(matrix,choice_method):
    
    if(choice_method == "1"):
        maze_solu = SolveMaze.DFS(matrix)
    elif(choice_method == "2"):
        maze_solu = SolveMaze.BFS(matrix)
    elif(choice_method == "3"):
        maze_solu = SolveMaze.astar(matrix,"Manhattan")
    else:
        maze_solu = SolveMaze.astar(matrix,"Euclidean")
    
    return maze_solu

def metric_used(metric,maze_solution):
    if (metric == "1"):
       metric_value = maze_solution.path_length
    elif (metric == "2"):
        metric_value = maze_solution.nodes_visited
    else:
        metric_value = maze_solution.max_fringe_size
    
    return metric_value

def simulated_Annealing(maze,method,para):
    
   
    print("Initial Maze")
    print(maze)
    print(method,para)
    original_maze = deepcopy(maze)
    original_maze_sol_class = Solve_Method(maze,method)
    original_maze_sol = original_maze_sol_class.maze
    hard_shortest_path = metric_used(para,original_maze_sol_class)
    print("Initial value of a metric ",hard_shortest_path)
    hard_maze = original_maze
    prev_metric_length = hard_shortest_path
    #print("Hardest s path",prev_metric_length)
    execution_count = 0
    T = 10
    Tmin = 0
    
    while T > Tmin:
        execution_count +=1 
        count = 0
        while True:
            count = count+1
            if count == 5000:
                print("cant generate more hard maze")
                print("Hardest maze so far ", maze)
                return
            
            new_maze = createHardMaze(maze)
            temp = SolveMaze.BFS(new_maze).path_length
            if temp != 0:
                new_maze_sol_class = Solve_Method(new_maze,method)
                new_maze_sol = new_maze_sol_class.maze
                new_metric_length = metric_used(para,new_maze_sol_class)
                #print(Solving_Maze.BFS(new_maze))
                break
    
        diff = new_metric_length - prev_metric_length
        if diff >= 0 or  cal_acceptProb(diff,T) > random.random():
            #print("here")
            if new_metric_length > hard_shortest_path:
                hard_shortest_path = new_metric_length 
                print("Hardests maze metric value",hard_shortest_path)
                #print(new_maze)
                hard_maze = deepcopy(new_maze)
                
            maze = new_maze
            prev_metric_length = new_metric_length
            
        T = temperatureDrop(T)
        
    print("Hardest Maze Generated", hard_maze)
                


def createHardMaze(maze):
    randRow = random.randint(0,len(maze)-1)
    randCol = random.randint(0,len(maze)-1)
    randRow2 = random.randint(0,len(maze)-1)
    randCol2 = random.randint(0,len(maze)-1)
    while((randRow == 0 and randCol == 0) or (randRow == len(maze)-1 and 
           randCol == len(maze)-1) or maze[randRow][randCol] == 1) :
        randRow = random.randint(0,len(maze)-1)
        randCol = random.randint(0,len(maze)-1)
    while((randRow2 == 0 and randCol2 == 0) or (randRow2 == len(maze)-1 and 
           randCol2 == len(maze)-1) or maze[randRow2][randCol2] == 0):
        randRow2 = random.randint(0,len(maze)-1)
        randCol2 = random.randint(0,len(maze)-1)
   
    maze[randRow][randCol] = 1
    maze[randRow2][randCol2] = 0
        
    return maze
    

def cal_acceptProb(diff,T):
	if diff > 0:
		return 1.0
	else:
		return float(cmath.exp((10)*diff/T).real)
    
def temperatureDrop(T):
	return T / 1.0008 - 0.00005

    


 





