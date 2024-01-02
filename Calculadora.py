from tkinter import *
from tkinter import ttk 


cor1 = "#07070a" #black
cor2 = "#feffff" #branco
cor3 = "#38576b"   #blu
cor4 = "#38576b" #blu carregado
cor5 = "#FFAB40" #Orange
cor6 = "#7d7d80" #cinza
janela =Tk()
janela.title("Calculadora")
janela.geometry("230x301")
janela.config(bg=cor1)
#width = largura
#height = Conprimento
#bg = para cor do botão
#fj = para cor do que esta dentro de botão
#font = tipo de letra que esta no espaço
#relief=RAISED = faz o botão ser sencivel ao mauose ao passar em cima
frame_tela = Frame(janela, width=235, height=50,bg=cor1,)
frame_tela.grid(ipadx=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(ipadx=1, column=0)


todos_valores = ""
#Função para calculadora rodar


def entrar_valores(event): 

    global todos_valores

    todos_valores = todos_valores + str (event) 
    
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    

    valor_texto.set(str(resultado))

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")




#criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto,width=16,height=2,padx=7,relief=FLAT,anchor="e",justify=RIGHT,font=('Ivi 18'),bg=cor1,fg=cor2)
app_label.place(x=0,y=0)
#criando botoes
botão_1 = Button(frame_corpo,command = limpar_tela, text="AC", width=11,height=2,bg=cor6,font=('Ivi 13 bold'),relief=[RAISED],overrelief=[RIDGE])
botão_1.place(x=0,y=0)
botão_2 = Button(frame_corpo, command=lambda: entrar_valores('%'),text= "%", width=5,height=2,bg=cor6,font=('Ivi 13 bold'),relief=[RAISED],overrelief=[RIDGE])
botão_2.place(x=118,y=0)
botão_4 = Button(frame_corpo, command=lambda: entrar_valores('/'),text="/", width=5,height=2,bg=cor5,fg=cor2,font=('Ivi 13 bold'),relief=[RAISED],overrelief=[RIDGE])
botão_4.place(x=177,y=0)


botão_5 = Button(frame_corpo, command=lambda: entrar_valores('7'),text= "7", width=5,height=2,bg=cor6,font=('Ivi 13 bold'),relief=[RAISED],overrelief=[RIDGE])
botão_5.place(x=0,y=52)
botão_6 = Button(frame_corpo, command=lambda: entrar_valores('8'),text= "8", width=5,height=2,bg=cor6,font=('Ivi 13 bold'),relief=[RAISED],overrelief=[RIDGE])
botão_6.place(x=58,y=52)
botão_7 = Button(frame_corpo, command=lambda: entrar_valores('9'), text="9", width=5,height=2,bg=cor6,font=('Ivi 13 bold'),relief=[RAISED],overrelief=[RIDGE])
botão_7.place(x=118,y=52)
botão_8 = Button(frame_corpo, command=lambda: entrar_valores('*'),text= "*", width=5,height=2,bg=cor5,fg=cor2,font=('Ivi 13 bold'),relief=[RAISED],overrelief=[RIDGE])
botão_8.place(x=177,y=52)

botão_9 = Button(frame_corpo, command=lambda: entrar_valores('4'),text= "4", width=5,height=2,bg=cor6,font=('Ivi 13 bold'),relief=[RAISED],overrelief=[RIDGE])
botão_9.place(x=0,y=104)
botão_10 = Button(frame_corpo,command=lambda: entrar_valores('5'), text= "5", width=5,height=2,bg=cor6,font=('Ivi 13 bold'),relief=[RAISED],overrelief=[RIDGE])
botão_10.place(x=59,y=104)
botão_11 = Button(frame_corpo, command=lambda: entrar_valores('6'),text="6", width=5,height=2,bg=cor6,font=('Ivi 13 bold'),relief=[RAISED],overrelief=[RIDGE])
botão_11.place(x=118,y=104)
botão_12 = Button(frame_corpo, command=lambda: entrar_valores('-'), text= "-", width=5,height=2,bg=cor5,fg=cor2,font=('Ivi 13 bold'),relief=[RAISED],overrelief=[RIDGE])
botão_12.place(x=177,y=104)

botão_9 = Button(frame_corpo, command=lambda: entrar_valores('1'),text= "1", width=5,height=2,bg=cor6,font=('Ivi 13 bold'),relief=[RAISED],overrelief=[RIDGE])
botão_9.place(x=0,y=156)
botão_10 = Button(frame_corpo, command=lambda: entrar_valores('2'),text= "2", width=5,height=2,bg=cor6,font=('Ivi 13 bold'),relief=[RAISED],overrelief=[RIDGE])
botão_10.place(x=58,y=156)
botão_11 = Button(frame_corpo, command=lambda: entrar_valores('3'),text="3", width=5,height=2,bg=cor6,font=('Ivi 13 bold'),relief=[RAISED],overrelief=[RIDGE])
botão_11.place(x=118,y=156)
botão_12 = Button(frame_corpo, command=lambda: entrar_valores('+'), text= "+", width=5,height=2,bg=cor5,fg=cor2,font=('Ivi 13 bold'),relief=[RAISED],overrelief=[RIDGE])
botão_12.place(x=177,y=156)

botão_1 = Button(frame_corpo,command=lambda: entrar_valores('0'), text="0", width=11,height=2,bg=cor6,font=('Ivi 13 bold'),relief=[RAISED],overrelief=[RIDGE])
botão_1.place(x=0,y=209)
botão_2 = Button(frame_corpo, command=lambda: entrar_valores(','),text= ",", width=5,height=2,bg=cor6,font=('Ivi 13 bold'),relief=[RAISED],overrelief=[RIDGE])
botão_2.place(x=118,y=209)
botão_4 = Button(frame_corpo,command = calcular, text="=", width=5,height=2,bg=cor5,fg=cor2,font=('Ivi 13 bold'),relief=[RAISED],overrelief=[RIDGE])
botão_4.place(x=177,y=209)




janela.mainloop()
