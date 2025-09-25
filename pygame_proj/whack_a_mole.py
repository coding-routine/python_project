import pygame, sys, random, time
pygame.init()
W, H = 480, 480
s = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

ROWS, COLS = 3, 3
CELL = W // COLS
mole = (random.randrange(ROWS), random.randrange(COLS))
next_time = time.time() + 1.0  # 1초마다 위치 변경
score, lives = 0, 5

def cell_rect(r, c):
    return pygame.Rect(c*CELL+10, r*CELL+10, CELL-20, CELL-20)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: pygame.quit(); sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            r, c = mole
            if cell_rect(r, c).collidepoint(e.pos):
                score += 1
                next_time = time.time()  # 즉시 이동
            else:
                lives -= 1

    # 시간되면 두더지 이동
    if time.time() >= next_time:
        mole = (random.randrange(ROWS), random.randrange(COLS))
        next_time = time.time() + max(0.5, 1.0 - score*0.03)  # 점수↑ → 더 빨라짐

    s.fill((30, 35, 40))
    # 격자
    for r in range(ROWS):
        for c in range(COLS):
            pygame.draw.rect(s, (70, 70, 90), cell_rect(r, c), border_radius=12)
    # 두더지
    r, c = mole
    pygame.draw.circle(s, (240, 200, 80), cell_rect(r, c).center, CELL//4)

    # UI
    font = pygame.font.SysFont(None, 32)
    s.blit(font.render(f"Score: {score}", True, (230,230,230)), (10, 10))
    s.blit(font.render(f"Lives: {lives}", True, (230,230,230)), (W-120, 10))
    if lives <= 0:
        s.blit(font.render("Game Over! Click to restart", True, (255,150,150)), (60, H//2))
        if pygame.mouse.get_pressed()[0]:
            score, lives = 0, 5
            next_time = time.time() + 1.0
    pygame.display.flip()
    clock.tick(60)
