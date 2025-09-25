import pygame, sys
pygame.init()
W, H = 640, 360
s = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# 패들/공
paddle = pygame.Rect(20, H//2 - 40, 12, 80)
ball = pygame.Rect(W//2, H//2, 12, 12)
vx, vy = 4, 3
score = 0

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: pygame.quit(); sys.exit()
    # 입력(마우스/키보드 둘 다 허용)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:   paddle.y -= 6
    if keys[pygame.K_DOWN]: paddle.y += 6
    mx, my = pygame.mouse.get_pos()
    if pygame.mouse.get_focused():
        paddle.centery = my
    paddle.clamp_ip(s.get_rect())

    # 공 이동
    ball.x += vx; ball.y += vy
    # 벽 충돌
    if ball.top <= 0 or ball.bottom >= H: vy *= -1
    if ball.right >= W: vx *= -1
    # 패들 충돌
    if ball.colliderect(paddle) and vx < 0:
        vx *= -1
        score += 1
        # 난이도 살짝 증가
        if vx > 0: vx += 0.2
        else: vx -= 0.2

    # 실패 처리
    if ball.left <= 0:
        score = 0
        ball.center = (W//2, H//2); vx, vy = 4, 3

    # 그리기
    s.fill((20, 20, 30))
    pygame.draw.rect(s, (200, 200, 200), paddle)
    pygame.draw.ellipse(s, (240, 120, 120), ball)
    # 점수
    font = pygame.font.SysFont(None, 36)
    img = font.render(f"Score: {score}", True, (230, 230, 230))
    s.blit(img, (W-150, 10))
    pygame.display.flip()
    clock.tick(60)
