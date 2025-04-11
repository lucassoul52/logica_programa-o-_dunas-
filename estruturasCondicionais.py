#tratamento de notas invalidas 

#condicional composta, estrada pelo usuario

nota=float(input('Qual a sua nota?'))

#if condição que ira determinar uma condição se a nota for menor ou igual a zero ou se for maior que 10.
if nota <= 0 or nota >10:
    print('Erro: nota invalida. digite um valor entre 0 e 10.')
#elif função que dara uma condição se a nota for maior ou igual a 8
elif nota >=8:
    print('aprovado')
#elif função que dara uma condição se a nota for maior ou igual a 6
elif nota >=6:
    print('recuperação')
#else função que dara uma condição se a nota for menor que 6
else:
    print('reprovado')
