# Dado uma string de expressão x. 
# Verifique se os pares e a ordem de ‘{’ , ‘}’ , ‘(’ , ‘)’ , ‘[’ , ‘]’ estão corretos.
# Por exemplo, a função deve retornar:
# ‘True’ para exp = “[()]{}{()()}” e 
# ‘False’ para exp = “[(])”.

from stack import Stack

def is_balanced(expression):
    pilha = Stack()

    aberturas = "({[" 
    fechamentos = ")}]"
    pares = {')': '(', '}': '{', ']': '['}

    for caractere in expression:
        if caractere in aberturas:
            pilha.push(caractere)
        elif caractere in fechamentos:
            if pilha.is_empty() or pilha.pop() != pares[caractere]:
                return False 
            
    return pilha.is_empty()

# Teste
print(is_balanced("[{}(2+2)]{}")) #Esperado True
print(is_balanced("[{}(2+2))]{}")) #Esperado False
print(is_balanced("[{}])")) #Esperado False