#Author Piotr Poloczek
from tkinter import *
from tkinter import ttk


class GUI(Frame):

	def __init__(self,master):
		Frame.__init__(self, master)
		self.pack()
		master.minsize(width=480, height=320)
			
		def key(event):
			kp = repr(event.char)
			print ("pressed", kp)
			return kp
			
		def callback(event):
			self.focus_set()
			print("cliked at", event.x, event.y)
			
		def insert_menubar():
			menu = Menu(self.master)
			self.master.config(menu = menu)
			file_bar = Menu(menu, tearoff = 0)
			file_bar.add_command(label = "Exit", command = self.exit_window)
			menu.add_cascade(label = "File", menu = file_bar)
			
		def insert_label(label_text, grid_column, grid_row):
			label_1 = ttk.Label(self, text = label_text + " ")
			label_1.grid(column = grid_column, row = grid_row)
			label_1_1 = ttk.Label(self, text = " mm")
			label_1_1.grid(column = grid_column + 2, row = grid_row)
			
		def insert_label_2(label_text_1, label_text_2, label_text_3, grid_column, grid_row):
			label_1 = ttk.Label(self, text = label_text_1 + " ")
			label_1.grid(column = grid_column, row = grid_row)
			
			label_2 = ttk.Label(self, text = label_text_2 + " ")
			label_2.grid(column = grid_column + 1, row = grid_row)
			
			label_3 = ttk.Label(self, text = label_text_3 + " ")
			label_3.grid(column = grid_column + 2, row = grid_row)
			
		def insert_textbox():
			
			text_1 = StringVar()
			textbox_1 = ttk.Entry(self, width = 20, textvariable = text_1)
			textbox_1.grid(column = 1, row = 0)
			
			text_2 = StringVar()
			textbox_2 = ttk.Entry(self, width = 20, textvariable = text_2)
			textbox_2.grid(column = 1, row = 1)
			
			text_3 = StringVar()
			textbox_3 = ttk.Entry(self, width = 20, textvariable = text_3)
			textbox_3.grid(column = 1, row = 2)
			
			text_4 = StringVar()
			textbox_4 = ttk.Entry(self, width = 20, textvariable = text_4)
			textbox_4.grid(column = 1, row = 3)
			
			text_5 = StringVar()
			textbox_5 = ttk.Entry(self, width = 20, textvariable = text_5)
			textbox_5.grid(column = 1, row = 4)
			
			insert_textbox.texts = [text_1, text_2, text_3, text_4, text_5]
		
		def solve():
			input_var  =[]
			texts_solve = insert_textbox.texts
			
			dia_wew = int(texts_solve[0].get())
			dia_zew = int(texts_solve[1].get())
			height = int(texts_solve[2].get())
			width_piece = int(texts_solve[3].get())
			height_piece = int(texts_solve[4].get())
			
			volume_1 = (3.14/4.0) * ((dia_zew^2) - (dia_wew^2)) * height
			volume_2 = (3.14/4.0) * (((dia_zew + width_piece)^2)-(dia_zew^2)) * height_piece
			volume_all = volume_1 + volume_2
			
			
			insert_label_2("Objętość:", str(volume_all), "mm3",  0, 10)
			
			
		def add_button():
			button_1 = ttk.Button(self, text = "Oblicz", command = solve)
			button_1.grid(column = 1, row = 5)
			
	
		insert_menubar()
		
		
		labels = ["Średnica wewnętrzna", "Średnica zewnętrzna", "Wysokość", "Szerokość grzebienia", "Wysokość grzebienia"]

		i = 0
		for label in labels:
			grid_row = i
			grid_column = 0
			label_text = label
			insert_label(label_text, grid_column, grid_row)
			i = i + 1

		
			
		insert_textbox()
		add_button()
		
		
		
		
	def exit_window(self):
		exit()
		
		

		

if __name__ == "__main__":
    tk = Tk()
    tk.wm_title("Prosty kalkulator obręczy")
    guiFrame = GUI(tk)
    guiFrame.mainloop()
