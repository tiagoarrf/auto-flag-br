import pyautogui
import sys
from time import sleep

for _ in range(2):

    #select pencil
    pyautogui.mouseUp(button='left')
    pyautogui.moveTo(309,69, duration=0.1)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseDown(button='left')
    sleep(0.1)
    pyautogui.mouseUp(button='left')

    #move to select black color pencil
    pyautogui.moveTo(876,63, duration=0.1)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')

    #initial position
    pyautogui.moveTo(94,411, duration=0.1)
    pyautogui.mouseDown(button='left')

    #retangle
    pyautogui.moveTo(105,216, duration=0.1)
    pyautogui.moveTo(211,215, duration=0.1)
    pyautogui.moveTo(240,223, duration=0.1)
    pyautogui.moveTo(259,226, duration=0.1)
    pyautogui.moveTo(301,227, duration=0.1)
    pyautogui.moveTo(346,225, duration=0.1)
    pyautogui.moveTo(404,220, duration=0.1)
    pyautogui.moveTo(432,215, duration=0.1)
    pyautogui.moveTo(425,268, duration=0.1)
    pyautogui.moveTo(421,346, duration=0.1)
    pyautogui.moveTo(421,414, duration=0.1)
    pyautogui.moveTo(391,417, duration=0.1)
    pyautogui.moveTo(344,417, duration=0.1)
    pyautogui.moveTo(310,423, duration=0.1)
    pyautogui.moveTo(260,423, duration=0.1)
    pyautogui.moveTo(239,416, duration=0.1)
    pyautogui.moveTo(212,413, duration=0.1)
    pyautogui.moveTo(180,410, duration=0.1)
    pyautogui.moveTo(155,410, duration=0.1)
    pyautogui.moveTo(124,413, duration=0.1)
    pyautogui.moveTo(95,423, duration=0.1)
    pyautogui.moveTo(94,404, duration=0.1)

    #initial losangle
    pyautogui.mouseUp(button='left')
    pyautogui.moveTo(161,310, duration=0.1)
    pyautogui.mouseDown(button='left')

    #losangle
    pyautogui.moveTo(258,256, duration=0.1)
    pyautogui.moveTo(364,310, duration=0.1)
    pyautogui.moveTo(251,371, duration=0.1)
    pyautogui.moveTo(161,310, duration=0.1)

    #initial circle
    pyautogui.mouseUp(button='left')
    pyautogui.moveTo(231,310, duration=0.1)
    pyautogui.mouseDown(button='left')

    #circle
    pyautogui.moveTo(233,300, duration=0.1)
    pyautogui.moveTo(238,292, duration=0.1)
    pyautogui.moveTo(247,287, duration=0.1)
    pyautogui.moveTo(257,284, duration=0.1)
    pyautogui.moveTo(268,285, duration=0.1)
    pyautogui.moveTo(275,287, duration=0.1)
    pyautogui.moveTo(285,294, duration=0.1)
    pyautogui.moveTo(288,303, duration=0.1)
    pyautogui.moveTo(288,313, duration=0.1)
    pyautogui.moveTo(285,324, duration=0.1)
    pyautogui.moveTo(276,333, duration=0.1)
    pyautogui.moveTo(262,336, duration=0.1)
    pyautogui.moveTo(247,334, duration=0.1)
    pyautogui.moveTo(236,326, duration=0.1)
    pyautogui.moveTo(231,317, duration=0.1)
    pyautogui.moveTo(231,307, duration=0.1)

    #border text track 1
    pyautogui.moveTo(233,299, duration=0.1)
    pyautogui.moveTo(253,304, duration=0.1)
    pyautogui.moveTo(261,306, duration=0.1)
    pyautogui.moveTo(268,310, duration=0.1)
    pyautogui.moveTo(275,315, duration=0.1)
    pyautogui.moveTo(284,323, duration=0.1)

    #initial position border text track 2
    pyautogui.mouseUp(button='left')
    pyautogui.moveTo(288,313, duration=0.1)
    pyautogui.mouseDown(button='left')

    #border text track 2
    pyautogui.moveTo(282,308, duration=0.1)
    pyautogui.moveTo(272,303, duration=0.1)
    pyautogui.moveTo(268,301, duration=0.1)
    pyautogui.moveTo(258,296, duration=0.1)
    pyautogui.moveTo(249,293, duration=0.1)
    pyautogui.moveTo(240,292, duration=0.1)
    pyautogui.mouseUp(button='left')
    
    #green color
    pyautogui.moveTo(1005,62, duration=0.1)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')

    #move to paint bucket
    pyautogui.moveTo(334,69, duration=0.1)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')

    #move to retangle
    pyautogui.moveTo(194,371, duration=0.1)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')

    #yelow color
    pyautogui.moveTo(984,61, duration=0.1)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')

    #move losangle
    pyautogui.moveTo(232,345, duration=0.1)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')

    #blue color
    pyautogui.moveTo(1052,61, duration=0.1)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')

    #move circle 1
    pyautogui.moveTo(252,317, duration=0.1)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')

    #move circle 2
    pyautogui.moveTo(271,289, duration=0.1)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')

    #move undo 8x
    pyautogui.moveTo(65,12, duration=0.1)
    #sys.exit()

    for _ in range(8):
        pyautogui.mouseDown(button='left')
        sleep(0.1)
        pyautogui.mouseUp(button='left')
    

    #sys.exit()








