import random

print("                   ┌───── •✧✧• ─────┐")
print("                        JOKENPÔ!! ")
print("                   └───── •✧✧• ─────┘ ")

print("            ==--==--==--==--==--==--==--==--==   ")

jogada = str(input("  Faça sua jogada Pedra (R), Papel (P) ou Tesoura (S): "))

# Escolha random do pc
ação = ("Pedra", "Papel", "Tesoura")
jogada_pc = random.choice(ação)

print("            ==--==--==--==--==--==--==--==--==   ")
print(f"             Jogada do adversário: 💥 {jogada_pc}💥")
if jogada_pc == "Pedra" and jogada == "P":
    print("               Resultado:     Você Perdeu!!    ")
elif jogada_pc == "Pedra" and jogada == "S":
    print("               Resultado:     Você Ganhou!!!    ")
elif jogada_pc == "Pedra" and jogada == "R":
    print("               Resultado:     Empate!    ")
elif jogada_pc == "Papel" and jogada == "P":
    print("               Resultado:     Empate!    ")
elif jogada_pc == "Papel" and jogada == "S":
    print("               Resultado:     Você Ganhou!!!    ")
elif jogada_pc == "Papel" and jogada == "R":
    print("               Resultado:     Você Perdeu!!    ")
elif jogada_pc == "Tesoura" and jogada == "P":
    print("              Resultado:     Você Perdeu!!    ")
elif jogada_pc == "Tesoura" and jogada == "S":
    print("               Resultado:     Empate!    ")
elif jogada_pc == "Tesoura" and jogada == "R":
    print("               Resultado:     Você Ganhou!!!    ")
else:
    print("           Digite uma jogada válida (R),(P),(S)!")
print("            ==--==--==--==--==--==--==--==--==   ")
