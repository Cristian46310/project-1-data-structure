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
    """
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
        recorridoAnchura():
            Performs a breadth-first traversal (BFS) of the AVL tree and returns a list of visited nodes.
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
    def eliminar(self, key):
        """
        Elimina un nodo del árbol AVL por su clave (id o world_x según cómo lo uses).
        """
        if hasattr(self, "root") and self.root is not None:
            self.root = self._eliminar_rec(self.root, key)

    def _eliminar_rec(self, nodo, key):
        if nodo is None:
            return None

        if key < nodo.key:
            nodo.left = self._eliminar_rec(nodo.left, key)
        elif key > nodo.key:
            nodo.right = self._eliminar_rec(nodo.right, key)
        else:
            # nodo a eliminar encontrado
            if nodo.left is None:
                return nodo.right
            elif nodo.right is None:
                return nodo.left

            # reemplazar con el mínimo del subárbol derecho
            min_larger_node = self._min_value_node(nodo.right)
            nodo.key = min_larger_node.key
            nodo.data = min_larger_node.data
            nodo.right = self._eliminar_rec(nodo.right, min_larger_node.key)

        # actualizar altura y balance aquí si usas AVL
        nodo = self._rebalance(nodo)
        return nodo

    def _min_value_node(self, nodo):
        current = nodo
        while current.left is not None:
            current = current.left
        return current

    def _rebalance(self, nodo):
        # tu código de rebalanceo AVL aquí
        return nodo
    def preOrden(self):
        self._preOrden(self.raiz)
    
    def _preOrden(self,nodo):
        if not nodo:
            return
        print(nodo.datos)
        self._preOrden(nodo.izquierda)
        self._preOrden(nodo.derecha)
    
    def inOrden(self):
        self._inOrden(self.raiz)
    
    def _inOrden(self,nodo):
        if not nodo:
            return
        self._inOrden(nodo.izquierda)
        print(nodo.datos)
        self._inOrden(nodo.derecha)

    def postOrden(self):
        self._postOrden(self.raiz)

    def _postOrden(self,nodo):
        if not nodo:
            return
        self._postOrden(nodo.izquierda)
        self._postOrden(nodo.derecha)
        print(nodo.datos)
    
    def recorridoAnchura(self):
        if not self.raiz:
            return []
        resultado = []
        cola = [self.raiz]
        while cola:
            nodo = cola.pop(0)
            resultado.append(nodo.datos)
            if nodo.izquierda:
                cola.append(nodo.izquierda)
            if nodo.derecha:
                cola.append(nodo.derecha)
        return resultado
    
    def consultarDistancia(self, x_min, x_max, y_min, y_max):
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
        
