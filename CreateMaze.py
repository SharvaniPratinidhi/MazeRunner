# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 20:35:15 2019

@author: Sharvani Pratinidhi
"""
from tkinter import *
import random
import numbers
import SolveMaze
import time
import numpy as np
import pandas as pd
import RunStatistics
import MazeThinning

#Default values
dimensions=10
probability=0.3

#Function to generate a maze of [dim][dim] dimensions
def generateMazeValues(prob,dim):
    grid=[ [0]*dim for _ in range(dim) ]
    for i in range(dim):
        for j in range(dim):
            if random.random() < prob:
                 grid[i][j] = 1
                 
    grid[0][0] = 2
    grid[dim - 1][dim - 1] = 3

    print(grid)
    return grid


class Maze(object):

    def __init__(self):
        self.dim = dimensions
        self.prob = probability
        self.grid=[ [0] * self.dim for _ in range(self.dim)]
        self.window = Tk()
        self.window.title("Maze Simulator")
        self.window.geometry('900x700+200+10')
        #Frame for options
        self.controlFrame=Frame(self.window,height=700)
        self.controlFrame.pack(side=LEFT)

        self.labelDim=Label(self.controlFrame,text='Dimensions')
        self.labelDim.pack()

        self.entryDim=Entry(self.controlFrame)
        self.entryDim.pack()

        self.labelProb=Label(self.controlFrame,text='Probability')
        self.labelProb.pack()

        self.entryProb=Entry(self.controlFrame)
        self.entryProb.pack()

        self.buttonGenerateMaze=Button(self.controlFrame, text="Generate Maze", command=self.generate_drawMaze)
        self.buttonGenerateMaze.pack()

        self.buttonDFS=Button(self.controlFrame, text="DFS", command=self.drawSolutionDFS)
        self.buttonDFS.pack()

        self.buttonBFS=Button(self.controlFrame, text="BFS", command=self.drawSolutionBFS)
        self.buttonBFS.pack()

        self.buttonAStarManhattan=Button(self.controlFrame, text="A* Manhattan Heuristic", command=self.drawSolutionAStarManhattan)
        self.buttonAStarManhattan.pack()
        
        self.buttonAStarEuclidean=Button(self.controlFrame, text="A* Euclidean Heuristic", command=self.drawSolutionAStarEuclidean)
        self.buttonAStarEuclidean.pack()

        self.buttonStats=Button(self.controlFrame, text="Generate Statistics", command=self.runStats)
        self.buttonStats.pack()
        
        self.labelMethod=Label(self.controlFrame,text='Method')
        self.labelMethod.pack()
        
        self.var1 = StringVar(self.controlFrame)
        
        self.var1.set("") # initial value
        
        self.option1 = OptionMenu(self.controlFrame, self.var1, "DFS","BFS","A* with Manhatten","A* with euclidian")
        self.option1.pack()
        print(self.var1.get())

        self.labelMetric=Label(self.controlFrame,text='Metric')
        self.labelMetric.pack()
        
        self.var2 = StringVar(self.controlFrame)
        self.var2.set("") # initial value

        self.option2 = OptionMenu(self.controlFrame, self.var2, "Shortest path length","number of nodes expanded","max fringe size")
        self.option2.pack()
        
        self.buttonLocalSearch=Button(self.controlFrame, text="Local Search Algorithm", command=self.simannealing)
        self.buttonLocalSearch.pack()
        
        self.buttonAStarMazeThinner=Button(self.controlFrame, text="A * Maze Thinner Heuristic", command=self.Thin)
        self.buttonAStarMazeThinner.pack()
        
        #Frame for drawing Maze
        self.mazeFrame=Frame(self.window, width=700, height=700)
        self.mazeFrame.pack(side=RIGHT)

        self.mazeCanvas=Canvas(self.mazeFrame, width=700, height=700)
        self.mazeCanvas.pack()

        self.window.mainloop()
     
    #To call maze thinning   
    def Thin(self):
        result=MazeThinning.astar(self.grid,self.dim,"MazeThinner",0.2)
        print(result.maze)
        self.drawMaze(result.maze)
    
    #For Simulated Annealing
    def simannealing(self):
 
        s = self.var1.get()
        if(s == "DFS"):
            method = "1"
        elif (s == "BFS"):
            method = "2"
        elif (s == "A* with Manhatten"):
            method = "3"
        else:
            method = "4"
            
        r = self.var2.get()
        if(r == "Shortest path length"):
            metric = "1"
        elif r == "number of nodes expanded":
            metric = "2"
        else:
            metric = "3"
        
        hard_Maze = Simulated_annealing_final.simulated_Annealing(self.grid,method,metric)

        self.drawMaze(hard_Maze)
    
    #To get values from entries and check if they are valid; and then generate the maze    
    def generateMaze(self):
        self.prob=self.entryProb.get()
        self.dim=self.entryDim.get()
        try:
           self.prob=float(self.entryProb.get())
           self.dim=int(self.entryDim.get())
        except ValueError:
            print ("Invalid parameters")
            return None
        if self.prob <= 0 and self.prob > 1:
            print ("Invalid parameter: " + str(self.prob))
            return None
        self.grid=generateMazeValues(self.prob,self.dim)
    
    #To run the program multiple times and get the statistics    
    def runStats(self):
       result=RunStatistics.getStats(self,100,10)
    
    #To generate and draw maze
    def generate_drawMaze(self):
        self.generateMaze()
        self.drawMaze(self.grid)

#Calls to functions in SolveMaze.py
    def drawSolutionDFS(self):
        result=SolveMaze.DFS(self.grid)
        print(result.maze)
        self.drawMaze(result.maze)

    def drawSolutionBFS(self):
        result=SolveMaze.BFS(self.grid)
        print(result.maze)
        self.drawMaze(result.maze)

    def drawSolutionAStarManhattan(self):
        result=SolveMaze.astar(self.grid,"Manhattan")
        print(result.maze)
        self.drawMaze(result.maze)

    def drawSolutionAStarEuclidean(self):
        result=SolveMaze.astar(self.grid,"Euclidean")
        print(result.maze)
        self.drawMaze(result.maze)
        
#To actually draw the maze on frame
    def drawMaze(self,maze):
        tileHeight = (680) / self.dim
        tileWidth = (680) / self.dim
        self.mazeCanvas.delete("all")    #Clear the canvas
        self.tiles = [[self.mazeCanvas.create_rectangle(10 + i * tileWidth, 10 + j * tileHeight,10 + (i + 1) * tileWidth, 10 + (j + 1) * tileHeight)for i in range(self.dim)] for j in range(self.dim)]

        for i in range(self.dim):
            for j in range(self.dim):
                if maze[i][j] == 1:
                    self.mazeCanvas.itemconfig(self.tiles[i][j], fill = "#000000")
                elif maze[i][j] == 5:
                    self.mazeCanvas.itemconfig(self.tiles[i][j], fill = "#0000ff")
                elif maze[i][j] == 7:
                    self.mazeCanvas.itemconfig(self.tiles[i][j], fill = "#ffff00")
        self.mazeCanvas.itemconfig(self.tiles[0][0], fill = "#ff0000")
        self.mazeCanvas.itemconfig(self.tiles[self.dim-1][self.dim-1], fill = "#228b22")

if __name__=="__main__":
    ms=Maze()
    
