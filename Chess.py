# -*- coding: utf-8 -*-
from tkinter import *
import time
import copy
class Piece(object):
    def __init__(self,row,col,color):
        self.row = row
        self.col = col
        self.color = color


class Pawn(Piece):
    def getString(self):
        if self.color == "white":
            return "wp"
        else:
            return "bp"
    def isLegal(self,data,oldRow,oldCol,newRow,newCol):
        if newRow == oldRow and newCol == oldCol:

            return False

        if self.color == "white": # can't move backwards
            if newRow > oldRow:
                return False

            if oldRow == 6 and newRow == 4 and oldCol == newCol and data.board.board[newRow][newCol] == None: # go two steps on first move
                if data.board.board[5][oldCol] == None:
                    return True

        if self.color == "black": # can't move backwards
            if newRow < oldRow:
                return False

            if oldRow == 1 and newRow == 3 and oldCol == newCol and data.board.board[newRow][newCol] == None: # go two steps on first move
                if data.board.board[2][oldCol] == None:
                    return True

        if newRow == oldRow - 1 and newCol == oldCol and data.board.board[newRow][newCol] == None\
        and data.board.board[oldRow][oldCol].color == "white": # one step forward
            return True

        elif newRow == oldRow + 1 and newCol == oldCol and data.board.board[newRow][newCol] == None\
        and data.board.board[oldRow][oldCol].color == "black": # one step forward
            return True

        elif newRow == oldRow - 1:
            if newCol == oldCol - 1 or newCol == oldCol + 1:
                if data.board.board[newRow][newCol] != None:
                    return True

        elif newRow == oldRow + 1:
            if newCol == oldCol - 1 or newCol == oldCol + 1:
                if data.board.board[newRow][newCol] != None:
                    return True

        return False

class Knight(Piece):
    def getString(self):
        if self.color == "white":
            return "wh"
        else:
            return "bh"

    def isLegal(self,data,oldRow,oldCol,newRow,newCol):
        if data.board.board[newRow][newCol] != None:
            if data.board.board[oldRow][oldCol].color == data.board.board[newRow][newCol].color:
                return False # can't kill it's own pieces

        if newRow == oldRow and newCol == oldCol:
            return False

        if (newRow == oldRow - 2 and newCol == oldCol - 1) or (newRow == oldRow - 2 and newCol == oldCol + 1):
            return True

        elif (newRow == oldRow + 2 and newCol == oldCol + 1) or (newRow == oldRow + 2 and newCol == oldCol - 1):
            return True

        elif (newCol == oldCol + 2 and newRow == oldRow - 1) or (newCol == oldCol + 2 and newRow == oldRow + 1):
            return True

        elif (newCol == oldCol - 2 and newRow == oldRow - 1) or (newCol == oldCol - 2 and newRow == oldRow + 1):
            return True

        return False

class King(Piece):
    def getString(self):
        if self.color == "white":
            return "wk"
        else:
            return "bk"
    def isLegal(self,data,oldRow,oldCol,newRow,newCol):

        try:


            if data.board.board[newRow][newCol] != None:
                if data.board.board[newRow][newCol].color == data.board.board[oldRow][oldCol].color:
                    return False

            if newRow == oldRow and newCol == oldCol:
                return False

            if newRow == oldRow + 1 and newCol == oldCol: # up
                return True

            elif newRow == oldRow - 1 and newCol == oldCol: # down
                return True

            elif newRow == oldRow and newCol == oldCol + 1: # right
                return True

            elif newRow == oldRow and newCol == oldCol - 1: # left
                return True

            elif newRow == oldRow - 1 and newCol == oldCol - 1: # diagonal
                return True

            elif newRow == oldRow + 1 and newCol == oldCol + 1: # diagonal
                return True

            elif newRow == oldRow - 1 and newCol == oldCol + 1: # diagonal
                return True

            elif newRow == oldRow + 1 and newCol == oldCol - 1: # diagonal
                return True

            return False

        except IndexError: # can't move outside of the board, so return False
            return False

