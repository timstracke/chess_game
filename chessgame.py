from tkinter import *
import string


def create_board():



    #black and white squares
    yi = 50
    for i in range(8):

        xi = 220
        yi +=66
        for j in range(8):

            if (i+j)%2 == 0:
                mcolor = "grey80"
            else:
                mcolor = "grey20"
            b = Label(frame, bg=mcolor, height=4, width=9)
            b.place(x=xi, y=yi)
            b.lower()
            xi += 66

    # numbers left and right of the board
    xi = -440
    for j in range(2):
        yi = 116
        xi += 594
        for i in range(8):
            b = Label(frame, height=4, width=9, text=str(i+1))
            b.place(x=xi, y=yi)
            b.lower()
            yi += 66


    # letters above and under the board
    abc = string.ascii_uppercase
    yi = -544
    for j in range(2):
        yi += 594
        xi = 220
        for i in range(8):
            b = Label(frame, height=4, width=9, text=abc[i])
            b.place(x=xi, y=yi)
            xi += 66





def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)




def button_click():

    From = FromEntry.get()
    To = ToEntry.get()
    print("NEW MOVE________________________________________")
    print(To)
    print(From)
    # function for the whole move
    if board[From][1] == turn[0]:
        if board[From][0](From, To):
            Feedback["text"] = "Make your move!"
            move(From, To)

        else:
            Feedback["text"] = "Invalid move!"
    else:
        Feedback["text"] = "Invalid move!"
    Empty.place_forget()







def WCheck():
    for position, value in board.items():
        if value[2] == WKing:
            King_pos = position
            break
    for position, value in board.items():
        if value[1]:
            print(position + ":  " + value[1])
        if value[1] == "b":
            print(value[0])
            if value[0](position, King_pos):
                print("CHECK: " + position)
                return True

    return False

def BCheck():
    for position, value in board.items():
        if value[2] == BKing:
            King_pos = position
            break
    for position, value in board.items():
        if value[1] == "w" and value[2] != Empty and value[0] != None:
            print(position)
            if value[0](position, King_pos):
                print("CHECK: " + position)
                return True

    return False


def GameOver():

    GOLabel.place(x=100, y=720)

    if turn[0] == "w":
        GOLabel["text"]="CHECK MATE \nWHITE WINS"
        GOLabel["bg"]="white"
        GOLabel["fg"] = "black"
    else:
        GOLabel["text"]="CHECK MATE \nBLACK WINS"
        GOLabel["bg"] = "black"
        GOLabel["fg"] = "white"






def Pawn(From, To):
    if board[From][1] == "w":                       # white pawn
        if board[From][3][0] == board[To][3][0] and board[From][3][1] == step + board[To][3][1] and board[From][1] == "w" and board[To][2] == Empty:   #x=x and yF = step + yT and farbe weiß and feld leer, one-stepper

            return True
        elif board[From][3][0] == board[To][3][0] and board[From][3][1] == 2*step + board[To][3][1] and board[From][1] == "w" and board[To][2] == Empty:    #two-stepper
            if board[From[0] + str(int((0.5*(int(From[1])+int(To[1])))))][2] == Empty:                                                                  #nothing between two-stepper
                return True
            else:
                return False
        elif (board[From][3][0] + step == board[To][3][0] or board[From][3][0] - step == board[To][3][0]) and board[From][3][1] == board[To][3][1] + step and board[From][1] == "w" and board[To][1] == "b":        #attack
            return True
        else:
            return False

    elif board[From][1] == "b":                     # black pawn
        if board[From][3][0] == board[To][3][0] and board[From][3][1] == board[To][3][1] - step and board[From][1] == "b" and board[To][2] == Empty:  # x=x and yF = step + yT and farbe weiß and feld leer, one-stepper
            return True
        elif board[From][3][0] == board[To][3][0] and board[From][3][1] == board[To][3][1] - 2 * step and board[From][1] == "b" and board[To][2] == Empty:      #two-stepper
            if board[From[0] + str(int((0.5 * (int(From[1]) + int(To[1])))))][2] == Empty:                                                              #nothing between two-stepper
                return True
            else:
                return False
        elif (board[From][3][0] + step == board[To][3][0] or board[From][3][0] - step == board[To][3][0]) and board[From][3][1] == board[To][3][1] - step and board[From][1] == "b" and board[To][1] == "w":        #attack
            return True
        else:
            return False
    else:
        return False

