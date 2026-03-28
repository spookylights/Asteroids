import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self, other):
        print(self.position)
        print(other.position)
        # print(f"self position: {self.position}, velocity: {self.velocity}")
        # print(f"other: {other.position}")
        print(f"other.position.distance_to(self.position) = {other.position.distance_to(self.position)}")
        if other.position.distance_to(self.position) < 10:
            print("collision")
            return True
        return False
