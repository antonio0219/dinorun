class dinosaur():
    def __init__(self, pygame):
        self.y = 150
        self.x = 50
        self.width = 116
        self.height = 24
        self.toJump = False
        self.jumpPower = -10
        self.velOfFalling = 0.5
        
        self.start = pygame.image.load("assets/dino/start.png")
        
    def letsJump(self):
        if self.y == 150:
            self.toJump = True
            self.jumpPower = -10
            self.velOfFalling = 0.5
            
    def jump(self):
        if self.toJump == True:
            self.y += self.jumpPower
            self.jumpPower += self.velOfFalling
        if self.y >= 150:
            self.y = 150
            self.toJump = False
        

    
    def draw(self, surface):
        surface.blit(self.start, (self.x, self.y))