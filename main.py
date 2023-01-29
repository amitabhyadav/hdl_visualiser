# Skunkworks HDl Visualiser
# v0.1
# developer: amitabh yadav [amitabh@syncmind.org]
# currently only for VHDL files.
# ** under construction **
# please wait for release.

import os
import tkinter as tk
from tkinter import filedialog, messagebox, PhotoImage

class skunkworksHDL:
    def __init__(self, root):
        self.root = root
        self.root.title("SkunkWorks HDL Visualiser")

        # Create menu bar
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)
        root.geometry("1550x850+50+50")
        logo = tk.PhotoImage(file="docs/pepe-le-pew.png")
        root.tk.call('wm', 'iconphoto', root._w, logo)

        # Create "File" menu
        file_menu = tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Create File", command=self.create_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.root.quit, accelerator="Alt+F4")
        root.bind("<Control-s>", self.save_file)
        
        # Create "Edit" menu
        edit_menu = tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut")#, command=self.cut_file_contents) #add functionality
        edit_menu.add_command(label="Copy")#, command=self.cut_file_contents) #add functionality
        edit_menu.add_command(label="Paste")#, command=self.cut_file_contents) #add functionality
        edit_menu.add_command(label="Comment")#, command=self.cut_file_contents) #add functionality
        edit_menu.add_command(label="Uncomment")#, command=self.cut_file_contents) #add functionality
        
        # Create "Template" menu # add functionality to all the template menu
        template_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Template", menu=template_menu)

        vhdl_menu = tk.Menu(template_menu, tearoff=0)
        template_menu.add_cascade(label="VHDL", menu=vhdl_menu)

        verilog_menu = tk.Menu(template_menu, tearoff=0)
        template_menu.add_cascade(label="Verilog", menu=verilog_menu)

        combinational_vhdl_menu = tk.Menu(vhdl_menu, tearoff=0)
        vhdl_menu.add_cascade(label="Combinational", menu=combinational_vhdl_menu)

        sequential_vhdl_menu = tk.Menu(vhdl_menu, tearoff=0)
        vhdl_menu.add_cascade(label="Sequential", menu=sequential_vhdl_menu)

        combinational_verilog_menu = tk.Menu(verilog_menu, tearoff=0)
        verilog_menu.add_cascade(label="Combinational", menu=combinational_verilog_menu)

        sequential_verilog_menu = tk.Menu(verilog_menu, tearoff=0)
        verilog_menu.add_cascade(label="Sequential", menu=sequential_verilog_menu)

        for i in range(5):
            combinational_vhdl_menu.add_command(label=f"Item {i+1}")
            sequential_vhdl_menu.add_command(label=f"Item {i+1}")
            combinational_verilog_menu.add_command(label=f"Item {i+1}")
            sequential_verilog_menu.add_command(label=f"Item {i+1}")
        
        # Create "Run" menu
        run_menu = tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label="Run", menu=run_menu)
        run_menu.add_command(label="Run", command=self.parse_vhdl_file)
        
        # Create "About" menu
        about_menu = tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label="?", menu=about_menu)
        about_menu.add_command(label="About hdl visualiser", command=self.about_sw)
        
        # Create icon bar
        self.icon_bar = tk.Frame(root)
        self.icon_bar.pack(side="top", fill="x")
        
        # Create buttons for icon bar
        parse_button = tk.Button(self.icon_bar, text="Run", command=self.parse_vhdl_file)
        parse_button.pack(side="left")
        template_button = tk.Button(self.icon_bar, text="Template", command=self.insert_template)
        template_button.pack(side="left")
        clear_button = tk.Button(self.icon_bar, text="Clear", command=self.clear_canvas)
        clear_button.pack(side="right")
        
        # Test buttons 
        # button1 = tk.Button(self.icon_bar, text="Create Circles", command=self.create_circles) #delete this later
        # button1.pack(side="left")#delete this later
        # button2 = tk.Button(self.icon_bar, text="Create Line", command=self.create_line)#delete this later
        # button2.pack(side="left")#delete this later
        # button3 = tk.Button(self.icon_bar, text="Create Port", command=self.create_port)#delete this later
        # button3.pack(side="left")#delete this later

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
        
    def create_file(self):
        file_name = filedialog.asksaveasfilename(initialdir = os.getcwd(), title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
        open(file_name, 'a').close()

    def open_file(self):
        filepath = filedialog.askopenfilename()
        with open(filepath, "r") as f:
            self.text_editor.insert("1.0", f.read())

    def save_file(self, event=None):
        filepath = filedialog.asksaveasfilename()
        with open(filepath, "w") as f:
            f.write(self.text_editor.get("1.0", "end"))
            
    def about_sw(self):
        # Use the messagebox class to create the dialog box
        about_message = "SkunkWorks HDL Visualiser\nMade with Python 3.10 + tkinter.\n\nCreated by Amitabh Yadav."
        tk.messagebox.showinfo("About", about_message)

    
    def clear_canvas(self):
        self.drawing_area.delete("all")
        
    def insert_template(self):
        template = """-- VHDL template
library IEEE;
use IEEE.std_logic_1164.all;

entity ENTITY_NAME is
    port (
        SIGNAL_1 : in std_logic;
        SIGNAL_2 : out std_logic
    );
end ENTITY_NAME;

architecture BEHAVIOR of ENTITY_NAME is
begin
    -- architecture body
end BEHAVIOR;"""
        self.text_editor.insert(tk.INSERT, template)
    
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

        # Draw a line between the two points#delete this later
        self.drawing_area.create_line(x1, y1, x2, y1, fill="black")#delete this later
        self.drawing_area.create_line(x2, y1, x2, y2, fill="black")#delete this later


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
