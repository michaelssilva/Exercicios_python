
def calcular(num1, num2, operacao):
 
  if operacao == 1:
    return num1 + num2
  elif operacao == 2:
    return num1 - num2
  elif operacao == 3:
    return num1 * num2
  elif operacao == 4:
    if num2 == 0:
      print("Divisão por zero não é permitida!")
      return 0
    else:
      return num1 / num2
  else:
    print("Operação inválida!")
    return 0

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = int(input("Digite o código da operação (1 - soma, 2 - subtração, 3 - multiplicação, 4 - divisão): "))

resultado = calcular(numero1, numero2, operacao)

print(f"Resultado: {resultado}")
