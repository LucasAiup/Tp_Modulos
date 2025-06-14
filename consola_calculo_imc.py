import CalculadoraIMC
c=input("c")
d=input("d")
test= CalculadoraIMC.calculadora_IMC(0,0,c,d,0)
print(round(test.calcular_IMC(), 2))
