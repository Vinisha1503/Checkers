
import tkinter as tk  # importing tkinter within program
from tkinter import *
import random


class MainWindow:  # first class for main window
    def __init__(self, parent):  # define all the title, sizes and bg colour of window.
        self.main_page = parent
        self.main_page.title("CHECKERS")
        self.main_page.geometry("820x650")
        self.main_page.configure(bg="#F0F0F0")

        self.frame12 = tk.Frame(self.main_page, height=700, width=900, bg="#F0F0F0")
        # self.checkers_img = PhotoImage(file="logo1.png")  # defines the logo of the window using a frame,
        #Label(self.main_page, image=self.checkers_img).place(x=250, y=50)  # placing image on screen via place and packing frame.
        self.frame12.pack()

        self.frame7 = tk.Frame(self.main_page, height=650, width=820, bg="#F0F0F0")
        self.quit_button = tk.Button(self.main_page,  # frame 7 creates the quit button for the window,
                                     text="QUIT",  # via self and using command. place and pack for
                                     font=("bahnschrift semi bold", 15),  # the button to show up.
                                     command=self.main_page.destroy)

        self.quit_button.place(x=355, y=575)
        self.quit_button.configure(height=1, width=8)
        self.frame7.pack()

        self.frame8 = tk.Frame(self.main_page, height=650, width=820, bg="#F0F0F0")
        self.play_button = tk.Button(self.main_page,
                                     text="COMPUTER",  # frame 8 creates the computer play button for window,
                                     font=("bahnschrift semi bold", 15),
                                     # it uses self and command. place and pack for the
                                     command=self.game_window_computer)  # window to show up on window.

        self.play_button.place(x=455, y=477)
        self.play_button.configure(height=1, width=8)
        self.frame8.pack()

        self.frame13 = tk.Frame(self.main_page, height=650, width=820, bg="#F0F0F0")
        self.play_button = tk.Button(self.main_page,  # third button created in frame 13 using self and
                                     text="HUMAN",  # command for human play button,
                                     font=("bahnschrift semi bold", 15),  # place and pack for window to show up.
                                     command=self.game_window_human)

        self.play_button.place(x=255, y=477)
        self.play_button.configure(height=1, width=8)
        self.frame13.pack()

    def game_window_computer(self):  # this procedure is written within the main window class,
        self.main_page.destroy()  # this actually destroys the main page when computer
        board_computer()  # button is opened.

    def game_window_human(self):  # this procedure is written within the main window class,
        self.main_page.destroy()  # this actually destroys the main page when human
        board_human()  # button is opened.


