import screen_brightness_control as sbc
from pynput import keyboard

# displayNumber = None for all monitor
displayNumber = 0

# pynput key documentation
# https://pynput.readthedocs.io/en/latest/keyboard.html

incrementValue = 25

increaseHotkey = '<ctrl>+<alt>+<up>'
decreaseHotkey = '<ctrl>+<alt>+<down>'

# Presets
brightness0Hotkey = '<ctrl>+<alt>+0'
brightness1Hotkey = '<ctrl>+<alt>+1'
brightness2Hotkey = '<ctrl>+<alt>+2'
brightness3Hotkey = '<ctrl>+<alt>+3'
brightness4Hotkey = '<ctrl>+<alt>+4'

#Exit condition
exitHotkey = '<ctrl>+<alt>+q'

def increase():
    sbc.set_brightness('+' + str(incrementValue), display=displayNumber)

def decrease():
    sbc.set_brightness('-' + str(incrementValue), display=displayNumber)

def brightness0():
    sbc.set_brightness(0, display=displayNumber)

def brightness1():
    sbc.set_brightness(25, display=displayNumber)

def brightness2():
    sbc.set_brightness(50, display=displayNumber)

def brightness3():
    sbc.set_brightness(75, display=displayNumber)

def brightness4():
    sbc.set_brightness(100, display=displayNumber)

def exitCond():
    exit();

with keyboard.GlobalHotKeys({
    increaseHotkey: increase,
    decreaseHotkey: decrease,
    brightness0Hotkey: brightness0,
    brightness1Hotkey: brightness1,
    brightness2Hotkey: brightness2,
    brightness3Hotkey: brightness3,
    brightness4Hotkey: brightness4,
    exitHotkey : exitCond
}) as h:
    h.join()
