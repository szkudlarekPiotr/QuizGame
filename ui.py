import tkinter
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class UI():
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.minsize(width=400, height=650)
        self.window.config(background=THEME_COLOR, padx=20)
        self.window.title("Quizler")


        self.canvas = tkinter.Canvas(width=350, height=400, background="white")
        self.question = self.canvas.create_text(175,200,text="msg", fill="black", width=350, font=("Arial", 15, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=30)

        self.right = tkinter.Button()
        self.true_image = tkinter.PhotoImage(file="./images/true.png")
        self.right.config(image=self.true_image, command=self.right_button)
        self.right.grid(column=0, row=2, pady=20)

        self.wrong = tkinter.Button()
        self.false_image = tkinter.PhotoImage(file="./images/false.png")
        self.wrong.config(image=self.false_image, command=self.wrong_button)
        self.wrong.grid(column=1, row=2, pady=20)

        self.score = tkinter.Label()
        self.score.config(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def right_button(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.right.configure(state="disabled")
        self.wrong.configure(state="disabled")

    def wrong_button(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.right.configure(state="disabled")
        self.wrong.configure(state="disabled")

    def get_next_question(self):
        self.canvas.config(bg="white")
        if not self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question, text="You have completed the quiz!")
            self.right.configure(state="disabled")
            self.wrong.configure(state="disabled")
            self.window.after(5000, self.window.destroy)
        else:
            self.score.config(text=f"Score: {self.quiz.score}")
            self.right.configure(state="active")
            self.wrong.configure(state="active")
            text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=text)

    def give_feedback(self, response):
        if response:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