class board_computer:  # class creates the game page for the computer board
    def __init__(self):

        self.game_page = tk.Tk()  # defines all the titles, sizes and bg colour for window
        self.game_page.title("CHECKERS VS COMPUTER")
        self.game_page.geometry("820x650")
        self.game_page.configure(bg="#F0F0F0")
        # frame1 creates the frame in which all the buttons are
        self.frame1 = tk.Frame(self.game_page, height=820, width=650, bg="#F0F0F0")  # placed on.

        self.game_quit_button = tk.Button(self.frame1,  # quit button created the same way within window
                                          text="QUIT ",
                                          font=("bahnschrift semi bold", 15),
                                          command=self.game_page.destroy)
        self.game_quit_button.grid(row=1, column=6)

        label = tk.Label(self.frame1, text="    ", font=("bahnschrift semi bold", 15,),
                         bg="#F0F0F0")  # used as gap between buttons
        label.grid(row=1, column=1)

        self.home_button = tk.Button(self.frame1,  # home/return button created the same way within window
                                     text="HOME",
                                     font=("bahnschrift semi bold", 15),
                                     command=self.main_page_computer)
        self.home_button.grid(row=1, column=0)

        label = tk.Label(self.frame1, text="    ", font=("bahnschrift semi bold", 15,),
                         bg="#F0F0F0")  # used as gap between buttons
        label.grid(row=1, column=3)

        self.rules_button = tk.Button(self.frame1,  # rules button created the same way within window
                                      text="RULES",
                                      font=("bahnschrift semi bold", 15),
                                      command=self.rules_window)
        self.rules_button.grid(row=1, column=2)

        label = tk.Label(self.frame1, text="    ", font=("bahnschrift semi bold", 15,),
                         bg="#F0F0F0")  # used as gap between buttons
        label.grid(row=0, column=5)

        self.pause_button = tk.Button(self.frame1,  # pause window created the same way within window
                                      text="PAUSE",
                                      font=("bahnschrift semi bold", 15),
                                      command=self.pause_window)
        self.pause_button.grid(row=1, column=4)

        label = tk.Label(self.frame1, text="", font=("bahnschrift semi bold", 15,),
                         bg="#F0F0F0")  # used as gap between buttons
        label.grid(row=2, column=0)

        self.frame1.pack()  # packed frame close so it actually shows up on window

        self.square = 534 // 8  # used 66
        self.checker_pieces = ("green", "blue")  # defines the colours of the checker pieces

        self.canvas = tk.Canvas(width=520, height=520)  # canvas that the game board will be displayed on.
        self.canvas.pack()

        self.canvas.bind('<Button-1>', self.click)  # uses click procedure to define the button being pressed

        for x in range(8):  # for loop to create the cehcker sqaures in a range of
            for y in range(8):  # eight by eight.
                x1 = 66 * x
                y1 = 66 * y
                x2 = 66 * (x + 1)
                y2 = 66 * (y + 1)
                self.canvas.create_rectangle(x1, y1, x2, y2,
                                             fill=("brown", "black")[(x + y) % 2])  # actually creates the sqaure

        # defines the individual variables to be used in the program.
        self.Player1 = None
        self.Player2 = None

        self.turn = None
        self.current_turn = None

        self.gameOn = 1
        self.change_piece = True

        self.new_game(0)

    def main_page_computer(self):  # main page, rules window and pause window are all
        self.game_page.destroy()  # again defined so that they can be opened up.
        MainWindow(tk.Tk())  # main page computer buttons closes the game page once
        # pressed, however other two do not in order to prevent unwanted closure.

    def rules_window(self):
        rules_page()

    def pause_window(self):
        pause_page()

    def new_game(self, mode):  # this new game procedure is used to create all variables in
        self.gameOn = 1  # program. defines the players and the ai player.
        self.change_piece = True  # used as a loop to ensure that the program functions
        self.Player1 = Player_computer(self, 0)  # and prevents program from not opening.
        self.Player2 = AIPlayer(self, 1)
        self.Players = [self.Player1, self.Player2]
        self.turn = self.Player1
        self.current_turn = None
        self.game_page.mainloop()

    def click(self, event):  # procedure that defines the click method of when player
        if not self.gameOn:  # clicks on square or piece.
            return  # event holders indicate sqaure been click on
        x, y = event.x, event.y
        square_x, square_y = x // self.square, y // self.square  # checks location in which mouse has been clicked on
        if (square_x + square_y) % 2 == 0:
            return
        if (square_x, square_y) in self.turn.location_of_piece:  # invalid move for odd number
            if not self.change_piece:
                return
            if self.current_turn:  # indicates highlight and change piece in block of code
                self.highlight(1)
            self.current_turn = self.turn.location_of_piece[
                (square_x, square_y)]  # attempts to move peice otherwise invalid
            self.highlight(0)
        else:
            if self.current_turn:
                outcome_of_move = self.current_turn.move(square_x, square_y)  # move doesn't work
                if outcome_of_move:
                    if outcome_of_move == 1 or (
                            self.current_turn.possible_routes() == []):  # changes possible routes afterwards too.
                        self.change_player()
                        self.current_turn = None

                        if isinstance(self.turn,
                                      AIPlayer):  # this defines the click for the ai player as they don't actually
                            self.turn.make_move()  # click on button, defines make move and then change player
                            self.change_player()

        self.canvas.bind('<Button-1>', self.click)  # defines click procedure on chosen part of board

    def click_ai(self):  # creates variables that defines the parts of the ai
        self.highlight(1)
        self.change_piece = True
        self.turn.make_move()
        self.change_player()

    def piece_on_board(self, x, y):  # defines that a piece is on the board
        if (x, y) in self.Player1.location_of_piece:  # finds the location of pieces on board at time
            return 0
        if (x, y) in self.Player2.location_of_piece:
            return 1
        return -1

    def change_player(self):  # procedure to change the player
        self.highlight(1)  # defines highlight is off
        self.change_piece = True

        self.turn = self.Player1 if self.turn == self.Player2 else self.Player2  # changes between player 1 and 2

        if isinstance(self.turn, AIPlayer):  # if its player 2 being ai they should define make move
            if self.turn.colour == 1:  # method, otherwise change it  to player 1 who can click on
                self.turn.make_move()  # button bind.
                self.change_player()
            else:
                self.canvas.bind('<Button-1>', self.click)

    def highlight(self, mode):  # procedure to create highlight for the checker button
        if mode == 0:  # mode defines 0 or 1 for the highlight is on or off
            colours = ("red", "red")
        else:
            colours = self.checker_pieces  # defines highlight to switch off, once checker piece is off
        colour = colours[self.current_turn.colour]
        self.canvas.itemconfig(self.current_turn.tag, fill=colour)


