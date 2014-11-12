# Trung Nguyen

import othello
import coordinate
import tkinter.ttk


DEFAULT_FONT = ('Helvetica', 13)



class Dialog:
    def __init__(self):
        self._dialog_window = tkinter.Tk()


        choose_value = [4,6,8,10,12,14,16]

        num_column = tkinter.Label(
            master = self._dialog_window, text = 'Number of columns:',
            font = DEFAULT_FONT)

        num_column.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._num_columns = tkinter.ttk.Combobox(
            master = self._dialog_window, width = 10, font = DEFAULT_FONT, value=choose_value, state = 'readonly')

        self._num_columns.grid(
            row = 0, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        num_row = tkinter.Label(
            master = self._dialog_window, text = 'Number of rows:',
            font = DEFAULT_FONT)

        num_row.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._num_rows = tkinter.ttk.Combobox(
            master = self._dialog_window, width = 10, font = DEFAULT_FONT, value=choose_value, state = 'readonly')

        self._num_rows.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        turn_player = tkinter.Label(
            master = self._dialog_window, text = 'Choose player go first:',
            font = DEFAULT_FONT)

        turn_player.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._turn_player = tkinter.ttk.Combobox(
            master = self._dialog_window, width = 10, font = DEFAULT_FONT, value=['White','Black'], state = 'readonly')

        self._turn_player.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 3, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.S)

        play_button = tkinter.Button(
            master = button_frame, text = 'Play', font = DEFAULT_FONT,
            command = self._on_play_button)

        play_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)

        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)


        # Finally, we'll initialize some attributes that will carry information
        # about the outcome of this dialog box (i.e., whether the user clicked
        # "Play" to dismiss it).

        self._play_clicked = False



    def show(self) -> None:
        # This is how we turn control over to our dialog box and make that
        # dialog box modal.
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()



    def was_play_clicked(self) -> bool:
        return self._play_clicked


    def get_num_columns(self) -> int:
        return self._num_columns


    def get_num_rows(self) -> int:
        return self._num_rows


    def get_turn_player(self) -> str:
        return self._turn_player


    def _on_play_button(self) -> None:
        self._play_clicked = True
        self._num_columns = self._num_columns.get()
        self._num_rows = self._num_rows.get()
        self._turn_player = self._turn_player.get()
        self._dialog_window.destroy()


    def _on_cancel_button(self) -> None:
        self._dialog_window.destroy()





