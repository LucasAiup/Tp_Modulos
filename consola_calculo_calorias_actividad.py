import CalculadoraIMC
a=input("edad")  
b=input("peso")
c=input("altura en metros")
d=input("Sexo h / m")
e=input("valor de actividad")
test= CalculadoraIMC.calculadora_IMC(a,0,b,c,d,e)
print(round(test.calcular_calorias_en_actividad(), 2))
