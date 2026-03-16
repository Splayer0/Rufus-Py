import psutil
import os
import subprocess


def GetUSBInfo(usb_path: str) -> dict:
    try:
        normalized_usb_path = os.path.normpath(usb_path)

        for part in psutil.disk_partitions(all=True):
            if os.path.normpath(part.mountpoint) == normalized_usb_path:
                device_node = part.device
                break
        else:
            print(f"Could not find device node for USB path: {usb_path}")
            return {}

        size_output = subprocess.check_output(
            ["lsblk", "-d", "-n", "-b", "-o", "SIZE", device_node],
            text=True,
            timeout=5,
        ).strip()

        usb_size = int(size_output) if size_output.isdigit() else 0
        if not size_output.isdigit():
            print(f"Warning: could not parse device size: {size_output!r}")

        if usb_size > 32 * 1024**3:
            print(f"USB device is large ({usb_size} bytes); confirm before flashing.")

        label = subprocess.check_output(
            ["lsblk", "-d", "-n", "-o", "LABEL", device_node], text=True, timeout=5
        ).strip()
        if not label:
            label = os.path.basename(usb_path)

        usb_info = {
            "device_node": device_node,
            "label": label,
            "mount_path": normalized_usb_path,
        }
        print(f"USB Info: {usb_info}")
        return usb_info
    except subprocess.TimeoutExpired as e:
        print(f"Timed out getting USB info for {usb_path}: {e}")
        return {}
    except PermissionError:
        print(f"Permission denied when trying to get USB info: {usb_path}")
        return {}
    except subprocess.CalledProcessError as e:
        print(f"Error getting USB info: {e}")
        return {}
    except Exception as err:
        print(f"Unexpected error getting USB info: {err}")
        return {}
