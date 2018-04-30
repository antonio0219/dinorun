class background():
    def __init__(self, pygame, type, x, y):
        self.type = type
        self.x = x
        self.y = y
        self.width = 116
        self.height = 24
        
        if self.type == 'floor1':
            self.image = pygame.image.load("assets/background/floor1.png")
        elif self.type == 'floor2':
            self.image = pygame.image.load("assets/background/floor2.png")
        elif self.type == 'cloud':
            pass
    def getWidth(self):
        return self.width
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))