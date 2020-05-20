# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


dataDFS = pd.read_csv("DFS_Statistics.csv") 
dataBFS = pd.read_csv("BFS_Statistics.csv") 
dataEuclidean = pd.read_csv("astar_Euclidean_Statistics.csv") 
dataManhattan = pd.read_csv("astar_Manhattan_Statistics.csv") 
BFSSolvable=dataBFS.loc[dataBFS["Solvable"]==1]
DFSSolvable=dataDFS.loc[dataDFS["Solvable"]==1]
EuclideanSolvable=dataEuclidean.loc[dataEuclidean["Solvable"]==1]
ManhattanSolvable=dataManhattan.loc[dataManhattan["Solvable"]==1]
probabilities=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

#Plot of Prabability vs Length of Path
def plotProbabilityLength():
    
    bfsmeanlengths=[]
    dfsmeanlengths=[]
    aeuclideanmeanlengths=[]
    amanhattanmeanlengths=[]
    
    
    for probability in probabilities:
        dfBFS= BFSSolvable.loc[BFSSolvable["Probability"]==probability]
        bfsmeanlengths.append(dfBFS["Path_Length"].mean())
        dfDFS= DFSSolvable.loc[DFSSolvable["Probability"]==probability]
        dfsmeanlengths.append(dfDFS["Path_Length"].mean())
        dfEuclidean= EuclideanSolvable.loc[EuclideanSolvable["Probability"]==probability]
        aeuclideanmeanlengths.append(dfEuclidean["Path_Length"].mean())
        dfManhattan= ManhattanSolvable.loc[ManhattanSolvable["Probability"]==probability]
        amanhattanmeanlengths.append(dfManhattan["Path_Length"].mean())
        
      
    print(dfsmeanlengths)
    print(bfsmeanlengths)
    print(aeuclideanmeanlengths)
    print(amanhattanmeanlengths)
    plt.plot(probabilities, bfsmeanlengths, color='g',label="BFS")
    plt.plot(probabilities, dfsmeanlengths, color='orange', label="DFS")
    plt.xlabel('Probabilities')
    plt.ylabel('Mean Path Lengths')
    plt.title('BFS, DFS Mean Path Lengths vs Probability ')
    plt.legend()
    plt.show()
    
    plt.plot(probabilities, amanhattanmeanlengths, color='blue')
    plt.xlabel('Probabilities')
    plt.ylabel('Mean Path Lengths')
    plt.title('A * Manhattan Mean Path Lengths vs Probability ')
    plt.show()
   
    plt.plot(probabilities, aeuclideanmeanlengths, color='red')
    plt.xlabel('Probabilities')
    plt.ylabel('Mean Path Lengths')
    plt.title('A* Euclidean Mean Path Lengths vs Probability ')
    plt.show()
       

# Plot of Probability vs Time
def plotProbabilityTime():
    bfsmeantime=[]
    dfsmeantime=[]
    aeuclideanmeantime=[]
    amanhattanmeantime=[]

    for probability in probabilities:
        dfBFS= BFSSolvable.loc[BFSSolvable["Probability"]==probability]
        bfsmeantime.append(dfBFS["Time"].mean())
        dfDFS= DFSSolvable.loc[DFSSolvable["Probability"]==probability]
        dfsmeantime.append(dfDFS["Time"].mean())
        dfEuclidean= EuclideanSolvable.loc[EuclideanSolvable["Probability"]==probability]
        aeuclideanmeantime.append(dfEuclidean["Time"].mean())
        dfManhattan= ManhattanSolvable.loc[ManhattanSolvable["Probability"]==probability]
        amanhattanmeantime.append(dfManhattan["Time"].mean())
        
      
    print(dfsmeantime)
    print(bfsmeantime)
    print(aeuclideanmeantime)
    print(amanhattanmeantime)
    plt.plot(probabilities, bfsmeantime, color='g',label="BFS")
    plt.plot(probabilities, dfsmeantime, color='orange', label="DFS")
    plt.xlabel('Probabilities')
    plt.ylabel('Mean time')
    plt.title('BFS, DFS Mean time vs Probability for 10x10 Maze')
    plt.legend()
    plt.show()
    
    plt.plot(probabilities, amanhattanmeantime, color='blue', label="Manhattan")
    plt.plot(probabilities, aeuclideanmeantime, color='red', label="Euclidean")
    plt.xlabel('Probabilities')
    plt.ylabel('Mean time')
    plt.legend()
    plt.title('A * Manhattan, A* Euclidean Mean time vs Probability ')
    plt.show()
   
