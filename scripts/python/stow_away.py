import subprocess
import os

# function that prints out the command and its output via the getoutput function
def run_command(command):
    print("\n\nRunning command: " + command)
    print(subprocess.getoutput(command))

def stow(target_dir, dotsubdir):
    # run in simulation mode
    run_command(f"stow -nvt {target_dir} {dotsubdir}" )
    # confirm stow... enter to continue
    input("Press Enter to continue to create the symlink...")
    # stow dotfiles using -vt flag
    run_command(f"stow -vt {target_dir} {dotsubdir}")

# stows dotfiles 
def stow_away():
    # get home dir
    home_dir = os.path.expanduser("~")
    # get dotfiles dir
    dotfiles_dir = home_dir + "/dotfiles"
    # get dotfiles list
    dotfiles = os.listdir(dotfiles_dir)
    # stow dotfiles except scripts folder
    # only goes through folders
    for dotfile in dotfiles:
        if dotfile in ["scripts",".git"]:
            pass
        elif dotfile == "config":
            stow(home_dir + "/.config", dotfile)
        else:
            stow(home_dir, dotfile)

stow_away()