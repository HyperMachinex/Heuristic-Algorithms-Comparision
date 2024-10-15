from PSO import PSO
import functions as functions
obj_func = functions.selectFunction(2)
from cli_spinner import CLI_spinner

lower_bound = -600
upper_bound = 600
dimension = 30
population = [100]
iteration = [100]

def do_test():    
        for i in population:
            for k in iteration:
                    for j in range(5):
                        spinner = CLI_spinner('PSO-griewank tests are running.', 'PSO-griewank tests are completed.', 0.1)
                        spinner.start()
                        print(f"\nParticle Swarm Optimization - Population: {i} - Iteration: {k} - Test Number: {j+1}")
                        pso(i, k, j+1, 'griewank')
                        spinner.stop()

def pso(pop_size, iter, rep, folder):
      PSO(obj_func, lower_bound, upper_bound, dimension, pop_size, iter, folder, rep)

def main():
      do_test()

if __name__ == "__main__":
      main()
