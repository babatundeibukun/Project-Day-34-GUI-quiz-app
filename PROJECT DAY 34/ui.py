from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # create canvas
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.old_text = self.canvas.create_text(150, 125, width=280, text="Text", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # create buttons
        right_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")
        self.right = Button(width=100, height=97, image=right_img, highlightthickness=0, command=self.true_pressed)
        self.wrong = Button(width=100, height=97, image=wrong_img, highlightthickness=0, command=self.false_pressed)
        self.right.grid(column=0, row=3)
        self.wrong.grid(column=1, row=3)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score:{self.quiz.score}")
            self.canvas.itemconfig(self.old_text, text=q_text)
        else:
            self.canvas.itemconfig(self.old_text, text="You have reached the end of the quiz")
            self.right.config(state= "disabled")
            self.wrong.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

