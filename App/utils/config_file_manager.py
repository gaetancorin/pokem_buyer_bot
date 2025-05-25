# manage config file by iteration
import configparser

config_file = None

def set_config_file(iteration):
    global config_file
    print("USE CONFIG FILE config"+str(iteration)+".ini")
    config_file = configparser.ConfigParser()
    config_file.read("config/config"+str(iteration)+".ini")
    return config_file

def set_config_file_on_debug_mode(iteration):
    global config_file
    print("USE CONFIG FILE config"+str(iteration)+".ini")
    config_file = configparser.ConfigParser()
    config_file.read("../config/config"+str(iteration)+".ini")
    return config_file

def get_config_file():
    global config_file
    return config_file

