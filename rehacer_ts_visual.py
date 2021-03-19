import sys
import os
import subprocess
import pandas
from tkinter import Label, Button, Radiobutton, Tk, IntVar
from tkinter import messagebox
from tkinter import simpledialog, filedialog
import datetime


BACKGROUND_COLOR = "#B1DDC6"



ffmpeg = 'ffmpeg.exe'

def rehacer():
    global video, video_old, video_temp
    if radio_state.get() == 0:
        messagebox.showinfo(title='Tipo', message='Selecione que hacer con el fichero')
    else:
        try:
            print(video, video_temp)
            subprocess.run([ffmpeg, '-i', video, '-vcodec', 'copy', '-acodec', 'copy', '-c:s', 'copy', '-map', '0:v:0', '-map','0:a', '-map', '-0:s','-ignore_unknown', '-sn', '-threads', '1', video_temp], shell=True,)
        except Exception as e:
            print(e)
            sys.exit(1)
        if radio_state.get() == 1:
            if os.path.exists(video_temp):
                os.rename(video, video_old)
            if os.path.exists(video) is False:
                os.rename(video_temp, video)
            messagebox.showinfo(title='copia', message='Fichero creado, el original se renombra añadiendo la extension .old')
        elif radio_state.get() == 2:
            MsgBox = messagebox.askyesno(title='Tipo', message='Esta usted seguro el video original se borrara')
            if MsgBox:
                if os.path.exists(video_temp):
                    os.remove(video)
                if os.path.exists(video) is False:
                    os.rename(video_temp, video)
                messagebox.showinfo(title='copia', message='Fichero Modificado')
            else:
                if os.path.exists(video_temp):
                    os.remove(video_temp)



window = Tk()
window.title("Rehacer TS")
window.config(width=850, height=550, padx=50, pady=50,  highlightthickness=0)
window.update()

video = filedialog.askopenfilename(title="Select a question file to open.", filetypes=[("mpg files", "*.mpg")]) 
path, file = os.path.split(video)
video_temp = path + '/temp.mpg'
video_old = video + '.old'
forma = 'copiado'
fichero = Label(text=video, highlightthickness=0, font=('Arial', 12, 'bold'))
fichero.grid(row=0, column=0, columnspan=2)
in_point_label = Label(text='Que se hace con el fichero de salida:', highlightthickness=0, font=('Arial', 12, 'bold'))
in_point_label.grid(row=1, column=0)
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Se Copia", value=1, font=('Arial', 12, 'bold'),variable=radio_state)
radiobutton2 = Radiobutton(text="Se sobrescribe", value=2, font=('Arial', 12, 'bold'),variable=radio_state)
radiobutton1.grid(row=1, column=1)
radiobutton2.grid(row=2, column=1)
salbar = Button(text='Rehacer', highlightthickness=0, font=('Arial', 12, 'bold'), command=rehacer)
salbar.grid(row=3, column=1)



window.mainloop()
    
