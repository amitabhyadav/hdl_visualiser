# Skunkworks HDl Visualiser
# v0.1
# developer: amitabh yadav [amitabh@syncmind.org]
# currently only for VHDL files.
# ** under construction **
# please wait for release.

import os
import tkinter as tk
from tkinter import filedialog

class skunkworksHDL:
    def __init__(self, root):
        self.root = root
        self.root.title("SkunkWorks HDL Visualiser")

        # Create menu bar
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)
        root.geometry("1550x850+50+50")

        # Create "File" menu
        file_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        root.bind("<Control-s>", self.save_file)

        # Create "Run" menu
        run_menu = tk.Menu(menu_bar)
        menu_bar.add_cascade(label="Run", menu=run_menu)
        run_menu.add_command(label="Run", command=self.parse_vhdl_file)
        
        # Create icon bar
        self.icon_bar = tk.Frame(root)
        self.icon_bar.pack(side="top", fill="x")
        
        # Create buttons for icon bar
        parse_button = tk.Button(self.icon_bar, text="Run", command=self.parse_vhdl_file)
        parse_button.pack(side="left")
        clear_button = tk.Button(self.icon_bar, text="Clear", command=self.clear_canvas)
        clear_button.pack(side="left")
        
        # Test buttons 
        button1 = tk.Button(self.icon_bar, text="Create Circles", command=self.create_circles) #delete this later
        button1.pack(side="left")#delete this later
        button2 = tk.Button(self.icon_bar, text="Create Line", command=self.create_line)#delete this later
        button2.pack(side="left")#delete this later
        button3 = tk.Button(self.icon_bar, text="Create Line", command=self.create_port)#delete this later
        button3.pack(side="left")#delete this later

        # Create text editor
        self.text_editor = tk.Text(root)
        self.text_editor.pack(side="left", fill="both", expand=True)

        # Create drawing area
        self.drawing_area = tk.Canvas(root)
        self.drawing_area.pack(side="right", fill="both", expand=True)
        
        # Create Status Bar
        self.line_number = tk.StringVar()
        self.status_bar = tk.Label(self.drawing_area, textvariable=self.line_number, relief=tk.SUNKEN)
        self.status_bar.place(x=self.drawing_area.winfo_width(), y=self.drawing_area.winfo_height(), width=50, height=20)
        self.text_editor.bind("<Motion>", self.update_line_number)
        
    def update_line_number(self, event):
        line_number = self.text_editor.index(tk.INSERT).split(".")[0]
        self.line_number.set("Line: " + line_number)

    def open_file(self):
        filepath = filedialog.askopenfilename()
        with open(filepath, "r") as f:
            self.text_editor.insert("1.0", f.read())

    def save_file(self, event=None):
        filepath = filedialog.asksaveasfilename()
        with open(filepath, "w") as f:
            f.write(self.text_editor.get("1.0", "end"))
    
    def clear_canvas(self):
        self.drawing_area.delete("all")
        
    def create_port(self): #modify all of this
        width = 250  #number of combinatorial logic and signals will define this #modify all of this
        height = 100 #modify all of this
        x = (self.drawing_area.winfo_width()/2 - width/2) - 10 #modify all of this
        y = self.drawing_area.winfo_height()/2 - height/2 + 5 #modify all of this
        self.drawing_area.create_line(x, y, x + 20, y, fill="black")#delete this later #modify all of this
    
    def create_circles(self):#delete this later
        x, y = 70, 50#delete this later
        self.x1, self.y1 = int(x), int(y)#delete this later
        x, y = 200, 100#delete this later
        self.x2, self.y2 = int(x), int(y)#delete this later
        self.circle1 = self.drawing_area.create_oval(self.x1-5, self.y1-5, self.x1+5, self.y1+5, fill='black')#delete this later
        self.circle2 = self.drawing_area.create_oval(self.x2-5, self.y2-5, self.x2+5, self.y2+5, fill='black')#delete this later

    def create_line(self):#delete this later
        # Determine the difference in x and y coordinates between the two points
        x1, y1 = 70, 50#delete this later
        x2, y2 = 200,100#delete this later
        x_diff = abs(x1 - x2)#delete this later
        y_diff = abs(y1 - y2)#delete this later

        # Draw a line between the two points#delete this later
        if x_diff > y_diff:#delete this later
            self.drawing_area.create_line(x1, y1, x2, y1, fill="black")#delete this later
        else:#delete this later
            self.drawing_area.create_line(x1, y1, x1, y2, fill="black")#delete this later


    def parse_vhdl_file(self):
        # main logic. this function needs a lot of work.
        self.clear_canvas()
        lines = self.text_editor.get("1.0", "end").split("\n")
        for line in lines:
            # read the entity and creates the entity box.
            if line.startswith("entity"):
                entity_name = ""
                for i in range(lines.index(line), len(lines)):
                    entity_name += line[line.index("entity")+7:line.index("is")].strip()
                    if "is" in lines[i]:
                        break
                width = 250  #number of combinatorial logic and signals will define this
                height = 100 # number of ports will define height
                x = self.drawing_area.winfo_width()/2 - width/2
                y = self.drawing_area.winfo_height()/2 - height/2
                self.drawing_area.create_rectangle(x, y, x + width, y + height)
                self.drawing_area.create_text(x + width/2, y + height/2, text=entity_name)
            # create ports in the canvas
            elif line.startswith("port"):
                for i in range(lines.index(line), len(lines)):
                    if ");" in lines[i]:
                        text = lines[i][lines[i].index("(")+1: lines[i].index(")")]
                        self.drawing_area.create_text(10, 10, text=text)
                        break

root = tk.Tk()
app = skunkworksHDL(root)
root.mainloop()
