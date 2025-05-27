import App.utils.config_file_manager as config_file_manager
from App.bot_launcher import launch_bot
from pathlib import Path
import sys

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) != 2:
        input("Error, corrupted .bat file, the action parameter must be 'buy', 'test', or 'choose_pickup_point'.")
        exit(1)
    action = sys.argv[1]
    if action == "buy":
        print("WARNING ! You are about to run a program THAT WILL BUY THE PRODUCT.")
        print("If you do not wish to continue, please close the terminal.")
        input("click ENTER to continue")

    config_dir = Path("config")
    file_names = [f.name for f in config_dir.iterdir() if f.is_file()]
    for file_name in file_names:
        if not file_name.endswith(".ini") or not file_name.startswith("config") or file_name == "config1_example.ini":
            file_names.remove(file_name)

    for i in range(1, len(file_names) + 1):
        config_file_manager.set_config_file(i)
        launch_bot(action=action)
    input("End of program, click ENTER to close")