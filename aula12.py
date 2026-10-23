# Condições com if, else e elif em Python

idade = 60
e_membro = True
if idade > 60:
    if e_membro:
     print( " 30 % de desconto" )
    else:
     print( " 20 % de desconto")
elif idade >= 50 :
  print("vale compras com cashback")
else:
  print( " sem desconto")