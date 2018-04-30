class background():
    def __init__(self, pygame, type, x, y):
        self.type = type
        self.x = x
        self.y = y
        self.width = 116
        self.height = 24
        
        self.start = pygame.image.load("assets/dino/start.png")
        
        
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))