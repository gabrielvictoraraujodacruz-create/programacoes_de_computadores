# 3) Leia a idade de uma pessoa e informe se ela é maior ou menor de idade (18 anos).
idade = int(input("Digite sua idade:"))
if idade < 18:  # CORRIGIDO: era <= 18, e quem tem 18 já é maior de idade
    print(f"É menor de idade")
else:
    print(f"É maior de idade")
