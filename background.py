class background():
    def __init__(self, pygame, type, x, y):
        self.type = type
        self.x = x
        self.y = y
        self.height = 24
        self.givedMensage = False
        
        if self.type == 'floor1':
            self.image = pygame.image.load("assets/background/floor1.png")
            self.width = 1088
        elif self.type == 'floor2':
            self.image = pygame.image.load("assets/background/floor2.png")
            self.width = 116
        elif self.type == 'cloud':
            pass
    def another(self, windowWidth):
        if self.x + self.width < windowWidth + 30 and self.type == 'floor1' and self.givedMensage == False:
            return True
            
    def autoDestruction(self, windowWidth):
        pass
    
    def mensageReceived(self):
        self.givedMensage = True
        
    def getWidth(self):
        return self.width
    
    def move(self, vel):
        self.x -= vel
        
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))