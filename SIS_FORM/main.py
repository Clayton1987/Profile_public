#Importando o Tkinter
from tkinter import *



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
        self.janela.mainloop()


    def frames(self):
        self.frame_cima = Frame(self.janela, width=310, height=50, bg=cor2, relief='flat')
        self.frame_cima.grid(row=0, column=0)
        self.frame_baixo = Frame(self.janela, width=310, height=403, bg=cor1, relief='flat')
        self.frame_baixo.grid(row=1, column=0)

if __name__ == "__main__":
    app()
