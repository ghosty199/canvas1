from tkinter import*
from tkinter import filedialog
import random
root=Tk()
from PIL import Image, ImageTk
root.geometry("500x500")
root.title("canvas")
input_box=Entry(root)
input_box.place(relx=0.2, rely=0.9)
input_box.insert(0,"black")

canvas=Canvas(root, height=400, width=400, bg="white")
canvas.pack()


img=ImageTk.PhotoImage(Image.open("start_point1.png"))

my_image=canvas.create_image(50,50,image=img)

direction=""
oldx=50
oldy=50
newx=50
newy=50


def right_dir(event):
    global direction
    global newy
    global oldy
    global oldx
    global newx
    oldx=newx
    oldy=newy
    newx=newx+5
    direction="right"
    draw(direction,oldx,oldy,newx,newy)
    
def left_dir(event):
    global direction
    global newy
    global oldy
    global oldx
    global newx
    oldx=newx
    oldy=newy
    newx=newx-5
    direction="left"
    draw(direction,oldx,oldy,newx,newy)
    
    
def up_dir(event):
    global direction
    global newy
    global oldy
    global oldx
    global newx
    oldx=newx
    oldy=newy
    newy=newy-5
    direction="up"
    draw(direction,oldx,oldy,newx,newy)
    
def down_dir(event):
    global direction
    global newy
    global oldy
    global oldx
    global newx
    oldx=newx
    oldy=newy
    newy=newy+5
    direction="down"
    draw(direction,oldx,oldy,newx,newy)
    

def draw(direction,oldx,oldy,newx,newy):
    fill_color=input_box.get()
    if(direction=="right"):
        right_line=canvas.create_line(oldx,oldy,newx,newy,width=3, fill=fill_color)
    if(direction=="left"):
         left_line=canvas.create_line(oldx,oldy,newx,newy,width=3, fill=fill_color)
    if(direction=="up"):
        up_line=canvas.create_line(oldx,oldy,newx,newy,width=3, fill=fill_color)
    if(direction=="down"):
        down_line=canvas.create_line(oldx,oldy,newx,newy,width=3, fill=fill_color)
          


root.bind("<Right>",right_dir)
root.bind("<Left>",left_dir)
root.bind("<Up>",up_dir)
root.bind("<Down>",down_dir)





label_image = Label(root, bg="white", text="enter color")
label_image.place(relx=0.10, rely=0.9, anchor=CENTER)





root.mainloop()