class Queen(Piece):
    def getString(self):
        if self.color == "white":
            return "wq"
        else:
            return "bq"
    def isLegal(self,data,oldRow,oldCol,newRow,newCol):

        if data.board.board[newRow][newCol] != None:
            if data.board.board[newRow][newCol].color == data.board.board[oldRow][oldCol].color:
                return False

        if newRow == oldRow and newCol == oldCol:
            return False

        if abs(newRow - oldRow) == abs(newCol - oldCol): # diagonal move
            for x in range(1,abs(newRow - oldRow)): # checks to see if path is blocked
                if newCol < oldCol and newRow < oldRow: # top left diagonal
                    if data.board.board[oldRow - x][oldCol - x] != None:
                        return False

                if newCol > oldCol and newRow > oldRow: # bottom right diagonal
                    if data.board.board[oldRow + x][oldCol + x] != None:
                        return False

                if newCol < oldCol and newRow > oldRow: # bottom left diagonal
                    if data.board.board[oldRow + x][oldCol - x] != None:
                        return False

                if newCol > oldCol and newRow < oldRow: # top right diagonal
                    if data.board.board[oldRow - x][oldCol + x] != None:
                        return False

            return True

        elif newRow == oldRow: # left - right
            for x in range(1,abs(newCol - oldCol)): # checks to see if path is blocked
                if newCol > oldCol:
                    if data.board.board[oldRow][oldCol + x] != None:
                        return False

                if newCol < oldCol:
                    if data.board.board[oldRow][oldCol - x] != None:
                        return False

            return True

        elif newCol == oldCol: # up - down
            for x in range(1,abs(newRow - oldRow)): # checks to see if path is blocked
                if newRow > oldRow:
                    if data.board.board[oldRow + x][oldCol] != None:
                        return False

                if newRow < oldRow:
                    if data.board.board[oldRow - x][oldCol] != None:
                        return False

            return True

        return False

class Bishop(Piece):
    def getString(self):
        if self.color == "white":
            return "wb"
        else:
            return "bb"

    def isLegal(self,data,oldRow,oldCol,newRow,newCol):


        if data.board.board[newRow][newCol] != None:
            if data.board.board[newRow][newCol].color == data.board.board[oldRow][oldCol].color:
                return False

        if newRow == oldRow and newCol == oldCol:
            return False

        if abs(newRow - oldRow) == abs(newCol - oldCol): # diagonal move
            for x in range(1,abs(newRow - oldRow)): # checks to see if path is blocked
                if newCol < oldCol and newRow < oldRow: # top left diagonal
                    if data.board.board[oldRow - x][oldCol - x] != None:
                        return False

                if newCol > oldCol and newRow > oldRow: # bottom right diagonal
                    if data.board.board[oldRow + x][oldCol + x] != None:
                        return False

                if newCol < oldCol and newRow > oldRow: # bottom left diagonal
                    if data.board.board[oldRow + x][oldCol - x] != None:
                        return False

                if newCol > oldCol and newRow < oldRow: # top right diagonal
                    if data.board.board[oldRow - x][oldCol + x] != None:
                        return False

            return True

        return False

class Rook(Piece):
    def getString(self):
        if self.color == "white":
            return "wr"
        else:
            return "br"

    def isLegal(self,data,oldRow,oldCol,newRow,newCol):
        if data.board.board[newRow][newCol] is not None and data.board.board[newRow][newCol] != None :
            if data.board.board[newRow][newCol].color == data.board.board[oldRow][oldCol].color:
                return False
        #if isBlockedRow(data,oldRow,oldCol):
        #    return False

        if newRow == oldRow and newCol == oldCol:
            return False

        if newRow == oldRow: # left - right
            for x in range(1,abs(newCol - oldCol)): # checks to see if path is blocked
                if newCol > oldCol:
                    if data.board.board[oldRow][oldCol + x] != None:
                        return False

                if newCol < oldCol:
                    if data.board.board[oldRow][oldCol - x] != None:
                        return False

            return True

        if newCol == oldCol: # up - down
            for x in range(1,abs(newRow - oldRow)): # checks to see if path is blocked
                if newRow > oldRow:
                    if data.board.board[oldRow + x][oldCol] != None:
                        return False

                if newRow < oldRow:
                    if data.board.board[oldRow - x][oldCol] != None:
                        return False

            return True

        return False

