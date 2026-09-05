def dividir(a, b):
    if b == 0:
        return "Erro:não é possível dividir por zero. "

    return a / b

numero_1 = float(input("Digite um número: ")) 
numero_2 = float(input("Digite um número: "))  

print("Divisão:", dividir(numero_1, numero_2))
     