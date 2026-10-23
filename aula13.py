# Condições com if, else e elif em Python

nota1 = 12
nota2 = 18
nota3 = 19

media = (nota1 + nota2 + nota3) / 3

if media >= 12 :
  print("Aprovada - NOTA :", round (media, 2))
elif media >= 10:
   print("Recuperação - NOTA :", round (media, 2))
else:
 print("Reprovada - NOTA ", round (media, 2))