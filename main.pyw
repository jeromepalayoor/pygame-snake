import pygame
import random
import time

swidth = 900
sheight = 600

win = pygame.display.set_mode((swidth,sheight))
pygame.display.set_caption("Snake")

width = 30

class Snake():
    def __init__(self):
        self.xv = 1
        self.yv = 0
        self.body = []
        self.body.append([(swidth//width)//2,(sheight//width)//2])
        self.add = 0

    def draw(self,win):
        if self.add == 0:
            if self.body[0][0] + self.xv != swidth//width and self.body[0][0] + self.xv != -1:
                if self.body[0][1] + self.yv != sheight//width and self.body[0][1] + self.yv != -1:
                    self.body.insert(0,[self.body[0][0]+self.xv,self.body[0][1]+self.yv])
                    self.body.pop()
                elif self.yv == 1:
                    self.body.insert(0,[self.body[0][0]+self.xv,0])
                    self.body.pop()
                else:
                    self.body.insert(0,[self.body[0][0]+self.xv,sheight//width-1])
                    self.body.pop()
            elif self.xv == 1:
                self.body.insert(0,[0,self.body[0][1]+self.yv])
                self.body.pop()
            else:
                self.body.insert(0,[swidth//width-1,self.body[0][1]+self.yv])
                self.body.pop()
        elif self.add == 1:
            if self.body[0][0] + self.xv != swidth//width and self.body[0][0] + self.xv != -1:
                if self.body[0][1] + self.yv != sheight//width and self.body[0][1] + self.yv != -1:
                    self.body.insert(0,[self.body[0][0]+self.xv,self.body[0][1]+self.yv])
                elif self.yv == 1:
                    self.body.insert(0,[self.body[0][0]+self.xv,0])
                else:
                    self.body.insert(0,[self.body[0][0]+self.xv,sheight//width-1])
            elif self.xv == 1:
                self.body.insert(0,[0,self.body[0][1]+self.yv])
            else:
                self.body.insert(0,[swidth//width-1,self.body[0][1]+self.yv])
            self.add = 0

        
        show_score(len(self.body))
        for i, _ in enumerate(self.body):
            if len(self.body) != 1 and i != len(self.body)-1:
                if self.body[0] == self.body[i+1]:
                    show_score(len(self.body),True)
                    time.sleep(2)
                    self.xv = 1
                    self.yv = 0
                    self.body.clear()
                    self.body.append([(swidth//width)//2,(sheight//width)//2])

        pygame.draw.rect(win,(255,0,0),(self.body[0][0]*width,self.body[0][1]*width,width,width))
        for i, _ in enumerate(self.body):
            if len(self.body) != 1 and i != len(self.body)-1:
                pygame.draw.rect(win,(200,0,0),(self.body[i+1][0]*width,self.body[i+1][1]*width,width,width))

def show_score(score,died=False):
    if not died:
        pygame.display.set_caption(f'Snake  --  {score}')
    else:
        pygame.display.set_caption(f'Snake  --  You died with a score of : {score}')

snake = Snake()
apple = [random.randint(0,(swidth//width)-1),random.randint(0,(sheight//width)-1)]

def draw_win(win,snake):
    win.fill((255,255,255))
    pygame.draw.rect(win,(0,255,0),(apple[0]*width,apple[1]*width,width,width))
    snake.draw(win)
    pygame.display.update()

run = True
clock = pygame.time.Clock()
while run:
    clock.tick(10)
    draw_win(win,snake)
    if snake.body[0] == apple:
        apple = [random.randint(0,(swidth//width)-1),random.randint(0,(sheight//width)-1)]
        snake.add = 1
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.xv != 1:
                snake.xv = -1
                snake.yv = 0
            elif event.key == pygame.K_RIGHT and snake.xv != -1:
                snake.xv = 1
                snake.yv = 0
            elif event.key == pygame.K_UP and snake.yv != 1:
                snake.xv = 0
                snake.yv = -1
            elif event.key == pygame.K_DOWN and snake.yv != -1:
                snake.xv = 0
                snake.yv = 1
            elif event.key == pygame.K_q:
                run = False

pygame.quit()
exit()