def Rook(From, To):
    c = 0

    if board[From][3][1] == board[To][3][1]:                        # Rook move on x
        if abs(board[From][3][0] - board[To][3][0]) == 66:          # if next to each other
            if board[To][1] != board[From][1] or board[To][2] == Empty:
                return True


        else:
            for position, value in board.items():           # check if any pieces between From and To
                if From[1] == position[1] and (position[0] in char_range(From[0], To[0]) or position[0] in char_range(To[0], From[0])) and position != From and position != To:
                    if value[2] == Empty:
                         c += 66

                    else:
                        return False

    if c != 0 and c + 66 == abs(board[From][3][0] - board[To][3][0]):
        if board[To][1] != board[From][1]:
            return True


    c = 0
    if board[From][3][0] == board[To][3][0]:                    # Rook move on y
        if abs(board[From][3][1] - board[To][3][1]) == 66:      # if next to each other
            if board[To][1] != board[From][1] or board[To][2] == Empty:
                return True


        else:
            for position, value in board.items():
                #print(range(int(From[1]) + 1, int(To[1])))
                print(position)
                if From[0] == position[0] and (int(position[1]) in range(int(From[1]) + 1, int(To[1])) or int(position[1]) in range(int(To[1]) + 1, int(From[1]))):

                    if value[2] == Empty:
                        c += 66
                        print("C")
                    else:
                        return False

    if c != 0 and c + 66 == abs(board[From][3][1] - board[To][3][1]):
        if board[To][1] != board[From][1] or board[To][2] == Empty:
            return True



def Knight(From, To):
    if abs(board[From][3][0] - board[To][3][0]) == step and abs(board[From][3][1] - board[To][3][1]) == 2*step:         # long y
        if board[To][1] != board[From][1] or board[To][2] == Empty:
            return True


    elif abs(board[From][3][0] - board[To][3][0]) == 2*step and abs(board[From][3][1] - board[To][3][1]) == step:       # long x
        if board[To][1] != board[From][1] or board[To][2] == Empty:
            return True

    else:
        return False



def Bishop(From, To):
    c = 0

    if abs(board[From][3][0] - board[To][3][0]) == abs(board[From][3][1] - board[To][3][1]):        # going the same distance on x and y
        if abs(board[From][3][0] - board[To][3][0]) == 66:                                          # if next to each other
            if board[To][1] != board[From][1] or board[To][2] == Empty:
                return True

        else:

            if int(To[1]) - int(From[1]) < 0 and string.ascii_uppercase.index(To[0]) - string.ascii_uppercase.index(From[0]) < 0:       #left top
                for position, value in board.items():
                    if From[0] > position[0] > To[0]:
                        if int(From[1]) - int(position[1]) == string.ascii_uppercase.index(From[0]) - string.ascii_uppercase.index(position[0]):
                            if value[2] == Empty:
                                c += 66

            elif int(To[1]) - int(From[1]) < 0 and string.ascii_uppercase.index(To[0]) - string.ascii_uppercase.index(From[0]) > 0:         # right top
                for position, value in board.items():
                    if From[0] < position[0] < To[0]:
                        if int(From[1]) - int(position[1]) == (string.ascii_uppercase.index(From[0]) - string.ascii_uppercase.index(position[0]))*-1:
                            if value[2] == Empty:
                                c += 66

            elif int(To[1]) - int(From[1]) > 0 and string.ascii_uppercase.index(To[0]) - string.ascii_uppercase.index(From[0]) < 0:       #left bottom
                for position, value in board.items():
                    if From[0] > position[0] > To[0]:
                        if int(From[1]) - int(position[1]) == (string.ascii_uppercase.index(From[0]) - string.ascii_uppercase.index(position[0]))*-1:
                            if value[2] == Empty:
                                c += 66

            elif int(To[1]) - int(From[1]) > 0 and string.ascii_uppercase.index(To[0]) - string.ascii_uppercase.index(From[0]) > 0:       #right bottom
                for position, value in board.items():
                    if From[0] < position[0] < To[0]:
                        if int(From[1]) - int(position[1]) == (string.ascii_uppercase.index(From[0]) - string.ascii_uppercase.index(position[0])):
                            if value[2] == Empty:
                                c += 66
            else:
                return False


    if c != 0 and c + 66 == abs(board[From][3][0] - board[To][3][0]):
        if board[To][1] != board[From][1] or board[From][2] == Empty:
            return True


    else:
        return False


