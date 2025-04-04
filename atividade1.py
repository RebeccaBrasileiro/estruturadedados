# Implementação de Lista Dinâmica: 

# Complete o programa abaixo para que funcione a implementação de lista dinâmica.

# Foram adicionadas saídas esperadas que devem ser cumpridas como testes.

class DynamicIntArray:

    def __init__(self, capacity=2):
        if capacity <= 0:
            raise ValueError("Capacidade inicial deve ser maior que 0.")
        self.capacity = capacity # Tamanho real do array interno
        self.size = 0 # Quantos elementos o usuário colocou
        self.data = [0] * self.capacity # Cria Array estático interno (só de inteiros)

    def is_empty(self):
        return self.size == 0

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Índice fora dos limites.")
        return self.data[index]

    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Índice fora dos limites.")
        self.data[index] = value

    def append(self, value):
        if self.size == self.capacity:
            self._resize_up(2 * self.capacity)
        self.data[self.size] = value
        self.size += 1

    def _resize_up(self, new_capacity):
        print(f"Redimensionando de {self.capacity} para {new_capacity}")
        new_data = [0] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def index_of(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1

    def contains(self, value):
        return self.index_of(value) != -1

    def __str__(self):
        return str(self.data[:self.size])



lista = DynamicIntArray()

# Saída: Lista vazia!

if lista.is_empty():
    print("Lista vazia!")
else:
    print("Lista tem elementos.")

print("Adicionando o 10;")
lista.append(10)

# Saída: Lista:  [10]
print("Lista: ", lista)

print("Verificando se 0 existe;")
# Saída: "0 existe na lista? Não"
print("0 existe na lista? ", "Sim" if lista.contains(0) else "Não")

print("Adicionando o 20;")
lista.append(20)

# Saída: Lista:  [10, 20]
print("Lista: ", lista)

print("Verificando o index do 20;")
# Saída: "Index do 20 é: 1"
print("Index do 20 é: ", lista.index_of(20))

print("Verificando se 20 existe;")
# Saída: "20 existe na lista? Sim"
print("20 existe na lista? ", "Sim" if lista.contains(20) else "Não")

print("Adicionando o 30;")
lista.append(30)

print("Lista: ", lista)
print("Tamanho da Lista para o usuário: ", lista.size)
print("Tamanho real da Lista internamente: ", lista.capacity)
print()

print("Adicionando o 40;")
lista.append(40)
print("Lista: ", lista)

print("Adicionando o 50;")
lista.append(50)
# Saída: [10, 20, 30, 40, 50]
print("Lista: ", lista)

# Buscar Elemento no índice 2
# Saída: 30
print("Elemento na posição 2: ", lista.get(2))

# Trocar Elemento no índice 2 para 99
# Saída: [10, 20, 99, 40, 50]
print("Trocando elemento no índice 2 para 99.")
lista.set(2, 99)
print("Lista: ", lista)