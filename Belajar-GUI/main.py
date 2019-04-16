import tkinter

main_window = tkinter.Tk()

def event_tekan():
    label2=tkinter.Label(main_window,text="Aku ditekan")
    label2.pack()

label=tkinter.Label(main_window,text="Halo ini Gui \nSederhana")
tombol=tkinter.Button(main_window,text="Tekan Aku", command=event_tekan)

label.pack()
tombol.pack()

main_window.mainloop()