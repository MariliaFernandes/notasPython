nota1 = float(input('Por favor digite a primeira nota: '))
nota2 = float(input('Por favor digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
  print('Voce está aprovado com media {}'.format(media))
if media == 10:
  print('Voce está Aprovado com Distinção com media {}'.format(media))

else:
  print('Voce está reprovado com media {}'.format(media))