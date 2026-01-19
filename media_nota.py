nota1 = 5
nota2 = 6.5
nota3 = 8

resultado = (nota1 + nota2 + nota3) / 3
print('A média de notas é: ' + str(resultado))
if resultado < 5:
    print('Reprovado')
elif resultado >= 5 and resultado < 7.5:
    print('Recuperação')
else:
    print('Aprovado')
