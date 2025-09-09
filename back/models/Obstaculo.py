class Obstaculos:
    def __init__(self,id, x, y, tipo, x1):
        self.id = id
        self.x = x
        self.y = y
        self.tipo = tipo
        self.x1 = x1
        self.y1 = y
    

    def toDict(self):
        obstaculos={
            'id': self.id,
            'x0': self.x,
            'y0': self.y,
            'x1': self.x1,
            'y1': self.y,
            'tipo': self.tipo
        }
        return obstaculos