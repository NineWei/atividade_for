inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

soma_pares = 0

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        soma_pares += numero

else:
    if soma_pares == 0:
        print("Não há números pares no intervalo informado.")
    else:
        print(f"A soma dos números pares no intervalo é: {soma_pares}")