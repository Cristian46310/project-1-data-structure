from back.utils.Arbol import ArbolAVL
import pygame
from pygame import draw, font

class AVLVisualizer:
    def __init__(self, screen, tree):
        self.screen = screen
        self.tree = tree
        self.node_radius = 20
        self.font = font.SysFont('Arial', 20)

    def _get_height(self, node):
        if node is None:
            return 0
        return 1 + max(self._get_height(node.izquierda), self._get_height(node.derecha))

    def draw_tree(self, node, x, y, x_offset, level_gap):
        if node is None:
            return

        node.pos_x = x
        node.pos_y = y

        # dibujar nodo
        draw.circle(self.screen, (0, 255, 0), (x, y), self.node_radius)
        text_surface = self.font.render(str(node.clave), True, (255, 255, 255))
        self.screen.blit(text_surface, (x - text_surface.get_width() // 2,
                                        y - text_surface.get_height() // 2))

        # hijos
        if node.izquierda:
            left_x = x - x_offset
            left_y = y + level_gap
            draw.line(self.screen, (255, 255, 255),
                      (x, y + self.node_radius), (left_x, left_y), 2)
            self.draw_tree(node.izquierda, left_x, left_y, x_offset // 2, level_gap)

        if node.derecha:
            right_x = x + x_offset
            right_y = y + level_gap
            draw.line(self.screen, (255, 255, 255),
                      (x, y + self.node_radius), (right_x, right_y), 2)
            self.draw_tree(node.derecha, right_x, right_y, x_offset // 2, level_gap)

    def highlight_node(self, node, color=(255, 0, 0)):
        self.visualize()  # Redibuja el árbol
        pygame.draw.circle(self.screen, color, (node.pos_x, node.pos_y), self.node_radius)
        text_surface = self.font.render(str(node.clave), True, (255, 255, 255))
        self.screen.blit(text_surface, (node.pos_x - text_surface.get_width() // 2,
                                        node.pos_y - text_surface.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(600)  # pausa de 600ms

    def visualize(self):
        self.screen.fill((0, 0, 0))
        if self.tree.raiz is None:
            pygame.display.flip()
            return

        # altura y profundidad del árbol
        height = self._get_height(self.tree.raiz)

        # ajuste dinámico horizontal
        total_width = self.screen.get_width()
        max_depth = max(height, 1)
        x_offset = max(total_width // (2 ** max_depth), 20)

        # ajuste dinámico vertical
        total_height = self.screen.get_height()
        level_gap = max((total_height - 100) // max_depth, 40)  # 100 px de margen arriba

        # dibujar desde la raíz
        self.draw_tree(self.tree.raiz, total_width // 2, 50, x_offset * 4, level_gap)

        # título
        draw.rect(self.screen, (255, 255, 255), (0, 0, self.screen.get_width(), 40))
        title_surface = self.font.render("AVL Tree Visualization", True, (0, 0, 0))
        self.screen.blit(title_surface, (self.screen.get_width() // 2 - title_surface.get_width() // 2, 10))

        pygame.display.flip()

    def wait_for_key(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    waiting = False
    def recorrido_inorden_visual(self, nodo):
        if nodo is None:
            return
        self.recorrido_inorden_visual(nodo.izquierda)
        self.highlight_node(nodo)
        self.recorrido_inorden_visual(nodo.derecha)

    def recorrido_preorden_visual(self, nodo):
        if nodo is None:
            return
        self.highlight_node(nodo)
        self.recorrido_preorden_visual(nodo.izquierda)
        self.recorrido_preorden_visual(nodo.derecha)

    def recorrido_postorden_visual(self, nodo):
        if nodo is None:
            return
        self.recorrido_postorden_visual(nodo.izquierda)
        self.recorrido_postorden_visual(nodo.derecha)
        self.highlight_node(nodo)

    def recorrido_anchura_visual(self):
        if not self.tree.raiz:
            return
        cola = [self.tree.raiz]
        while cola:
            nodo = cola.pop(0)
            self.highlight_node(nodo)
            if nodo.izquierda:
                cola.append(nodo.izquierda)
            if nodo.derecha:
                cola.append(nodo.derecha)
