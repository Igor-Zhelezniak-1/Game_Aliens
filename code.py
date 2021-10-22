#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This is code

import ugame
import stage

import constans


def game_scene():
    # This function is the main game game_scene
    
    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    # buttons that you want to keep state information on
    a_button = constants
    
    # sets the background to image 0 in the image bank
    #   and the sie (10x8 titles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)
    
    ship = stage.Sprite(image_bank_sprites, 5, 75, constans.SCREEN_Y - (2 * constans.SPRITE_SIZE))
    
    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [ship] + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        # A button to fire
        if keys & ugame.K_X != 0:
            print("A")
        if keys & ugame.K_O != 0:
            print("B")
        if keys & ugame.K_START != 0:
            print("Start")
        if keys & ugame.K_SELECT != 0:
            print("Select")
        
        if keys & ugame.K_RIGHT != 0:
            if ship.x < (constans.SCREEN_X - constans.SPRITE_SIZE):
                ship.move((ship.x + constans.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move((constans.SCREEN_X - constans.SPRITE_SIZE), ship.y)
                           
        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move((ship.x - constans.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)
                
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass
        
        # updete game logic
        
        # redraw Sprites
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
