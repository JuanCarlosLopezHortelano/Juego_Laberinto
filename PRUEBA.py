import pygame

# Definir las dimensiones de la pantalla
WIDTH, HEIGHT = 640, 480

# Inicializar Pygame
pygame.init()

# Crear la ventana del juego
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Definir los colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definir la fuente para el texto
font = pygame.font.Font(None, 36)

# Definir la función para mostrar el menú principal
def show_menu():
    while True:
        # Dibujar el fondo de pantalla y el título del menú
        screen.fill(BLACK)
        title_text = font.render("Menú Principal", True, WHITE)
        title_rect = title_text.get_rect(center=(WIDTH/2, 50))
        screen.blit(title_text, title_rect)

        # Dibujar las opciones del menú
        option1_text = font.render("Jugar", True, WHITE)
        option1_rect = option1_text.get_rect(center=(WIDTH/2, 150))
        screen.blit(option1_text, option1_rect)

        option2_text = font.render("Salir", True, WHITE)
        option2_rect = option2_text.get_rect(center=(WIDTH/2, 250))
        screen.blit(option2_text, option2_rect)

        # Actualizar la pantalla
        pygame.display.flip()

        # Esperar a que el usuario seleccione una opción
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if option1_rect.collidepoint(mouse_pos):
                    # El usuario ha seleccionado "Jugar"
                    # Cambiar a la pantalla del laberinto
                    show_labyrinth_menu()
                    return
                elif option2_rect.collidepoint(mouse_pos):
                    # El usuario ha seleccionado "Salir"
                    pygame.quit()
                    exit()

# Definir la función para mostrar el menú de selección de laberinto
import pygame
import time


def loading_animation(screen):
    clock = pygame.time.Clock()
    sprite_sheet = pygame.image.load("run_animation.png").convert_alpha()
    sprite_width = 64
    sprite_height = 64
    x_pos = 0
    y_pos = 0
    total_frames = 8
    current_frame = 0
    frame_duration = 80  # milliseconds
    start_time = time.time()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Calculate which frame to show
        time_since_start = int((time.time() - start_time) * 1000)
        current_frame = (time_since_start // frame_duration) % total_frames

        # Clear the screen and draw the current frame
        screen.fill((255, 255, 255))
        sprite_rect = pygame.Rect(current_frame * sprite_width, 0, sprite_width, sprite_height)
        screen.blit(sprite_sheet, (x_pos, y_pos), sprite_rect)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

        # Check if it's been 5 seconds and exit the loop
        if time.time() - start_time > 5:
            running = False


def show_labyrinth_menu():
    while True:
        # Dibujar el fondo de pantalla y el título del menú
        screen.fill(BLACK)
        title_text = font.render("ELIGE LA PARTIDA", True, WHITE)
        title_rect = title_text.get_rect(center=(WIDTH/2, 50))
        screen.blit(title_text, title_rect)

        # Dibujar las opciones del menú
        option1_text = font.render("Laberinto_Juego Con 2 habitaciones", True, WHITE)
        option1_rect = option1_text.get_rect(center=(WIDTH/2, 150))
        screen.blit(option1_text, option1_rect)

        option2_text = font.render("Laberinto_Juego Con 4 habitaciones", True, WHITE)
        option2_rect = option2_text.get_rect(center=(WIDTH/2, 250))
        screen.blit(option2_text, option2_rect)

        # Actualizar la pantalla
        pygame.display.flip()

        # Esperar a que el usuario seleccione una opción
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if option1_rect.collidepoint(mouse_pos):

                    return
                elif option2_rect.collidepoint(mouse_pos):
                    # El usuario ha seleccionado "Salir"
                    pygame.quit()
                    exit()

# Mostrar el menú principal
show_menu()

# Salir del juego
pygame.quit()


if __name__ == '__main__':
    pass


