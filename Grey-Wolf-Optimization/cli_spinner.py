import multiprocessing
import time
import colorama
from colorama import Fore, Style

class CLI_spinner:
    def __init__(self, message = "", message_end = "", speed = 0.1) -> None:
        self.message = message
        self.speed = speed
        self.message_end = message_end

        self.process = multiprocessing.Process(
            target = self.spin,
            args=(),
            name = "CLI Spinner"
        )


    def spin(self):
        spinner = ['-', '\\', '|', '/']
        n = 0
        while True:
            print(Fore.YELLOW + f'\r{self.message} [{spinner[n]}]', end = "")
            n += 1
            if n >= len(spinner):
                n = 0
            time.sleep(self.speed)


    def start(self):
        self.process.start()

    def stop(self):
        if not self.process.is_alive():
            print("Warning: CLI Spinner is not running.")
        else:
            self.process.terminate()
            print('\r' + ' ' * (len(self.message) + 10), end='')
            print(Fore.GREEN + f'\r{self.message_end}', end = "")
            print(Style.RESET_ALL)
