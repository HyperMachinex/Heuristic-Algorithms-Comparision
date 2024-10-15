from PSO import PSO
import functions as functions
obj_func = functions.selectFunction(8)
from cli_spinner import CLI_spinner

lower_bound = -5
upper_bound = 10
dimension = 30
population = [100, 250, 500, 1000]
iteration = [100, 250, 500, 1000]

def do_test():    
        for i in population:
            for k in iteration:
                    for j in range(5):
                        spinner = CLI_spinner('PSO-zakharov tests are running.', 'PSO-zakharov tests are completed.', 0.1)
                        spinner.start()
                        print(f"\nParticle Swarm Optimization - Population: {i} - Iteration: {k} - Test Number: {j+1}")
                        pso(i, k, j+1, 'zakharov')
                        spinner.stop()

def pso(pop_size, iter, rep, folder):
      PSO(obj_func, lower_bound, upper_bound, dimension, pop_size, iter, folder, rep)

def main():
      do_test()

if __name__ == "__main__":
      main()
