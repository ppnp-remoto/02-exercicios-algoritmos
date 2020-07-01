nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: ")) 
nota_3 = float(input("Digite a terceira nota: ")) 

media = (nota_1 + nota_2 + nota_3) / 3

# Estrutura condicional
if(media >= 7):
    print("Aprovado com a média: ", media)
elif media >= 5 and media <= 6.9:
    print("Recuperação com a média: ", media)
else:
    print("Reprovado com a média: ", media)