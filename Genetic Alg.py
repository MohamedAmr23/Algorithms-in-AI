###initial population#############
import numpy as np
def init_pop(pop_size):
    return np.random.randint(8,size=(pop_size,8))
initial_populaion=init_pop(4)
print(initial_populaion)

#####fitness#######################
def calc_fitness(population):
    fitness_val=[]
    for x in population:
        penalty=0
        for i in range(8):
            r=x[i]
            for j in range(8):
                if i==j:
                    continue
                d=abs(i-j)
                if x[j] in[r,r-d,r+d]:
                    penalty+=1
        fitness_val.append(penalty)
    return-1*np.array(fitness_val)    
fitness=calc_fitness(initial_populaion)
print(fitness)
##################selection##################
def selection(population,fitness_val):
    probs=fitness_val.copy()
    probs+=abs(probs.min())+1
    probs=probs/probs.sum()
    N=len(population)
    indicies=np.arange(N)
    selection_indicies=np.random.choice(indicies,size=N,p=probs)
    selection_population=population[selection_indicies]
    return selection_population