class rules_page:  # class that creates the rules of the program
    def __init__(self):
        self.rules_page = tk.Tk()  # defines that it uses tkinter, defines all the titles, sizes
        self.rules_page.title("RULES")  # and background colour
        self.rules_page.geometry("600x500+80+100")
        self.rules_page.configure(bg="#F0F0F0")

        self.frame10 = tk.Frame(self.rules_page, height=680, width=820,
                                bg="#F0F0F0")  # creates a frame10 to display the frame in which the
        self.rules_quit_button = tk.Button(self.frame10,  # text will show upon.
                                           text="QUIT ",
                                           font=("bahnschrift semi bold", 15),
                                           command=self.rules_page.destroy)
        self.rules_quit_button.place(x=252, y=410)
        self.rules_quit_button.configure(height=1, width=8)
        self.frame10.pack()

        label = tk.Label(self.frame10, text="RULES:",
                         font=("bahnschrift semi bold", 15))  # all labels are used for all the text
        label.place(x=270, y=30)
        label = tk.Label(self.frame10, text="1. Player may only move their designated pieces.",
                         font=("bahnschrift semi bold", 15))
        label.place(x=10, y=60)
        label = tk.Label(self.frame10, text="2. Pieces can only move diagonally.",
                         font=("bahnschrift semi bold", 15))
        label.place(x=10, y=90)
        label = tk.Label(self.frame10, text="3. Single pieces can only move forwards.",
                         font=("bahnschrift semi bold", 15))
        label.place(x=10, y=120)
        label = tk.Label(self.frame10, text="4. Single pieces can only move one place per go.",
                         font=("bahnschrift semi bold", 15))
        label.place(x=10, y=150)
        label = tk.Label(self.frame10, text="5. Piece must jump over opponents piece diagonally to remove",
                         font=("bahnschrift semi bold", 15))
        label.place(x=10, y=180)
        label = tk.Label(self.frame10, text="their piece, landing square must therefore be empty.",
                         font=("bahnschrift semi bold", 15))
        label.place(x=10, y=210)
        label = tk.Label(self.frame10, text="6. When piece has moved from your end of game_board to other",
                         font=("bahnschrift semi bold", 15))
        label.place(x=10, y=240)
        label = tk.Label(self.frame10, text="end it will become a king.", font=("bahnschrift semi bold", 15))
        label.place(x=10, y=270)
        label = tk.Label(self.frame10, text="7. Kings can move only diagonally but also backwards.",
                         font=("bahnschrift semi bold", 15))
        label.place(x=10, y=300)
        label = tk.Label(self.frame10, text="8. To win all pieces must be removed or opponent cannot",
                         font=("bahnschrift semi bold", 15))
        label.place(x=10, y=330)
        label = tk.Label(self.frame10, text="make any further moves.", font=("bahnschrift semi bold", 15))
        label.place(x=10, y=360)


