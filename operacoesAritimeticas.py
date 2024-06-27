def operacaoAritimetica(operacao,num1,num2):
  if(operacao == 1):
    return (num1 + num2)
  if(operacao == 2):
    return (num1 - num2)
  if(operacao == 3):
    return(num1 + num2)
  if(operacao == 4 and (num1 <= 0 or num2 <= 0)):
    return "Tentativa de calculo invalida com numeros iguais ou menores a zero,\nFavor utilizar valores válidos"
  elif(operacao == 4):
    return num1 / num2


print("iniciando loop de calculos")

mensagem = "\nInforme a opção de operação matemática desejada\n-----------------------\n1: Soma\n2: Subtração\n3: Multiplicação\n4: Divisão\n-----------------------\n0: Sair"
print(mensagem)

opcao = int(input())

opcoesValidas = [1,2,3,4,0]

while(opcao != 0):
  
  if(opcao != 0 and  opcao in opcoesValidas):
    print("Informe o primeiro numero")
    n1 = float(input())

    print("Informe o segundo numero")
    n2 = float(input())

    print(operacaoAritimetica(opcao, n1 , n2))
  else:
    print("\nEssa opção não existe.\nEscolha uma das opções abaixo:")
    
  print(mensagem)
  opcao = int(input())

print("Encerrando loop")
