import subprocess

print("Test for GWO-ackley")
subprocess.call(['python', 'gwo-ackley.py'])

print("Test for GWO-dixon-price")
subprocess.call(['python', 'gwo-dixon-price.py'])

print("Test for GWO-griewank")
subprocess.call(['python', 'gwo-griewank.py'])

print("Test for GWO-perm")
subprocess.call(['python', 'gwo-perm.py'])

print("Test for GWO-rastrigin")
subprocess.call(['python', 'gwo-rastrigin.py'])

print("Test for GWO-rosenbrock")
subprocess.call(['python', 'gwo-rosenbrock.py'])

print("Test for GWO-schwefel")
subprocess.call(['python', 'gwo-schwefel.py'])

print("Test for GWO-sphere")
subprocess.call(['python', 'gwo-sphere.py'])

print("Test for GWO-zakharov")
subprocess.call(['python', 'gwo-zakharov.py'])
