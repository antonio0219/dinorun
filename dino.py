class dinosaur():
    def __init__(self, pygame):
        self.y = 155
        self.x = 50
        self.width = 59
        self.height = 63
        self.toJump = False
        self.jumpPower = -10
        self.velOfFalling = 0.5
        self.runningState = 1
        self.runningTime = 0
        self.dodging = False
        
        self.start = pygame.image.load("assets/dino/start.png")
        self.running1 = pygame.image.load("assets/dino/running1.png")
        self.running2 = pygame.image.load("assets/dino/running2.png")
        self.dodging1 = pygame.image.load("assets/dino/dodging1.png")
        self.dodging2 = pygame.image.load("assets/dino/dodging2.png")
        
    def letsJump(self):
        if self.y == 155:
            self.toJump = True
            self.jumpPower = -10
            self.velOfFalling = 0.5
        
    def letsDodge(self, can):
        if can == 'True' and self.y >= 155 and self.dodging == False:
            self.dodging = True
            self.width = 80
            self.height = 38
            if self.runningState < 3:
                self.runningState = 4
            self.y = 180
        else:
            self.dodging = False
            self.width = 59
            self.height = 63
            if self.runningState >= 3:
                self.runningState = 1
            self.y = 155
            
        
        
            
    def jump(self):
        if self.toJump == True and self.dodging == False:
            self.y += self.jumpPower
            self.jumpPower += self.velOfFalling
        if self.y >= 155 and self.dodging == False:
            self.toJump = False
        
    
    def draw(self, surface, gameState, GAME_TIME):
        if self.toJump == True or gameState == 0:
            surface.blit(self.start, (self.x, self.y))
        if self.toJump == False and gameState > 0:
            if self.runningTime == 0:
                self.runningTime = GAME_TIME.get_ticks()
            if GAME_TIME.get_ticks() - self.runningTime > 150:
                self.runningTime = 0
                if self.dodging == False:
                    if self.runningState == 1:
                        self.runningState = 2
                    if self.runningState == 2:
                        self.runningState = 1
                if self.dodging:
                    if self.runningState == 3:
                        self.runningState = 4
                    if self.runningState == 4:
                        self.runningState = 3
                    
            if self.runningState == 1:
                surface.blit(self.running1, (self.x, self.y))
            if self.runningState == 2:
                surface.blit(self.running2, (self.x, self.y))
            if self.runningState == 3:
                surface.blit(self.dodging1, (self.x, self.y))
            if self.runningState == 4:
                surface.blit(self.dodging2, (self.x, self.y))
                
        