class Ball:
    def __init__(self, screen_width, screen_height):
        self.radius = 25
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.color = (255, 0, 0)
        self.step = 20
        self.screen_width = screen_width
        self.screen_height = screen_height

    def move(self, direction):
        if direction == "UP":
            if self.y - self.radius - self.step >= 0:
                self.y -= self.step

        elif direction == "DOWN":
            if self.y + self.radius + self.step <= self.screen_height:
                self.y += self.step

        elif direction == "LEFT":
            if self.x - self.radius - self.step >= 0:
                self.x -= self.step

        elif direction == "RIGHT":
            if self.x + self.radius + self.step <= self.screen_width:
                self.x += self.step

    def draw(self, surface):
        import pygame
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)