# Funções em Python

def calcular_media(lista):
  soma = sum(lista)
  return soma / len(lista)

n1 = [1, 2, 3, 4, 5, 6, 7]

media = calcular_media(n1)
print("Média: ", media)
