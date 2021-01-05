# SimpleHotkeyBrightnessControl
Python based DDC/CI Hotkey implementation for brightness control directly on Windows

# Available Mode
- Incremental and Decremental Brightness control (Ctrl + Alt + Up / Down)
- Brightness Preset (Ctrl + Alt + 0/1/2/3/4) Similar to how Lunar on MacOS does brightness preset with (⌘+ ALT + Number)

# Prerequisite
-Pynput - `pip3 install pynput`
-screen-brightness-control - `pip3 install screen-brightness-control`

# Installation
Method #1 - Windows 10 
- Windows + R > `shell:startup` > Drop it there

P.S. You can run it manually too if you don't want to install it.

# How to use (Hotkey are customizable)

- Incremental Mode

`Ctrl + Alt + Up` = Brightness Up

`Ctrl + Alt + Down` = Brightness Down


- Preset Mode

`Ctrl + Alt + 0` = 0% Brightness

`Ctrl + Alt + 1` = 25% Brightness

`Ctrl + Alt + 2` = 50% Brightness

`Ctrl + Alt + 3` = 75% Brightness

`Ctrl + Alt + 4` = 100% Brightness

# Notes

Default display is set to 0 since I only had a single monitor, however you should be able to set it to `None` to make it work for all monitor.  