class pause_page:  # class that creates the pause window of program
    def __init__(self):
        self.pause_page = tk.Tk()  # defines that it uses tkinter, defines all the sizes, titles
        self.pause_page.title("")  # and colour of bg
        self.pause_page.geometry("150x60+350+300")
        self.pause_page.configure(bg="#F0F0F0")

        self.frame11 = tk.Frame(self.pause_page, height=1000, width=1000,
                                bg="#F0F0F0")  # frame11 creates the frame for the button to show up
        self.pause_quit_button = tk.Button(self.frame11,  # creates the unpause button of window
                                           text="UNPAUSE",
                                           font=("bahnschrift semi bold", 15),
                                           command=self.pause_page.destroy)
        self.pause_quit_button.place(x=23, y=10)
        self.pause_quit_button.configure(height=1, width=8)
        self.frame11.pack()


class Player_computer:  # this class defines the player of the game
    def __init__(self, board, colour):
        self.colour = colour
        self.board = board

        self.location_of_piece = {}  # defines the location of piece and amount on
        self.pieces_on_board = 12  # board at current time.

        for row in range(3):  # for the row of 3 rows of checker pieces.
            y = (7 - row) * (1 - colour) + row * colour

            for col in range((colour + row) % 2, 8, 2):
                self.location_of_piece[(col, y)] = piece_computer(self.board, col, y, self.colour)

    def remove_piece(self, x, y):  # procedure to remove checker piece of board
        piece = self.location_of_piece.pop((x, y), None)
        if piece:  # removes piece via pop of board
            self.board.canvas.delete(piece.tag)  # tag allows specific removal of piece
            self.pieces_on_board -= 1  # meaning a piece has been removed from list


