# IDM Freezer & Activation Tool v3.0
An enhanced open-source tool to activate, freeze trial, and manage Internet Download Manager

![Capture](https://github.com/user-attachments/assets/fdaf3422-b3c5-4b72-82d8-6ab18ae7abfe)


## What's New in Version 3.0
- **🔧 Fixed Critical Bugs**: Resolved PowerShell download errors and French locale issues
- **🌐 Enhanced Network Handling**: Robust connectivity checks and retry mechanisms
- **🛡️ Admin Privilege Detection**: Automatic detection and elevation requests
- **📝 Advanced Logging System**: Detailed operation tracking with log viewer
- **⚙️ Configuration Management**: Save preferences with config file
- **💾 Smart Backup System**: Auto-backup with detailed backup history
- **🎨 Improved UI**: Better visual feedback with icons and colors
- **🔍 Enhanced Status Checks**: More detailed IDM installation information
- **📊 Settings Menu**: Customize logging, auto-backup, and update checks
- **🌍 Better Locale Support**: Works correctly with non-English Windows systems
- **⚡ Performance Improvements**: Faster operations and better error handling

## Features
- **Fully Self-Contained** - No external dependencies or downloads required
- IDM freeze trial and activation with registry key lock method
- Activation and trial persist even after installing IDM updates
- IDM trial reset
- IDM status checking with detailed information
- Advanced backup and restore with history
- Automatic update checking
- Comprehensive logging system
- Configuration management
- Settings menu for customization
- Fully open source
- Based on transparent batch and Python scripts
- Works offline for activation and freeze operations

## Usage

### Running the Application

**Python Interface (Recommended)**
```bash
python "IDM Manager v3.0.py"
```
For best results, run as administrator (right-click → Run as administrator)

**Direct Command Line**
Use `zied.cmd` directly with the following parameters:

- `/act` - Activate IDM
- `/frz` - Freeze IDM trial
- `/res` - Reset IDM activation/trial
- `/sts` - Check IDM status
- `/upd` - Check for updates

### New Features in v3.0

**Settings Menu** (Option 9 in main menu)
- Toggle auto-backup before operations
- Enable/disable logging
- Configure automatic update checks
- View and manage log files

**Enhanced Backup/Restore** (Option 5 in main menu)
- Timestamped backups with detailed information
- View all existing backups with size and date
- Restore from any previous backup

**Better Error Handling**
- Automatic admin privilege detection and elevation
- Network connectivity checks before online operations
- French locale support (and other non-English systems)
- Detailed error messages with troubleshooting tips

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
- Python 3.6+ (for GUI)
- Required Python packages (install with `pip install -r requirements.txt`):
  - colorama
  - pillow (optional, for future GUI enhancements)
  - requests (optional, for enhanced network operations)

### Installation
1. Clone or download this repository
2. Open Command Prompt or PowerShell in the folder
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python "IDM Manager v3.0.py"
   ```

## Troubleshooting

### "Le chemin d'accès spécifié est introuvable" or Path Errors
- Make sure `zied.cmd` is in the same folder as the Python script
- Run the application with administrator privileges
- Check your internet connection for activation/freeze operations

### Admin Privileges Required
- Right-click on the Python script and select "Run as administrator"
- Or the application will automatically request elevation when needed

### Network Errors
- Verify your internet connection
- Check if your firewall is blocking the application
- Try again after a few moments

### IDM Not Detected
- Make sure IDM is installed
- Download IDM from the official website: https://www.internetdownloadmanager.com/download.html

## Disclaimer
I would like to make it clear that I am not the original creator of this script. 
When I first uploaded this script to GitHub, the main author had not yet established an official GitHub repository. 
Consequently, users had to go to the official forum to download and use the script until the GitHub repository was eventually created.
My primary goal in setting up this repository was to simplify the process for users. Additionally, 
I made sure to acknowledge the original creators of the script to show respect for their work.
### 💖 Donations
If you feel like showing your love and/or appreciation for this simple project, then how about buying me a coffee or milk? ☕🥛

[<img src="https://github.com/zinzied/Website-login-checker/assets/10098794/24f9935f-3637-4607-8980-06124c2d0225">](https://www.buymeacoffee.com/Zied)
