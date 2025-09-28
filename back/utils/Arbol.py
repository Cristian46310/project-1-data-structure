from back.Repository.ObstaculoJson import ObstacleJson
class NodoAVL:
    def __init__(self,clave,datos):
        self.clave=clave #Id con el cual se va a insertar
        self.datos=datos #datos del Json
        #Hijos izquierdo y derecho
        self.izquierda=None
        self.derecha=None
        #Altura del nodo
        self.altura=1
    
class ArbolAVL:
    """"
    AVL Tree implementation for storing and managing obstacles with spatial data.
    Attributes:
        raiz (NodoAVL): The root node of the AVL tree.
    Methods:
        altura(nodo):
            Returns the height of a given node.
        obtenerFactorBalance(nodo):
            Calculates and returns the balance factor of a node.
        rotacionDerecha(y):
            Performs a right rotation on the given subtree rooted at node y.
        rotacionIzquierda(x):
            Performs a left rotation on the given subtree rooted at node x.
        insertar(clave, datos):
            Inserts a new node with the specified key and data into the AVL tree.
        preOrden():
            Prints the nodes of the tree in pre-order traversal.
        inOrden():
            Prints the nodes of the tree in in-order traversal.
        postOrden():
            Prints the nodes of the tree in post-order traversal.
        consultarDistancia(x_min, x_max, y_min, y_max):
            Returns a list of obstacle data whose 'x' and 'y' values are within the specified range.
        insertarJson():
            Reads obstacle data from a JSON source and inserts each obstacle into the AVL tree.
        mostrarArbol(nodo=None, nivel=0, lado="Raíz"):
            Recursively prints the structure of the tree for visualization and debugging purposes.
        """
    def __init__(self):
        self.raiz=None
    
    # Obtener la altura de un nodo
    def altura(self,nodo):
        if not nodo:
            return 0
        return nodo.altura
    
    # Obtener el factor de balance de un nodo
    def obtenerFactorBalance(self,nodo):
        if not nodo:
            return 0
        return self.altura(nodo.izquierda)-self.altura(nodo.derecha)
    
    #Rotaciones
    def rotacionDerecha(self,y):
        x=y.izquierda
        T2=x.derecha
        
        x.derecha=y
        y.izquierda=T2
        
        y.altura=1+max(self.altura(y.izquierda),self.altura(y.derecha))
        x.altura=1+max(self.altura(x.izquierda),self.altura(x.derecha))
        
        return x
    
    def rotacionIzquierda(self,x):
        y=x.derecha
        T2=y.izquierda
        
        y.izquierda=x
        x.derecha=T2
        
        x.altura=1+max(self.altura(x.izquierda),self.altura(x.derecha))
        y.altura=1+max(self.altura(y.izquierda),self.altura(y.derecha))
        
        return y
    
    def insertar(self,clave,datos):
        self.raiz=self._insertar(self.raiz,clave,datos)
    
    def _insertar(self,nodo,clave,datos):
        if not nodo:
            return NodoAVL(clave,datos)
        elif clave< nodo.clave:
            nodo.izquierda=self._insertar(nodo.izquierda,clave,datos)
        elif clave> nodo.clave:
            nodo.derecha=self._insertar(nodo.derecha,clave,datos)
        else:
            return nodo
        
        nodo.altura=1+max(self.altura(nodo.izquierda),self.altura(nodo.derecha))
        
        factorBalance=self.obtenerFactorBalance(nodo)
        
        if factorBalance>1 and clave< nodo.izquierda.clave:
            return self.rotacionDerecha(nodo)
        if factorBalance<-1 and clave> nodo.derecha.clave:
            return self.rotacionIzquierda(nodo)
        if factorBalance>1 and clave> nodo.izquierda.clave:
            nodo.izquierda=self.rotacionIzquierda(nodo.izquierda)
            return self.rotacionDerecha(nodo)
        if factorBalance<-1 and clave< nodo.derecha.clave:
            nodo.derecha=self.rotacionDerecha(nodo.derecha)
            return self.rotacionIzquierda(nodo)
        return nodo
    
    def preOrden(self):
        self._preOrden(self.raiz)
    
    def _preOrden(self,nodo):
        if not nodo:
            return
        print(nodo)
        self._preOrden(nodo.izquierda)
        self._preOrden(nodo.derecha)
    
    def inOrden(self):
        self._inOrden(self.raiz)
    
    def _inOrden(self,nodo):
        if not nodo:
            return
        self._inOrden(nodo.izquierda)
        print(nodo)
        self._inOrden(nodo.derecha)

    def postOrden(self):
        self._postOrden(self.raiz)

    def _postOrden(self,nodo):
        if not nodo:
            return
        self._postOrden(nodo.izquierda)
        self._postOrden(nodo.derecha)
        print(nodo)
    
    def consultarDistancia(self, x_min, x_max, y_min, y_max):
        """
        Retorna una lista de obstáculos (datos) cuyos valores 'x' y 'y' están dentro del rango especificado.
        """
        resultado = []
        self._consultarDistancia(self.raiz, x_min, x_max, y_min, y_max, resultado)
        return resultado

    def _consultarDistancia(self, nodo, x_min, x_max, y_min, y_max, resultado):
        if not nodo:
            return
        x = nodo.datos.get('x0')
        y = nodo.datos.get('y0')
        if x is not None and y is not None:
            if x_min <= x <= x_max and y_min <= y <= y_max:
                resultado.append(nodo.datos)
        self._consultarDistancia(nodo.izquierda, x_min, x_max, y_min, y_max, resultado)
        self._consultarDistancia(nodo.derecha, x_min, x_max, y_min, y_max, resultado)
    
    def insertarJson(self):
        obtacle_json=ObstacleJson()
        obstacles=obtacle_json.readJsonObstacle()
        if not obstacles:
            return None
        else:
            for obs in obstacles:
                self.insertar(obs['id'],obs)
            return self.raiz
        

        #FUNCION INUTIL SOLO PARA VERIFICAR QUE EL ARBOL ESTA BIEN, SE BORRARA AL FINAL DEL PROYECTO
    def mostrarArbol(self, nodo=None, nivel=0, lado="Raíz"):
        # Solo en la primera llamada tomamos la raíz
        if nodo is None and nivel == 0:
            nodo = self.raiz
        
        if nodo is None:
            return  

        # Subárbol derecho
        self.mostrarArbol(nodo.derecha, nivel + 1, "Der")

        # Nodo actual
        print("    " * nivel + f"[{lado}] id={nodo.clave}, datos={nodo.datos}")

        # Subárbol izquierdo
        self.mostrarArbol(nodo.izquierda, nivel + 1, "Izq")
        
