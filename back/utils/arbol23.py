import json  # Importa la librería para manejar archivos JSON

# Clase que representa un nodo del árbol 2-3
class Node:
    def _init_(self, data=None):
        # Constructor: inicializa el nodo con datos y lo marca como hoja
        self.data = [] if data is None else [data]  # Lista de obstáculos (máximo 2)
        self.children = []  # Lista de hijos (0, 2 o 3 dependiendo del tipo de nodo)
        self.is_leaf = True  # Por defecto, el nodo es una hoja

    def is_full(self):
        # Verifica si el nodo tiene 2 datos (nodo 3)
        return len(self.data) == 2

    def insert_data(self, obstacle):
        # Inserta un nuevo obstáculo en el nodo y lo ordena por ID
        self.data.append(obstacle)
        self.data.sort(key=lambda x: x['id'])

# Clase que representa el árbol 2-3 completo
class Tree23:
    def _init_(self):
        # Constructor: inicializa el árbol sin raíz
        self.root = None

    def insert(self, obstacle):
        # Inserta un obstáculo en el árbol
        if self.root is None:
            # Si el árbol está vacío, crea la raíz con el obstáculo
            self.root = Node(obstacle)
        else:
            # Inserta recursivamente en el árbol
            self.root = self._insert(self.root, obstacle)

    def _insert(self, node, obstacle):
        # Método recursivo que inserta en el nodo adecuado
        if node.is_leaf:
            # Si es hoja, verifica si ya existe un obstáculo en esa posición
            for obj in node.data:
                if (obj['x0'], obj['y0'], obj['x1'], obj['y1']) == (obstacle['x0'], obstacle['y0'], obstacle['x1'], obstacle['y1']):
                    print("❌ Coordenadas duplicadas. No se inserta.")
                    return node
            # Inserta el obstáculo
            node.insert_data(obstacle)
            # Si el nodo está lleno (2 datos), se divide para balancear
            if node.is_full():
                return self._split(node)
            return node
        else:
            # Si no es hoja, decide en qué hijo insertar según el ID
            if obstacle['id'] < node.data[0]['id']:
                node.children[0] = self._insert(node.children[0], obstacle)
            elif len(node.data) == 1 or obstacle['id'] < node.data[1]['id']:
                node.children[1] = self._insert(node.children[1], obstacle)
            else:
                node.children[2] = self._insert(node.children[2], obstacle)
            return node

    def _split(self, node):
        # Divide un nodo lleno en dos nodos y crea un nuevo nodo raíz
        left = Node(node.data[0])   # Nodo izquierdo con el primer dato
        right = Node(node.data[1])  # Nodo derecho con el segundo dato
        new_root = Node()           # Nuevo nodo raíz
        new_root.data = [node.data[1]]  # El segundo dato sube a la raíz
        new_root.children = [left, right]  # Asigna los nuevos hijos
        new_root.is_leaf = False
        return new_root  # Retorna el nuevo nodo balanceado

    def in_order(self, node=None):
        # Recorrido in-order (izquierda, raíz, derecha)
        if node is None:
            node = self.root
        if node.is_leaf:
            for data in node.data:
                print(data)
        else:
            self.in_order(node.children[0])  # Recursivo: hijo izquierdo
            print(node.data[0])
            self.in_order(node.children[1])  # Recursivo: hijo medio
            if len(node.data) == 2:
                print(node.data[1])
                self.in_order(node.children[2])  # Recursivo: hijo derecho

    def range_query(self, x_min, x_max, y_min, y_max, node=None, result=None):
        # Consulta obstáculos dentro de un rango de coordenadas
        if result is None:
            result = []
        if node is None:
            node = self.root
        for data in node.data:
            # Verifica si el obstáculo está dentro del área visible
            if x_min <= data['x0'] <= x_max and y_min <= data['y0'] <= y_max:
                result.append(data)
        if not node.is_leaf:
            # Recursivo: consulta en todos los hijos
            for child in node.children:
                self.range_query(x_min, x_max, y_min, y_max, child, result)
        return result

    def insertarJson(self):
        # Importa la clase ObstacleJson para leer obstáculos del archivo JSON
        from back.Repository.ObstaculoJson import ObstacleJson
        
        obstacle_json = ObstacleJson()
        obstacles = obstacle_json.readJsonObstacle()
        
        if not obstacles:
            return None
        else:
            for obs in obstacles:
                self.insert(obs)
            return self.root

    def mostrarArbol(self, nodo=None, nivel=0, lado="Raíz"):
        # Función para visualizar la estructura del árbol
        if nodo is None:
            nodo = self.root
        if nodo is None:
            print("El árbol está vacío")
            return
        
        indent = "  " * nivel
        print(f"{indent}{lado}: {[obs['id'] for obs in nodo.data]} (Hoja: {nodo.is_leaf})")
        
        if not nodo.is_leaf:
            for i, child in enumerate(nodo.children):
                if i == 0:
                    self.mostrarArbol(child, nivel + 1, "Izquierdo")
                elif i == 1:
                    self.mostrarArbol(child, nivel + 1, "Medio")
                else:
                    self.mostrarArbol(child, nivel + 1, "Derecho")