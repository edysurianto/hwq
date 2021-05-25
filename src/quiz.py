from tkinter import *
from tkinter import messagebox as mb
import os
import json
	
class Quiz:
    # Initial method
	def __init__(self):
		self.q_no=0
		self.display_title()
		self.display_question()
		self.opt_selected=IntVar()
		self.opts=self.radio_buttons()
		self.display_options()
		self.buttons()
		self.data_size=len(question)
		self.correct=0

    # Calculate and display result in new message box
	def display_result(self):
		
		# Count wrong & correct
		wrong_count = self.data_size - self.correct
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {wrong_count}"
		
		# calcultaes percentage of correct answers
		score = int(self.correct / self.data_size * 100)
		result = f"Score: {score}%"
		
		# Shows a message box to display the result
		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


	# Validate answer after click on method next_btn
	def check_ans(self, q_no):
		if self.opt_selected.get() == answer[q_no]:
			return True

	# Check the answer and add to "correct" counter if the answer is correct
	def next_btn(self):
		if self.check_ans(self.q_no):
			self.correct += 1
		
		self.q_no += 1

		if self.q_no==self.data_size:
			self.display_result()
			gui.destroy()

		else:
			self.display_question()
			self.display_options()


	# Show 2 buttons,
	# "Next" to move to next question
	# and "Quit" to close the application
	def buttons(self):
		next_button = Button(gui, text="Next",command=self.next_btn,
		width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
		next_button.place(x=350,y=380)

		quit_button = Button(gui, text="Quit", command=gui.destroy,
		width=5,bg="black", fg="white",font=("ariel",16," bold"))
		quit_button.place(x=800,y=400)


	# Reset selection on radio button, and display options for current question
	def display_options(self):
		val=0
		self.opt_selected.set(0)
		
		for option in options[self.q_no]:
			self.opts[val]['text']=option
			val+=1


	# Shows the question on the screen
	def display_question(self):
		q_no = Label(gui, text=question[self.q_no], width=60,
		font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
		q_no.place(x=70, y=100)


	# Display title on screen
	def display_title(self):
		title = Label(gui, text="Hello World Quiz",
		width=53, bg="green",fg="white", font=("ariel", 20, "bold"))
		title.place(x=0, y=2)


	# Display radio buttons to select answer
	def radio_buttons(self):
		q_list = []
		y_pos = 150

		while len(q_list) < 4:
			radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
			value = len(q_list)+1,font = ("ariel",14))
			q_list.append(radio_btn)
			radio_btn.place(x = 100, y = y_pos)
			y_pos += 40
		
		return q_list
		
		
# Create GUI window for main display
gui = Tk()
gui.geometry("900x450")
gui.title("HWQ")

# Import and set quiz data from json file
cur_path = os.path.abspath(__file__)
parent_path = os.path.abspath(os.path.dirname(cur_path) + os.path.sep)
file_path = os.path.join(parent_path,'quiz.json')
print("External file path:"+file_path)
with open(file_path,'r', encoding='UTF-8') as f:
	data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])

# create object of the Quiz.
quiz = Quiz()

# Start the GUI
gui.mainloop()

# END
