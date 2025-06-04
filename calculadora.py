print("Escolha uma operação:")

print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operação = input("Digite a operação")

if operação in ["1", "2", "3", "4"]:
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número:"))


if operação == "1":
  resultado = num1+num2
  print("Resultado:", resultado)

elif operação == "2":
  resultado = num1-num2
  print("Resultado:", resultado)

elif operação == "3":
  resultado = num1*num2
  print("Resultado:", resultado)


elif operação == "4":
    if num2 == 0:
      print("Erro: divisão por zero!")
    else:
      resultado = num1 / num2
    print("Resultado:", resultado)

else:
   print("Operação inválida.")