def Queen(From, To):
    if From[0] == To[0] or From[1] == To[1]:
        print("QUEENROOK")
        if Rook(From, To):
            return True
    else:
        print("Queenbishop")
        if Bishop(From, To):
            return True
    return False

def King(From, To):
    if abs(board[From][3][0] - board[To][3][0]) <= step and abs(board[From][3][1] - board[To][3][1]) <= step:
        if board[To][1] != board[From][1] or board[To][2] == Empty:
            return True
    return False

def isCheckMate():
    for position1, value1 in board.items():
        if value1[1] != turn[0] and value1[2] != Empty and value1[0] != None:
            for position2 in board.keys():
                if value1[0](position1, position2):
                    print("__________" + position1 + " TO " + position2 + "_____________")
                    if sim_move(position1, position2):
                        #move(position1, position2)
                        return False
    return True





def sim_move(From, To):
    Store1 = None
    Store2 = None
    Store3 = Empty
    if board[To][2] != Empty:
        Store1 = board[To][0]
        Store2 = board[To][1]
        Store3 = board[To][2]
        board[To][2].place_forget()
        board[To][0] = None
        board[To][1] = None
        board[To][2] = Empty

    board[To][0], board[From][0] = board[From][0], board[To][0]
    board[To][1], board[From][1] = board[From][1], board[To][1]
    board[To][2], board[From][2] = board[From][2], board[To][2]

    if turn[0] == "b":
        if WCheck():
            board[To][0], board[From][0] = board[From][0], board[To][0]
            board[To][1], board[From][1] = board[From][1], board[To][1]
            board[To][2], board[From][2] = board[From][2], board[To][2]
            print(board[To][0])
            if board[To][0] == None:
                board[To][0] = Store1
                board[To][1] = Store2
                board[To][2] = Store3
                print(board[To][2])
                board[To][2].place(x=board[To][3][0], y=board[To][3][1])
            return False
    else:
        if BCheck():
            board[To][0], board[From][0] = board[From][0], board[To][0]
            board[To][1], board[From][1] = board[From][1], board[To][1]
            board[To][2], board[From][2] = board[From][2], board[To][2]
            print(board[To][0])
            if board[To][2] == Empty:
                board[To][0] = Store1
                board[To][1] = Store2
                board[To][2] = Store3
                print(board[To][2])
                board[To][2].place(x=board[To][3][0], y=board[To][3][1])
            return False

    board[To][0], board[From][0] = board[From][0], board[To][0]
    board[To][1], board[From][1] = board[From][1], board[To][1]
    board[To][2], board[From][2] = board[From][2], board[To][2]
    if board[To][2] == Empty:
        board[To][0] = Store1
        board[To][1] = Store2
        board[To][2] = Store3
        board[To][2].place(x=board[To][3][0], y=board[To][3][1])
    return True

