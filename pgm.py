from tkinter import *
from tkinter import messagebox
import os


pasta = os.path.dirname(__file__)
diretorio = pasta+"\\registros.txt"

def gravarDados():
    arquivo = open(diretorio,"a")
    arquivo.write("Nome: %s" % vnome.get())
    arquivo.write("\nTelefone: %s" % vtel.get())
    arquivo.write("\n\n")
    arquivo.close()
    vnome.delete(0,END)
    vtel.delete(0,END)
    messagebox.showinfo("Gravação","Registro salvo")
    

tela = Tk()
tela.title("Interface")
tela.geometry("300x200")
tela.configure(background="#0F0")

Label(tela,text="Nome:",background="#0F0").place(x=5,y=20,height=20,width=50)
vnome = Entry(tela)
vnome.place(y=20,x=60,height=20,width=120)

Label(tela,text="Telefone:",background="#0F0").place(x=5,y=55,height=20,width=50)
vtel = Entry(tela)
vtel.place(y=55,x=60,height=20,width=65)

Button(tela,text="Gravar",command=gravarDados).place(x=5,y=100,height=25,width=80)

Label(tela,text="Desenvolvido pelo João Gustavo",background="#0F0",foreground="#00f").place(x=25,y=150,height=25,width=250)

tela.mainloop()