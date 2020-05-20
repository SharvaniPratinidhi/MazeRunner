# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 14:46:17 2019

@author: Sharvani Pratinidhi
"""
import CreateMaze
import SolveMaze
import time
import pandas as pd
import numpy as np
import MazeThinning

#To get all statistics of algorithms and save them as CSV files for further use.
def getStats(object,n,dim):
        n=100
        dim=50
        dataDFS=[]
        dataBFS=[]
        dataManhattan=[]
        dataEuclidean=[]
        probabilities=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
        for probability in probabilities:
            for i in range(n):
                maze=CreateMaze.generateMazeValues(probability,dim)
                start = time.time()
                result = SolveMaze.DFS(maze)
                end = time.time()
                t=end-start
                dataDFS.append([dim,probability,result.nodes_visited,result.path_length,result.solvable,t])
                start = time.time()
                result = SolveMaze.BFS(maze)
                end = time.time()
                t=end-start
                dataBFS.append([dim,probability,result.nodes_visited,result.path_length,result.solvable,t])
                start = time.time()
                result = SolveMaze.astar(maze,"Manhattan")
                end = time.time()
                t=end-start
                dataManhattan.append([dim,probability,result.nodes_visited,result.path_length,result.solvable,t])
                start = time.time()
                result = SolveMaze.astar(maze,"Euclidean")
                end = time.time()
                t=end-start
                dataEuclidean.append([dim,probability,result.nodes_visited,result.path_length,result.solvable,t])
                
                
        statsDFS=pd.DataFrame(dataDFS,columns=["Dimension","Probability","Number_of_nodes_visited","Path_Length","Solvable","Time"])
        statsDFS.to_csv("DFS_Statistics.csv", sep=',', encoding='utf-8',mode='a')
        statsBFS=pd.DataFrame(dataBFS,columns=["Dimension","Probability","Number_of_nodes_visited","Path_Length","Solvable","Time"])
        statsBFS.to_csv("BFS_Statistics.csv", sep=',', encoding='utf-8',mode='a')
        statsManhattan=pd.DataFrame(dataManhattan,columns=["Dimension","Probability","Number_of_nodes_visited","Path_Length","Solvable","Time"])
        statsManhattan.to_csv("astar_Manhattan_Statistics.csv", sep=',', encoding='utf-8',mode='a')
        statsEuclidean=pd.DataFrame(dataEuclidean,columns=["Dimension","Probability","Number_of_nodes_visited","Path_Length","Solvable","Time"])
        statsEuclidean.to_csv("astar_Euclidean_Statistics.csv", sep=',', encoding='utf-8',mode='a')
        DimTime()
        AstarMazeThinningStatistics()  
        return None

#Dimension vs Time Statistics for all algrithms for a range of dimensions
def DimTime():
    probabilities=[0.1,0.2,0.3,0.4]
    dataDFS=[]
    dataBFS=[]
    dataManhattan=[]
    dataEuclidean=[]
    dimensions=[10,15,20,25,50,75,100,200,400,500]
    for probability in probabilities:
        for dim in dimensions:
            maze=CreateMaze.generateMazeValues(probability,dim)
            start = time.time()
            result = SolveMaze.DFS(maze)
            end = time.time()
            t=end-start
            dataDFS.append([dim,probability,result.nodes_visited,result.path_length,result.solvable,t])
            start = time.time()
            result = SolveMaze.BFS(maze)
            end = time.time()
            t=end-start
            dataBFS.append([dim,probability,result.nodes_visited,result.path_length,result.solvable,t])
            start = time.time()
            result = SolveMaze.astar(maze,"Manhattan")
            end = time.time()
            t=end-start
            dataManhattan.append([dim,probability,result.nodes_visited,result.path_length,result.solvable,t])
            start = time.time()
            result = SolveMaze.astar(maze,"Euclidean")
            end = time.time()
            t=end-start
            dataEuclidean.append([dim,probability,result.nodes_visited,result.path_length,result.solvable,t])
        
    statsDFS=pd.DataFrame(dataDFS,columns=["Dimension","Probability","Number_of_nodes_visited","Path_Length","Solvable","Time"])
    statsDFS.to_csv("DFS_StatisticsDimension.csv", sep=',', encoding='utf-8',mode='a')
    statsBFS=pd.DataFrame(dataBFS,columns=["Dimension","Probability","Number_of_nodes_visited","Path_Length","Solvable","Time"])
    statsBFS.to_csv("BFS_StatisticsDimension.csv", sep=',', encoding='utf-8',mode='a')
    statsManhattan=pd.DataFrame(dataManhattan,columns=["Dimension","Probability","Number_of_nodes_visited","Path_Length","Solvable","Time"])
    statsManhattan.to_csv("astar_Manhattan_StatisticsDimension.csv", sep=',', encoding='utf-8',mode='a')
    statsEuclidean=pd.DataFrame(dataEuclidean,columns=["Dimension","Probability","Number_of_nodes_visited","Path_Length","Solvable","Time"])
    statsEuclidean.to_csv("astar_Euclidean_StatisticsDimension.csv", sep=',', encoding='utf-8',mode='a')
        
    return None

def AstarMazeThinningStatistics():
     n=100
     dim=50
     dataMazeThinning=[]
     dataAstarManhattan=[]
     dataAstarEuclidean=[]
     probability=0.3
     qvalues=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
     for q in qvalues:
         for i in range(n):
             maze=CreateMaze.generateMazeValues(probability,dim)
             start = time.time()
             result = MazeThinning.astar(maze,dim,"MazeThinning",q)
             end = time.time()
             t=end-start  
             dataMazeThinning.append([dim,probability,q,result.nodes_visited,result.path_length,result.solvable,t])
             start = time.time()
             result = SolveMaze.astar(maze,"Manhattan")
             end = time.time()
             t=end-start  
             dataAstarManhattan.append([dim,probability,q,result.nodes_visited,result.path_length,result.solvable,t])
             start = time.time()
             result = SolveMaze.astar(maze,"Euclidean")
             end = time.time()
             t=end-start  
             dataAstarEuclidean.append([dim,probability,q,result.nodes_visited,result.path_length,result.solvable,t])
     statsMazeThinning=pd.DataFrame(dataMazeThinning,columns=["Dimension","Probability","q-values","Number_of_nodes_visited","Path_Length","Solvable","Time"])
     statsMazeThinning.to_csv("MazeThinning.csv", sep=',', encoding='utf-8',mode='a')
     statsAstarManhattan=pd.DataFrame(dataAstarManhattan,columns=["Dimension","Probability","q-values","Number_of_nodes_visited","Path_Length","Solvable","Time"])
     statsAstarManhattan.to_csv("AstarManhattanTime.csv", sep=',', encoding='utf-8',mode='a')
     statsAstarEuclidean=pd.DataFrame(dataAstarEuclidean,columns=["Dimension","Probability","q-values","Number_of_nodes_visited","Path_Length","Solvable","Time"])
     statsAstarEuclidean.to_csv("AstarEuclideanTime.csv", sep=',', encoding='utf-8',mode='a')
     