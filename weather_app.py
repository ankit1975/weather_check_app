import tkinter as tk
from PIL import Image,ImageTk
# from
root=tk.Tk()
root.title("weather app")
root.geometry('600x600')
# 2**3**5
imag=Image.open('./we.jpg','r')
imag=imag.resize((600,600),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(imag)
image_label=tk.Label(root,image=img_photo)
image_label.place(x=0,y=0,width=600,height=600)
label=tk.Label(image_label,text="weather checker ...")
label.place(x=80,y=16)
frame=tk.Frame(image_label,bg='blue')
frame.place(x=80,y=60,width=300 ,height=50)
entrybox=tk.Text(frame,width=200,height=50)
entrybox.pack()
searchbutton=tk.Button(image_label,text="get weather ",fg="green")
searchbutton.place(x=400,y=60,width=100,height=50)
frame2=tk.Frame(image_label,bg='black')
frame2.place(x=80,y=130,width=400 ,height=300)
label1=tk.Label(frame2)
label1.place()
# text_area=tk.Text(frame,width=150)
# text_area.pack()
# entry=tk.Entry(frame,width=17)
# entry.grid(row=0,column=1)
root.mainloop()