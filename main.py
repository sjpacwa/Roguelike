import libtcodpy as libtcod

# actual size of the window
SCREEN_WIDTH = 100
SCREEN_HEIGHT = 50


def handle_keys():
    global playerx, playery

    key = libtcod.console_wait_for_keypress(True)

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

    elif key.vk == libtcod.KEY_ESCAPE:
        return True  # exit game

    # movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP) and playery != 1:
        playery -= 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN) and playery != SCREEN_HEIGHT - 22:
        playery += 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT) and playerx != 1:
        playerx -= 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT) and playerx != SCREEN_WIDTH - 22:
        playerx += 1


#############################################
# Initialization & Main Loop
#############################################

libtcod.console_set_custom_font('lucida12x12_gs_tc.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Roguelike', False)

playerx = SCREEN_WIDTH // 2
playery = SCREEN_HEIGHT // 2

floaterX = 10
floaterY = 10

while not libtcod.console_is_window_closed():
    floaterX -= 1
    floaterY -= 1
    libtcod.console_print_frame(0, 0, 0, SCREEN_WIDTH - 20, SCREEN_HEIGHT, True, fmt="Local")
    libtcod.console_print_frame(0, SCREEN_WIDTH - 20, 0, 20, 20, True, fmt="Global")
    libtcod.console_print_frame(0, SCREEN_WIDTH - 20, 20, 20, SCREEN_HEIGHT - 20, True, fmt="Actions")
    libtcod.console_set_default_foreground(0, libtcod.white)
    libtcod.console_put_char(0, playerx, playery, '@', libtcod.BKGND_NONE)
    libtcod.console_put_char(0, floaterX, floaterY, 'D', libtcod.BKGND_NONE)


    libtcod.console_flush()

    #libtcod.console_put_char(0, floaterX, floaterY, ' ', libtcod.BKGND_NONE)
    #libtcod.console_put_char(0, playerx, playery, ' ', libtcod.BKGND_NONE)

    # handle keys and exit game if needed
    exit = handle_keys()
    if exit:
        break