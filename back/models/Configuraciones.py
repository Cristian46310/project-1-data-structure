class Configuracion:
    def __init__(self,distanciaTotal,velocidad,refresco_ms,salto_altura,color,x0,x1,y1):
        self.distanciaTotal = distanciaTotal
        self.velocidad = velocidad
        self.refresco_ms = refresco_ms
        self.salto_altura = salto_altura
        self.color = color
        self.x0 = x0
        self.x1 = x1
        self.y1 = y1
        self.y2= y1

    def toDict(self):
        settings={
            'distanciaTotal': self.distanciaTotal,
            'velocidad': self.velocidad,
            'refresco_ms': self.refresco_ms,
            'salto_altura': self.salto_altura,
            'color': self.color,
            'x0': self.x0,
            'x1': self.x1,
            'y1': self.y1,
            'y2': self.y2
        }
        return settings
       
 