# importanto o tkinter
from tkinter import *

# Cores do projeto
cor0 = "#f0f3f5" 
cor1 = "#2a5353" 
cor2 = "#4D3434" 
cor3 = "#38576b" 
cor4 = "#403d3d" 
cor5 = "#e06636" 
cor6 = "#038cfc" 
cor7 = "#ef5350" 
cor8 = "#263238" 
cor9 = "#e9edf5" 

#criando janela 

janela = Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background=cor9)
janela.resizable(width=False, height=False)


#divisao de janela 
frame_cima = Frame(janela, width=310, height=50, bg=cor2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=400, bg=cor0, relief='flat')
frame_baixo.grid(row=1, column=0)

frame_direita = Frame(janela, width=588,height=403, bg=cor1,relief='flat')
frame_direita.grid(row=0,column=1, rowspan=2,padx=1,pady=0, sticky=NSEW)

#label superior
app_nome = Label(frame_cima, text='Consult Form', anchor=NW,font=('Ivy 13 bold') ,bg=cor2,fg=cor1, relief='flat')
app_nome.place(x=10,y=20)

#Configurar Frame Inferior


#sempre ultima linha
janela.mainloop()