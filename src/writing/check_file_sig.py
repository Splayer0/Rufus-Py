import psutil
import os

def CheckFileSignature(file_path) -> bool:
    # Check if the file:
    # - exists
    # - is a regular file (not a directory)
    # - has proper "magic numbers" for an ISO file (0x43 0x44 0x30 0x30 at offset 32769)

    # this will make sure user doesn't try to break the program by passing a fake .iso

    if not os.path.isfile(file_path):
        print(f"File does not exist: {file_path}")
        return False
    
    try:
        with open(file_path, 'rb') as f:
            f.seek(32769) # moves offset to where magic numbers should be
            magic = f.read(5) # read 5 bytes to read CD001
            if magic == b'\x43\x44\x30\x30\x31':  # "CD001" in hex (applied)
                print(f"Valid ISO file: {file_path}")
                return True
            else:
                print(f"Invalid ISO file (magic number mismatch): {file_path}")
                return False
    except PermissionError:
        print(f"Permission denied when trying to read file: {file_path}")
        return False
    except Exception as err:
        print(f"Error checking file signature: {err}")
        return False

def _is_removable_device(device_node) -> bool:
    """Check that a device is removable (e.g. USB stick) before writing to it."""
    base_name = os.path.basename(device_node).rstrip("0123456789")
    removable_path = f"/sys/block/{base_name}/removable"
    try:
        with open(removable_path, "r") as f:
            return f.read().strip() == "1"
    except OSError:
        return False


def _resolve_device_node(usb_mount_path) -> str | None:
    """Resolve a mount path to its underlying device node for dd."""
    normalized = os.path.normpath(usb_mount_path)
    for part in psutil.disk_partitions():
        if os.path.normpath(part.mountpoint) == normalized:
            return part.device
    return None