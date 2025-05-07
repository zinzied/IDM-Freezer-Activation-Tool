# IDM Freezer & Activation Tool v2.0
An enhanced open-source tool to activate, freeze trial, and manage Internet Download Manager

![image](https://github.com/user-attachments/assets/f1762de2-7f15-4a75-a00a-1386c2bba01b)

## What's New in Version 2.0
- Improved Python GUI with colorful interface
- Added IDM status checking feature
- Added backup/restore functionality for IDM settings
- Integrated IAS.ps1 and IAS.CMD for better activation
- Added automatic update checking
- Enhanced error handling and user feedback
- Progress indicators for operations

## Features
- IDM freeze trial and activation with registry key lock method
- Activation and trial persist even after installing IDM updates
- IDM trial reset
- IDM status checking
- Backup and restore IDM settings
- Automatic update checking
- Fully open source
- Based on transparent batch and Python scripts

## Usage
Run the `IDM Freezer.py` script to access the enhanced GUI, or use `zied.cmd` directly with the following parameters:

- `/act` - Activate IDM
- `/frz` - Freeze IDM trial
- `/res` - Reset IDM activation/trial
- `/sts` - Check IDM status
- `/upd` - Check for updates

## Methods

### Freeze Trial
IDM provides a 30-day trial period. This option locks the trial period for lifetime so you won't have to reset the trial again and your trial won't expire.
This method requires internet access at the time of applying this option.
IDM updates can be installed directly without having to freeze it again.

### Activation
Uses the latest activation method to register IDM with a valid serial key.

### Reset IDM Activation / Trial
Resets the IDM activation or trial period. This option can also be used to restore status if IDM reports a fake serial key or other similar errors.

### Check IDM Status
Checks the current status of your IDM installation (activated, in trial, or expired).

### Backup/Restore IDM Settings
Allows you to backup your current IDM settings and restore them later if needed.

## Requirements
- Windows 7/8/8.1/10/11
- PowerShell
- Python 3.x (for GUI)
- Colorama Python package (for GUI)

## Disclaimer
I would like to make it clear that I am not the original creator of this script. 
When I first uploaded this script to GitHub, the main author had not yet established an official GitHub repository. 
Consequently, users had to go to the official forum to download and use the script until the GitHub repository was eventually created.
My primary goal in setting up this repository was to simplify the process for users. Additionally, 
I made sure to acknowledge the original creators of the script to show respect for their work.
