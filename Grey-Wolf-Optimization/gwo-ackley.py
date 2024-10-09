from GWO import GWO
import functions as functions
obj_func = functions.selectFunction(0)

lower_bound = -32.768
upper_bound = 32.768
dimension = 30
population = [100, 250, 500, 1000]
iteration = [100, 250, 500, 1000]

def do_test():
    for j in range(5):
        for i in population:
            for k in iteration:
                print(f"Grey Wolf Algorithm - Population: {i} - Iteration: {k}, Test Number: {j+1}")
                gwo(i, k, j+1, 'ackley')

def gwo(pop_size, iter, rep, folder):
    GWO(obj_func, lower_bound, upper_bound, dimension, SearchAgents_no = pop_size, Max_iter = iter, repeat = rep, folder = folder)

def main():
    do_test()


if __name__ == "__main__":
    main()