diasentrada = int(input())

anos = int(diasentrada/365)
diasentrada -= anos*365

meses = int(diasentrada/30)
diasentrada -= meses*30

dias = diasentrada

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(anos,meses,dias))