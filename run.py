import functions
from enumFunctions import Functions
import GA
from SA import simulated_annealing  
from GWO import GWO
obj_func = functions.selectFunction(Functions.ackley)

def gwo():
    #obj_func = functions.selectFunction(Functions.schwefel)
    # dim array size, -5 lb +5 lb 
    GWO(obj_func, -3200, 3200, dim = 30, SearchAgents_no = 1000, Max_iter = 1000)

def GeneticAlgorithm():
    #functionIndex = Functions.schwefel
    #_lb = -500
    #_ub = 500
    #dim = 30
    #pop_size = 1000 # pop size
    #maxiter = 1000
    #obj_func = functions.selectFunction(Functions.schwefel)
    #sol = GA.GA(obj_func, _lb, _ub, dim, pop_size, maxiter)
    sol = GA.GA(obj_func, lb = -500, ub = 500, dim = 30, popSize = 1000, iters = 1000)
    return sol


def SimulatedAnnealing():
    #obj_func = functions.selectFunction(Functions.schwefel)
    # dim array size, -5 lb +5 lb 
    simulated_annealing( min_values = [-500,-500,-500,-500,-500,-500,-500,-500,-500, -500], 
                         max_values = [500,500,500,500,500,500,500,500,500,500], 
                         mu = 0, sigma = 1, initial_temperature = 10.0, temperature_iterations = 100,
                         final_temperature = 0.0001, alpha = 0.9, alpha2=0.0114, geo=1, target_function = obj_func, verbose = True)

def main():
    algo = 3
    if(algo == 1):
        SimulatedAnnealing()
    if(algo == 2):
        sol = GeneticAlgorithm()
    if(algo == 3):
        gwo()


if __name__ == "__main__":
    main()