class Board(object):
    def nextCheckPos(data,oldRow,oldCol,newRow,newCol):
        newBoard = copy.deepcopy(data.board.board)
        newBoard[newRow][newCol] = newBoard[oldRow][oldCol]
        newBoard[oldRow][oldCol] = None
        moves = get_available_moves(data)

        for move in moves:
            if newRow == moves[2] and newCol == moves[3]:
                return True

        return False

    def inCheck(self,data):

        for king in range(len(data.kings)): # find out if the king is in check
            for row1 in range(8):
                for col1 in range(8):
                    if data.board.board[row1][col1] != None:
                        if data.board.board[row1][col1].isLegal(data,row1,col1,data.kings[king][0],data.kings[king][1])\
                        and data.board.board[row1][col1].color != data.board.board[data.kings[king][0]][data.kings[king][1]].color:
                            data.checkColor = data.board.board[row1][col1].color
                            data.checkRow = row1
                            data.checkCol =  col1
                            return True


        return False

    def inCheckmate(self,data): # True if king is in check and spots around him are illegal
        data.kings = []

        for row in range(8): # find the position of the kings
            for col in range(8):
                if type(data.board.board[row][col]) == King:
                    data.kings.append((row,col,data.board.board[row][col].color))

        if data.board.inCheck(data) == True:
            data.inCheck = True



        if data.inCheck == True: # checks to see if king can move anywhere around it
            newBoard = copy.deepcopy(data.board.board)


            moves = get_available_moves(data,newBoard)



            for king in range(len(data.kings)):
                count = 0
                for move in moves:
                    if move[0] == data.kings[king][0] and move[1] == data.kings[king][1]:
                        for move2 in moves:
                            if move2[0] == data.kings[king][0] and move2[1] == data.kings[king][1] and move2[2] != move[2] and move2[3] != move[3]:
                                return False

                    

            return True


    def nextCheckPos(data,oldRow,oldCol,newRow,newCol):
        newBoard = copy.deepcopy(data.board.board)
        newBoard[newRow][newCol] = newBoard[oldRow][oldCol]
        newBoard[oldRow][oldCol] = None
        moves = get_available_moves(data)

        for move in moves:
            if newRow == moves[2] and newCol == moves[3]:
                return True

        return False

    def getCellWidth(self,data):
        return data.width/self.cols

    def getCellHeight(self,data):
        return data.height/self.rows

    def __init__(self, board = [[None]*8 for x in range(8)]): # rows start at the top of the board
        self.rows = 8
        self.cols = 8
        self.board = board

        if board == [[None]*8 for x in range(8)]:
            for row in range(self.rows):
                for col in range(self.cols):
                    if row == 6: # White pawns
                        self.board[row][col] = Pawn(row,col,"white")

                    elif row == 1: # black pawns
                        self.board[row][col] = Pawn(row,col,"black")

                    elif (row == 0 and col == 0) or (row == 0 and col == 7):
                        self.board[row][col] = Rook(row,col,"black") # black rooks

                    elif (row == 7 and col == 0) or (row == 7 and col == 7):
                        self.board[row][col] = Rook(row,col,"white") # white rooks

                    elif  (row == 0 and col == 1) or (row == 0 and col == 6):
                        self.board[row][col] = Knight(row,col,"black") # black knight

                    elif (row == 7 and col == 1) or (row == 7 and col == 6):
                        self.board[row][col] = Knight(row,col,"white") # white knight

                    elif  (row == 0 and col == 2) or (row == 0 and col == 5):
                        self.board[row][col] = Bishop(row,col,"black") # black bishop

                    elif (row == 7 and col == 2) or (row == 7 and col == 5):
                        self.board[row][col] = Bishop(row,col,"white") # white bishop

                    elif  (row == 0 and col == 3): # black queen
                        self.board[row][col] = Queen(row,col,"black")

                    elif (row == 7 and col == 3): # white queen
                        self.board[row][col] = Queen(row,col,"white")

                    elif  (row == 0 and col == 4): # black king
                        self.board[row][col] = King(row,col,"black")

                    elif (row == 7 and col == 4): # white king
                        self.board[row][col] = King(row,col,"white")


    def displayBoard(self,canvas,data): # draws black & white grid from top-left down
        cellWidth = data.width/self.cols
        cellHeight = data.height/self.rows
        data.board.board = self.board

        for row in range(self.rows):
            for col in range(self.cols):
                if (row + col) % 2 == 0:
                    canvas.create_rectangle(row*cellWidth,col*cellHeight,(row+1)*cellWidth,(col+1)*cellHeight, fill = "black")
                else:
                    canvas.create_rectangle(row*cellWidth,col*cellHeight,(row+1)*cellWidth,(col+1)*cellHeight, fill = "white")

