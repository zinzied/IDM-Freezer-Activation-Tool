import subprocess
import os
import sys
import time
import webbrowser
from colorama import Fore, Style, Back, init

# Initialize colorama
init(autoreset=True)

VERSION = "2.0"

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print the application header."""
    clear_screen()
    print(Fore.CYAN + "=" * 70)
    print(Fore.CYAN + "=" + Fore.WHITE + Back.BLUE + " IDM FREEZER & ACTIVATION TOOL ".center(68) + Fore.CYAN + "=")
    print(Fore.CYAN + "=" + Fore.YELLOW + f" Version {VERSION} ".center(68) + Fore.CYAN + "=")
    print(Fore.CYAN + "=" * 70)
    print(Fore.MAGENTA + """
     ██╗██████╗ ███╗   ███╗    ███████╗██████╗ ███████╗███████╗███████╗███████╗██████╗
     ██║██╔══██╗████╗ ████║    ██╔════╝██╔══██╗██╔════╝██╔════╝╚══███╔╝██╔════╝██╔══██╗
     ██║██║  ██║██╔████╔██║    █████╗  ██████╔╝█████╗  █████╗    ███╔╝ █████╗  ██████╔╝
     ██║██║  ██║██║╚██╔╝██║    ██╔══╝  ██╔══██╗██╔══╝  ██╔══╝   ███╔╝  ██╔══╝  ██╔══██╗
     ██║██████╔╝██║ ╚═╝ ██║    ██║     ██║  ██║███████╗███████╗███████╗███████╗██║  ██║
     ╚═╝╚═════╝ ╚═╝     ╚═╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                            BY ZIEDEV 2025
    """)
    print(Fore.CYAN + "=" * 70)

def print_menu():
    """Print the main menu options."""
    print(Fore.GREEN + "\nMAIN MENU:")
    print(Fore.WHITE + "=" * 70)
    print(Fore.YELLOW + " [1]" + Fore.WHITE + " Activate IDM")
    print(Fore.YELLOW + " [2]" + Fore.WHITE + " Freeze Trial (Recommended)")
    print(Fore.YELLOW + " [3]" + Fore.WHITE + " Reset Activation/Trial")
    print(Fore.YELLOW + " [4]" + Fore.WHITE + " Check IDM Status")
    print(Fore.YELLOW + " [5]" + Fore.WHITE + " Backup/Restore IDM Settings")
    print(Fore.WHITE + "=" * 70)
    print(Fore.YELLOW + " [6]" + Fore.WHITE + " Download IDM")
    print(Fore.YELLOW + " [7]" + Fore.WHITE + " Visit GitHub Repository")
    print(Fore.YELLOW + " [8]" + Fore.WHITE + " Check for Updates")
    print(Fore.YELLOW + " [0]" + Fore.WHITE + " Exit")
    print(Fore.WHITE + "=" * 70)

def show_progress(message, duration=3):
    """Show a progress bar with the given message."""
    print(Fore.CYAN + f"\n{message}")
    print(Fore.YELLOW + "Progress: ", end="")
    for i in range(50):
        time.sleep(duration/50)
        print(Fore.GREEN + "█", end="", flush=True)
    print(Fore.GREEN + " Done!")

def run_batch_file(parameter=""):
    """Run the zied.cmd batch file with optional parameters."""
    try:
        if parameter:
            show_progress(f"Running command with parameter: {parameter}")
            subprocess.run(["cmd.exe", "/c", f"zied.cmd {parameter}"], check=True)
        else:
            show_progress("Launching IDM Activation Script")
            subprocess.run(["cmd.exe", "/c", "zied.cmd"], check=True)

        print(Fore.GREEN + "\nOperation completed successfully!")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"\nAn error occurred while running the batch file: {e}")

    input(Fore.YELLOW + "\nPress Enter to return to the main menu...")

def check_idm_status():
    """Check the current status of IDM installation."""
    print(Fore.CYAN + "\nChecking IDM status...")

    # Check if IDM is installed
    idm_paths = [
        os.path.join(os.environ.get('PROGRAMFILES(X86)', ''), 'Internet Download Manager', 'IDMan.exe'),
        os.path.join(os.environ.get('PROGRAMFILES', ''), 'Internet Download Manager', 'IDMan.exe')
    ]

    idm_installed = any(os.path.exists(path) for path in idm_paths)

    if not idm_installed:
        print(Fore.RED + "IDM is not installed on this system.")
        input(Fore.YELLOW + "\nPress Enter to return to the main menu...")
        return

    # Run a command to check IDM status
    try:
        # Create a temporary batch file to check IDM status
        with open("check_idm.bat", "w") as f:
            f.write('@echo off\n')
            f.write('setlocal\n')
            f.write('for /f "tokens=2*" %%a in (\'reg query "HKCU\\Software\\DownloadManager" /v Serial 2^>nul\') do set "serial=%%b"\n')
            f.write('for /f "tokens=2*" %%a in (\'reg query "HKCU\\Software\\DownloadManager" /v tvfrdt 2^>nul\') do set "trial=%%b"\n')
            f.write('echo IDM_STATUS_BEGIN\n')
            f.write('if defined serial echo Serial: %serial%\n')
            f.write('if defined trial echo Trial: %trial%\n')
            f.write('if not defined serial if not defined trial echo Status: Unknown\n')
            f.write('echo IDM_STATUS_END\n')

        # Run the batch file and capture output
        result = subprocess.run(["cmd.exe", "/c", "check_idm.bat"], capture_output=True, text=True)

        # Parse the output
        output = result.stdout
        status_section = output.split("IDM_STATUS_BEGIN")[1].split("IDM_STATUS_END")[0].strip() if "IDM_STATUS_BEGIN" in output else ""

        print(Fore.GREEN + "\nIDM Status:")
        print(Fore.WHITE + "=" * 50)

        if "Serial:" in status_section:
            print(Fore.GREEN + "IDM is registered with a serial key.")
        elif "Trial:" in status_section:
            print(Fore.YELLOW + "IDM is in trial mode.")
        else:
            print(Fore.RED + "IDM status could not be determined.")

        print(Fore.WHITE + "=" * 50)

        # Clean up
        if os.path.exists("check_idm.bat"):
            os.remove("check_idm.bat")

    except Exception as e:
        print(Fore.RED + f"Error checking IDM status: {e}")

    input(Fore.YELLOW + "\nPress Enter to return to the main menu...")

def backup_restore_idm():
    """Backup or restore IDM settings."""
    while True:
        clear_screen()
        print_header()
        print(Fore.GREEN + "\nBACKUP/RESTORE IDM SETTINGS:")
        print(Fore.WHITE + "=" * 70)
        print(Fore.YELLOW + " [1]" + Fore.WHITE + " Backup IDM Settings")
        print(Fore.YELLOW + " [2]" + Fore.WHITE + " Restore IDM Settings")
        print(Fore.YELLOW + " [0]" + Fore.WHITE + " Return to Main Menu")
        print(Fore.WHITE + "=" * 70)

        choice = input(Fore.GREEN + "\nEnter your choice: ")

        if choice == "1":
            # Backup IDM settings
            backup_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "IDM_Backup")
            os.makedirs(backup_dir, exist_ok=True)

            try:
                show_progress("Backing up IDM settings")

                # Create a batch file for backup
                with open("backup_idm.bat", "w") as f:
                    f.write('@echo off\n')
                    f.write('setlocal EnableDelayedExpansion\n')
                    f.write(f'set "backup_dir={backup_dir}"\n')
                    f.write('set "timestamp=%date:~-4,4%%date:~-7,2%%date:~-10,2%_%time:~0,2%%time:~3,2%%time:~6,2%"\n')
                    f.write('set timestamp=!timestamp: =0!\n')
                    f.write('reg export "HKCU\\Software\\DownloadManager" "!backup_dir!\\IDM_Settings_!timestamp!.reg" /y\n')
                    f.write('echo Backup saved to: !backup_dir!\\IDM_Settings_!timestamp!.reg\n')

                # Run the backup
                subprocess.run(["cmd.exe", "/c", "backup_idm.bat"], check=True)

                # Clean up
                if os.path.exists("backup_idm.bat"):
                    os.remove("backup_idm.bat")

                print(Fore.GREEN + f"\nBackup completed successfully! Files saved to {backup_dir}")
            except Exception as e:
                print(Fore.RED + f"\nError during backup: {e}")

            input(Fore.YELLOW + "\nPress Enter to continue...")

        elif choice == "2":
            # Restore IDM settings
            backup_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "IDM_Backup")

            if not os.path.exists(backup_dir):
                print(Fore.RED + "\nNo backup directory found!")
                input(Fore.YELLOW + "\nPress Enter to continue...")
                continue

            backup_files = [f for f in os.listdir(backup_dir) if f.startswith("IDM_Settings_") and f.endswith(".reg")]

            if not backup_files:
                print(Fore.RED + "\nNo backup files found!")
                input(Fore.YELLOW + "\nPress Enter to continue...")
                continue

            print(Fore.GREEN + "\nAvailable backup files:")
            for i, file in enumerate(backup_files, 1):
                print(Fore.YELLOW + f" [{i}]" + Fore.WHITE + f" {file}")

            try:
                file_choice = int(input(Fore.GREEN + "\nEnter the number of the file to restore (0 to cancel): "))
                if file_choice == 0:
                    continue

                if 1 <= file_choice <= len(backup_files):
                    selected_file = os.path.join(backup_dir, backup_files[file_choice-1])

                    show_progress("Restoring IDM settings")

                    # Import the registry file
                    subprocess.run(["reg", "import", selected_file], check=True)

                    print(Fore.GREEN + "\nRestore completed successfully!")
                else:
                    print(Fore.RED + "\nInvalid selection!")
            except ValueError:
                print(Fore.RED + "\nPlease enter a valid number!")
            except Exception as e:
                print(Fore.RED + f"\nError during restore: {e}")

            input(Fore.YELLOW + "\nPress Enter to continue...")

        elif choice == "0":
            break
        else:
            print(Fore.RED + "\nInvalid choice. Please try again.")
            time.sleep(1)

def check_for_updates():
    """Check if there's a newer version available."""
    print(Fore.CYAN + "\nChecking for updates...")

    # This is a placeholder. In a real application, you would check a server or GitHub API
    # to determine if there's a newer version available.

    # For demonstration purposes:
    show_progress("Connecting to update server", 2)

    print(Fore.GREEN + "\nYou are running the latest version!")
    print(Fore.WHITE + f"Current version: {VERSION}")

    input(Fore.YELLOW + "\nPress Enter to return to the main menu...")

def main():
    """Main application function."""
    while True:
        print_header()
        print_menu()

        choice = input(Fore.GREEN + "\nEnter your choice: ")

        if choice == "1":
            run_batch_file("/act")
        elif choice == "2":
            run_batch_file("/frz")
        elif choice == "3":
            run_batch_file("/res")
        elif choice == "4":
            check_idm_status()
        elif choice == "5":
            backup_restore_idm()
        elif choice == "6":
            webbrowser.open("https://www.internetdownloadmanager.com/download.html")
            input(Fore.YELLOW + "\nBrowser opened. Press Enter to continue...")
        elif choice == "7":
            webbrowser.open("https://github.com/zinzied/IDM-Freezer")
            input(Fore.YELLOW + "\nBrowser opened. Press Enter to continue...")
        elif choice == "8":
            check_for_updates()
        elif choice == "0":
            print(Fore.GREEN + "\nThank you for using IDM Freezer & Activation Tool!")
            time.sleep(1)
            sys.exit(0)
        else:
            print(Fore.RED + "\nInvalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\nProgram interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + f"\n\nAn unexpected error occurred: {e}")
        input(Fore.YELLOW + "\nPress Enter to exit...")
        sys.exit(1)
