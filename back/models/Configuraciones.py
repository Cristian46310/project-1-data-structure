class Configuracion:
    def __init__(self,distanciaTotal,velocidad,refresco_ms,salto_altura,color):
        self.distanciaTotal = distanciaTotal
        self.velocidad = velocidad
        self.refresco_ms = refresco_ms
        self.salto_altura = salto_altura
        self.color = color

    def toDict(self):
        settings={
            'distanciaTotal': self.distanciaTotal,
            'velocidad': self.velocidad,
            'refresco_ms': self.refresco_ms,
            'salto_altura': self.salto_altura,
            'color': self.color
        }
        return settings
       
 