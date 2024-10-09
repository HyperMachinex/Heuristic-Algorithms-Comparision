from GWO import GWO
import functions as functions
obj_func = functions.selectFunction(0)

lower_bound = -32.768
upper_bound = 32.768
dimension = 30
population = [100, 250, 500, 1000]
iteration = [100, 250, 500, 1000]
a_values = [2,3,4]

def do_test():
    for j in range(5):
        for i in population:
            for k in iteration:
                for l in a_values:
                    print(f"Grey Wolf Algorithm - Population: {i} - Iteration: {k} - Value-a: {l}, Test Number: {j+1}")
                    gwo(i, k, j+1, 'ackley', l)

def gwo(pop_size, iter, rep, folder, a):
    GWO(obj_func, lower_bound, upper_bound, dimension, SearchAgents_no = pop_size, Max_iter = iter, repeat = rep, folder = folder, value_a = a)

def main():
    do_test()


if __name__ == "__main__":
    main()