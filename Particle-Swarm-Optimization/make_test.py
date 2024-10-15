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

print(f"\n{Colors.HEADER}Test for PSO-ackley{Colors.END}")
subprocess.call(['python', 'pso-ackley.py'])

print(f"\n{Colors.HEADER}Test for PSO-dixon-price{Colors.END}")
subprocess.call(['python', 'pso-dixon-price.py'])

print(f"\n{Colors.HEADER}Test for PSO-griewank{Colors.END}")
subprocess.call(['python', 'pso-griewank.py'])

print(f"\n{Colors.HEADER}Test for PSO-perm{Colors.END}")
subprocess.call(['python', 'pso-perm.py'])

print(f"\n{Colors.HEADER}Test for PSO-rastrigin{Colors.END}")
subprocess.call(['python', 'pso-rastrigin.py'])

print(f"\n{Colors.HEADER}Test for PSO-rosenbrock{Colors.END}")
subprocess.call(['python', 'pso-rosenbrock.py'])

print(f"\n{Colors.HEADER}Test for PSO-schwefel{Colors.END}")
subprocess.call(['python', 'pso-schwefel.py'])

print(f"\n{Colors.HEADER}Test for PSO-sphere{Colors.END}")
subprocess.call(['python', 'pso-sphere.py'])

print(f"\n{Colors.HEADER}Test for PSO-zakharov{Colors.END}")
subprocess.call(['python', 'pso-zakharov.py'])
