#Importando o Tkinter
from tkinter import *

# Importando Calendario
#from tkcalendar import Calendar, DateEntry
from tkcalendar import DateEntry


################ cores ######################


cor0 = "#f0f3f5" # preta
cor1 = "#feffff" # branca
cor2 = "#4fa882" # verde
cor3 = "#385f6b" # verde valor
cor4 = "#403d3d" # letra
cor5 = "#e06636" # - profit
cor6 = "#038cfc" # azul
cor7 = "#ef5350" # vermelha
cor8 = "#263238" # + verde
cor9 = "#e9edf5" # skyblue


################ APP ######################

class app():

    def __init__(self):
        self.janela = Tk()
        self.janela.title("Formulario de Cadastro")
        self.janela.geometry("1043x453")
        self.janela.configure(background='black')
        self.janela.resizable(width=FALSE,height=True)
        self.frames()
        self.widgets()
        self.janela.mainloop()


    def frames(self):
        self.frame_cima = Frame(self.janela, width=310, height=50, bg=cor2, relief='flat')
        self.frame_cima.grid(row=0, column=0)
        self.frame_baixo = Frame(self.janela, width=310, height=403, bg=cor1, relief='flat')
        self.frame_baixo.grid(row=1, column=0,padx=1,pady=0,sticky=NSEW)
        self.frame_direita = Frame(self.janela, width=688, height=403, bg=cor1, relief='flat')
        self.frame_direita.grid(row=0, column=1, rowspan=2,padx=1,pady=0,sticky=NSEW)


    def widgets(self):
        #### label titulo
        self.lb_titulo = Label(self.frame_cima, text="Formulario de Consultoria", anchor=NW, font=('arial 15 bold'), bg=cor2, fg=cor1, relief='flat')
        self.lb_titulo.place(x=35,y=20)

        ################### dados cadastrais ########################
        # NOME
        self.lb_nome = Label(self.frame_baixo, text="Nome: *", anchor=NW, font=('arial 10 bold'), bg=cor1, fg=cor4, relief='flat')
        self.lb_nome.place(x=10,y=10)

        self.ent_nome = Entry(self.frame_baixo, width=35, justify='left', relief='solid')
        self.ent_nome.place(x=12,y=40)

        # EMAIL
        self.lb_email = Label(self.frame_baixo, text="Email: *", anchor=NW, font=('arial 10 bold'), bg=cor1, fg=cor4, relief='flat')
        self.lb_email.place(x=10,y=70)

        self.ent_email = Entry(self.frame_baixo, width=35, justify='left', relief='solid')
        self.ent_email.place(x=12,y=100)
    
        # TELEFONE
        self.lb_phone = Label(self.frame_baixo, text="Telefone: *", anchor=NW, font=('arial 10 bold'), bg=cor1, fg=cor4, relief='flat')
        self.lb_phone.place(x=10,y=130)

        self.ent_phone = Entry(self.frame_baixo, width=35, justify='left', relief='solid')
        self.ent_phone.place(x=12,y=160)

        # DATA CONSULTA
        self.lb_dat_con = Label(self.frame_baixo, text="Data Consulta: *", anchor=NW, font=('arial 10 bold'), bg=cor1, fg=cor4, relief='flat')
        self.lb_dat_con.place(x=10,y=190)

        self.ent_dat_con = DateEntry(self.frame_baixo,  width=12, backgroud='dakrblue', foreground='white', borderwidth=2)
        self.ent_dat_con.place(x=12,y=220)

        # ESTADO CONSULTA
        self.lb_dat_con = DateEntry(self.frame_baixo, text="Estado Consulta: *", anchor=NW, font=('arial 10 bold'), bg=cor1, fg=cor4, relief='flat')
        self.lb_dat_con.place(x=10,y=190)

        self.ent_dat_con = Entry(self.frame_baixo, width=12, backgroud='dakrblue', foreground='white', borderwidth=2)
        self.ent_dat_con.place(x=12,y=220)

        # CONSULTA
        self.lb_dat_con = Label(self.frame_baixo, text="Estado Consulta: *", anchor=NW, font=('arial 10 bold'), bg=cor1, fg=cor4, relief='flat')
        self.lb_dat_con.place(x=10,y=190)

        self.ent_dat_con = Entry(self.frame_baixo, width=35, justify='left', relief='solid')
        self.ent_dat_con.place(x=12,y=220)

if __name__ == "__main__":
    app()