def init(data):
    data.onStart = True
    data.displayInstructions = False
    data.board = Board()
    data.isWhiteTurn = True
    data.withAI = True
    data.inCheck = False
    data.gameOver = False

    data.newSelectedRow = None
    data.newSelectedCol = None
    data.lastSelectedRow = None
    data.lastSelectedCol = None

    data.minDepth = 0
    data.maxDepth = 0
    data.depth = 0
    data.AIDifficulty = 4 # default difficulty is medium

    data.moveHistory3 = [] # AI cannot repeat the same move 3 consecutive times
                           # because that is a draw by chess rules


    data.whitePawn = PhotoImage(file = "white_pawn.gif") # all of these pieces found at: http://s1192.photobucket.com/user/Greatday2die/media/2D%20Symbols/DGTChessPieces_zps6c43ca08.png.html
    data.whiteBishop = PhotoImage(file = "white_bishop.gif")
    data.whiteQueen = PhotoImage(file = "white_queen.gif")
    data.whiteKing = PhotoImage(file = "white_king.gif")
    data.whiteRook = PhotoImage(file = "white_rook.gif")
    data.whiteKnight = PhotoImage(file = "white_knight.gif")

    data.blackPawn = PhotoImage(file = "black_pawn.gif")
    data.blackBishop = PhotoImage(file = "black_bishop.gif")
    data.blackQueen = PhotoImage(file = "black_queen.gif")
    data.blackKing = PhotoImage(file = "black_king.gif")
    data.blackRook = PhotoImage(file = "black_rook.gif")
    data.blackKnight = PhotoImage(file = "black_knight.gif")


    data.checkMateImages = []

    data.foolsMate = PhotoImage(file = "Fools_Mate.gif") # all images found at: http://www.chess-game-strategies.com/famous-checkmates.html
    data.scholarsMate = PhotoImage(file = "Scholars_Mate.gif")
    data.bsmMate = PhotoImage(file = "bsm_mate.gif")
    data.hippoMate = PhotoImage(file = "hippo_mate.gif")
    data.legallsMate = PhotoImage(file = "legalls_mate.gif")
    data.seaMate = PhotoImage(file = "sea_mate.gif")
    data.smotheredMate = PhotoImage(file = "smothered_mate.gif")
    data.smotheredMate2 = PhotoImage(file = "smothered_different_mate.gif")







    data.checkMateImages.append(data.foolsMate)
    data.checkMateImages.append(data.scholarsMate)
    data.checkMateImages.append(data.bsmMate)
    data.checkMateImages.append(data.hippoMate)
    data.checkMateImages.append(data.legallsMate)
    data.checkMateImages.append(data.seaMate)
    data.checkMateImages.append(data.smotheredMate)
    data.checkMateImages.append(data.smotheredMate2)


    data.InstructionsText = """
                                                            \tObjective Of The Game:
    The objective of the game is to "checkmate" an opponent’s king.
    A checkmate is defined as a position held by a king wherein if he does not move, then he
    remains under attack. However, a checkmate also requires that any available position that
    the king is able to move into will place him immediately under attack by another piece.
    So, a checkmate just means the king is trapped, poor king. \n \n

                                                            \tHow Pieces Move:
    - The king can only move one space in any direction

    - The queen can move as many spaces as she wants in any direction (up, down, diagonally, left, right)
      as long as they’re empty or she’s attacking

    - The rook can move for as many spaces as it likes up, down, left, or right, but NOT diagonally

    - The bishop ONLY moves diagonally but it can move for as many spaces as it likes

    - The knight is unique in that it does not move in a straight line. The knight can move in any direction
      as long as it goes two cells in the same direction (these two can’t be diagonal) and then goes one cell
      either left or right (or up or down depending on how it’s facing)

    - The pawn is a sad piece… It can only move up a space. Unless it’s attacking, when it can only attack
      diagonally
    """ # the instructions were taken from my proposal where I wrote the same instructions


def get_available_moves(data,board):
    moves = []
    for row in range(8):
        for col in range(8):
            if board[row][col] is not None and board[row][col] != None:
                for row1 in range(8):
                    for col1 in range(8):

                        try:
                            if board[row][col].color == "black" and board[row][col].isLegal(data,row,col,row1,col1):
                                moves.append((row,col,row1,col1))

                        except AttributeError:
                            pass


    return moves

