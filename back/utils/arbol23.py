import json  # Importa la librería para manejar archivos JSON

# Clase que representa un nodo del árbol 2-3
class Node:
    def __init__(self, data=None):
        self.data = [] if data is None else [data]
        self.children = []
        self.is_leaf = True

    def is_full(self):
        # Verifica si el nodo tiene 2 datos (nodo 3)
        return len(self.data) == 2

    def insert_data(self, obstacle):
        # Inserta un nuevo obstáculo en el nodo y lo ordena por ID
        self.data.append(obstacle)
        self.data.sort(key=lambda x: x['id'])

# Clase que representa el árbol 2-3 completo
class Tree23:
    """
    A 2-3 Tree implementation for storing obstacles with coordinate and ID information.
    Methods
    -------
    __init__():
        Initializes an empty 2-3 tree with no root.
    insert(obstacle):
        Inserts an obstacle into the tree. If the tree is empty, creates the root node.
        Otherwise, recursively finds the correct position for the obstacle.
    _insert(node, obstacle):
        Recursively inserts an obstacle into the appropriate node. Handles duplicate coordinates
        and splits full nodes to maintain balance.
    _split(node):
        Splits a full node (with two data elements) into two nodes and creates a new root node
        to maintain the 2-3 tree properties.
    in_order(node=None):
        Performs an in-order traversal of the tree, printing each obstacle's data.
    range_query(x_min, x_max, y_min, y_max, node=None, result=None):
        Returns a list of obstacles whose coordinates fall within the specified rectangular range.
    insertarJson():
        Reads obstacles from a JSON file using the ObstacleJson class and inserts them into the tree.
    mostrarArbol(nodo=None, nivel=0, lado="Raíz"):
        Prints a visual representation of the tree structure, showing each node's data and whether it is a leaf.
    """
    def __init__(self):
        # Constructor: inicializa el árbol sin raíz
        self.root = None

    def insert(self, obstacle):
        # Inserta un obstáculo en el árbol
        if self.root is None:
            self.root = Node(obstacle)
        else:
            result = self._insert(self.root, obstacle)
            # Si el split sube un nuevo nodo, actualiza la raíz
            if isinstance(result, tuple):
                # (middle, left, right)
                middle, left, right = result
                new_root = Node(middle)
                new_root.is_leaf = False
                new_root.children = [left, right]
                self.root = new_root
            else:
                self.root = result

    def _insert(self, node, obstacle):
        if node.is_leaf:
            for obj in node.data:
                if (
                    obj.get('x0') == obstacle.get('x0') and
                    obj.get('y0') == obstacle.get('y0') and
                    obj.get('x1') == obstacle.get('x1') and
                    obj.get('y1') == obstacle.get('y1')
                ):
                    print(" Coordenadas duplicadas. No se inserta.")
                    return node
            node.insert_data(obstacle)
            if len(node.data) > 2:
                # Split leaf: return (middle, left, right)
                left = Node(node.data[0])
                right = Node(node.data[2])
                middle = node.data[1]
                return (middle, left, right)
            return node
        else:
            # Asegurar hijos
            while len(node.children) < len(node.data) + 1:
                node.children.append(Node())
            # Decidir a qué hijo insertar
            if obstacle['id'] < node.data[0]['id']:
                idx = 0
            elif len(node.data) == 1 or obstacle['id'] < node.data[1]['id']:
                idx = 1
            else:
                idx = 2
            result = self._insert(node.children[idx], obstacle)
            if isinstance(result, tuple):
                # Split hijo: insertar middle en este nodo
                middle, left, right = result
                node.data.insert(idx, middle)
                node.children[idx] = left
                node.children.insert(idx + 1, right)
                if len(node.data) > 2:
                    # Split este nodo
                    left_node = Node(node.data[0])
                    right_node = Node(node.data[2])
                    left_node.is_leaf = False
                    right_node.is_leaf = False
                    left_node.children = node.children[:2]
                    right_node.children = node.children[2:]
                    middle = node.data[1]
                    return (middle, left_node, right_node)
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