def move(From,To):
    print("MOVE____________________________________")
    Store1 = None
    Store2 = None
    Store3 = Empty
    if board[To][2] != Empty:
        Store1 = board[To][0]
        Store2 = board[To][1]
        Store3 = board[To][2]
        board[To][2].place_forget()
        board[To][0] = None
        board[To][1] = None
        board[To][2] = Empty

    board[To][0], board[From][0] = board[From][0], board[To][0]
    board[To][1], board[From][1] = board[From][1], board[To][1]
    board[To][2], board[From][2] = board[From][2], board[To][2]


    if board[To][1] == "w":             #white moved
        print("White moved")
        if WCheck():
            print("WCHECK TRUE")
            Feedback["text"] = "Invalid move!"
            board[From][2].place(x=board[From][3][0], y=board[From][3][1])
            board[To][0], board[From][0] = board[From][0], board[To][0]
            board[To][1], board[From][1] = board[From][1], board[To][1]
            board[To][2], board[From][2] = board[From][2], board[To][2]
            board[To][0] = Store1
            board[To][1] = Store2
            board[To][2] = Store3
            board[To][2].place(x=board[To][3][0], y=board[To][3][1])
            return None
        if BCheck():
            if isCheckMate():
                GameOver()
            else:
                Check_label["fg"] = "red"

        else:
            Check_label["fg"] = "grey50"


    elif board[To][1] == "b":           #black moved
        print("Black moved")
        if BCheck():
            Feedback["text"] = "Invalid move!"
            board[To][0], board[From][0] = board[From][0], board[To][0]
            board[To][1], board[From][1] = board[From][1], board[To][1]
            board[To][2], board[From][2] = board[From][2], board[To][2]
            board[To][0] = Store1
            board[To][1] = Store2
            board[To][2] = Store3
            board[To][2].place(x=board[To][3][0], y=board[To][3][1])
            return None
        if WCheck():
            if isCheckMate():

                GameOver()
            else:
                Check_label["fg"] = "red"

        else:
            Check_label["fg"] = "grey50"

    board[From][2].place(x=board[From][3][0], y=board[From][3][1])
    board[To][2].place(x=board[To][3][0], y=board[To][3][1])
    Empty.place_forget()

    if turn[0] == "w":
        turn[0] = "b"
        TurnLabel["text"] = "BLACK IS ON"

    else:
        turn[0] = "w"
        TurnLabel["text"] = "WHITE IS ON"
    return True



window = Tk()
window.geometry("1000x900")
window.title("CHESS GAME")
frame = Frame(window, relief="ridge", borderwidth=5, bg="grey50")
frame.pack(fill="both", expand=1)
label = Label(frame, text="Welcome to chess!", font=("Helvetica", 16))      #Welcome Text
label.pack(expand=1)
label.place(x=390, y=15)


xx = 233
yy = 63
step = 66
From = ""
To = ""

WPawnImg = PhotoImage(file="C:\\Users\\Anwender\\.PyCharmCE2018.2\\config\\scratches\\chessgame\\PiecesImages\\WPawn.png")
BPawnImg = PhotoImage(file="C:\\Users\\Anwender\\.PyCharmCE2018.2\\config\\scratches\\chessgame\\PiecesImages\\BPawn.png")
WRookImg = PhotoImage(file="C:\\Users\\Anwender\\.PyCharmCE2018.2\\config\\scratches\\chessgame\\PiecesImages\\WRook.png")
BRookImg = PhotoImage(file="C:\\Users\\Anwender\\.PyCharmCE2018.2\\config\\scratches\\chessgame\\PiecesImages\\BRook.png")
WKnightImg = PhotoImage(file="C:\\Users\\Anwender\\.PyCharmCE2018.2\\config\\scratches\\chessgame\\PiecesImages\\WKnight.png")
BKnightImg = PhotoImage(file="C:\\Users\\Anwender\\.PyCharmCE2018.2\\config\\scratches\\chessgame\\PiecesImages\\BKnight.png")
WBishopImg = PhotoImage(file="C:\\Users\\Anwender\\.PyCharmCE2018.2\\config\\scratches\\chessgame\\PiecesImages\\WBishop.png")
BBishopImg = PhotoImage(file="C:\\Users\\Anwender\\.PyCharmCE2018.2\\config\\scratches\\chessgame\\PiecesImages\\BBishop.png")
WKingImg = PhotoImage(file="C:\\Users\\Anwender\\.PyCharmCE2018.2\\config\\scratches\\chessgame\\PiecesImages\\WKing.png")
BKingImg = PhotoImage(file="C:\\Users\\Anwender\\.PyCharmCE2018.2\\config\\scratches\\chessgame\\PiecesImages\\BKing.png")
WQueenImg = PhotoImage(file="C:\\Users\\Anwender\\.PyCharmCE2018.2\\config\\scratches\\chessgame\\PiecesImages\\WQueen.png")
BQueenImg = PhotoImage(file="C:\\Users\\Anwender\\.PyCharmCE2018.2\\config\\scratches\\chessgame\\PiecesImages\\BQueen.png")


