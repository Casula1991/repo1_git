def soma(a,b):
	return a+b

def subtracao(a,b):
	return a-b

def produto(a,b):
	return a*b

def divisao(a,b):
	return a/b

############################################

def calculadora(a,b, func):
	x = func(a,b)
	return x

print(calculadora(10,5, func = soma))

############################################
print(calculadora(10,5, func = soma))
print(calculadora(10,5, func = subtracao))
print(calculadora(10,5, func = produto))
print(calculadora(10,5, func = divisao))