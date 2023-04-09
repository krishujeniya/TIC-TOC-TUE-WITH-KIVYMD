from kivy.lang import Builder
from kivymd.app import MDApp
from random import choice
from kivymd.toast import toast



class Example(MDApp):
    def build(self):
        self.title = "Tic Toc Tue"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("GUI.kv")
    turn = "X"
    winner = False
    X_win = 0
    O_win = 0
    def nowi(self):
        if self.winner == False and \
                self.root.ids.btn1.disabled == True and \
                self.root.ids.btn2.disabled == True and \
                self.root.ids.btn3.disabled == True and \
                self.root.ids.btn4.disabled == True and \
                self.root.ids.btn5.disabled == True and \
                self.root.ids.btn6.disabled == True and \
                self.root.ids.btn7.disabled == True and \
                self.root.ids.btn8.disabled == True and \
                self.root.ids.btn9.disabled == True:
            self.root.ids.score.text = "It's a tie!!"
            toast("It's a tie!!")
            self.restart2()

    def disable_all_buttons(self):
        self.root.ids.btn1.disabled = True
        self.root.ids.btn2.disabled = True
        self.root.ids.btn3.disabled = True
        self.root.ids.btn4.disabled = True
        self.root.ids.btn5.disabled = True
        self.root.ids.btn6.disabled = True
        self.root.ids.btn7.disabled = True
        self.root.ids.btn8.disabled = True
        self.root.ids.btn9.disabled = True

    def End_game(self, a, b, c):
        self.winner = True
        self.disable_all_buttons()
        self.root.ids.score.text = f""
        toast(f"{a.text} Wins!")
        if a.text == "X":
            self.X_win += 1
        if a.text == "O":
            self.O_win += 1
        self.root.ids.game1.text = f"X - {self.X_win} | O - {self.O_win}"

        self.restart2()

    def win(self):
        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn2.text and self.root.ids.btn2.text == self.root.ids.btn3.text:
            self.End_game(self.root.ids.btn1,
                          self.root.ids.btn2, self.root.ids.btn3)
        if self.root.ids.btn4.text != "" and self.root.ids.btn4.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn6.text:
            self.End_game(self.root.ids.btn4,
                          self.root.ids.btn5, self.root.ids.btn6)
        if self.root.ids.btn7.text != "" and self.root.ids.btn7.text == self.root.ids.btn8.text and self.root.ids.btn8.text == self.root.ids.btn9.text:
            self.End_game(self.root.ids.btn7,
                          self.root.ids.btn8, self.root.ids.btn9)
        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn4.text and self.root.ids.btn4.text == self.root.ids.btn7.text:
            self.End_game(self.root.ids.btn1,
                          self.root.ids.btn4, self.root.ids.btn7)
        if self.root.ids.btn2.text != "" and self.root.ids.btn2.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn8.text:
            self.End_game(self.root.ids.btn2,
                          self.root.ids.btn5, self.root.ids.btn8)
        if self.root.ids.btn3.text != "" and self.root.ids.btn3.text == self.root.ids.btn6.text and self.root.ids.btn6.text == self.root.ids.btn9.text:
            self.End_game(self.root.ids.btn3,
                          self.root.ids.btn6, self.root.ids.btn9)
        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn9.text:
            self.End_game(self.root.ids.btn1,
                          self.root.ids.btn5, self.root.ids.btn9)
        if self.root.ids.btn3.text != "" and self.root.ids.btn3.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn7.text:
            self.End_game(self.root.ids.btn3,
                          self.root.ids.btn5, self.root.ids.btn7)
        self.nowi()

    def presser(self, btn):
        if self.turn == "X":
            btn.text = "X"
            btn.disabled = True
            self.root.ids.score.text = "O's Turn!"
            self.turn = "O"
        else:
            btn.text = "O"
            btn.disabled = True
            self.root.ids.score.text = "X's Turn!"
            self.turn = "X"
        self.win()

    def restart2(self):
        a = choice("XO")
        self.turn = a
        self.root.ids.btn1.disabled = False
        self.root.ids.btn2.disabled = False
        self.root.ids.btn3.disabled = False
        self.root.ids.btn4.disabled = False
        self.root.ids.btn5.disabled = False
        self.root.ids.btn6.disabled = False
        self.root.ids.btn7.disabled = False
        self.root.ids.btn8.disabled = False
        self.root.ids.btn9.disabled = False

        self.root.ids.btn1.text = ""
        self.root.ids.btn2.text = ""
        self.root.ids.btn3.text = ""
        self.root.ids.btn4.text = ""
        self.root.ids.btn5.text = ""
        self.root.ids.btn6.text = ""
        self.root.ids.btn7.text = ""
        self.root.ids.btn8.text = ""
        self.root.ids.btn9.text = ""

        self.root.ids.btn1.color = "green"
        self.root.ids.btn2.color = "green"
        self.root.ids.btn3.color = "green"
        self.root.ids.btn4.color = "green"
        self.root.ids.btn5.color = "green"
        self.root.ids.btn6.color = "green"
        self.root.ids.btn7.color = "green"
        self.root.ids.btn8.color = "green"
        self.root.ids.btn9.color = "green"
        self.winner = False
        self.root.ids.score.text = f"{a}'s Turn!"

    def restart1(self):
        a = choice("XO")
        self.turn = a
        self.root.ids.btn1.disabled = False
        self.root.ids.btn2.disabled = False
        self.root.ids.btn3.disabled = False
        self.root.ids.btn4.disabled = False
        self.root.ids.btn5.disabled = False
        self.root.ids.btn6.disabled = False
        self.root.ids.btn7.disabled = False
        self.root.ids.btn8.disabled = False
        self.root.ids.btn9.disabled = False

        self.root.ids.btn1.text = ""
        self.root.ids.btn2.text = ""
        self.root.ids.btn3.text = ""
        self.root.ids.btn4.text = ""
        self.root.ids.btn5.text = ""
        self.root.ids.btn6.text = ""
        self.root.ids.btn7.text = ""
        self.root.ids.btn8.text = ""
        self.root.ids.btn9.text = ""

        self.root.ids.btn1.color = "green"
        self.root.ids.btn2.color = "green"
        self.root.ids.btn3.color = "green"
        self.root.ids.btn4.color = "green"
        self.root.ids.btn5.color = "green"
        self.root.ids.btn6.color = "green"
        self.root.ids.btn7.color = "green"
        self.root.ids.btn8.color = "green"
        self.root.ids.btn9.color = "green"
        self.winner = False
        self.X_win = 0
        self.O_win = 0
        self.root.ids.game1.text = f"X - {self.X_win} | O - {self.O_win}"
        self.root.ids.score.text = f"{a}'s Turn!"


if __name__ == "__main__":
    app = Example()
    app.run()