def evaluate(data,board): # citations for this included at the bottom alongside minimax
    summ = 0
    for row in range(8):
        for col in range(8):
            if board[row][col] != None:
                if type(board[row][col]) == King:
                    if board[row][col].color == "black":
                        summ += 200

                    if board[row][col].color == "white":
                        summ -= 100 # AI is made to be defensive so these values are lower


                elif type(board[row][col]) == Queen:
                    if board[row][col].color == "black":
                        summ += 150

                    if board[row][col].color == "white":
                        summ -= 75



                elif type(board[row][col]) == Bishop:
                    if board[row][col].color == "black":
                        summ += 50

                    if board[row][col].color == "white":
                        summ -= 30


                elif type(board[row][col]) == Knight:
                    if board[row][col].color == "black":
                        summ += 50

                    if board[row][col].color == "white":
                        summ -= 30


                elif type(board[row][col]) == Rook:
                    if board[row][col].color == "black":
                        summ += 50

                    if board[row][col].color == "white":
                        summ -= 30

                elif type(board[row][col]) == Pawn:
                    if board[row][col].color == "black":
                        summ += 1

                    if board[row][col].color == "white":
                        summ -= 1


    return summ



def next_state(data,move):
    newBoard = copy.deepcopy(data.board.board)
    newBoard[move[2]][move[3]] = newBoard[move[0]][move[1]]
    newBoard[move[0]][move[1]] = None
    return newBoard




def mousePressed(event, data):
    if data.onStart:
        pass # clicking on the start button in the initial page registers a click, that click must be ignored

    else:
        for row in range(len(data.board.board)):
            for col in range(len(data.board.board[row])):
                if event.x > col*data.board.getCellWidth(data) and event.x < (col+1)*data.board.getCellWidth(data) \
                and event.y > row*data.board.getCellHeight(data) and event.y < (row+1)*data.board.getCellHeight(data): # finds the piece that is clicked on by the player

                    data.lastSelectedCol = data.newSelectedCol
                    data.lastSelectedRow = data.newSelectedRow

                    data.newSelectedRow = row
                    data.newSelectedCol = col


def restart(data):
    time.sleep(.1) # .1 second delay so the transition to new game is smoother
    init(data)

def keyPressed(event, data):
    pass

def isLegalMove(data):
    if data.board.board[data.lastSelectedRow][data.lastSelectedCol] != None:

        if data.board.board[data.newSelectedRow][data.newSelectedCol] != None: # checks if attacking opposite color
            if data.board.board[data.lastSelectedRow][data.lastSelectedCol].color == data.board.board[data.newSelectedRow][data.newSelectedCol].color:
                return False

        if type(data.board.board[data.lastSelectedRow][data.lastSelectedCol]) == Pawn: # checks legality of pawn move
            if data.board.board[data.lastSelectedRow][data.lastSelectedCol].isLegal(data,data.lastSelectedRow,data.lastSelectedCol,data.newSelectedRow,data.newSelectedCol):
                return True

        elif type(data.board.board[data.lastSelectedRow][data.lastSelectedCol]) == Knight: # checks legality of Knight move
            if data.board.board[data.lastSelectedRow][data.lastSelectedCol].isLegal(data,data.lastSelectedRow,data.lastSelectedCol,data.newSelectedRow,data.newSelectedCol):
                return True

        elif type(data.board.board[data.lastSelectedRow][data.lastSelectedCol]) == Queen: # checks legality of Queen move
            if data.board.board[data.lastSelectedRow][data.lastSelectedCol].isLegal(data,data.lastSelectedRow,data.lastSelectedCol,data.newSelectedRow,data.newSelectedCol):
                return True

        elif type(data.board.board[data.lastSelectedRow][data.lastSelectedCol]) == King: # checks legality of King move
            if data.board.board[data.lastSelectedRow][data.lastSelectedCol].isLegal(data,data.lastSelectedRow,data.lastSelectedCol,data.newSelectedRow,data.newSelectedCol):
                return True

        elif type(data.board.board[data.lastSelectedRow][data.lastSelectedCol]) == Bishop: # checks legality of Bishop move
            if data.board.board[data.lastSelectedRow][data.lastSelectedCol].isLegal(data,data.lastSelectedRow,data.lastSelectedCol,data.newSelectedRow,data.newSelectedCol):
                return True

        elif type(data.board.board[data.lastSelectedRow][data.lastSelectedCol]) == Rook: # checks legality of Rook move
            if data.board.board[data.lastSelectedRow][data.lastSelectedCol].isLegal(data,data.lastSelectedRow,data.lastSelectedCol,data.newSelectedRow,data.newSelectedCol):
                return True

