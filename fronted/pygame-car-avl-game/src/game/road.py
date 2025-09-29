class Road:
    def __init__(self, length, speed):
        self.length = length
        self.speed = speed
        self.position = 0

    def update(self):
        self.position += self.speed
        if self.position >= self.length:
            self.position = 0

    def render(self, screen):
        # Draw the road as a rectangle
        road_rect = pygame.Rect(0, 0, screen.get_width(), screen.get_height())
        pygame.draw.rect(screen, (50, 50, 50), road_rect)

        # Draw lane markings
        lane_width = 10
        for i in range(0, screen.get_height(), 40):
            pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() // 2 - lane_width // 2, i + self.position % 40, lane_width, 20))