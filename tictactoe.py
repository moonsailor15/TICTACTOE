#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 22:36:01 2022

@author: valeria
"""

#-----------TIC TAC TOE-----------------#
#global variables 
#-------------------------#
# if game is being played 
playing = True

# if theres a winner 
winner = None

# the current player 
current = "X"

#the board 
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#FUNCTIONS# 
#-----------------------------------------------------------------#
#function to create my board and display it 
def showBoard():
  print("\n")
  print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|    1 | 2 | 3")
  print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|    4 | 5 | 6")
  print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|    7 | 8 | 9")
  print("\n")


#function to play the game 
def play():
  #display my board
  showBoard()
    
  #creating while loop for different game instances 
  while playing:
    # handle the turns of each player 
    turns(current)
    # check if game is done or not 
    checkGameStatus()
    # switch back and forth between players for game 
    switchPlayer()
        
  #game is done 
  if winner == "X" or winner == "O":
    print(winner + "WINS!")
  elif winner == None:
    print("TIE.")


#function for handeling turns 
def turns(player):
  print(player + "'s turn to play.")
  pos = input("Select your positiion to play on the board (1-9): ")
  
  #check if spot is available 
  valid = False
  while not valid:

    while pos not in ["1","2","3","4","5","6","7","8","9"]:
      pos = input("Invalid. Choose a position from 1 to 9: ")
          
    pos = int(pos) - 1      
    if board[pos] == "-":
      valid = True
    else:
      print("spot taken. Pick another location")
  
  #place the player on board   
  board[pos] = player
  #show updated board    
  showBoard()

#function to check if game is over or not     
def checkGameStatus():
  checkWin()
  checkTie()
    
#Function to check for a winner 
def checkWin():
  #set up global 
  global winner
  #cols 3 in a row 
  colWinner = checkCols()
  #rows 3 in a row 
  rowWinner = checkRows()
  #diags 3 in a row
  diagWinner = checkDiags()
  #find winner  
  if rowWinner():
    #win
    winner = rowWinner
  elif colWinner():
    #win 
    winner = colWinner
  elif diagWinner():
    #win
    winner = diagWinner
  else:
    winner = None   


#if true return X or O and flag while loop
def checkRows():
  #set up global 
  global playing
  #check for any win from rows 
  row1 = board[0] == board[1] == board[2] != "-"
  row2 = board[3] == board[4] == board[5] != "-"
  row3 = board[6] == board[7] == board[8] != "-"
  #if any row has a match, theres a win 
  if row1 or row2 or row3:
    playing = False
  if row1:
    return board[0]
  elif row2:
    return board[3]
  elif row3:
    return board[6]
  else:
    return None
    

def checkCols():
  global playing
  #check for any win from cols 
  col1 = board[0] == board[3] == board[6] != "-"
  col2 = board[1] == board[4] == board[7] != "-"
  col3 = board[2] == board[5] == board[8] != "-"
  #if any row has a match, theres a win 
  if col1 or col2 or col3:
    playing = False
  if col1:
    return board[0]
  elif col2:
    return board[1]
  elif col3:
    return board[2]
  else:
    return None

def checkDiags():
  global playing
  #check for any win from rows 
  diag1 = board[0] == board[4] == board[8] != "-"
  diag2 = board[6] == board[4] == board[2] != "-"
  #if any row has a match, theres a win 
  if diag1 or diag2:
    playing = False
  if diag1:
    return board[0]
  elif diag2:
    return board[6] 
  else:
    return None 

#Funtion to check for a tie 
def checkTie():
  global playing 
  if "-" not in board:
    playing = False
    return True
  else:
    return False


#Function to switch my players 
def switchPlayer():
  #set up global 
  global current
  #if X is playing, next is O
  if current == "X":
    current = "0"
  #if O is playing switch to X 
  elif current == "0":
    current = "X"    

#start full game     
play()
#-----------TIC TAC TOE-----------------#
    
 
