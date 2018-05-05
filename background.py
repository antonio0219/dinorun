class background():
    def __init__(self, pygame, type, x, y):
        self.type = type
        self.x = x
        self.y = y
        self.givedMensage = False
        
        if self.type == 'floor1':
            self.image = pygame.image.load("assets/background/floor1.png")
            self.width = 1088
            self.height = 24
        elif self.type == 'floor2':
            self.image = pygame.image.load("assets/background/floor2.png")
            self.width = 116
            self.height = 24
        elif self.type == 'cloud':
            self.image = pygame.image.load("assets/background/cloud.png")
            self.width = 75
            self.height = 21
    def another(self, windowWidth):
        if self.x + self.width < windowWidth + 30 and self.type == 'floor1' and self.givedMensage == False:
            return True
        if self.x + self.width < windowWidth - 150 and self.type == 'cloud' and self.givedMensage == False:
            return True
    def autoDestruction(self, windowWidth):
        if self.x + self.width < windowWidth - 30:
            return True
    
    def mensageReceived(self):
        self.givedMensage = True
        
    def getWidth(self):
        return self.width
    
    def getType(self):
        return self.type
    
    def move(self, vel):
        if self.type == 'cloud':
            self.x -= int(vel/4)
        else:    
            self.x -= vel
        
        
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))