#Plot of Probability vs Number of Nodes Visited
def plotProbabilityNodes():
    bfsmean_nodes_visited=[]
    dfsmean_nodes_visited=[]
    aeuclideanmean_nodes_visited=[]
    amanhattanmean_nodes_visited=[]
    
    for probability in probabilities:
        dfBFS= BFSSolvable.loc[BFSSolvable["Probability"]==probability]
        bfsmean_nodes_visited.append(dfBFS["Number_of_nodes_visited"].mean())
        dfDFS= DFSSolvable.loc[DFSSolvable["Probability"]==probability]
        dfsmean_nodes_visited.append(dfDFS["Number_of_nodes_visited"].mean())
        dfEuclidean= EuclideanSolvable.loc[EuclideanSolvable["Probability"]==probability]
        aeuclideanmean_nodes_visited.append(dfEuclidean["Number_of_nodes_visited"].mean())
        dfManhattan= ManhattanSolvable.loc[ManhattanSolvable["Probability"]==probability]
        amanhattanmean_nodes_visited.append(dfManhattan["Number_of_nodes_visited"].mean())
        
      
    print(dfsmean_nodes_visited)
    print(bfsmean_nodes_visited)
    print(aeuclideanmean_nodes_visited)
    print(amanhattanmean_nodes_visited)
    plt.plot(probabilities, bfsmean_nodes_visited, color='g',label="BFS")
    plt.plot(probabilities, dfsmean_nodes_visited, color='orange', label="DFS")
    plt.xlabel('Probabilities')
    plt.ylabel('Mean Nodes Visited')
    plt.title('BFS, DFS Mean Nodes Visited vs Probability ')
    plt.legend()
    plt.show()
    
    plt.plot(probabilities, amanhattanmean_nodes_visited, color='blue',label="Manhattan")
    plt.plot(probabilities, aeuclideanmean_nodes_visited, color='red', label="Euclidean")
    plt.xlabel('Probabilities')
    plt.ylabel('Mean Nodes Visited')
    plt.title('A * Manhattan, A* Euclidean Mean Nodes Visited vs Probability')
    plt.legend()
    plt.show()
   
#Plot of Probability vs Solvability
def plotProbabilitySolvability():
   
    solvability=[]
    for probability in probabilities:
        dfBFS= BFSSolvable.loc[BFSSolvable["Probability"]==probability]
        solvability.append((dfBFS["Solvable"].count())/100)
        
      
    print(solvability)
    plt.plot(probabilities, solvability, color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=12) 
  

    plt.xlabel('Probabilities of block being ')
    plt.ylabel('Probability of Solvability')
    plt.title('Solvability vs Probability ') 
    plt.show()    

