from Core.Networking.Server import Server
from Protocol.Messages.Server.LobbyInfoMessage import LobbyInfoMessage
from Utils.Helpers import Helpers
import colorama
from colorama import Fore, Back, Style
import time

def main():

    print(Fore.MAGENTA + "Server started, If error Unable to connect to Mongo server check the entered data in соnfig.json.")

    print(Fore.WHITE + "zip by @xmopser & @d1ld0br3k")
    time.sleep(0.1)
    print(Fore.BLUE + "zip by @xmopser & @d1ld0br3k")
    time.sleep(0.1)
    print(Fore.RED + "zip by @xmopser & @d1ld0br3k")
    time.sleep(0.1)
    print(Fore.CYAN + "zip by @xmopser & @d1ld0br3k")
    time.sleep(0.1)
    print(Fore.MAGENTA + "zip by @xmopser & @d1ld0br3k")
    time.sleep(0.1)
    print(Fore.YELLOW + "zip by @xmopser & @d1ld0br3k")
    time.sleep(0.1)
    print(Fore.BLACK + "zip by @xmopser & @d1ld0br3k")
    time.sleep(0.1)
    print(Fore.GREEN + "zip by @xmopser & @d1ld0br3k")
    time.sleep(0.1)

    Server("0.0.0.0", 9339).start()


if __name__ == '__main__':
    main()
