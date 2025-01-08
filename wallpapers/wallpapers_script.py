import os
import pathlib
import random

def set_nitrogen_wallpaper(wallpaper):
    print(wallpaper)
    os.system(f"nitrogen {wallpaper} --set-auto ")

def set_betterlockscreen_walppaper(wallpaper):
    print(wallpaper)
    os.system(f"betterlockscreen -u {wallpaper}")

def set_rofi_wallpaper(wallpaper):
    pass

def validate_picture(file):
     if file.endswith(".png") or file.endswith(".jpg"):
          return True
     return False

def validate_wallpaper(wallpaper):
    file = open("/home/vlad/Documents/test-coding/wallpapers/cur_wallpaper", "r")
    if (file.read() == wallpaper):
        file.close()
        return False
    file = open("/home/vlad/Documents/test-coding/wallpapers/cur_wallpaper", "w")
    file.write(wallpaper)
    file.close()
    return True
    

def get_wallpapers(path):
    wallpapers = []
    path = pathlib.Path(path)

    for file in pathlib.Path.iterdir(path):
        file_path = str(file)
        if validate_picture(file_path):
            wallpapers.append(file_path)
    return wallpapers


def get_random_wallpaper(wallpapers):
    wallpaper = random.choice(wallpapers)
    if validate_wallpaper(wallpaper):
        return wallpaper
    return get_random_wallpaper(wallpapers)

def main():
    os.chdir("/")
    path = "/home/vlad/Pictures/"
    wallpapers = get_wallpapers(path)
    current_wallpaper = get_random_wallpaper(wallpapers)
    set_nitrogen_wallpaper(current_wallpaper)
    set_betterlockscreen_walppaper(current_wallpaper)
    # set_rofi_wallpaper(current_wallpaper)

if __name__ == "__main__":
    main()
