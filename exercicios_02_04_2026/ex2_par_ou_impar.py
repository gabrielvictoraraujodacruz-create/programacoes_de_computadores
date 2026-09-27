# 2) Leia um número inteiro e verifique se ele é par ou ímpar.
numero = int(input("digitar numero: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.")  # CORRIGIDO: faltava a indentação dentro do if/else
else:
    print(f"O número {numero} é impar.")
