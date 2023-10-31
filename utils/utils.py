import os
import re


def rgba_to_hex(rgba_color):
    """ Extracts the RGB components from the RGBA color
    and converts RGB components to hexadecimal format
       e.g. 'rgba(255, 101, 80, 1)' -> #FF6550
    """
    rgba_color = re.search(r'rgba?\((.*?)\)', rgba_color).group(1)
    r, g, b, a = map(int, rgba_color.split(', '))
    # Convert RGB components to hexadecimal format
    hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
    return hex_color

def clear_downloaded_file_by_name(download_dir = "./download_taf/", file_name = "EPAM_Corporate_Overview_Q3_october.pdf"):
    # Define the path to the file
    file_path = os.path.join(download_dir, file_name)
    try:
        # Check if the file exists
        if os.path.exists(file_path):
            # Delete the file
            os.remove(file_path)
            print(f"{file_name} has been deleted successfully!")
        else:
            print(f"{file_name} does not exist in {download_dir}.")
    except:
        pass


if __name__ == '__main__':
    rgba = 'rgba(255, 101, 80, 1)'
    print(rgba_to_hex(rgba))
    rgba = 'rgba(0, 0, 0, 1)'
    print(rgba_to_hex(rgba))
