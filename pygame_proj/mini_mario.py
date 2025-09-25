import pygame, sys
pygame.init()
W, H = 720, 400
s = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# 플레이어
player = pygame.Rect(80, 280, 28, 28)
vx, vy = 0, 0
SPEED, GRAV, JUMP = 4, 0.5, -10
on_ground = False

# 월드(플랫폼들) & 골지점
platforms = [
    pygame.Rect(0, 360, 900, 40),
    pygame.Rect(160, 300, 120, 16),
    pygame.Rect(320, 250, 120, 16),
    pygame.Rect(500, 210, 120, 16),
    pygame.Rect(640, 170, 120, 16),
]
goal = pygame.Rect(760, 130, 24, 40)

def reset():
    global vx, vy, on_ground
    player.x, player.y = 80, 280
    vx, vy = 0, 0
    on_ground = False

reset()

while True:
    # 이벤트
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
            reset()

    # 입력
    keys = pygame.key.get_pressed()
    vx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * SPEED
    if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and on_ground:
        vy = JUMP
        on_ground = False

    # 물리
    vy += GRAV
    # ---- X 이동 & 충돌
    player.x += int(vx)
    for p in platforms:
        if player.colliderect(p):
            if vx > 0:
                player.right = p.left
            elif vx < 0:
                player.left = p.right
    # ---- Y 이동 & 충돌
    player.y += int(vy)
    on_ground = False
    for p in platforms:
        if player.colliderect(p):
            if vy > 0:
                player.bottom = p.top; vy = 0; on_ground = True
            elif vy < 0:
                player.top = p.bottom; vy = 0

    # 카메라(월드 오프셋)
    cam_x = -(player.centerx - W//2)

    # 그리기
    s.fill((30, 35, 45))
    # 플랫폼
    for p in platforms:
        pygame.draw.rect(s, (90, 160, 220), p.move(cam_x, 0), border_radius=4)
    # goal flag
    pygame.draw.rect(s, (250, 220, 90), goal.move(cam_x, 0))
    pygame.draw.polygon(s, (240, 120, 120), [
        (goal.x+goal.w+cam_x, goal.y+5),
        (goal.x+goal.w+cam_x+18, goal.y+15),
        (goal.x+goal.w+cam_x, goal.y+25)
    ])
    # 플레이어
    pygame.draw.rect(s, (240, 120, 120), player.move(cam_x, 0), border_radius=4)

    # 승리
    font = pygame.font.SysFont(None, 28)
    if player.colliderect(goal):
        s.blit(font.render("YOU WIN! Press R to restart", True, (255,230,230)),
               (W//2-140, 30))

    pygame.display.flip()
    clock.tick(60)