WKing = Label(frame, image=WKingImg, height=45, width=40)

WQueen = Label(frame, image=WQueenImg, height=45, width=40)

WKnight1 = Label(frame, image=WKnightImg, height=45, width=40)

WKnight2 = Label(frame, image=WKnightImg, height=45, width=40)

WBishop1 = Label(frame, image=WBishopImg, height=45, width=40)

WBishop2 = Label(frame, image=WBishopImg, height=45, width=40)

WRook1 = Label(frame, image=WRookImg, height=45, width=40)

WRook2 = Label(frame, image=WRookImg, height=45, width=40)

WPawn1 = Label(frame, image=WPawnImg, height=45, width=40)

WPawn2 = Label(frame, image=WPawnImg, height=45, width=40)

WPawn3 = Label(frame, image=WPawnImg, height=45, width=40)

WPawn4 = Label(frame, image=WPawnImg, height=45, width=40)

WPawn5 = Label(frame, image=WPawnImg, height=45, width=40)

WPawn6 = Label(frame, image=WPawnImg,height=45, width=40)

WPawn7 = Label(frame, image=WPawnImg, height=45, width=40)

WPawn8 = Label(frame, image=WPawnImg, height=45, width=40)

# black pieces

b = xx + 0 * step

BKing = Label(frame, image=BKingImg, height=45, width=40)

BQueen = Label(frame, image=BQueenImg, height=45, width=40)

BKnight1 = Label(frame, image=BKnightImg, height=45, width=40)

BKnight2 = Label(frame, image=BKnightImg, height=45, width=40)

BBishop1 = Label(frame, image=BBishopImg, height=45, width=40)

BBishop2 = Label(frame, image=BBishopImg, height=45, width=40)

BRook1 = Label(frame, image=BRookImg, height=45, width=40)

BRook2 = Label(frame, image=BRookImg, height=45, width=40)

BPawn1 = Label(frame, image=BPawnImg, height=45, width=40)

BPawn2 = Label(frame, image=BPawnImg, height=45, width=40)

BPawn3 = Label(frame, image=BPawnImg, height=45, width=40)

BPawn4 = Label(frame, image=BPawnImg, height=45, width=40)

BPawn5 = Label(frame, image=BPawnImg, height=45, width=40)

BPawn6 = Label(frame, image=BPawnImg, height=45, width=40)

BPawn7 = Label(frame, image=BPawnImg, height=45, width=40)

BPawn8 = Label(frame, image=BPawnImg, height=45, width=40)




WKing.place(x=xx+4*step, y=yy+8*step)

WQueen.place(x=xx+3*step, y=yy+8*step)

WKnight1.place(x=xx+1*step, y=yy+8*step)

WKnight2.place(x=xx+6*step, y=yy+8*step)

WBishop1.place(x=xx+2*step, y=yy+8*step)

WBishop2.place(x=xx+5*step, y=yy+8*step)

WRook1.place(x=xx+0*step, y=yy+8*step)

WRook2.place(x=xx+7*step, y=yy+8*step)

WPawn1.place(x=xx+0*step, y=yy+7*step)

WPawn2.place(x=xx+1*step, y=yy+7*step)

WPawn3.place(x=xx+2*step, y=yy+7*step)

WPawn4.place(x=xx+3*step, y=yy+7*step)

WPawn5.place(x=xx+4*step, y=yy+7*step)

WPawn6.place(x=xx+5*step, y=yy+7*step)

WPawn7.place(x=xx+6*step, y=yy+7*step)

WPawn8.place(x=xx+7*step, y=yy+7*step)

# black pieces

#b = xx+0*step

BKing.place(x=xx+4*step, y=yy+1*step)

BQueen.place(x=xx+3*step, y=yy+1*step)

BKnight1.place(x=xx+1*step, y=yy+1*step)

BKnight2.place(x=xx+6*step, y=yy+1*step)

BBishop1.place(x=xx+2*step, y=yy+1*step)

