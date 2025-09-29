import pygame
import os
from back.Controller.ObstacleController import ObstacleController
from back.utils.Arbol import ArbolAVL

OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 80, 80
LANES = 3

def get_lane_from_y(y0, lane_height=0):
    if y0 <= lane_height:
        return 0
    elif y0 <= 2 * lane_height:
        return 1
    else:
        return 2

class ObstacleManager:
    def __init__(self, assets_path, lane_height, screen_width):
        self.assets_path = assets_path
        self.lane_height = lane_height
        self.screen_width = screen_width

        # Cargar imágenes
        self.persona_img = self.load_image("persona.png", (60, 80))
        self.cono_img = self.load_image("cono.png", (50, 50))
        self.bache_img = self.load_image("bache.png", (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.roca_img = self.load_image("roca.png", (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

        # Árbol de obstáculos (tu código existente)
        self.controller = ObstacleController()
        self.arbol = ArbolAVL()
        self.arbol.insertarJson()  # carga desde JSON

        # Lista de obstáculos visibles en la pantalla actual (cada frame se rellena)
        self.visible_obstacles = []

        # Conjunto de obstáculos ya "consumidos" por colisión (identificados por su world_x)
        self.consumed_world_x = set()

        # Distancia mínima (en coordenadas world) entre el coche y el obstáculo
        # para que el obstáculo se considere "seguro" y no choque instantáneo al iniciar.
        self.safe_spawn_margin = 120  # ajústalo si hace falta
    def remaining_obstacles(self):
        """Devuelve True si todavía hay obstáculos que no se han consumido"""
        # Consultar todos los obstáculos en el árbol
        all_obstacles = self.arbol.inorder()  # o el método que devuelva todos los nodos
        # Filtrar los que no han sido consumidos
        remaining = [o for o in all_obstacles if o['x0'] not in self.consumed_world_x]
        return remaining

    def load_image(self, name, size=None):
        path = os.path.join(self.assets_path, name)
        img = pygame.image.load(path).convert_alpha()
        if size:
            img = pygame.transform.scale(img, size)
        return img

    def get_visible_obstacles(self, car_x, screen_height):
        """Consulta al árbol los obstáculos en el rango visible (world coords)."""
        x_min = car_x
        x_max = car_x + self.screen_width
        y_min = 0
        y_max = screen_height
        return self.arbol.consultarDistancia(x_min, x_max, y_min, y_max)

    def draw_obstacles(self, screen, car_x, lane_height):
        """Dibuja los obstáculos visibles en pantalla sin hitboxes visibles."""

        obstaculos_visibles = self.get_visible_obstacles(car_x, lane_height * LANES)
        MIN_SEPARACION_X = 50
        ultimas_x_por_carril = [None] * LANES
        self.visible_obstacles = []  # limpiar lista actual

        for obs in sorted(obstaculos_visibles, key=lambda o: o['x0']):
            world_x = obs['x0']

            # Omitir obstáculos ya consumidos
            if world_x in self.consumed_world_x:
                continue

            # Ignorar obstáculos demasiado cerca al coche
            if world_x <= car_x + self.safe_spawn_margin:
                continue

            # Determinar carril
            lane_actual = get_lane_from_y(obs['y0'], lane_height)
            obs_x = world_x - car_x + 50
            obs_y = lane_actual * lane_height + (lane_height * 2 // 4) - (OBSTACLE_HEIGHT // 2)

            if ultimas_x_por_carril[lane_actual] is not None:
                if obs_x - ultimas_x_por_carril[lane_actual] < MIN_SEPARACION_X:
                    obs_x = ultimas_x_por_carril[lane_actual] + MIN_SEPARACION_X
            ultimas_x_por_carril[lane_actual] = obs_x

            # Seleccionar imagen y daño
            if obs['tipo'] == "persona":
                img = self.persona_img
                damage = 30
            elif obs['tipo'] == "cono":
                img = self.cono_img
                damage = 10
            elif obs['tipo'] == "bache":
                img = self.bache_img
                damage = 20
            elif obs['tipo'] == "roca":
                img = self.roca_img
                damage = 40
            else:
                img = self.cono_img
                damage = 15

            # Dibujar imagen
            screen.blit(img, (obs_x, obs_y))

            # Guardar rect para colisiones (sin dibujar)
            rect = pygame.Rect(obs_x, obs_y, img.get_width(), img.get_height())

            self.visible_obstacles.append({
                "rect": rect,
                "damage": damage,
                "tipo": obs['tipo'],
                "world_x": world_x,
                "id": obs['id']
            })


    def get_obstacles(self):
        """Devuelve la lista de obstáculos visibles (rect, damage, tipo, world_x)."""
        return self.visible_obstacles

    def mark_obstacle_consumed(self, world_x):
        """Marca un obstáculo por su coordenada world_x como ya golpeado/consumido."""
        self.consumed_world_x.add(world_x)
