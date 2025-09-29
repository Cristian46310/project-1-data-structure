import pygame
import os

class Car:
    def __init__(self, assets_path, x, y, width, height, speed=0):
        self.image = pygame.image.load(os.path.join(assets_path, "car.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))

        self.speed = speed
        self.is_jumping = False
        self.jump_height = 0
        self.in_air = False
        self.energy = 100

        # Invulnerabilidad tras un impacto (ms)
        self.invulnerable_until = 0
        self.invulnerability_ms = 600

        # Cargar sonido de salto
        jump_sound_path = os.path.join(assets_path, "jump.mp3")
        if os.path.exists(jump_sound_path):
            self.jump_sound = pygame.mixer.Sound(jump_sound_path)
        else:
            self.jump_sound = None
            print("⚠️ No se encontró jump.wav en assets_path")

    def update(self):
        self.rect.x += self.speed
        if self.is_jumping:
            self.jump()

    def jump(self):
        MAX_JUMP_HEIGHT = 50
        JUMP_SPEED = 1

        if self.jump_height < MAX_JUMP_HEIGHT:
            self.rect.y -= JUMP_SPEED
            self.jump_height += 1
            self.in_air = True
        elif self.jump_height < MAX_JUMP_HEIGHT * 2:
            self.rect.y += JUMP_SPEED
            self.jump_height += 1
            self.in_air = True
        else:
            self.is_jumping = False
            self.jump_height = 0
            self.in_air = False

    def render(self, screen, show_hitbox=True):
        screen.blit(self.image, self.rect)

    def start_jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            # Reproducir sonido de salto
            if self.jump_sound:
                self.jump_sound.play()

    def reset_position(self, x=0, y=300):
        self.rect.x = x
        self.rect.y = y

    def consume_energy(self, amount):
        self.energy -= amount
        if self.energy < 0:
            self.energy = 0

    def recharge_energy(self, amount):
        self.energy += amount
        if self.energy > 100:
            self.energy = 100

    def get_rect(self):
        return self.rect

    def hit(self, damage):
        if self.in_air:
            return False
        now = pygame.time.get_ticks()
        if now < self.invulnerable_until:
            return False
        self.consume_energy(damage)
        self.invulnerable_until = now + self.invulnerability_ms
        return True
