import random
import numpy as np
import math
initial_size=int(input("ENTER THE POPULATION INITIALISATION SIZE OF CHROMOSOME: "));
size=int(input("ENTER THE NUMBER OF CHROMOSOMES: "))
pop_data=np.empty((size,initial_size),dtype=np.int32)
for i in range(size):
    for j in range(initial_size):
        pop_data[i,j]=random.randint(0,40)
print("POPULATION: ")
print(pop_data)

#Fitness
def fitness(pop_data):
    f=[]
    for i in range(pop_data.shape[0]):
        s,k=0,1
        for j in range(pop_data.shape[1]):
            s+=k*pop_data[i,j]
            k+=1
        f.append(1/(1+np.abs(s-30)))
    return f;
f=fitness(pop_data)
print("FITNESS: ")
print(f)

def r_wheel(pop_data,f):
    sof=sum(f)
    print("TOTAL SUM: ")
    print(sof)
    p=[]
    for i in range(len(f)):
        p.append(f[i]/sof)
    print("PROBABILITY OF EACH CHROMOSOME: ")
    print(p)
    c_p=[]
    for i in range(len(f)):
            s=0
            for j in range(0,i+1):
                s+=p[j]
            c_p.append(s)
    print("CUMMULATIVE PROBABILITY: " )
    print(c_p)
    r=[]
    for i in range(len(f)):
        r.append(random.random())
    print("RANDOM NUMBER: ")
    print(r)
    index=[]
    for i in range(len(r)):
        
        for j in range(len(c_p)):
            if(c_p[j]>r[i]):
                index.append(j)
                break
    new_pop=np.empty((size,initial_size),dtype=np.int32)
    for i in range(size):
        new_pop[i]=pop_data[index[i],:]
    print("NEW CHROMOSOME: ")
    return (new_pop)
   
print(r_wheel(pop_data,f))
new_pop=r_wheel(pop_data,f)


#crossover

def cross(l,q,k):
    for i in range(k,size):
        l[i], q[i] = q[i], l[i]
    return l, q 

def crossover(new_pop,rate):
    r=[]
    for i in range(size):
        r.append(random.random())
    print("RANDOM: ")
    print(r)
    index=[]
    no_parents_selected=int(rate*new_pop.shape[0])
    for i in range(no_parents_selected):
        for j in range(size):
            if(r[j]<rate):
                index.append(j)
    print("SELECTED CHROMOSOME: ")
    print(index)
    R=random.randint(1,initial_size-1)
    print("CROSSOVER POINT: ")
    print(R)
    for i in range(0,len(index)):
        j=i+1;
        while (j<(len(index)-1)):
            new_pop[i],new_pop[j]=cross(new_pop[j],new_pop[i],R)
print(crossover(new_pop,0.25))
print("POPULATION AFTER CROSSOVER: ")
print(new_pop)

def mutation(new_pop,m_rate):
    total_gen=size*initial_size;
    R=random.randint(1,24)
    if(R<(m_rate*total_gen)):
        r=random.randint(1,size-1)
        s=random.randint(1,initial_size-1)
        new_pop[r][s]=R
    return new_pop
n_pop=mutation(new_pop,0.1)
print("NEW POPULATION AFTER MUTATION: ")
print(n_pop)
fitty=fitness(n_pop)
s_um=sum(fitty)
prob=[]
for i in range(len(fitty)):
    prob.append(fitty[i]/s_um)
print("PROBABILITY OF EACH CHROMOSOME: ")
print(prob)
print("FITTEST CHROMOSOME PROBABILITY: ")
m=max(prob)
print(m)
i=prob.index(m)
print("FITTEST CHROMOSOME: ")
print(new_pop[i])


       