class piece_computer:  # class for piece for the computer mode
    def __init__(self, board, x, y, colour):
        self.board = board  # labelling variables

        self.square = board.square
        self.checker_radius = self.square // 6  # sizing of the checker piece

        self.x = x
        self.y = y

        self.king = False

        self.colour = colour

        self.tag = self.board.canvas.create_oval(self.square * x + self.checker_radius,
                                                 # creates the individual piece with a tag for checker
                                                 self.square * y + self.checker_radius,
                                                 self.square * (x + 1) - self.checker_radius,
                                                 self.square * (y + 1) - self.checker_radius,
                                                 fill=self.board.checker_pieces[self.colour])

    def legal_moves(self):  # procedure defines the legal moves that piece can make
        moves = []  # empty list

        if self.king:  # for king
            for x_dir, y_dir in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:  # directions in which piece can move
                moves += self._moves_in_direction(x_dir, y_dir)
        else:
            y_dir = 1 if self.colour == 0 else -1
            moves += self._moves_in_direction(-1, y_dir)
            moves += self._moves_in_direction(1, y_dir)

        valid_moves = []  # empty valid move list

        for move in moves:  # explains the moves in which the piece can be moved
            x, y = move
            if not (0 <= x < 8 and 0 <= y < 8): # invalid for less than 0 and bigger than 8 for move
                continue

            if self.board.piece_on_board(x, y) == self.colour:
                continue  # if current players piece on board, invalid move

            if abs(x - self.x) == 1:
                if (x, y) in self.board.Player1.location_of_piece or (x, y) in self.board.Player2.location_of_piece:
                    continue  # checks if location moving piece to is on left or right of board with this and below code.

            if abs(y - self.y) == 1:
                if (x, y) in self.board.Player1.location_of_piece or (x, y) in self.board.Player2.location_of_piece:
                    continue

            else:
                jumped_x, jumped_y = (x + self.x) // 2, (y + self.y) // 2
                if self.board.piece_on_board(jumped_x, jumped_y) != 1 - self.colour:
                    continue  # checks if move is valid by checking if square being moved to is empty
                              # checks if jump is necessary
            valid_moves.append(move)

        return valid_moves

    def _moves_in_direction(self, dx, dy):
        moves = []  # defines empty list
        x = self.x
        y = self.y
        while True:   # loop
            x += dx
            y += dy  # updates position of piece on board using coordinates
            if x < 0 or x >= 8 or y < 0 or y >= 8:  # makes sure piece isn't outside board
                break
            if (x, y) in self.board.Player1.location_of_piece or (x, y) in self.board.Player2.location_of_piece:
                # checks if new move has a piece already on square.
                break
            moves.append((x, y))  # appends so adds tuple to move list
        return moves

    def create_king(self, x, y):
        self.board.canvas.delete(self.tag)  #  deletes piece of board via tag

        if y in (0, 7):
            self.king = True
            self.checker_radius //= 6

        self.tag = self.board.canvas.create_oval(self.square * x + self.checker_radius,
                                                 self.square * y + self.checker_radius,
                                                 self.square * (x + 1) - self.checker_radius,
                                                 self.square * (y + 1) - self.checker_radius,
                                                 fill=self.board.checker_pieces[self.colour])
        # used to create individual king peice, then for every that becomes
        self.board.Players[self.colour].location_of_piece.pop((self.x, self.y), None) # removes from dictionary
        self.board.Players[self.colour].location_of_piece[(x, y)] = self  # updates dictionary with location
        self.x = x
        self.y = y # new attributes of location

    def move(self, x, y):
        if self.board.piece_on_board(x, y) >= 0:  # is piece on board at location
            return 0

        if self.king:
            return self.king_piece(x, y) if self.king else None

        if abs(self.x - x) == 1 and y == self.y + 2 * self.colour - 1:
            self.create_king(x, y)  # valid move to become king
            return 1 # becomes king

        if abs(self.x - x) == 2 and abs(y - self.y) == 2:

            x1 = (self.x + x) // 2
            y1 = (self.y + y) // 2

            if self.board.piece_on_board(x1, y1) == abs(1 - self.colour):
                self.board.Players[abs(1 - self.colour)].remove_piece(x1, y1)  # removes piece via jump
                self.create_king(x, y)  # becomes king by removing opponents piece

                self.board.highlight(0)  # changing highlight
                self.board.change_piece = False
                return 2  # reached end of row

    def king_piece(self, x, y):
        if abs(self.x - x) != abs(self.y - y):  # checks if the move is diagonal
            return  # returns part

        x_direction = 1 if (x - self.x) > 0 else -1  # checks x direction of move
        y_direction = 1 if (y - self.y) > 0 else -1  # checks y direction of move

        t = abs(1 - self.colour)  # checks colour of opponent
        positions = []  # defines empty list
        for index in range(1, abs(self.x - x) + 1):  # for loop to check if sqaure is by player or opponents piece
            occupied = self.board.piece_on_board(self.x + index * x_direction, self.y + index * y_direction)
            if occupied == self.colour:  # if it's occupied by certain colour
                return
            positions.append(occupied)  # append occupied piece

        if all(piece == -1 for piece in positions):  # checks if positions are not occupied
            self.create_king(x, y)  # creates king
            return 1

        captures = [i for i, p in enumerate(positions) if p == t]  # iterates over position list, and obtains index of i
        # checks if p is occupied by opponents colour, adds it to list
        if len(captures) == 1:
            x1 = self.x + x_direction * (captures[0] + 1)
            y1 = self.y + y_direction * (captures[0] + 1)
            # calculates amount on list
            self.board.Players[t].remove_piece(x1, y1)  # removes  piece from board
            self.create_king(x, y)  # creates king on board
            self.board.highlight(0)  # highlights the piece
            self.board.change_piece = False  # prevents piece from changing
            return 2  # returns capture piece and king piece in situation.

    def possible_routes(self):
        routes = [(-2, -2), (2, -2), (-2, 2), (2, 2)]  # possible diagonal routes
        if self.king:
            for x in range(3, 8):
                for y in range(3, 8):
                    for x_direction, y_direction in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        routes.append((x * x_direction, y * y_direction))
                        # for king, it adds all diagonal moves to routes list
        ways = []  # empty list
        x, y = self.x, self.y
        for move_x, move_y in routes:  # checks all squares available
            x1, y1 = x + move_x, y + move_y
            if 7 >= x1 >= 0 > self.board.piece_on_board(x1, y1) and 0 <= y1 <= 7:  # checks the bounds
                x2, y2 = (x1 + x) // 2, (y1 + y) // 2
                if (x2, y2) in self.board.Players[1 - self.colour].location_of_piece:
                    ways.append((x1, y1))  # adds to ways list
        return ways


