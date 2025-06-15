import CalculadoraIMC
c=input("peso")
d=input("altura en metros")
test= CalculadoraIMC.calculadora_IMC(0,0,c,d,0)
print(f"Resultado:{round(test.calcular_IMC(), 2)}")
