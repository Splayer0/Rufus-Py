import subprocess
import states

### DISK FORMATTING ###
def volumecustomlabel():
    # 1. detect the file type
    # 2. unmount the drive
    # 3. change the label using the command specific for that file type
    # 4. mount the drive again
    pass

def cluster():
    # detect the current selected cluster and put it in a variable
    # convert the clusters to sectors fat32
    pass

def quickformat():
    # detect quick format option ticked or not and put it in a variable
    # the if logic will be implemented later
    pass

def createextended():
    # detect create extended label and icon files check box and put it in a variable
    pass

def checkdevicebadblock():
    # following may be used?
    # pkexec badblocks -wsv path
    # no idea how to use passes tho
    pass

def dskformat(usb_mount_path):
    path = usb_mount_path
    type = states.currentFS
    #These can later be turned to a notification or error box using pyqt
    def pkexecNotFound():
        print("Error: The command pkexec was not found on your system.")
    def FormatFail():
        print("Error: Formatting failed. Was the password correct? Is the drive unmounted?")
    def unexpected():
        print(f"An unexpected error occurred")
    # 0 -> NTFS 
    # 1 -> FAT32 
    # 2 -> exFAT
    # 3 -> ext4
    #THIS WILL ASK FOR PASSWORD NEED TO FETCH PASSWORD so we are using pkexec from polkit to prompt the user for a password. need to figure out a way to use another method or implement this everywhere.
    # instead of FileNotFoundError we can also use shutil(?)
    clusters = "4096" # default will be changed to link to the output from the cluster function
    sectors = "8" # default

    if type==0:
        try:
            subprocess.run(["pkexec", "mkfs.ntfs", "-c", clusters, "-Q", path], check=True)
            print("success format to ntfs!")
        except FileNotFoundError:
            pkexecNotFound()
        except subprocess.CalledProcessError:
            FormatFail()
        except Exception:
            unexpected()
    elif type==1:
        try:
            subprocess.run(["pkexec", "mkfs.vfat", "-s", sectors, "-F", "32", path], check=True)
            print("success format to fat32!")
        except FileNotFoundError:
            pkexecNotFound()
        except subprocess.CalledProcessError:
            FormatFail()
        except Exception:
            unexpected()
    elif type==2:
        try:
            subprocess.run(["pkexec", "mkfs.exfat", "-b", clusters, path], check=True)
            print("success format to exFAT!")
        except FileNotFoundError:
            pkexecNotFound()
        except subprocess.CalledProcessError:
            FormatFail()
        except Exception:
            unexpected()
    elif type==3:
        try:
            subprocess.run(["pkexec", "mkfs.ext4", "-b", clusters, path], check=True)
            print("success format to ext4!")
        except FileNotFoundError:
            pkexecNotFound()
        except subprocess.CalledProcessError:
            FormatFail()
        except Exception:
            unexpected()
    else:
        unexpected()
