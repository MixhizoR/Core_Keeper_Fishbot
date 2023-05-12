# -*- coding: utf-8 -*-
import pyautogui as pag
from time import sleep
import mss

def main():
    with mss.mss() as sct:
        while True:
            # Get the RGB value of a pixel
            pixelRGB = sct.grab((932,373,994,440)).pixel(20, 20)
            # Check if the pixel color matches certain criteria
            if 195 <= pixelRGB[0] <= 205 and 200 <= pixelRGB[1] <= 210 and 215 <= pixelRGB[2] <= 230:
                # Call a function with a delay
                right_click(0.1)
                
                # Grab the screen image
                im = sct.grab((755,833,1165,880))
                
                # Get the RGB values of two pixels
                fpixel = im.pixel(300,7)
                spixel = im.pixel(30,7)
                
                # Check if the pixel colors match certain criteria
                
                if 15 <= fpixel[0] <= 25 and 55 <= fpixel[1] <= 70 and 165 <= fpixel[2] <= 180 and \
                    20 <= spixel[0] <= 30 and 128 <= spixel[1] <= 138 and 213 <= spixel[2] <= 225:
                    while True:
                        im = sct.grab((755,844,1165,845))
                        fishCatch = False
                        # Check pixel colors in a range of coordinates
                        
                        for i in range(0, 405, 2):
                            pix = im.pixel(i, 0)
                            if 210 <= pix[0] <= 245 and 140 <= pix[1] <= 175 and 30 <= pix[2] <= 90:
                                fishCatch = True
                                break
                            elif 175 <= pix[0] <= 205 and 15 <= pix[1] <= 45 and 0 <= pix[2] <= 30:
                                print("balık sinirli, bırakılacak!")
                                fishCatch = False
                                break
                        # Perform mouse actions based on the result
                        if fishCatch:
                            pag.mouseDown(button="right")
                        else:
                            pag.mouseUp(button="right")
                        
                        # Get the RGB value of a pixel
                        green_fish = im.pixel(34, 0)
                        
                        # Check if the fish color is green(it means succesfuly catched the fish)
                        if 65 <= green_fish[0] <= 70 and 158 <= green_fish[1] <= 165 and 0 <= green_fish[2] <= 30:
                            sleep(1)
                            right_click(1)
                            break
                        
                        sleep(0.05)
                else:
                    sleep(0.75)
                    right_click(1)
            
            sleep(0.3)

def right_click(x):
    # Perform a right mouse click with a delay
    pag.mouseDown(button="right")
    sleep(x)
    pag.mouseUp(button="right")
    
if __name__ == '__main__':
    main()