BBishop2.place(x=xx+5*step, y=yy+1*step)

BRook1.place(x=xx+0*step, y=yy+1*step)

BRook2.place(x=xx+7*step, y=yy+1*step)

BPawn1.place(x=xx+0*step, y=yy+2*step)

BPawn2.place(x=xx+1*step, y=yy+2*step)

BPawn3.place(x=xx+2*step, y=yy+2*step)

BPawn4.place(x=xx+3*step, y=yy+2*step)

BPawn5.place(x=xx+4*step, y=yy+2*step)

BPawn6.place(x=xx+5*step, y=yy+2*step)

BPawn7.place(x=xx+6*step, y=yy+2*step)

BPawn8.place(x=xx+7*step, y=yy+2*step)


Empty = Label(frame)

board = {"A1": [Rook, "b", BRook1, (xx + 0 * step, yy + 1 * step)],
        "A2": [Pawn, "b", BPawn1, (xx + 0 * step, yy + 2 * step)],
        "A3": [None, None, Empty, (xx + 0 * step, yy + 3 * step)],
        "A4": [None, None, Empty, (xx + 0 * step, yy + 4 * step)],
        "A5": [None, None, Empty, (xx + 0 * step, yy + 5 * step)],
        "A6": [None, None, Empty, (xx + 0 * step, yy + 6 * step)],
        "A7": [Pawn, "w", WPawn1, (xx + 0 * step, yy + 7 * step)],
        "A8": [Rook, "w", WRook1, (xx + 0 * step, yy + 8 * step)],
        "B1": [Knight, "b", BKnight1, (xx + 1 * step, yy + 1 * step)],
        "B2": [Pawn, "b", BPawn2, (xx + 1 * step, yy + 2 * step)],
        "B3": [None, None, Empty,(xx + 1 * step, yy + 3 * step)],
        "B4": [None, None, Empty, (xx + 1 * step, yy + 4 * step)],
        "B5": [None, None, Empty, (xx + 1 * step, yy + 5 * step)],
        "B6": [None, None, Empty, (xx + 1 * step, yy + 6 * step)],
        "B7": [Pawn, "w", WPawn2, (xx + 1 * step, yy + 7 * step)],
        "B8": [Knight, "w", WKnight1, (xx + 1 * step, yy + 8 * step)],
        "C1": [Bishop, "b", BBishop1, (xx + 2 * step, yy + 1 * step)],
        "C2": [Pawn, "b", BPawn3, (xx + 2 * step, yy + 2 * step)],
        "C3": [None, None, Empty, (xx + 2 * step, yy + 3 * step)],
        "C4": [None, None, Empty, (xx + 2 * step, yy + 4 * step)],
        "C5": [None, None, Empty, (xx + 2 * step, yy + 5 * step)],
        "C6": [None, None, Empty, (xx + 2 * step, yy + 6 * step)],
        "C7": [Pawn, "w", WPawn3, (xx + 2 * step, yy + 7 * step)],
        "C8": [Bishop, "w", WBishop1, (xx + 2 * step, yy + 8 * step)],
        "D1": [Queen, "b", BQueen, (xx + 3 * step, yy + 1 * step)],
        "D2": [Pawn, "b", BPawn4, (xx + 3 * step, yy + 2 * step)],
        "D3": [None, None, Empty,(xx + 3 * step, yy + 3 * step)],
        "D4": [None, None, Empty,(xx + 3 * step, yy + 4 * step)],
        "D5": [None, None, Empty,(xx + 3 * step, yy + 5 * step)],
        "D6": [None, None, Empty, (xx + 3 * step, yy + 6 * step)],
        "D7": [Pawn, "w", WPawn4, (xx + 3 * step, yy + 7 * step)],
        "D8": [Queen, "w", WQueen, (xx + 3 * step, yy + 8 * step)],
        "E1": [King, "b", BKing, (xx + 4 * step, yy + 1 * step)],
        "E2": [Pawn, "b", BPawn5, (xx + 4 * step, yy + 2 * step)],
        "E3": [None, None, Empty, (xx + 4 * step, yy + 3 * step)],
        "E4": [None, None, Empty, (xx + 4 * step, yy + 4 * step)],
        "E5": [None, None, Empty, (xx + 4 * step, yy + 5 * step)],
        "E6": [None, None, Empty, (xx + 4 * step, yy + 6 * step)],
        "E7": [Pawn, "w", WPawn5, (xx + 4 * step, yy + 7 * step)],
        "E8": [King, "w", WKing, (xx + 4 * step, yy + 8 * step)],
        "F1": [Bishop, "b", BBishop2, (xx + 5 * step, yy + 1 * step)],
        "F2": [Pawn, "b",  BPawn6,(xx + 5 * step, yy + 2 * step)],
        "F3": [None, None, Empty, (xx + 5 * step, yy + 3 * step)],
        "F4": [None, None, Empty, (xx + 5 * step, yy + 4 * step)],
        "F5": [None, None, Empty, (xx + 5 * step, yy + 5 * step)],
        "F6": [None, None, Empty, (xx + 5 * step, yy + 6 * step)],
        "F7": [Pawn, "w", WPawn6, (xx + 5 * step, yy + 7 * step)],
        "F8": [Bishop, "w", WBishop2, (xx + 5 * step, yy + 8 * step)],
        "G1": [Knight, "b", BKnight2, (xx + 6 * step, yy + 1 * step)],
        "G2": [Pawn, "b", BPawn7, (xx + 6 * step, yy + 2 * step)],
        "G3": [None, None, Empty, (xx + 6 * step, yy + 3 * step)],
        "G4": [None, None, Empty, (xx + 6 * step, yy + 4 * step)],
        "G5": [None, None, Empty, (xx + 6 * step, yy + 5 * step)],
        "G6": [None, None, Empty, (xx + 6 * step, yy + 6 * step)],
        "G7": [Pawn, "w", WPawn7, (xx + 6 * step, yy + 7 * step)],
        "G8": [Knight, "w", WKnight2, (xx + 6 * step, yy + 8 * step)],
        "H1": [Rook, "b", BRook2, (xx + 7 * step, yy + 1 * step)],
        "H2": [Pawn, "b", BPawn8, (xx + 7 * step, yy + 2 * step)],
        "H3": [None, None, Empty, (xx + 7 * step, yy + 3 * step)],
        "H4": [None, None, Empty, (xx + 7 * step, yy + 4 * step)],
        "H5": [None, None, Empty, (xx + 7 * step, yy + 5 * step)],
        "H6": [None, None, Empty,(xx + 7 * step, yy + 6 * step)],
        "H7": [Pawn, "w", WPawn8, (xx + 7 * step, yy + 7 * step)],
        "H8": [Rook, "w", WRook2, (xx + 7 * step, yy + 8 * step)],
        }



