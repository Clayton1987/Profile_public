#Importando o Tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Importando Calendario
from tkcalendar import Calendar, DateEntry
#from tkcalendar import DateEntry

# Importando o views
from view import *

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
class funcs():
    def limpar_campos(self):
        self.ent_nome.delete(0, END)
        self.ent_email.delete(0, END)
        self.ent_phone.delete(0, END)
        self.ent_dat_con.delete(0, END)
        self.ent_estado.delete(0, END)
        self.ent_info.delete(0, END)


    def inserir_dados(self):
        # Inserir dados no banco de dados
        self.nome = self.ent_nome.get()
        self.email = self.ent_email.get()
        self.phone = self.ent_phone.get()
        self.data = self.ent_dat_con.get()
        self.estado = self.ent_estado.get()
        self.sobre = self.ent_info.get()

        self.lista = [self.nome, self.email, self.phone, self.data, self.estado, self.sobre]

        if self.nome=='':
            messagebox.showerror("Erro", "Preencha todos os campos")
        else:
            inserir_info(self.lista)
            messagebox.showinfo('Sucesso', 'Dados inseridos com Sucesso')
            self.limpar_campos()
            self.grid_view().destroy()
            self.grid_view()

class app(funcs):

    def __init__(self):
        self.janela = Tk()
        self.janela.title("Formulario de Cadastro")
        self.janela.geometry("1043x453")
        self.janela.configure(background='black')
        self.janela.resizable(width=FALSE,height=True)
        self.frames()
        self.widgets()
        self.grid_view()
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

        self.ent_dat_con = DateEntry(self.frame_baixo,  width=12,justify='left', relief='solid') #, backgroud='darkblue', foreground='white', borderwidth=2)
        self.ent_dat_con.place(x=12,y=220)

        # ESTADO CONSULTA
        self.lb_estado = Label(self.frame_baixo, text="Estado Consulta: *", anchor=NW, font=('arial 10 bold'), bg=cor1, fg=cor4, relief='flat')
        self.lb_estado.place(x=150,y=190)

        self.ent_estado = Entry(self.frame_baixo, width=15,justify='left', relief='solid') #, backgroud='darkblue', foreground='white', borderwidth=2)
        self.ent_estado.place(x=152,y=220)

        # INFORMAÇÕES DA CONSULTA
        self.lb_info = Label(self.frame_baixo, text="Informações Extra: *", anchor=NW, font=('arial 10 bold'), bg=cor1, fg=cor4, relief='flat')
        self.lb_info.place(x=10,y=250)

        self.ent_info = Entry(self.frame_baixo, width=35, justify='left', relief='solid')
        self.ent_info.place(x=12,y=280)

        ####################### Botoes ###########################
        # Inserir
        self.bt_inserir = Button(self.frame_baixo, text="Inserir", width=10, anchor='center', font=('arial 10 bold'), bg=cor6, fg=cor1, relief='raised', overrelief='ridge', command=self.inserir_dados)
        self.bt_inserir.place(x=10,y=320)

        # Alterar
        self.bt_inserir = Button(self.frame_baixo, text="Alterar", width=10, anchor='center', font=('arial 10 bold'), bg=cor2, fg=cor1, relief='raised', overrelief='ridge')
        self.bt_inserir.place(x=110,y=320)

        # Deletar
        self.bt_inserir = Button(self.frame_baixo, text="Deletar", width=10, anchor='center', font=('arial 10 bold'), bg=cor7, fg=cor1, relief='raised', overrelief='ridge')
        self.bt_inserir.place(x=210,y=320)

        # Limpar
        self.bt_inserir = Button(self.frame_baixo, text="Limpar", width=10, anchor='center', font=('arial 10 bold'), bg=cor3, fg=cor1, relief='raised', overrelief='ridge', command=self.limpar_campos)
        self.bt_inserir.place(x=110,y=350)

        

    def grid_view(self):
        #self.lista = [[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7]]
        self.lista = mostrar_info()

        # Lista HEAD
        self.tab_head = ['ID','Nome','email','telefone','Data','Estado','Sobre']

        #Criando a Tabela
        self.tree = ttk.Treeview(self.frame_direita, selectmode="extended", column=self.tab_head, show="headings")

        # Vertical scrollbar
        vsb = ttk.Scrollbar(self.frame_direita, orient="vertical", command=self.tree.yview)
        vsb.grid(column=1, row=0, sticky='nsew')

        # horizontal scrollbar
        hsb = ttk.Scrollbar(self.frame_direita, orient="horizontal", command=self.tree.xview)
        hsb.grid(column=0, row=1, sticky='nsew')


        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew')

        self.frame_direita.grid_rowconfigure(0, weight=12)

        self.hd = ["nw","nw","nw","nw","nw","center","center"]
        self.h = [30,170,140,100,120,50,100]
        self.n = 0

        for col in self.tab_head:
            self.tree.heading(col, text=col.title(), anchor='center')
            # Ajuste colunas width e head
            self.tree.column(col, anchor=self.hd[self.n], width=self.h[self.n])

            self.n+=1

        for item in self.lista:
            self.tree.insert('','end',values=item)
            







if __name__ == "__main__":
    app()
