#!/usr/bin/python

#A recreation of connect4 in Python
#Based upon https://github.com/firegodjr/connect4
#Designed to run in the terminal
#Written by firegodjr

import math
import sys

#Class of dynamic prompts
class prompts:
    def playerMsg(player, message="Please input your chosen slot"):
        return "Please input your chosen slot, Player " + plChar(player) + "\n: "
    def invalidInput(input, message="Invalid input"):
        return message + ": " + str(input)
    def delLastLine():
        CURSOR_UP_ONE = '\x1b[1A'
        ERASE_LINE = '\x1b[2K'
        print(CURSOR_UP_ONE + ERASE_LINE)

#Validator class
class vdr:
    #Check user input
    def chkuin(s):
        snum = int(s)
        return len(s) == 1 \
            and not math.isnan(snum) \
            and not snum > 7 \
            and not snum < 1

playerturn = 0
board = []
for i in range(6):
    board.append([])
    for j in range(7):
        board[i].append(0)

def startGame():
    playerturn = 1
    handleInput(playerturn)

# Handles coin-drop input
def handleInput(player):
    valid = False
    uinput = ""

    #Validates slot input
    uinput = input(prompts.playerMsg(player))
    valid = vdr.chkuin(uinput)
    while not valid:
        renderBoard()
        print(prompts.invalidInput(uinput))
        uinput = input(prompts.playerMsg(player))
        valid = vdr.chkuin(uinput)

#Board Management

def getNextEmptySlot(slot):
    for i in range(6)
        board[slot][]

#Visual Utilities

def plChar(n):
    if n == 1:
        return "X"
    elif n == 2:
        return "O"
    else:
        return " "

def renderBoard():
    print("")
    for i in range(1, 8):
        print("", end=" ")
        print(str(i), end=" ")
    for row in board:
        print("")
        for col in row:
            print("[" + plChar(col) + "]", end="")
    print("\n")

renderBoard()
startGame()