#Plot of Dimension vs Time with respect to Algorithms   
def plotDimTimeAlgorithmWise():
    dataDFSDim = pd.read_csv("DFS_StatisticsDimension.csv")
    DFSSolvable=dataDFSDim.loc[dataDFSDim["Solvable"]==1]
    dfDFS= DFSSolvable.loc[DFSSolvable["Probability"]==0.1]
    plt.plot(dfDFS["Dimension"], dfDFS["Time"], color='blue',label="0.1")
    dfDFS= DFSSolvable.loc[DFSSolvable["Probability"]==0.2]
    plt.plot(dfDFS["Dimension"], dfDFS["Time"], color='red',label="0.2")
    dfDFS= DFSSolvable.loc[DFSSolvable["Probability"]==0.3]
    plt.plot(dfDFS["Dimension"], dfDFS["Time"], color='green',label="0.3")
    dfDFS= DFSSolvable.loc[DFSSolvable["Probability"]==0.4]
    plt.plot(dfDFS["Dimension"], dfDFS["Time"], color='pink',label="0.4")
    plt.xlabel('Dimension')
    plt.ylabel('Time')
    plt.title('DFS: Dimension vs Time')
    plt.legend()
    plt.show() 
    
    dataEuclideanDim = pd.read_csv("astar_Euclidean_StatisticsDimension.csv") 
    EuclideanSolvable=dataEuclideanDim.loc[dataEuclideanDim["Solvable"]==1]
    dfEuclidean= EuclideanSolvable.loc[EuclideanSolvable["Probability"]==0.1]
    plt.plot(dfEuclidean["Dimension"], dfEuclidean["Time"], color='blue',label="0.1")
    dfEuclidean= EuclideanSolvable.loc[EuclideanSolvable["Probability"]==0.2]
    plt.plot(dfEuclidean["Dimension"], dfEuclidean["Time"], color='red',label="0.2")
    dfEuclidean= EuclideanSolvable.loc[EuclideanSolvable["Probability"]==0.3]
    plt.plot(dfEuclidean["Dimension"], dfEuclidean["Time"], color='green',label="0.3")
    dfEuclidean= EuclideanSolvable.loc[EuclideanSolvable["Probability"]==0.4]
    plt.plot(dfEuclidean["Dimension"], dfEuclidean["Time"], color='pink',label="0.4")
    plt.xlabel('Dimension')
    plt.ylabel('Time')
    plt.title('A * Euclidean: Dimension vs Time')
    plt.legend()
    plt.show()     
    
    dataManhattanDim = pd.read_csv("astar_Manhattan_StatisticsDimension.csv")
    ManhattanSolvable=dataManhattanDim.loc[dataManhattanDim["Solvable"]==1]
    dfManhattan= ManhattanSolvable.loc[ManhattanSolvable["Probability"]==0.1]
    plt.plot(dfManhattan["Dimension"], dfManhattan["Time"], color='blue',label="0.1")
    dfManhattan= ManhattanSolvable.loc[ManhattanSolvable["Probability"]==0.2]
    plt.plot(dfManhattan["Dimension"], dfManhattan["Time"], color='red',label="0.2")
    dfManhattan= ManhattanSolvable.loc[ManhattanSolvable["Probability"]==0.3]
    plt.plot(dfManhattan["Dimension"], dfManhattan["Time"], color='green',label="0.3")
    dfManhattan= ManhattanSolvable.loc[ManhattanSolvable["Probability"]==0.4]
    plt.plot(dfManhattan["Dimension"], dfManhattan["Time"], color='pink',label="0.4")
    plt.xlabel('Dimension')
    plt.ylabel('Time')
    plt.title('A * Manhattan: Dimension vs Time')
    plt.legend()
    plt.show()   
    
    dataBFSDim = pd.read_csv("BFS_StatisticsDimension.csv")
    BFSSolvable=dataBFSDim.loc[dataBFSDim["Solvable"]==1]
    dfBFS= BFSSolvable.loc[BFSSolvable["Probability"]==0.1]
    plt.plot(dfBFS["Dimension"], dfBFS["Time"], color='blue',label="0.1")
    dfBFS= BFSSolvable.loc[BFSSolvable["Probability"]==0.2]
    plt.plot(dfBFS["Dimension"], dfBFS["Time"], color='red',label="0.2")
    dfBFS= BFSSolvable.loc[BFSSolvable["Probability"]==0.3]
    plt.plot(dfBFS["Dimension"], dfBFS["Time"], color='green',label="0.3")
    dfBFS= BFSSolvable.loc[BFSSolvable["Probability"]==0.4]
    plt.plot(dfBFS["Dimension"], dfBFS["Time"], color='pink',label="0.4")
    plt.xlabel('Dimension')
    plt.ylabel('Time')
    plt.title('BFS: Dimension vs Time')
    plt.legend()
    plt.show()

