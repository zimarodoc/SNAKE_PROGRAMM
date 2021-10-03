import pygame
import sys
import random
pygame.init()

SIZE_BLOCK = 20
FRAME_COLOR = (0, 255, 204)
WHITE = (255,255,255)
MAGENTA = (200,255,255)
HEADER_COLOR = (250,254,153)
RED = (200,0,0)
COUNT_BLOCKS = 20
MARGIN = 1
SNAKE_COLOR = (150,150,115)
HEADER_MARGIN = 80
size = [SIZE_BLOCK*COUNT_BLOCKS + 2* SIZE_BLOCK + MARGIN*COUNT_BLOCKS,
        SIZE_BLOCK*COUNT_BLOCKS + 2* SIZE_BLOCK + MARGIN*COUNT_BLOCKS + HEADER_MARGIN]


screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')
timer = pygame.time. Clock()
calibri = pygame.font.SysFont('calibri', 36)

class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def is_inside(self):
        return 0<= self.x<COUNT_BLOCKS and self.y<COUNT_BLOCKS

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y ==other.y

def get_random_empty_block():
    x = random.randint(0, COUNT_BLOCKS-1)
    y = random.randint(0, COUNT_BLOCKS - 1)
    empty_block = SnakeBlock(x,y)
    while empty_block in snake_blocks:
        empty_block.x = random.randint(0, COUNT_BLOCKS-1)
        empty_block.y = random.randint(0, COUNT_BLOCKS - 1)
    return empty_block

def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1), SIZE_BLOCK,
                                     SIZE_BLOCK])

snake_blocks = [SnakeBlock(9,8), SnakeBlock(9,9), SnakeBlock(9,10)]
apple = get_random_empty_block()

d_row = 0
d_col = 1
total = 0
speed = 1

while True:

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              print('exit')
              pygame.quit()
              sys.exit()

          elif event.type == pygame.KEYDOWN:
              if event.key == pygame. K_UP and d_col !=0:
                  d_row = -1
                  d_col = 0

              elif event.key == pygame. K_DOWN and d_col !=0:
                  d_row = 1
                  d_col = 0

              elif event.key == pygame.K_RIGHT and d_row !=0:
                  d_row = 0
                  d_col = 1

              elif event.key == pygame.K_LEFT and d_row !=0:
                  d_row = 0
                  d_col = -1

      screen.fill(FRAME_COLOR)
      pygame.draw.rect(screen, HEADER_COLOR, [0,0, size[0], HEADER_MARGIN])

      text_total = calibri.render(f"Total:{total}", 0, RED)
      text_speed = calibri.render(f"Speed:{speed}", 0, RED)
      screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
      screen.blit(text_speed, (SIZE_BLOCK+240, SIZE_BLOCK))

      for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = MAGENTA
            else:
                color = WHITE

            draw_block(color, row, column)

      head = snake_blocks[-1]
      if not head. is_inside():
          print('crash')
          pygame.quit()
          sys.exit()

      draw_block(RED, apple.x, apple.y)

      for block in snake_blocks:

          draw_block(SNAKE_COLOR, block.x, block.y)


      if apple == head:
          total+=1
          speed+= total//5+1
          snake_blocks.append(apple)
          apple = get_random_empty_block()

      head = snake_blocks[-1]
      new_head = SnakeBlock(head.x + d_row, head.y + d_col)
      snake_blocks.append(new_head)
      snake_blocks.pop(0)

      pygame.display.flip()
      timer.tick(2+speed)
