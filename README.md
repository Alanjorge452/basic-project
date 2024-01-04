
Essa forma de trabalhar com funções me ajudou muito na finalização do código.

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