#Plot of Dimension vs Time with respect to Probability
def plotDimTimeProbabilityWise():
    dataDFSDim = pd.read_csv("DFS_StatisticsDimension.csv") 
    dataEuclideanDim = pd.read_csv("astar_Euclidean_StatisticsDimension.csv") 
    dataManhattanDim = pd.read_csv("astar_Manhattan_StatisticsDimension.csv")
    dataBFSDim = pd.read_csv("BFS_StatisticsDimension.csv")
    BFSSolvable=dataBFSDim.loc[dataBFSDim["Solvable"]==1]
    DFSSolvable=dataDFSDim.loc[dataDFSDim["Solvable"]==1]
    EuclideanSolvable=dataEuclideanDim.loc[dataEuclideanDim["Solvable"]==1]
    ManhattanSolvable=dataManhattanDim.loc[dataManhattanDim["Solvable"]==1]
    
    dfDFS= DFSSolvable.loc[DFSSolvable["Probability"]==0.1]
    plt.plot(dfDFS["Dimension"], dfDFS["Time"], color='orange',label="DFS")
    dfEuclidean= EuclideanSolvable.loc[EuclideanSolvable["Probability"]==0.1]
    plt.plot(dfEuclidean["Dimension"], dfEuclidean["Time"], color='red',label="A* Euclidean")
    dfManhattan= ManhattanSolvable.loc[ManhattanSolvable["Probability"]==0.1]
    plt.plot(dfManhattan["Dimension"], dfManhattan["Time"], color='blue',label="A* Manhattan")
    dfBFS= BFSSolvable.loc[BFSSolvable["Probability"]==0.1]
    plt.plot(dfBFS["Dimension"], dfBFS["Time"], color='green',label="BFS")
    plt.xlabel('Dimension')
    plt.ylabel('Time')
    plt.title('Dimension vs Time with Probability 0.1')
    plt.legend()
    plt.show() 
    
    dfDFS= DFSSolvable.loc[DFSSolvable["Probability"]==0.2]
    plt.plot(dfDFS["Dimension"], dfDFS["Time"], color='orange',label="DFS")
    dfEuclidean= EuclideanSolvable.loc[EuclideanSolvable["Probability"]==0.2]
    plt.plot(dfEuclidean["Dimension"], dfEuclidean["Time"], color='red',label="A* Euclidean")
    dfManhattan= ManhattanSolvable.loc[ManhattanSolvable["Probability"]==0.2]
    plt.plot(dfManhattan["Dimension"], dfManhattan["Time"], color='blue',label="A* Manhattan")
    dfBFS= BFSSolvable.loc[BFSSolvable["Probability"]==0.2]
    plt.plot(dfBFS["Dimension"], dfBFS["Time"], color='green',label="BFS")
    plt.xlabel('Dimension')
    plt.ylabel('Time')
    plt.title('Dimension vs Time with Probability 0.2')
    plt.legend()
    plt.show()
    
    dfDFS= DFSSolvable.loc[DFSSolvable["Probability"]==0.3]
    plt.plot(dfDFS["Dimension"], dfDFS["Time"], color='orange',label="DFS")
    dfEuclidean= EuclideanSolvable.loc[EuclideanSolvable["Probability"]==0.3]
    plt.plot(dfEuclidean["Dimension"], dfEuclidean["Time"], color='red',label="A* Euclidean")
    dfManhattan= ManhattanSolvable.loc[ManhattanSolvable["Probability"]==0.3]
    plt.plot(dfManhattan["Dimension"], dfManhattan["Time"], color='blue',label="A* Manhattan")
    dfBFS= BFSSolvable.loc[BFSSolvable["Probability"]==0.3]
    plt.plot(dfBFS["Dimension"], dfBFS["Time"], color='green',label="BFS")
    plt.xlabel('Dimension')
    plt.ylabel('Time')
    plt.title('Dimension vs Time with Probability 0.3')
    plt.legend()
    plt.show()
     
    dfDFS= DFSSolvable.loc[DFSSolvable["Probability"]==0.4]
    plt.plot(dfDFS["Dimension"], dfDFS["Time"], color='orange',label="DFS")
    dfEuclidean= EuclideanSolvable.loc[EuclideanSolvable["Probability"]==0.4]
    plt.plot(dfEuclidean["Dimension"], dfEuclidean["Time"], color='red',label="A* Euclidean")
    dfManhattan= ManhattanSolvable.loc[ManhattanSolvable["Probability"]==0.4]
    plt.plot(dfManhattan["Dimension"], dfManhattan["Time"], color='blue',label="A* Manhattan")
    dfBFS= BFSSolvable.loc[BFSSolvable["Probability"]==0.4]
    plt.plot(dfBFS["Dimension"], dfBFS["Time"], color='green',label="BFS")
    plt.xlabel('Dimension')
    plt.ylabel('Time')
    plt.title('Dimension vs Time with Probability 0.4')
    plt.legend()
    plt.show()
    

