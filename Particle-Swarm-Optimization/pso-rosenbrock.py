from PSO import PSO
import functions as functions
obj_func = functions.selectFunction(5)
from cli_spinner import CLI_spinner

lower_bound = -2048
upper_bound = 2048
dimension = 30
population = [100]
iteration = [100]

def do_test():    
        for i in population:
            for k in iteration:
                    for j in range(5):
                        spinner = CLI_spinner('PSO-rosenbrock tests are running.', 'PSO-rosenbrock tests are completed.', 0.1)
                        spinner.start()
                        print(f"\nParticle Swarm Optimization - Population: {i} - Iteration: {k} - Test Number: {j+1}")
                        pso(i, k, j+1, 'rosenbrock')
                        spinner.stop()

def pso(pop_size, iter, rep, folder):
      PSO(obj_func, lower_bound, upper_bound, dimension, pop_size, iter, folder, rep)

def main():
      do_test()

if __name__ == "__main__":
      main()