class AIPlayer(Player_computer, piece_computer):  # class that defines it's an ai player rather than human
    def __init__(self, board, colour):
        super().__init__(board, colour)

    def make_move(self):  # procedure used within other parts of coding to make ai make
        # a move.
        pieces = list(self.location_of_piece.values())  # chooses between the list they have and picks random
        random.shuffle(pieces)

        for piece in pieces:  # for loop to check if the move is valid,
            legal_moves = piece.legal_moves()  # valid move can be made otherwise piece cannot move.
            if legal_moves:
                random_move = random.choice(legal_moves)
                piece.move(random_move[0], random_move[1])
                return


class board_human:  # class that represents the board for the human vs human
    def __init__(self):

        self.game_page_human = tk.Tk()  # defines that it uses tkinter
        self.game_page_human.title("CHECKERS VS HUMAN")  # defines the title
        self.game_page_human.geometry("820x650")  # defines the sizing
        self.game_page_human.configure(bg="#F0F0F0")  # defines the background colour

        self.frame2 = tk.Frame(self.game_page_human, height=820, width=650,
                               bg="#F0F0F0")  # defines the frame2 for the frame of buttons

        self.game_quit_button = tk.Button(self.frame2,  # creates the quit button
                                          text="QUIT ",
                                          font=("bahnschrift semi bold", 15),
                                          command=self.game_page_human.destroy)
        self.game_quit_button.grid(row=1, column=6)  # places button on grid

        label = tk.Label(self.frame2, text="    ", font=("bahnschrift semi bold", 15,),
                         bg="#F0F0F0")  # leaves a gap between buttons.
        label.grid(row=1, column=1)  # places gap by grid.

        self.home_button = tk.Button(self.frame2,  # creates the home button
                                     text="HOME",
                                     font=("bahnschrift semi bold", 15),
                                     command=self.main_page_computer)
        self.home_button.grid(row=1, column=0)  # places button on grid

        label = tk.Label(self.frame2, text="    ", font=("bahnschrift semi bold", 15,),
                         bg="#F0F0F0")  # leaves a gap between buttons.
        label.grid(row=1, column=3)  # places gap by grid.

        self.rules_button = tk.Button(self.frame2,  # creates the rules button
                                      text="RULES",
                                      font=("bahnschrift semi bold", 15),
                                      command=self.rules_window)
        self.rules_button.grid(row=1, column=2)  # places button on grid

        label = tk.Label(self.frame2, text="    ", font=("bahnschrift semi bold", 15,),
                         bg="#F0F0F0")  # leaves a gap between buttons.
        label.grid(row=0, column=5)  # places gap by grid.

        self.pause_button = tk.Button(self.frame2,  # creates the pause button
                                      text="PAUSE",
                                      font=("bahnschrift semi bold", 15),
                                      command=self.pause_window)
        self.pause_button.grid(row=1, column=4)  # places button on grid

        label = tk.Label(self.frame2, text="", font=("bahnschrift semi bold", 15,),
                         bg="#F0F0F0")  # leaves a gap between buttons.
        label.grid(row=2, column=0)  # places gap by grid.

        self.frame2.pack()  # packs the frame to show the buttons.

        self.square = 534 // 8  # used 66                                                                               # the size of the individual square for checker square
        self.checker_pieces = ("green", "blue")  # the colours of the checker pieces

        self.canvas = tk.Canvas(width=520, height=520)  # creates the canvas frame for the window
        self.canvas.pack()  # pack the frame closed

        self.canvas.bind('<Button-1>', self.click())  # binds the button to a click

        for x in range(8):  # creates a for loop for 8 squares in a row of 8
            for y in range(8):
                x1 = 66 * x  # coordinates of the checker squares
                y1 = 66 * y
                x2 = 66 * (x + 1)
                y2 = 66 * (y + 1)
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=("brown", "black")[
                    (x + y) % 2])  # creates the individual square with the colours

        # variables used within program are defined inside class

        self.Player1 = None
        self.Player2 = None
        self.turn = None
        self.current_turn = None

        self.gameOn = 1
        self.change_piece = True

        self.new_game(0)

    def main_page_computer(self):  # this is defined within board human class
        self.game_page_human.destroy()  # closes down game page once button is pressed
        MainWindow(tk.Tk())  # opens main window via tkinter

    def rules_window(self):  # opens rules window via rules button
        rules_page()

    def pause_window(self):  # opens pause window via pause button
        pause_page()

    def new_game(self, mode):  # creates a set of variables that defines the parts in the game
        self.gameOn = 1  # of human vs human.
        self.change_piece = True
        self.Player1 = Player_human(self, 0)  # list of variables can be used for program.
        self.Player2 = Player_human(self, 1)
        self.Players = [self.Player1, self.Player2]
        self.turn = self.Player1
        self.current_turn = None
        self.game_page_human.mainloop()  # mainloop is important for human v human game play.

    def click(self):
        def _click(event):  # procedure that defines the click method of when player
            if not self.gameOn:  # clicks on square or piece.
                return  # event holders indicate sqaure been click on
            x, y = event.x, event.y
            square_x, square_y = x // self.square, y // self.square  # checks location in which mouse has been clicked on
            if (square_x + square_y) % 2 == 0:
                return
            if (square_x, square_y) in self.turn.location_of_piece:  # invalid move for odd number
                if not self.change_piece:
                    return
                if self.current_turn:  # indicates highlight and change piece in block of code
                    self.highlight(1)
                self.current_turn = self.turn.location_of_piece[
                    (square_x, square_y)]  # attempts to move peice otherwise invalid
                self.highlight(0)
            else:
                if self.current_turn:
                    outcome_of_move = self.current_turn.move(square_x, square_y)  # move doesn't work
                    if outcome_of_move:
                        if outcome_of_move == 1 or (
                                self.current_turn.possible_routes() == []):  # changes possible routes afterwards too.
                            self.change_player()
                            self.current_turn = None

        return _click

    def piece_on_board(self, x, y):  # to define the specific piece on board,
        if (x, y) in self.Player1.location_of_piece:  # locates between player 1 and 2 using different locations.
            return 0
        if (x, y) in self.Player2.location_of_piece:
            return 1
        return -1

    def change_player(self):  # changes player procedure between player 1 and player 2
        self.highlight(1)  # defines highlight and then player changes so piece changes
        self.change_piece = True

        self.turn = self.Player2 if self.turn == self.Player1 else self.Player1

    def highlight(self, mode):  # highlight procedure to define highlight of chosen checker piece
        if mode == 0:
            colours = ("red", "red")  # mode which is 0 to define the red of the checker highlight
        else:
            colours = self.checker_pieces
        colour = colours[self.current_turn.colour]  # so highlight switches off once moved or different piece chosen
        self.canvas.itemconfig(self.current_turn.tag, fill=colour)


