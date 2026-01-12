# Trabalhando com listas em Python

notas = [6.3, 9.0, 7.5, 10.0]

print("Notas:", notas)
print("Primeira nota:", notas[0])
print("Última nota:", notas[-1])

notas.append(8)
print("Lista atualizada:", notas)

media = sum(notas) / len(notas)
print("Média:", media)