turn = ["w"]









# Labels and Entries for users move

FromLabel = Label(frame, text="Move from", font=("Helvetica", 13))
FromLabel.place(x=200, y= 720)

From = "From"
FromEntry = Entry(frame, bd=2, width=12, textvariable=From)
FromEntry.place(x=290, y=720)

ToLabel = Label(frame, text="to", font=("Helvetica", 13))
ToLabel.place(x=385, y= 720)

To = "To"
ToEntry = Entry(frame, bd=2, width=12, textvariable=To)
ToEntry.place(x=420, y=720)

Submit_Button = Button(frame, text="Submit", command=lambda: button_click())
Submit_Button.place(x=470, y=720)

Feedback = Label(frame, text="Make your move!", font=("Helvetica", 13))
Feedback.place(x=350, y= 750)

Check_label = Label(frame, text="CHECK!", font=("Helvetica", 15), fg="grey50", bg="grey50")
Check_label.place(x=850, y=400)

TurnLabel = Label(frame, text="WHITE IS ON", font=("Helvetica", 17), fg="black")
TurnLabel.place(x=650, y=720)

Instruction = Label(frame, text="Enter the boardposition like \"A1\". The letter in caps(A-H) followed by the number(1-8)")
Instruction.place(x=200, y=810)

GOLabel = Label(frame, font=("Helvetica", 22), fg="grey50", height=4, width=45)


create_board()




window.mainloop()

