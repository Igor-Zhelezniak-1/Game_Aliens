#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This is code

import ugame
import stage

import constans


def menu_scene():
    # this function is the menu scene
    
    # image banks for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    # add text object
    text = []
    text1 = stage.Text(width=26, height=12, font=None, pallete=constans.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)
    
    text2 = stage.Text(width=26, height=12, font=None, pallete=constans.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)
    
    # sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_mt_background, constans.SCREEN_X,
                            constans.SCREEN_Y)
    
    # create a stage for the background to show up on 
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constans.FPS)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        # Start button selected
        if keys & ugame.K_START != 0:
            game_scene()
            
        # update game logic
        game.tick() # wait until refresh rate finishes
    

def game_scene():
    # This function is the main game game_scene
    
    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    # buttons that you want to keep state information on
    a_button = constans.button_state["button_up"]
    b_button = constans.button_state["button_up"]
    start_button = constans.button_state["button_up"]
    select_button = constans.button_state["button_up"]
    
    # ger sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    
    # sets the background to image 0 in the image bank
    #   and the sie (10x8 titles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)
    
    ship = stage.Sprite(image_bank_sprites, 5, 75, constans.SCREEN_Y - (2 * constans.SPRITE_SIZE))
    
    alien = stage.Sprite(image_bank_sprites, 9,
                    int(constans.SCREEN_X / 2 - constans.SPRITE_SIZE / 2),
                    16)
    
    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [ship] + [background]
    # render the background and initial location of sprite list
    # MT Game Studiosmost likely you will only render background once per scene
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        # A button to fire
        if keys & ugame.K_X != 0:
            if a_button == constans.button_state["button_up"]:
                a_button = constans.button_state["button_just_pressed"]
            elif a_button == constans.button_state["button_just_pressed"]:
                a_button = constans.button_state["button_still_pressed"]
        else:
            if a_button == constans.button_state["button_still_pressed"]:
                a_button = constans.button_state["button_released"]
            else:
                a_button = constans.button_state["button_up"]
        # B button
        if keys & ugame.K_O != 0:
            pass
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
        # play sound of A was button_just_presed
        if a_button == constans.button_state["button_just_presed"]:
            sound.play(pew_sound)
        
        # redraw Sprites
        game.render_sprites([ship] + [alien])
        game.tick()


if __name__ == "__main__":
    game_scene()
