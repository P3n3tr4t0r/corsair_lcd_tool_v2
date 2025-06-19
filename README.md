# Important!
This is a fork of [corsair_lcd_tool](https://github.com/UDPSendToFailed/corsair_lcd_tool "corsair_lcd_tool") by [UDPSendToFailed](https://github.com/UDPSendToFailed "UDPSendToFailed") only tested on Linux. I deleted the openRGB stuff to just control the display.

# Features
- Display any image or GIF without size or length limits on the LCD screen of a compatible Corsair AIO.
- Saving and loading of the last image position, size, etc.
- Low resources usage compared to iCUE.

# Planned Features
- .rpm installer
- Overlay text
- Implement temperatures

# Usage
- Install [Python](https://www.python.org/downloads/ "Python") 3.6 or newer.
- Clone the repo or download as ZIP and extract it to a new folder.
- Install the required modules using `pip install -r requirements.txt`.
- If you are running on Linux run the install.sh to update your udev rules
- Run the script.

# Tested devices
- Corsair iCUE H170i ELITE LCD (non-XT), 0x1b1c / 0x0c39 (from Fork)
- Corsair iCUE ELITE CPU Cooler LCD Display Upgrade Kit, 0x1b1c / 0x0c39

# FAQ
This was only tested on Linux.
It might work on Windows but to get sure use the original [corsair_lcd_tool by UDPSendToFailed](https://github.com/UDPSendToFailed/corsair_lcd_tool "corsair_lcd_tool by UDPSendToFailed")

# WHY
Because Corsair decided to do nothing for Linux users.
If I have some time I might also integrate RGB Controllers in another repo!

# Thanks to
- [UDPSendToFailed](https://github.com/UDPSendToFailed "UDPSendToFailed") for the work. The main functionality is all in [corsair_lcd_tool](https://github.com/UDPSendToFailed/corsair_lcd_tool "corsair_lcd_tool")
- [browserdotsys](https://github.com/browserdotsys "browserdotsys") for [the gist](https://gist.github.com/browserdotsys/ef1b22c60c31d9c61e18cca30b3ce903 "the gist") that's used as a base of this script to communicate with the AIO.


# Any questions?
Feel free to contact me on Discord: @shutdown4life

