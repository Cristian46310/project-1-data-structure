#Clase en desarrollo

class Node:
    def __init__(self,value,parent=None):
        self.value = value
        self.left= None
        self.right= None
        self.parent = parent

class AVL:
    def __init__(self):
        self.root = None

    # Insert a new value into the BST
    def insert(self, value):
        node = self.search(value)
        if(node is not None):
          print("Node with value " , value, " already exists.")
        else:
          new_node = Node(value)
          if self.root is None:
              self.root = new_node
          else:
              self._insert(self.root, new_node)

    def _insert(self, current_node, new_node):
        if new_node.value < current_node.value:
            if current_node.left is None:
                current_node.left = new_node
                new_node.parent = current_node
            else:
                self._insert(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
                new_node.parent = current_node
            else:
                self._insert(current_node.right, new_node)

    # Search for a value in the BST
    def search(self, value):
        if(self.root is None):
          print("The tree is empty.")
          return None
        else:
          return self._search(self.root, value)

    def _search(self, current_node, value):
        if current_node is None or current_node.value == value:
            return current_node
        if value < current_node.value:
            return self._search(current_node.left, value)
        return self._search(current_node.right, value)

    # Find the inorder predecessor (the maximum in the left subtree)
    def _getPredecessor(self, node):
        if node.left is not None:
            current = node.left
            while current.right is not None:
                current = current.right
            return current
        return None

    # Replace one subtree with another (adjusts parent references)
    def changeNodePosition(self, node_to_replace, new_subtree_root):
        if node_to_replace.parent is None:  # If replacing the root
            self.root = new_subtree_root
        else:
            if node_to_replace == node_to_replace.parent.left:
                node_to_replace.parent.left = new_subtree_root
            else:
                node_to_replace.parent.right = new_subtree_root
        if new_subtree_root is not None:
            new_subtree_root.parent = node_to_replace.parent

    # Delete a node by value
    def delete(self, value):
        node_to_delete = self.search(value)
        if node_to_delete is not None:
            self._delete(node_to_delete)

    def _delete(self, node_to_delete):
        # Case 1: node is a leaf (no children)
        if node_to_delete.left is None and node_to_delete.right is None:
            self.changeNodePosition(node_to_delete, None)
            return

        # Case 2: node has two children
        if node_to_delete.left is not None and node_to_delete.right is not None:
            predecessor = self._getPredecessor(node_to_delete)
            if predecessor.parent != node_to_delete:  # predecessor is not a direct child
                self.changeNodePosition(predecessor, predecessor.left)
                predecessor.left = node_to_delete.left
                predecessor.left.parent = predecessor
            self.changeNodePosition(node_to_delete, predecessor)
            predecessor.right = node_to_delete.right
            predecessor.right.parent = predecessor
            return

        # Case 3: node has only one child
        if node_to_delete.left is not None:
            self.changeNodePosition(node_to_delete, node_to_delete.left)
        else:
            self.changeNodePosition(node_to_delete, node_to_delete.right)

    # Inorder traversal (left → root → right)
    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder(node.left)
        print(node.value, end=" ")
        if node.right:
            self.inorder(node.right)

   
    def obtener_altura(self, nodo):
        """Devuelve la altura del nodo."""
        return 0 if nodo is None else nodo.altura

    def obtener_factor_balance(self, nodo):
        """Devuelve el factor de balance del nodo."""
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha) if nodo else 0

    def rotacion_derecha(self, y):
        """Realiza una rotación a la derecha."""
        x = y.izquierda
        T2 = x.derecha

        x.derecha = y
        y.izquierda = T2

        # Actualizar alturas
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))
        x.altura = 1 + max(self.obtener_altura(x.izquierda), self.obtener_altura(x.derecha))

        return x

    def rotacion_izquierda(self, x):
        """Realiza una rotación a la izquierda."""
        y = x.derecha
        T2 = y.izquierda

        y.izquierda = x
        x.derecha = T2

        x.altura = 1 + max(self.obtener_altura(x.izquierda), self.obtener_altura(x.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y