#Plot of A* with different techniques: Manhattan Distance, Euclidean Distance and Maze Thinning 
def astarqvalue():
    meantimeMazeThinning=[]
    meantimeManhattan=[]
    meantimeEuclidean=[]
    aeuclideanmean_nodes_visited=[]
    amanhattanmean_nodes_visited=[]
    amazethinning_nodes_visited=[]
    qvalues=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
    dataAstar = pd.read_csv("MazeThinning.csv")
    dataAstarManhattan = pd.read_csv("AstarManhattanTime.csv")
    dataAstarEuclidean = pd.read_csv("AstarEuclideanTime.csv")
    AstarSolvable=dataAstar.loc[dataAstar["Solvable"]==1]
    ManhattanSolvable=dataAstarManhattan.loc[dataAstarManhattan["Solvable"]==1]
    EuclideanSolvable=dataAstarEuclidean.loc[dataAstarEuclidean["Solvable"]==1]
    for q in qvalues:
        dfAstar= AstarSolvable.loc[AstarSolvable["q-values"]==q]
        meantimeMazeThinning.append(dfAstar["Time"].mean())
        amazethinning_nodes_visited.append(dfAstar["Number_of_nodes_visited"].mean())
        dfAstarManhattan= ManhattanSolvable.loc[ManhattanSolvable["q-values"]==q]
        meantimeManhattan.append(dfAstarManhattan["Time"].mean())
        amanhattanmean_nodes_visited.append(dfAstarManhattan["Number_of_nodes_visited"].mean())
        dfAstarEuclidean= EuclideanSolvable.loc[EuclideanSolvable["q-values"]==q]
        meantimeEuclidean.append(dfAstarEuclidean["Time"].mean())
        aeuclideanmean_nodes_visited.append(dfAstarEuclidean["Number_of_nodes_visited"].mean())
        
    plt.plot(qvalues,meantimeManhattan,color='red', label="Manhattan")   
    plt.plot(qvalues,meantimeEuclidean,color='green', label="Euclidean")   
    plt.plot(qvalues, meantimeMazeThinning, color='blue', label="Maze Thinning")
    plt.xlabel('q-value')
    plt.ylabel('Time')
    plt.legend()
    plt.title('A* q-value vs Time')
    plt.show() 

    plt.plot(qvalues,amanhattanmean_nodes_visited,color='red', label="Manhattan")   
    plt.plot(qvalues,aeuclideanmean_nodes_visited,color='green', label="Euclidean")   
    plt.plot(qvalues, amazethinning_nodes_visited, color='blue', label="Maze Thinning")
    plt.xlabel('q-value')
    plt.ylabel('Time')
    plt.legend()
    plt.title('A* q-value vs Nodes Visited')
    plt.show() 


#Calls to all functions
plotProbabilityLength()
plotProbabilityTime()
plotProbabilityNodes()
plotProbabilitySolvability()
plotDimTimeAlgorithmWise()
plotDimTimeProbabilityWise()
astarqvalue()