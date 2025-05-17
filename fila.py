from stack import Stack

class Fila:
    def __init__(self):
        self.entrada = Stack()
        self.saida = Stack()

    def enqueue(self, item):
        self.entrada.push(item)
        print(f"{item} enfileirado")

    def dequeue(self):
        if self.saida.is_empty():
            while not self.entrada.is_empty():
                self.saida.push(self.entrada.pop())

        if self.saida.is_empty():
            raise IndexError("Fila Vazia")

        return self.saida.pop()
