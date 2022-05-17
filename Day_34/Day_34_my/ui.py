from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("My Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250,width=300, bg= "white")
        self.question_text = self.canvas.create_text(150,100,
                                                     text=f"Q0: here is the first question",
                                                     font=("Arial",25,"italic"),
                                                     width=280,
                                                     fill = THEME_COLOR,
                                                     )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)


        self.label = Label(text="Score: 0",font=("Arial",19,"italic"), highlightthickness=0, bg=THEME_COLOR, fg="white")
        self.label.grid(column=1, row=0)

        true_image = PhotoImage(file="true.png")
        false_image = PhotoImage(file="false.png")
        self.true_button = Button(image=true_image,highlightthickness=0,command=self.true_button_com)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_image, highlightthickness=0,command=self.false_button_com)
        self.false_button.grid(column=1, row=2)

        self.get_new_question()

        self.window.mainloop()

    def get_new_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_have_question():
            self.label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text,text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_com(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def false_button_com(self):
        self.give_feedback(self.quiz.check_answer(user_answer="False"))

    def give_feedback(self,feedback):
        if feedback:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(100,self.get_new_question)