def timerFired(data):
    if data.board.inCheckmate(data):
        data.gameOver = True
        return

    if data.isWhiteTurn == False and data.withAI == True:
        nBoard = copy.deepcopy(data.board.board)
        bestMove = minimax(data)
        nBoard[bestMove[2]][bestMove[3]] = nBoard[bestMove[0]][bestMove[1]]
        nBoard[bestMove[0]][bestMove[1]] = None

        data.board = Board(nBoard)
        data.isWhiteTurn = True
        return

    if (data.isWhiteTurn == True and data.withAI == True) or (data.withAI == False):
        if data.lastSelectedRow != None and data.lastSelectedCol != None: # if with AI should encompass this and then copy paste below when not with AI

            if data.newSelectedRow != None and data.newSelectedCol != None:

                newBoard = copy.deepcopy(data.board.board)

                if isLegalMove(data):
                    data.inCheck = False
                    if data.withAI == False: # in two player mode, check whose turn it is
                        if data.isWhiteTurn == True and data.board.board[data.lastSelectedRow][data.lastSelectedCol].color == "white":
                            newBoard[data.lastSelectedRow][data.lastSelectedCol] = None
                            newBoard[data.newSelectedRow][data.newSelectedCol] = data.board.board[data.lastSelectedRow][data.lastSelectedCol]
                            data.isWhiteTurn = not data.isWhiteTurn

                        elif data.isWhiteTurn == False and data.board.board[data.lastSelectedRow][data.lastSelectedCol].color == "black":
                            newBoard[data.lastSelectedRow][data.lastSelectedCol] = None
                            newBoard[data.newSelectedRow][data.newSelectedCol] = data.board.board[data.lastSelectedRow][data.lastSelectedCol]
                            data.isWhiteTurn = not data.isWhiteTurn

                    else: # playing against AI
                        newBoard[data.lastSelectedRow][data.lastSelectedCol] = None
                        newBoard[data.newSelectedRow][data.newSelectedCol] = data.board.board[data.lastSelectedRow][data.lastSelectedCol]
                        data.isWhiteTurn = not data.isWhiteTurn

                data.lr = data.lastSelectedRow
                data.nc = data.lastSelectedCol
                data.nr = data.newSelectedRow
                data.lc = data.lastSelectedCol

                data.newSelectedRow = None # next 100 milliseconds, if no mouse click, newSelectedRow == lastSelectedRow if this doesn't happen
                data.newSelectedCol = None

                data.lastSelectedRow = None # same as above
                data.lastSelectedCol = None

                data.board = Board(newBoard)

def startGame(data):
    data.onStart = False

def AIOn(data): # turn AI on
    data.withAI = True

def easyAI(data):
    data.AIDifficulty = 2 # number of moves ahead it will simulate

def mediumAI(data):
    data.AIDifficulty = 4

def hardAI(data):
    data.AIDifficulty = 6


def VSPlayer(data):# Turn AI off to player 2 player mode
    data.withAI = False

def drawInstructions(data):
    data.displayInstructions = not data.displayInstructions

def findImage(data):
    imageNum = time.strftime("%d/%m/%Y") # note: day/month/year format
    try:
        hashNum = int(imageNum[0:2]) # try to see if it's a 2-digit number that doesn't start with 0
    except:
        pass
    else:
        hashNum = int(imageNum[1:2]) # if not two digit, it starts with zero(ex: the value is "04") so take the second digit only
    return data.checkMateImages[hashNum%len(data.checkMateImages)] # the above implementation assumes the length of checkMateImages is <= 99

