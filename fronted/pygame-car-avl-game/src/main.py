import pygame
from game.config import Config
from game.road import Road
from game.car import Car
from game.obstacle import Obstacle
from game.avl_tree import AVLTree
from game.avl_visualizer import AVLVisualizer

def main():
    pygame.init()
    
    # Load configuration
    config = Config()
    screen_width = config.screen_width
    screen_height = config.screen_height
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Car Game with AVL Tree Obstacles")

    # Initialize game elements
    road = Road(config.road_length)
    car = Car(config.car_start_position, config.car_speed)
    obstacles = AVLTree()
    obstacles.load_obstacles(config.obstacles)
    avl_visualizer = AVLVisualizer(obstacles)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game elements
        road.update()
        car.update()

        # Render everything
        screen.fill((255, 255, 255))  # Clear screen with white
        road.render(screen)
        car.render(screen)
        avl_visualizer.render(screen)

        pygame.display.flip()
        clock.tick(config.refresh_rate)

    pygame.quit()

if __name__ == "__main__":
    main()