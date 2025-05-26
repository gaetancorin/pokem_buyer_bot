import App.utils.config_file_manager as config_file_manager
from App.bot_launcher import launch_bot
import sys

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) != 3:
        input("Erreur sur les arguments donnees au fichier .bat, reessayer")
        exit(1)
    else:
        if not sys.argv[1].isdigit():
            input("Erreur sur la selection du numero de fichier de config")
            exit(1)
        if sys.argv[2] not in ["buy", "test", "choose_pickup_point"]:
            input("Erreur, fichier .bat corrompu, le parametre action doit etre buy, test, ou choose_pickup_point.")
            exit(1)
    config_number = int(sys.argv[1])
    action = sys.argv[2]
    if action == "buy":
        print("WARNING ! You are about to run a program THAT WILL BUY THE PRODUCT.")
        print("If you do not wish to continue, please close the terminal.")
        input("click ENTER to continue")

    config_file_manager.set_config_file(config_number)
    launch_bot(action=action)
    input("End of program, click ENTER to close")
