from GWO import GWO
import functions as functions
obj_func = functions.selectFunction(3)
from cli_spinner import CLI_spinner

lower_bound = -30
upper_bound = 30
dimension = 30
population = [100, 250, 500, 1000]
iteration = [100, 250, 500, 1000]
a_values = [2,3,4]

def do_test():
        for i in population:
            for k in iteration:
                for l in a_values:
                    for j in range(5):
                        spinner = CLI_spinner('GWO-perm tests are running.', 'GWO-perm tests are completed.', 0.1)
                        spinner.start()
                        print(f"\nGrey Wolf Algorithm - Population: {i} - Iteration: {k} - Value-a: {l}, Test Number: {j+1}")
                        gwo(i, k, j+1, 'perm', l)
                        spinner.stop()

def gwo(pop_size, iter, rep, folder, a):
    GWO(obj_func, lower_bound, upper_bound, dimension, SearchAgents_no = pop_size, Max_iter = iter, repeat = rep, folder = folder, value_a = a)

def main():
    do_test()

if __name__ == "__main__":
    main()