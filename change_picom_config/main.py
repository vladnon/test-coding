import os

def kill_picom():
    os.system("pkill picom")

def get_new_config():
    f = open("/home/vlad/Documents/test-coding/change_picom_config/current_picom_config", "r")
    if f.read() == "config1":
        f.close()
        f = open("/home/vlad/Documents/test-coding/change_picom_config/current_picom_config", "w")
        f.write("config2")
        f.close()
        return True
    else:
        f.close()
        f = open("/home/vlad/Documents/test-coding/change_picom_config/current_picom_config", "w")
        f.write("config1")
        f.close()
        return False
    


def set_config(new_conf):
    os.system(f"picom --config {new_conf} -b")



if __name__ == "__main__":
    config1 = ".config/picom/picom.conf"
    config2 = ".config/picom/picom2.conf"
    kill_picom()
    cur_config = get_new_config()
    if cur_config:
        set_config(config2)
    else:
        set_config(config1)
    



