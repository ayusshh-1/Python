THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
from quiz_brain import QuizBrain
class QuestionInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window  = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0",fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.text_q = self.canvas.create_text(150,125,width=280,text="",font=("Arial",20,"italic"),fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2,padx=10, pady=10)
        self.imag_right = PhotoImage(file="./images/true.png")
        self.imag_wrong = PhotoImage(file="./images/false.png")
        self.right_button  = Button(image=self.imag_right,highlightthickness=0,command=self.right_ans)
        self.right_button.grid(row=2,column=0,padx=10,pady=10)
        self.wrong_button = Button(image=self.imag_wrong,highlightthickness=0,command=self.wrong_ans)
        self.wrong_button.grid(row=2, column=1, padx=10, pady=10)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        next_q = self.quiz.next_question()
        self.canvas.itemconfig(self.text_q, text=next_q)

    def right_ans(self):
        check_ans = self.quiz.check_answer("True")
        self.give_feedback(check_ans)
    def wrong_ans(self):
        check_ans =self.quiz.check_answer("False")
        self.give_feedback(check_ans)
    def give_feedback(self,check_ans):
        if check_ans :
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