class User_GUI:

    def __init__(self, G: othello.OthelloGameState):
        # self._state = state
        # self._gamestate = othello.OthelloGameState
        self._gamestate = G

        dialog = Dialog()
        dialog.show()


        if dialog.was_play_clicked():

            input_columns = dialog.get_num_columns()
            input_rows = dialog.get_num_rows()
            input_turn_player = dialog.get_turn_player()


            # Chek for None(Null) value
            if input_columns == '':
                input_columns = 4
            else:
                input_columns = int(input_columns) # casting to type int

            if input_rows == '':
                input_rows = 4
            else:
                input_rows = int(input_rows)

            if input_turn_player == 'Black':
                input_turn_player = 'X'
            else:
                input_turn_player = 'O'


            self._gamestate.new_game_state(input_columns,input_rows,input_turn_player)
            self._root_window = tkinter.Tk()


            self._label0 = tkinter.Label(
                master = self._root_window, text = 'Black: ' + str (len(G.get_point('X'))), relief= 'ridge', font = DEFAULT_FONT,
                width = 6, height = 2,)
            self._label0.grid(
                row = 0, column = 0, padx = 5, pady = 5,
                sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)


            if G.turn == 'X':
                    current_turn = 'Turn: Black'
            else:
                    current_turn = 'Turn: White'
            self._label1 = tkinter.Label(
                master = self._root_window, text = current_turn, relief= 'ridge', font = DEFAULT_FONT)
            self._label1.grid(
                row = 0, column = 1, padx = 5, pady = 5,
                sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)


            self._label2 = tkinter.Label(
                master = self._root_window, text = 'White: ' + str (len(G.get_point('O'))), relief= 'ridge', font = DEFAULT_FONT)
            self._label2.grid(
                row = 0, column = 2, padx = 5, pady = 5,
                sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)


            self._canvas = tkinter.Canvas(
                master = self._root_window, width = 360, height = 360,
                background = '#006000')
            self._canvas.grid(
                row = 1, column = 0, columnspan = 3,padx = 10, pady = 10,
                sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)


            self._root_window.rowconfigure(0, weight = 1)
            self._root_window.rowconfigure(1, weight = 4)
            self._root_window.columnconfigure(0, weight = 1)
            self._root_window.columnconfigure(1, weight = 1)
            self._root_window.columnconfigure(2, weight = 1)


            self._canvas.bind('<Configure>', self._on_canvas_resized)
            self._canvas.bind('<Button-1>', self._on_canvas_clicked)

        else:
            print('Program exits by user click Cancel!')




    def start(self):
        self._root_window.mainloop()




    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        # Whenever the Canvas' size changes, redraw all of the spots,
        # since their sizes have changed, too.
        self._redraw_all()





    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        # When the canvas is clicked, tkinter generates an event.  Since
        # we've bound to this method to that event, this method will be
        # called whenever the canvas is clicked.

        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        width_distance = canvas_width / self._gamestate.board_columns
        height_distance = canvas_height / self._gamestate.board_rows


        user_input = coordinate.from_point(
            (event.x, event.y), (width_distance, height_distance))


        print('event.x:', event.x)
        print('event.y:', event.y)
        print('coordinate:', user_input.point())
        print('Possible move:',self._gamestate.get_possible_move())

        # Making a move and update Gameboard.
        self._gamestate.make_a_move(user_input.point())

        # Redraw all the spots
        self._redraw_all()

        # Check for game over or not
        print('Check for game over or not -> ',B.check_game_not_over())

        if B.check_game_not_over() == False:
            end_window = tkinter.Toplevel()

            if len(B.get_point('X')) > len(B.get_point('O')):
                end_message = 'BLACK PLAYER WIN'
            elif len(B.get_point('X')) < len(B.get_point('O')):
                end_message = 'WHITE PLAYER WIN'
            else:
                end_message = 'There\'s no winner. The game is tied!'

            end_label = tkinter.Label(master = end_window, text = end_message,font = DEFAULT_FONT, width = 40, height = 5)
            end_label.grid(row = 0, column = 0,columnspan = 3, padx = 10, pady = 10)

            end_window.grab_set()
            end_window.wait_window()
            self._root_window.destroy()







    def _redraw_all(self) -> None:
        # Delete and update.
        self._label0.config(text = 'Black: ' + str (len(self._gamestate.get_point('X'))))
        self._label2.config(text = 'White: ' + str (len(self._gamestate.get_point('O'))))
        if self._gamestate.turn == 'X':
                current_turn = 'Turn: Black'
        else:
                current_turn = 'Turn: White'
        self._label1.config(text = current_turn)

        self._canvas.delete(tkinter.ALL)


        canvas_height = self._canvas.winfo_height()
        canvas_width = self._canvas.winfo_width()
        height_distance = canvas_height / self._gamestate.board_rows
        width_distance = canvas_width / self._gamestate.board_columns


        for c in range(self._gamestate.board_columns):
            self._canvas.create_line(c*width_distance, 0, c*width_distance, canvas_height, width=2, fill='black')
        for r in range(self._gamestate.board_rows):
            self._canvas.create_line(0, r*height_distance, canvas_width, r*height_distance, width=2, fill='black')


        for c in range(self._gamestate.board_columns):
            for r in range(self._gamestate.board_rows):
                if self._gamestate.board[c][r] == 'O':

                    self._canvas.create_oval(
                        c*width_distance + width_distance/10, r*height_distance + height_distance/10,
                        (c+1)*width_distance - width_distance/10, (r+1)*height_distance - height_distance/10,
                        fill = 'white', outline = 'black')

                elif self._gamestate.board[c][r] == 'X':

                    self._canvas.create_oval(
                        c*width_distance + width_distance/10, r*height_distance + height_distance/10,
                        (c+1)*width_distance - width_distance/10, (r+1)*height_distance - height_distance/10,
                        fill = 'black', outline = 'black')


        for i in self._gamestate.get_possible_move():
            self._canvas.create_oval(
                        i.col*width_distance + width_distance/2.3 , i.row*height_distance + height_distance/2.3,
                        (i.col+1)*width_distance - width_distance/2.3, (i.row+1)*height_distance - height_distance/2.3,
                        fill = 'green', outline = 'black')





if __name__ == '__main__':

    B = othello.OthelloGameState()
    User_GUI(B).start()







