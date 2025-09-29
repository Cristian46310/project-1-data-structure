import pygame
from back.utils.arbol23 import Tree23
class Visualizer23:
    def __init__(self, screen, tree=None):
        self.screen = screen
        self.tree = tree if tree else Tree23()
        self.max_width = 950  # límite horizontal en px para el árbol

    def update_tree(self):
        self.tree = Tree23()
        self.tree.insertarJson()

    def draw(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 18)

        GAMA_WIDTH = 0  
        SCREEN_WIDTH = self.screen.get_width()
        SCREEN_HEIGHT = self.screen.get_height()
        avl_surface = self.screen.subsurface((GAMA_WIDTH, 0, SCREEN_WIDTH - GAMA_WIDTH, SCREEN_HEIGHT))

        avl_width, avl_height = avl_surface.get_width(), avl_surface.get_height()
        start_x = avl_width // 2
        start_y = int(avl_height * 0.07)

        max_tree_width = avl_width

        # Dibujar el árbol a partir de la raíz
        self._draw_node(self.tree.root, start_x, start_y, font, max_tree_width, 0, avl_surface, avl_width, avl_height)

    def _draw_node(self, node, x, y, font, area_width, nivel, surface, total_width, total_height):
        if node is None:
            return

        # Tamaño proporcional del nodo
        node_width = max(60, int(total_width * 0.09))
        node_height = max(28, int(total_height * 0.06))
        color = (0, 200, 200) if node.is_leaf else (200, 200, 0)

        # Mostrar hasta 2 claves
        ids = [str(d['id']) for d in node.data]
        while len(ids) < 2:
            ids.append(' ')
        text = font.render(f"{ids[0]} | {ids[1]}", True, (255, 255, 255))

        # Dibujar el nodo
        rect = pygame.Rect(x - node_width // 2, y, node_width, node_height)
        pygame.draw.rect(surface, color, rect, 2)
        surface.blit(text, (x - text.get_width() // 2, y + int(node_height * 0.2)))

        # Dibujar los hijos si existen
        if not node.is_leaf and node.children:
            num_children = len(node.children)
            spread = max(int(total_width * 0.22), area_width // max(num_children, 1))
            if spread * num_children > area_width:
                spread = area_width // num_children

            base_x = x - (spread * (num_children - 1)) // 2
            child_y = y + int(total_height * 0.15)

            for i, child in enumerate(node.children):
                child_x = base_x + i * spread
                pygame.draw.line(
                    surface,
                    (255, 255, 255),
                    (x, y + node_height),
                    (child_x, child_y)
                )
                self._draw_node(child, child_x, child_y, font, spread, nivel + 1, surface, total_width, total_height)
