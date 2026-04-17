import pygame
import sys
from player import MusicPlayer

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Mickey Music Player")
    fps = pygame.time.Clock()

    # Шрифты
    font_big = pygame.font.SysFont("Arial", 32, bold=True)
    font_mid = pygame.font.SysFont("Arial", 24)
    font_small = pygame.font.SysFont("Arial", 18)

    player = MusicPlayer()

    # Цвета
    BG = (30, 30, 30)
    WHITE = (255, 255, 255)
    YELLOW = (255, 220, 50)
    GREEN = (50, 220, 100)
    RED = (220, 50, 50)
    GRAY = (150, 150, 150)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    player.play()
                elif event.key == pygame.K_s:
                    player.stop()
                elif event.key == pygame.K_n:
                    player.next_track()
                elif event.key == pygame.K_b:
                    player.prev_track()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        screen.fill(BG)

        # Заголовок
        title = font_big.render("🎵 Music Player", True, YELLOW)
        screen.blit(title, (600 // 2 - title.get_width() // 2, 40))

        # Название трека
        track_name = player.get_track_name()
        track_surf = font_mid.render(f"Track: {track_name}", True, WHITE)
        screen.blit(track_surf, (600 // 2 - track_surf.get_width() // 2, 120))

        # Номер трека
        if player.playlist:
            num = font_small.render(
                f"{player.current_index + 1} / {len(player.playlist)}",
                True, GRAY
            )
            screen.blit(num, (600 // 2 - num.get_width() // 2, 160))

        # Статус
        status_color = GREEN if player.is_playing else RED
        status = font_mid.render(player.get_status(), True, status_color)
        screen.blit(status, (600 // 2 - status.get_width() // 2, 210))

        # Позиция (секунды)
        pos = player.get_position()
        minutes = pos // 60
        seconds = pos % 60
        pos_surf = font_mid.render(f"Time: {minutes:02d}:{seconds:02d}", True, WHITE)
        screen.blit(pos_surf, (600 // 2 - pos_surf.get_width() // 2, 255))

        # Управление
        controls = [
            "P = Play    S = Stop",
            "N = Next    B = Previous",
            "Q = Quit"
        ]
        for i, text in enumerate(controls):
            ctrl = font_small.render(text, True, GRAY)
            screen.blit(ctrl, (600 // 2 - ctrl.get_width() // 2, 310 + i * 25))

        pygame.display.flip()
        fps.tick(30)

if __name__ == "__main__":
    main()