import pygame, sys, random
pygame.init()
W, H = 420, 600
s = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

player = pygame.Rect(80, H//2, 30, 30)
vy, g = 0.0, 0.5
pipes = []
gap = 160
spawn_cd = 0
score = 0
alive = True

def spawn_pipe():
    y = random.randint(120, H-120)
    top = pygame.Rect(W, 0, 60, y - gap//2)
    bot = pygame.Rect(W, y + gap//2, 60, H - (y + gap//2))
    return [top, bot]

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: pygame.quit(); sys.exit()
        if alive and (e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE):
            vy = -8
        if not alive and e.type == pygame.KEYDOWN:
            # 리셋
            player.y, vy, pipes, score, alive = H//2, 0, [], 0, True

    # 스폰
    if alive:
        spawn_cd -= 1
        if spawn_cd <= 0:
            pipes += spawn_pipe()
            spawn_cd = 90  # 줄이면 난이도↑

    # 물리
    if alive:
        vy += g
        player.y += int(vy)

    # 파이프 이동 & 점수
    for r in pipes:
        r.x -= 3
    # 통과 체크 (player.x == 파이프 중앙 부근)
    for i in range(0, len(pipes), 2):
        if pipes[i].x + 60 == player.x:  # 대충 통과 시점
            score += 1

    # 충돌/바닥
    if player.top <= 0 or player.bottom >= H: alive = False
    if any(player.colliderect(r) for r in pipes): alive = False

    # 화면 밖 제거
    pipes = [r for r in pipes if r.right > 0]

    # 그리기
    s.fill((30, 30, 40))
    for i, r in enumerate(pipes):
        color = (90, 200, 120) if i % 2 == 0 else (90, 200, 120)
        pygame.draw.rect(s, color, r, border_radius=6)
    pygame.draw.rect(s, (240, 120, 120), player, border_radius=6)

    font = pygame.font.SysFont(None, 36)
    s.blit(font.render(f"Score: {score}", True, (230,230,230)), (10, 10))
    if not alive:
        s.blit(font.render("Space to Restart", True, (255,180,180)), (W//2-110, H//2))

    pygame.display.flip()
    clock.tick(60)
