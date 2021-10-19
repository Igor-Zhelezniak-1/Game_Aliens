#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This is code

import ugame
import stage


def game_scene():
    # This function is the main game game_scene
    
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    background = stage.Grid(image_bank_background, 10, 8)
    game = stage.Stage(ugame.display, 60)
    game.layers = [ship] + [background]
    game.render_block()
    
    # repeat forever, game loop
    while True:
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()
