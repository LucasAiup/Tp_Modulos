class calculadora_IMC():
    def __init__(self,edad,valorGenero,peso,altura,Sexo,valorActividad):
        self.edad= int(edad)
        self.valorGenero= int(valorGenero)
        self.peso= float(peso)
        self.altura= float(altura)
        self.sexo=f"{Sexo}"
        self.valorActividad= float(valorActividad)
    def calcular_IMC(self):
        return round((self.peso/(self.altura**2)), 2)
    def calcular_porcentaje_grasa(self):
        Valor_Genero=self.calcular_valor_genero_grasa()
        imc=self.calcular_IMC()
        resultado=(1.2*imc)+(0.23*self.edad)-5.4-Valor_Genero 
        return resultado
    def calcular_calorias_en_reposo(self):
        Valor_Genero=self.calcular_valor_genero()
        tmb=(10*self.peso)+(6.25*(self.altura*100))-(5*self.edad)+Valor_Genero
        return tmb
    def calcular_calorias_en_actividad(self):
        tmb=self.calcular_calorias_en_reposo()
        return tmb*self.valorActividad
    def consumo_calorias_recomendado_para_adelgazar(self):
        tmb=self.calcular_calorias_en_reposo()
        min_result= tmb*0.80
        max_result= tmb*0.85
        return (f"Para adelgazar lo recomendado es que consumas entre: {round(min_result, 2)} y {round(max_result, 2)} calorias por dia")
    def calcular_valor_genero_grasa(self):
        if (self.sexo=="h"):
            return 10.8
        else:
            return 0
    def calcular_valor_genero(self):
        if (self.sexo=="h"):
            return 5
        else:
            return -161