def redrawAll(canvas, data):

    # if data.onStart press 'a' to play against AI and 'p' to play against another player
    if data.onStart:
        if data.displayInstructions == True: # instructions clicked on when on front page
            canvas.create_rectangle(0,0, data.width, data.height, fill = "white")
            canvas.create_text(11*data.width/24 + 5, 3*data.height/8, text = data.InstructionsText)

        else: # creates (and redraws) front page
            canvas.create_text(data.width/2, data.height/8, text = "Welcome to Chess!", font = ("Helvetica",42))
            canvas.create_text(data.width/2, data.height - 10, text = "A Carlos Gonzalez Production")
            canvas.create_text(data.width/2,7*data.height/8 - 20, text = "Checkmate of the day", font = ("Helvetica",24))
            canvas.create_text(data.width/2,11*data.height/12, text = "To play against another player, click VS. Player then click start\n\nTo play against an AI: click VS. AI, then easy, medium or hard. Then click start!", font = ("Comic Sans",14), fill = "red")
            # there are only 8 different "checkmate of the day" pictures, but it's still a cool feature and it's easy to add more
            # I just didn't have time to find more. They do actually cycle by day :)
            canvas.create_image(data.width/2,data.height/2,image = findImage(data))

    elif (data.displayInstructions == True):
        # Instructions are just created on top of whatever canvas you are on, and then gets deleted, giving illusion of going back to same place
        canvas.create_rectangle(0,0, data.width, data.height, fill = "white")
        canvas.create_text(11*data.width/24 + 5, data.height/2, text = data.InstructionsText)


    else:
        data.board.displayBoard(canvas,data) # draws grid

        for row in range(data.board.rows):
            for col in range(data.board.cols):
                if data.board.board[row][col] != None:
                    if data.board.board[row][col].getString() == "wp": # re-draw remaining white pawns
                        canvas.create_image(data.board.getCellHeight(data)*col+data.board.getCellHeight(data)/2,data.board.getCellWidth(data)*row+data.board.getCellWidth(data)/2,image = data.whitePawn)

                    elif data.board.board[row][col].getString() == "bp": # re-draw remaining black pawns
                        canvas.create_image(data.board.getCellHeight(data)*col+data.board.getCellHeight(data)/2,data.board.getCellWidth(data)*row+data.board.getCellWidth(data)/2,image = data.blackPawn)

                    elif data.board.board[row][col].getString() == "wk":
                        canvas.create_image(data.board.getCellHeight(data)*col+data.board.getCellHeight(data)/2,data.board.getCellWidth(data)*row+data.board.getCellWidth(data)/2,image = data.whiteKing)

                    elif data.board.board[row][col].getString() == "bk":
                        canvas.create_image(data.board.getCellHeight(data)*col+data.board.getCellHeight(data)/2,data.board.getCellWidth(data)*row+data.board.getCellWidth(data)/2,image = data.blackKing)

                    elif data.board.board[row][col].getString() == "wh":
                        canvas.create_image(data.board.getCellHeight(data)*col+data.board.getCellHeight(data)/2,data.board.getCellWidth(data)*row+data.board.getCellWidth(data)/2,image = data.whiteKnight)

                    elif data.board.board[row][col].getString() == "bh":
                        canvas.create_image(data.board.getCellHeight(data)*col+data.board.getCellHeight(data)/2,data.board.getCellWidth(data)*row+data.board.getCellWidth(data)/2,image = data.blackKnight)

                    elif data.board.board[row][col].getString() == "wq":
                        canvas.create_image(data.board.getCellHeight(data)*col+data.board.getCellHeight(data)/2,data.board.getCellWidth(data)*row+data.board.getCellWidth(data)/2,image = data.whiteQueen)

                    elif data.board.board[row][col].getString() == "bq":
                        canvas.create_image(data.board.getCellHeight(data)*col+data.board.getCellHeight(data)/2,data.board.getCellWidth(data)*row+data.board.getCellWidth(data)/2,image = data.blackQueen)

                    elif data.board.board[row][col].getString() == "wb":
                        canvas.create_image(data.board.getCellHeight(data)*col+data.board.getCellHeight(data)/2,data.board.getCellWidth(data)*row+data.board.getCellWidth(data)/2,image = data.whiteBishop)

                    elif data.board.board[row][col].getString() == "bb":
                        canvas.create_image(data.board.getCellHeight(data)*col+data.board.getCellHeight(data)/2,data.board.getCellWidth(data)*row+data.board.getCellWidth(data)/2,image = data.blackBishop)

                    elif data.board.board[row][col].getString() == "wr":
                        canvas.create_image(data.board.getCellHeight(data)*col+data.board.getCellHeight(data)/2,data.board.getCellWidth(data)*row+data.board.getCellWidth(data)/2,image = data.whiteRook)

                    elif data.board.board[row][col].getString() == "br":
                        canvas.create_image(data.board.getCellHeight(data)*col+data.board.getCellHeight(data)/2,data.board.getCellWidth(data)*row+data.board.getCellWidth(data)/2,image = data.blackRook)

        if data.gameOver:
            canvas.create_text(data.width/2,data.height/2 - 20,text = "Checkmate! Click restart to play again", font = ("Helvetica",30), fill = "red")

