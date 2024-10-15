import subprocess
import colorama
from colorama import Fore, Style
print(Style.RESET_ALL)
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

print(f"\n{Colors.HEADER}Test for GWO-ackley{Colors.END}")
subprocess.call(['python', 'gwo-ackley.py'])

print(f"\n{Colors.HEADER}Test for GWO-dixon-price{Colors.END}")
subprocess.call(['python', 'gwo-dixon-price.py'])

print(f"\n{Colors.HEADER}Test for GWO-griewank{Colors.END}")
subprocess.call(['python', 'gwo-griewank.py'])

print(f"\n{Colors.HEADER}Test for GWO-perm{Colors.END}")
subprocess.call(['python', 'gwo-perm.py'])

print(f"\n{Colors.HEADER}Test for GWO-rastrigin{Colors.END}")
subprocess.call(['python', 'gwo-rastrigin.py'])

print(f"\n{Colors.HEADER}Test for GWO-rosenbrock{Colors.END}")
subprocess.call(['python', 'gwo-rosenbrock.py'])

print(f"\n{Colors.HEADER}Test for GWO-schwefel{Colors.END}")
subprocess.call(['python', 'gwo-schwefel.py'])

print(f"\n{Colors.HEADER}Test for GWO-sphere{Colors.END}")
subprocess.call(['python', 'gwo-sphere.py'])

print(f"\n{Colors.HEADER}Test for GWO-zakharov{Colors.END}")
subprocess.call(['python', 'gwo-zakharov.py'])