class Player_human:
    def __init__(self, board, colour):
        # defines all the variables as they are.
        self.colour = colour
        self.board = board
        # defines amount of peices and location
        self.location_of_piece = {}
        self.pieces_on_board = 12

        for row in range(3):
            y = (7 - row) * (1 - colour) + row * colour  # calculates y coordinate to place piece in right place.

            for col in range((colour + row) % 2, 8, 2): # places piece on second column till 8
                self.location_of_piece[(col, y)] = piece_human(self.board, col, y, self.colour)
                # adds into list for locations of pieces

    def remove_piece(self, x, y):
        piece = self.location_of_piece.pop((x, y), None) # removes piece of board due to pop
        if piece:
            self.board.canvas.delete(piece.tag)  # removes the piece via tag
            self.pieces_on_board -= 1  # removes a piece of board from the list of 12


class piece_human:
    def __init__(self, board, x, y, colour):
        self.board = board  # defines board

        self.square = board.square  # defines square from my variables
        self.checker_radius = self.square // 6  # defines size of radius of piece

        # defines all variables as they are
        self.x = x
        self.y = y

        self.king = False

        self.colour = colour

        self.tag = self.board.canvas.create_oval(self.square * x + self.checker_radius,
                                                 self.square * y + self.checker_radius,
                                                 self.square * (x + 1) - self.checker_radius,
                                                 self.square * (y + 1) - self.checker_radius,
                                                 fill=self.board.checker_pieces[self.colour])
        # creates checker piece by create oval using variables to define parts of coding of piece.

    def create_king(self, x, y):
        self.board.canvas.delete(self.tag)  # deletes piece of board via tag

        if y in (0, 7):
            self.king = True
            self.checker_radius //= 6

        self.tag = self.board.canvas.create_oval(self.square * x + self.checker_radius,
                                                 self.square * y + self.checker_radius,
                                                 self.square * (x + 1) - self.checker_radius,
                                                 self.square * (y + 1) - self.checker_radius,
                                                 fill=self.board.checker_pieces[self.colour])
        # used to create individual king peice, then for every that becomes
        self.board.Players[self.colour].location_of_piece.pop((self.x, self.y), None)  # removes from dictionary
        self.board.Players[self.colour].location_of_piece[(x, y)] = self  # updates dictionary with location
        self.x = x
        self.y = y  # new attributes of location

    def move(self, x, y):
        if self.board.piece_on_board(x, y) >= 0:  # is piece on board at location
            return 0

        if self.king:
            return self.king_piece(x, y) if self.king else None

        if abs(self.x - x) == 1 and y == self.y + 2 * self.colour - 1:
            self.create_king(x, y)  # valid move to become king
            return 1  # becomes king

        if abs(self.x - x) == 2 and abs(y - self.y) == 2:

            x1 = (self.x + x) // 2
            y1 = (self.y + y) // 2

            if self.board.piece_on_board(x1, y1) == abs(1 - self.colour):
                self.board.Players[abs(1 - self.colour)].remove_piece(x1, y1)  # removes piece via jump
                self.create_king(x, y)  # becomes king by removing opponents piece

                self.board.highlight(0)  # changing highlight
                self.board.change_piece = False
                return 2  # reached end of row

    def king_piece(self, x, y):
        if abs(self.x - x) != abs(self.y - y):  # checks if the move is diagonal
            return  # returns part

        x_direction = 1 if (x - self.x) > 0 else -1  # checks x direction of move
        y_direction = 1 if (y - self.y) > 0 else -1  # checks y direction of move

        t = abs(1 - self.colour)  # checks colour of opponent
        positions = []  # defines empty list
        for index in range(1, abs(self.x - x) + 1):  # for loop to check if sqaure is by player or opponents piece
            occupied = self.board.piece_on_board(self.x + index * x_direction, self.y + index * y_direction)
            if occupied == self.colour:  # if it's occupied by certain colour
                return
            positions.append(occupied)  # append occupied piece

        if all(piece == -1 for piece in positions):  # checks if positions are not occupied
            self.create_king(x, y)  # creates king
            return 1

        captures = [i for i, p in enumerate(positions) if p == t]  # iterates over position list, and obtains index of i
        # checks if p is occupied by opponents colour, adds it to list
        if len(captures) == 1:
            x1 = self.x + x_direction * (captures[0] + 1)
            y1 = self.y + y_direction * (captures[0] + 1)
            # calculates amount on list
            self.board.Players[t].remove_piece(x1, y1)  # removes  piece from board
            self.create_king(x, y)  # creates king on board
            self.board.highlight(0)  # highlights the piece
            self.board.change_piece = False  # prevents piece from changing
            return 2  # returns capture piece and king piece in situation.

    def possible_routes(self):
        routes = [(-2, -2), (2, -2), (-2, 2), (2, 2)]  # possible diagonal routes
        if self.king:
            for x in range(3, 8):
                for y in range(3, 8):
                    for x_direction, y_direction in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        routes.append((x * x_direction, y * y_direction))
                        # for king, it adds all diagonal moves to routes list
        ways = []   #empty list
        x, y = self.x, self.y
        for move_x, move_y in routes:  # checks all squares available
            x1, y1 = x + move_x, y + move_y
            if 7 >= x1 >= 0 > self.board.piece_on_board(x1, y1) and 0 <= y1 <= 7:  # checks the bounds
                x2, y2 = (x1 + x) // 2, (y1 + y) // 2
                if (x2, y2) in self.board.Players[1 - self.colour].location_of_piece:
                    ways.append((x1, y1))  # adds to ways list
        return ways


if __name__ == "__main__":  # checks whether script is being run in program
    root = tk.Tk()  # initiates tkinter and runs it
    start_page = MainWindow(root)  # passes main window as argument
    root.mainloop()  # starts loop
