produto_1 = int(input("Digite um valor: "))
produto_2 = int(input("Digite o segundo valor:"))

resultado = produto_1 + produto_2



par_impar = resultado % 2

if par_impar == 0:
    print("a soma dos valores eh um numero par!")
elif par_impar == 1:
    print("a soma dos valores eh um nomero impar!")
else:
    print('ERRO')
