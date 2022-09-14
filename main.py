def potencia(x,y):
  resultado = x ** y
  if y == 0:
    return 1

  return resultado

def fatorial(x):
  contador = 1
  while x > 0 :
    contador = contador * x
    x -= 1
  return contador

def permuta(x,y):
  resultado = fatorial(x)/ fatorial(x - y)

  return resultado

def combina(x,y):
  resultado = fatorial(x)/ (fatorial(x - y) * fatorial(y))

  return resultado

def binomio(x):
  calc = ''
  for a in range(x + 1):
    calc += f'{int(combina(x,a))} * a^{x - a} * b^{a}'
    if a < x:
      calc += ' + '
  return calc

def curvaBezier(x):
  calc = ''
  for a in range(x + 1):
    calc += f'{int(combina(x, a))}*(1-t)^{x-a} *t{a} *B{a}'
    if a < x:
      calc += ' + '
    calc += ', t E [0,1]'

  return calc

print("Bem vindo a sua calculadora personalizada, por favor escolha a operação que deseja:")
print("-Ponteciação(1) ")
print("-Fatoriação(2)")
print("-Permutação(3)")
print("-Combinação(4)")
print("-Polinomio Binomial(5)")
print("-Curva de Beziel(6)")

c = int(input("Qual vai querer?: "))
while c < 1 or c > 6:
  print ("entrada inválida, por favor coloque um número válido")
  c = int(input("Qual vai querer?: "))

if c == 1:
  x = int(input("Digite o número que quer elevar: "))
  y = int(input("Digite quanto quer elevar: "))
  print("resultado = " , potencia(x,y))
elif c == 2:
  x = int(input("Digite o número que quer fatorar: "))
  print("resultado = " , fatorial(x))
  
elif c == 3:
  x = int(input("Digite o n da permutação: "))
  y = int(input("Agora digite o r: "))
  print("resultado = " , permuta(x,y))
  
elif c == 4:
  x = int(input("Digite o n da combinação: "))
  y = int(input("Agora digite o r: "))
  print("resultado = " , combina(x,y))
elif c == 5:
  x = int(input("Digite o quanto quer elevar o seu binomio: "))
  print("resultado = " , binomio(x))
  
elif c == 6:
  x = int(input("Digite o n para a curva de Bezier: "))
  print("resultado = " , curvaBezier(x))