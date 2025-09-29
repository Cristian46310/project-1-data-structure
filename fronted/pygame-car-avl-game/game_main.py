import pygame
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from back.utils.Arbol import ArbolAVL
from src.game.obstacle import ObstacleManager
from src.game.car import Car
from src.game.avl_visualizer import AVLVisualizer
from back.Controller.ObstacleController import ObstacleController
# Configuración básica
SCREEN_WIDTH = 1200
GAMA_WIDTH = 900
SCREEN_HEIGHT = 400
LANES = 3
LANE_HEIGHT = SCREEN_HEIGHT // LANES
CAR_WIDTH, CAR_HEIGHT = 180,135
CARRILES_Y = [
    (LANE_HEIGHT - CAR_HEIGHT) // 2,                      # Carril superior
    LANE_HEIGHT + (LANE_HEIGHT - CAR_HEIGHT) // 2,        # Carril medio
    2 * LANE_HEIGHT + (LANE_HEIGHT - CAR_HEIGHT) // 2     # Carril inferior
]
ASSETS_PATH = os.path.join(os.path.dirname(__file__), "assets")


def get_lane_from_y(y0):
    if y0 <= LANE_HEIGHT:
        return 0
    elif y0 <= 2 * LANE_HEIGHT:
        return 1
    else:
        return 2


def load_image(name, size=None):
    path = os.path.join(ASSETS_PATH, name)
    img = pygame.image.load(path).convert_alpha()
    if size:
        img = pygame.transform.scale(img, size)
    return img


def draw_car(   screen, lane, car_img):
    x = 50
    y = CARRILES_Y[lane]
    screen.blit(car_img, (x, y))


def draw_lanes(screen):
    for i in range(1, LANES):
        pygame.draw.line(screen, (255, 255, 255), (0, i * LANE_HEIGHT), (SCREEN_WIDTH, i * LANE_HEIGHT), 2)


def show_menu(screen):
    font = pygame.font.SysFont(None, 60)
    small_font = pygame.font.SysFont(None, 36)
    title = font.render("Car Game with AVL Obstacles", True, (255, 255, 255))
    start_text = small_font.render("Presiona ENTER o haz clic para empezar", True, (200, 200, 0))

    screen.fill((30, 30, 30))
    screen.blit(title, ((SCREEN_WIDTH - title.get_width()) // 2, SCREEN_HEIGHT // 3))
    screen.blit(start_text, ((SCREEN_WIDTH - start_text.get_width()) // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False


def draw_score(screen, score):
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(ASSETS_PATH, "musica.mp3"))
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Car Game with AVL Obstacles")

    # Fondo
    fondo_img = load_image("fondo.png", (GAMA_WIDTH, SCREEN_HEIGHT))

    # Crear carro
    CAR_SCREEN_X = 50
    car = Car(ASSETS_PATH, CAR_SCREEN_X, CARRILES_Y[1], CAR_WIDTH, CAR_HEIGHT, speed=0)

    # Árbol AVL y visualizador
    arbol = ArbolAVL()
    arbol.insertarJson()
    avl_visualizer = AVLVisualizer(screen, arbol)

    show_menu(screen)

    # Manejo de obstáculos
    obstacle_manager = ObstacleManager(ASSETS_PATH, LANE_HEIGHT, GAMA_WIDTH)
    obstacle_controller = ObstacleController()

    clock = pygame.time.Clock()
    running = True
    lane = 1
    score = 0
    car_x = 50

    ADVANCE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(ADVANCE_EVENT, 200)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and lane > 0:
                    lane -= 1
                    if not car.is_jumping:
                        car.rect.y = CARRILES_Y[lane]
                elif event.key == pygame.K_DOWN and lane < LANES - 1:
                    lane += 1
                    if not car.is_jumping:
                        car.rect.y = CARRILES_Y[lane]
                elif event.key == pygame.K_SPACE:
                    car.start_jump()
            elif event.type == ADVANCE_EVENT:
                score += 1
                car_x += 80

        if not car.is_jumping:
            car.rect.y = CARRILES_Y[lane]

        car.update()

        # Limpiar pantalla
        screen.fill((0, 0, 0))
        screen.blit(fondo_img, (0, 0))
        draw_lanes(screen)
        draw_score(screen, score)

        obstacle_manager.draw_obstacles(screen, car_x, LANE_HEIGHT)
        obstacles = obstacle_manager.get_obstacles()

        # Procesar colisiones
        for obs in obstacles:
            if car.get_rect().colliderect(obs["rect"]):
                applied = car.hit(obs["damage"])
                if applied:
                    print(f"💥 Colisión con {obs['tipo']} (ID={obs.get('id', obs['world_x'])})")
                    obstacle_manager.mark_obstacle_consumed(obs["world_x"])
                    obstacle_controller.deleteObstacle(obs.get("id", obs["world_x"]))
                    arbol = ArbolAVL()
                    arbol.insertarJson()
                    avl_visualizer.tree = arbol

        # Barra de energía
        bar_x, bar_y, bar_w, bar_h = 10, 10, 200, 16
        pygame.draw.rect(screen, (100, 100, 100), (bar_x, bar_y, bar_w, bar_h))
        energy_w = int((car.energy / 100) * bar_w)
        pygame.draw.rect(screen, (0, 200, 0), (bar_x, bar_y, energy_w, bar_h))

        car.render(screen)

        # AVL
        avl_surface = screen.subsurface((GAMA_WIDTH, 0, SCREEN_WIDTH - GAMA_WIDTH, SCREEN_HEIGHT))
        avl_surface.fill((0, 0, 0))
        avl_visualizer.screen = avl_surface
        avl_visualizer.visualize()

        # =============================
        # Comprobar derrota
        if car.energy <= 0:
            font = pygame.font.SysFont(None, 50)
            text = font.render("🚨 Juego Terminado: ¡Perdiste!", True, (255, 0, 0))
            screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2 - text.get_height()//2))
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False
            continue

        # Comprobar victoria
        remaining_obstacles = [o for o in obstacle_manager.get_obstacles() if o["world_x"] not in obstacle_manager.consumed_world_x]
        if not remaining_obstacles:
            font = pygame.font.SysFont(None, 50)
            text = font.render("🏆 ¡Ganaste! No quedan obstáculos", True, (0, 255, 0))
            screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2 - text.get_height()//2))
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False
            continue

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main() # end main