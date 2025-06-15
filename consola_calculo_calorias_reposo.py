import CalculadoraIMC
a=input("edad")  
b=input("peso")
c=input("altura en metros")
d=input("Sexo h / m")
test= CalculadoraIMC.calculadora_IMC(a,0,b,c,d,0)
print(f"Resultado:{round(test.calcular_calorias_en_reposo(), 2)}")