""" Minimax explained:
The following algorithm, minimax, tries to minimize the amount of damage that
the player who is implementing it takes. In this case, I implemented it with
the computer so the computer tries to take the minimum amount of damage. I did
this by using two helper functions minplay and maxplay which calculate, not
surprisingly, the plays which give the minimum score and maximum score, respectively.
The implemented version below can be thought of like this: every piece gets a
value with the king being the highest and the other pieces in decreasing order of
importance (so a queen is more valuable than a bishop, etc.). The algorithm will
then go through and "simulate" every legal move that can be taken by the current
board. It will then evaluate those boards according to the point system described
above and return the board that minimizes damage for the person who implemented
it. Furthermore, the algorithm can be extended to "simulate" more than one step
ahead, as I have done below depending on the difficulty of the AI. The algorithm
does this by instead of returning a score after the simulation of the first move, it
takes those simulated boards and simulates their legal moves and again evaluates
all of the outcomes. In this way, minimax can be set to simulate "deeper" states,
which increases the intelligence of the AI.
"""
def minimax(data): # citations for mini max are included at the bottom. There were too many to put here.
    newBoard = copy.deepcopy(data.board.board)
    data.depth, data.minDepth, data.maxDepth = 0, 0, 0
    moves = get_available_moves(data,newBoard)
    best_move = moves[0]
    best_score = float('-inf')
    while data.depth < data.AIDifficulty: # number of moves ahead the AI will compute
        data.depth += 1
        for move in moves:
            clone = next_state(data,move)
            score = min_play(data,clone)
            if score > best_score:
                if len(data.moveHistory3) >= 5 and move in data.moveHistory3:
                    data.moveHistory3.append(best_move)
                    data.moveHistory3 = data.moveHistory3[1:] # "forgets" a move once the history is greater than 5
                else: # a move cannot be repeated 3 times
                    best_move = move
                    best_score = score
                    data.moveHistory3.append(best_move)

    return best_move


def min_play(data,clone):
    newBoard = Board(clone)
    if newBoard.inCheck(data) or data.minDepth == data.AIDifficulty:
        return evaluate(data,newBoard.board) # checks to see who won theoretical board and adds points accordingly
    moves = get_available_moves(data,newBoard.board)
    best_score = float('inf')
    while data.minDepth < data.AIDifficulty:
        data.minDepth += 1
        for move in moves:
            clone = next_state(data,move)
            score = max_play(data,clone)
            if score < best_score:
                best_move = move
                best_score = score
    return best_score

def max_play(data,clone):
    newBoard = Board(clone)

    if newBoard.inCheck(data) or data.maxDepth == data.AIDifficulty:
        return evaluate(data,newBoard.board)
    moves = get_available_moves(data,newBoard.board)
    best_score = float('-inf')
    while data.maxDepth < data.AIDifficulty:
        data.maxDepth += 1
        for move in moves:
            clone = next_state(data,move)
            score = min_play(data,clone)
            if score > best_score:
                best_move = move
                best_score = score
    return best_score



def run(width=300, height=300): # run function taken from lecture notes, slightly modified
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.wm_title("Chess")

    data.root = root

    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()

    ##
    buttonFrame = Frame(data.root) # edited from 15-112 spring-17 website
    startButton = Button(buttonFrame, text="Start Game", command=lambda:startGame(data))
    startButton.grid(row=0,column=0)
    instructionsButton = Button(buttonFrame, text="Instructions", command=lambda:drawInstructions(data))
    instructionsButton.grid(row=0,column=1)
    VSAIButton = Button(buttonFrame, text="VS. AI", command=lambda:AIOn(data))
    VSAIButton.grid(row=0,column=3)
    VSPlayerButton = Button(buttonFrame, text="VS. Player", command=lambda:VSPlayer(data))
    VSPlayerButton.grid(row=0,column=2)
    easyAIButton = Button(buttonFrame, text="Easy", command=lambda:easyAI(data))
    easyAIButton.grid(row=0,column=4)
    mediumAIButton = Button(buttonFrame, text="Medium", command=lambda:mediumAI(data))
    mediumAIButton.grid(row=0,column=5)
    hardAIButton = Button(buttonFrame, text="Hard", command=lambda:hardAI(data))
    hardAIButton.grid(row=0,column=6)
    restartButton = Button(buttonFrame, text="Restart", command=lambda:restart(data))
    restartButton.grid(row=0,column=7)

    buttonFrame.pack(side=BOTTOM)

    ##
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 600)

"""
Mini max citations:
I read all of these links when researching minimax. There's pseudo-code in some of them.
In the minimax function, I wrote the get_legal_moves function from scratch, the next_state
function from scratch, and the evaluate function from scratch.

http://chessprogramming.wikispaces.com/Evaluation
http://aima.cs.berkeley.edu/python/games.html
https://chessprogramming.wikispaces.com/Minimax
https://www.naftaliharris.com/blog/chess/
http://giocc.com/concise-implementation-of-minimax-through-higher-order-functions.html

"""
