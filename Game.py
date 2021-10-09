import Characters
import pygame
import yaml


with open('Configuration.yaml', 'r') as yamlConfig:
    config = yaml.load(yamlConfig, Loader=yaml.FullLoader)

k_adapter = config['window_config']['window_images_adapter']
k_black = config['colors']['black']
k_blue = config['colors']['blue']
k_column = config['window_config']['column_number']
k_fps = config['FPS']
k_height = config['window_config']['height']
k_movement = config['movement']
k_row = config['window_config']['row_number']
k_width = config['window_config']['width']

k_sources = config['src']

with open(k_sources['map'], 'r') as maze_file:
    k_maze = maze_file.readlines()


def game_state_draw(maze, player, size_x, size_y, window):
    y = 0

    for row in maze:
        x = 0
        for item in row:
            if item == '0':
                pygame.draw.rect(window, (k_black['red'], k_black['green'], k_black['blue']), pygame.Rect(x, y, size_x,
                                                                                                          size_y))
            if item == '1':
                pygame.draw.rect(window, (k_blue['red'], k_blue['green'], k_blue['blue']), pygame.Rect(x, y, size_x,
                                                                                                       size_y))
            x += size_x
        y += size_y

    window.blit(pygame.transform.scale(pygame.image.load(player.get_image()), (player.get_size_x(), player.get_size_y())
                                       ), (player.get_x(), player.get_y()))

    pygame.display.update()


def __main__():
    run = True

    size_x = (k_width//k_row)
    size_y = (k_height//k_column)

    character_x = (k_width//2) - (2 * size_x)
    character_y = 0
    while character_y < k_height/2:
        character_y += size_y

    pygame.init()
    pygame.Surface((k_width - (k_width - size_x * k_row), k_height - (k_height - size_y * k_column)))
    window = pygame.display.set_mode((k_width - (k_width - size_x * k_row), k_height - (k_height - size_y * k_column)))
    pygame.display.set_caption('PUC-MAN')

    k_clock = pygame.time.Clock()

    player = Characters.Player(k_sources['images']['player']['left'], character_x, character_y, (size_x * k_adapter),
                               (size_y * k_adapter), k_maze, k_movement, k_row, k_column, k_adapter)
    player.start()

    while run:
        k_clock.tick(k_fps)

        game_state_draw(k_maze, player, size_x, size_y, window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                player.set_run(False)

            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_DOWN]:
                player.set_direction(player.get_down())
                player.set_image(k_sources['images']['player']['down'])
            if key_pressed[pygame.K_LEFT]:
                player.set_direction(player.get_left())
                player.set_image(k_sources['images']['player']['left'])
            if key_pressed[pygame.K_RIGHT]:
                player.set_direction(player.get_right())
                player.set_image(k_sources['images']['player']['right'])
            if key_pressed[pygame.K_UP]:
                player.set_direction(player.get_up())
                player.set_image(k_sources['images']['player']['up'])

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    __main__()
