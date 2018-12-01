# -*- coding: utf-8 -*-
"""
Projecto Final em Otimização de Grafos 

O problemo do TSP

Erwan Dufresne 

Novembro 2018
"""
# all global variable and impot needed

global somme_path # a mettre a chaque fois avant de relancer minimum_line
global ville 
global x
global path
global debut
global save
global best_path
global best_somme_path

import numpy as np
import itertools
import matplotlib.pyplot as plt
import time 
from random import randint

global x
global y
global mat2
global path
global save
global best_path
global best_somme_path
global mat
global somme_path
global ville
global debut




#%%

#the first part here, is to show the running of the heuristic
print("\n\n\n\n\n\n#################################################\n")
print("                 Part 1")
print("\n#################################################\n")

def to_start(valeur):
    "initialisation needed for the beginning"
    global x
    global y
    global mat2
    global path
    global save
    global best_path
    global best_somme_path
    global mat
    global somme_path
    global ville
    global debut
    #nombre de villes
    x= valeur
    #max value of the cost of a single trip between two cities
    y=15 
    #matriz identidad com 1000 (infinity)
    mat2=np.eye(x,x)*1000
    #vector path
    path = np.arange(x)*0
    #save to stock the first city
    save = np.arange(x)*0
    best_path = np.arange(x)*0
    best_somme_path=100000    
    #generatção matriz aleatoiria com distancia entre 1 e y
    for i in range (0,x,1):
        for i2 in range (i,x,1):
            if i!=i2:
                mat2[i][i2]=randint(1,y)
                mat2[i2][i]=mat2[i][i2]          
    #print (mat2)
    mat=np.eye(x,x)*0
    #cost camino
    somme_path = 0
    ville = 0 
    debut = 0  
    remise_mat()



def remise_mat():
    "stock values of the original matrix, to not modified the original one"
    for i in range (0,x,1):
        for y in range (0,x,1):
            mat[i][y]=mat2[i][y]
    #print(mat)




def gene_save():
    "to fill the 'save' vector of values of the first city studied"
    for i in range (0,x):
        save[i] = mat[i,debut]
        #print("save",save)
        #print(ville)

        


def find_the_minimum_path_from(var):
    "find the minimum path from a city"
    global ville
    global somme_path
    global path
    global save
    global debut
    path[0]=debut
    #print("path : ",path)
    #print(ville)
    mini = 1000
    col=1000
    mat[:,var]=1001
    for i in range (0,x,1):
        #print("isso é i",i)
        if mini > mat[var][i] and mat[var][i]<900:
            mini = mat[var][i]
            col = i
            #print("mininum colonne : ",i,"avec ",mini)
    if col == 1000:
        #print("var = ",var)
        path[ville]=var 
        #print("test : ",save[var])
        somme_path=somme_path+save[var]
        #print("save",save[var])
        #print("somme path :",somme_path)
        #print("ville retour :",ville)
        return 0
    somme_path=somme_path + mat[var][col]
    #print("somme path pour la ville ",ville,":",somme_path)
    mat[var]=1002
    mat[:,col]=1001
    #print(mat)
    ville = ville + 1
    path[ville]= col   
    #print("path = ",path)
    find_the_minimum_path_from(col)
    exit
    #somme_path=somme_path + mat[var][col]
    #print("ville retour :",ville)



#find_the_minimum_path_from(debut)
#print(path," somme : ",somme_path)
                                                        
                                                        



def find_the_best():
    "do the 'best' camino for each city and keep the best one find"
    global debut
    global best_somme_path
    global somme_path
    global path
    global best_bath
    global ville
    for i in range (0,x):
        debut=i
        remise_mat()
        gene_save()
        somme_path = 0
        ville=0
        find_the_minimum_path_from(debut)
        #print("somme_path version ",i," est ",somme_path," avec ",path)
        if somme_path < best_somme_path:
            best_somme_path = somme_path
            for y in range (0,x):
                best_path[y]=path[y]
    #print("the best path is : ",best_path," with a cost of ",best_somme_path)#################
        
        



def colnum_string(n):
    "convert a number in letter, to be easier to read by a human"
    string = ""
    n=n+1
    while n > 0:
        n, remainder = divmod(n -1 , 26)
        string = chr(65 + remainder) + string
    return string

#print ("loooooool",colnum_string(0))




def transform_path(camino):
    "transform a path with number, in the same path with letter, to be read easier"
    camino2=[]
    for i in range (0,x):
        camino2.append(colnum_string(camino[i]))
    print(camino2)

#print((best_path))
    
    
#%%
    
#with a huge number of vertice    
    
#do the algorithm, and print the results
to_start(120) ##############################################################   modified here to change de number of vertices
gene_save() 
find_the_best()
print("\n\n\n")
print("with number of cities = ",x," the best path is : ",best_path," with a cost of ",best_somme_path)
print("or also : ")
transform_path(best_path) 

 
    
#%%  

    
#with a short number of vertice    

#do the algorithm, and print the results
to_start(7) ##############################################################   modified here to change de number of vertices
gene_save() 
find_the_best()
print("\n\n\n")
print("with number of cities = ",x," the best path is : ",best_path," with a cost of ",best_somme_path)
print("or also : ")
transform_path(best_path)




#%%


#this second part is to show the Brute force method, compared to the first one
print("\n\n\n\n\n\n#################################################\n")
print("                 Part 2")
print("\n#################################################\n")
      
      
#brute force

def nao_tem_dobro(cam):
    "check if a city is visited twice or not (return True if there is each city only one time)"
    for w in range (0,x):
        for v in range (w+1,x):
            #print(" temos :",cam[w]," et ",cam[v])
            if cam[w]==cam[v]:
                return False
    return True




#global variable needed
    
global costo_min_bf
global path_opti_bf




def init_bf():
    "initialisation for the brute force method"
    global costo_min_bf
    global path_opti_bf
    costo_min_bf=100000
    path_opti_bf=np.arange(x)*0
    #print("tenho isso : ",x)




def costo_cam(cami):
    "give the cost of a path betxeen different city"
    global costo_min_bf
    global path_opti_bf
    costo=0
    for u in range(0,x-1):
        abs=cami[u]
        ord=cami[u+1]
        costo=costo+mat2[abs][ord]
        #print("eu ;",mat2[abs][ord])
    abs=cami[x-1]
    ord=cami[0]
    costo=costo+mat2[abs][ord]
    #print("eu2 ;",mat2[abs][ord])
    if costo<costo_min_bf:
        costo_min_bf=costo
        #print("costo min changed : ",costo)
        for v in range (0,x):
            path_opti_bf[v]=cami[v]
    return costo

#print("this is costo :" ,costo_cam([0,1,3,2]))
#mat2[ligne][colonne]



def programme_bf():
    "crate all path possible"
    "plot the best path possible and print the result, "
    "it also compare it (by printing) with the result of the heuristic algoritm"
    global x
    tudo=[]
    for i in range(0,x):
        tudo.append(i)
    #print("tudo : ",tudo)
    d = {'A': tudo}
    #print(d)
    p = {}
    for k in d.keys():
        p[k] = [i for i in itertools.permutations(d[k])]
    
    #print(p)
    length_key = len(p['A'])
    #print("isso ? : ",length_key)
    #for i in range(0,length_key):
        #print (p.get("A")[i])
    for i in range(0,length_key):
        costo_cam(p.get("A")[i])
    print("\n\n\n\n\n\n\n\n\n\nCom o numero de cidade = ",x,"\n")
    print(" o camino minimo ta : ",path_opti_bf," o se quiser : ")
    transform_path(path_opti_bf)
    print(" com um costo de : ",costo_min_bf)
    print("\n e temos, com a heuristic, o melhor camino que ta : ",best_path," que é tb : ")
    transform_path(best_path)
    print(" com um costo de ",best_somme_path)


#let's run this aogrithm
init_bf()
programme_bf()




#%%


# this third part is to see the time needed by the Brute Force algorithm to solve the TSP problem by finding the cheepest path
# and we will plot these reults
print("\n\n\n\n\n\n#################################################\n")
print("                 Part 3")
print("\n#################################################\n")

      

def programme_bf2():
    "create all path possible"
    global x
    tudo=[]
    for i in range(0,x):
        tudo.append(i)
    #print("tudo : ",tudo)
    d = {'A': tudo}
    #print(d)
    p = {}
    for k in d.keys():
        p[k] = [i for i in itertools.permutations(d[k])]
    length_key = len(p['A'])
    for i in range(0,length_key):
        costo_cam(p.get("A")[i])




global timed
def evaluate_time_bf():
    "plot the time needed by the Brut Force Algorithm to solve the TSP problem, depending the number of vertices"
    "do not run with more than 10 vertices, or it will crash"
    global x
    global timed
    ma=10########################################################    "here limites of vertices possible is 10
    timed=np.arange(ma)*0
    for i in range(2,ma):
        time1 = time.time()
        to_start(i)
        gene_save()
        init_bf()     
        programme_bf2()
        time2 = time.time()
        tim=(time2-time1)*1000.0
        #print("timeeeeeeeee: ",tim)
        timed[i]=tim
    print("\n\n\n\n\ndifferents time depending numbers of vertices, by Brute Fore : ",timed,"\n\n\n\n")
    plt.plot(timed)
    plt.title("time for Brute force")
    plt.xlabel("vertices")
    plt.ylabel("time in ms")
    plt.show()
    plt.close()
            
        
# Let's run the algoritm
evaluate_time_bf()



#%%

# This part is for the Grafic plotting of the Heuristic Part
print("\n\n\n\n\n\n#################################################\n")
print("                 Part 4")
print("\n#################################################\n")

      
      
global timed2
def evaluate_time_heu():
    "estimatate the time needed by the heuristics, depending of the number of vertices and also plot the graphics"
    global x
    global timed2
    ma=60####################################################################################### aqui limitation 
    timed2=np.arange(ma)*0
    for i in range(2,ma):
        time1 = time.time()
        to_start(i)
        gene_save()
        #init_bf()     
        find_the_best()
        time2 = time.time()
        tim2=(time2-time1)*1000.0
        #print("timeeeeeeeee: ",tim)
        timed2[i]=tim2
    print("\n\n\n\n\n differents time depending numbers of vertices, by Heuristic : ",timed2,"\n\n\n")
    plt.plot(timed2)
    plt.title("time for heuri")
    plt.xlabel("vertices")
    plt.ylabel("time in ms")
    plt.show()
    plt.close()
            


#let's run the algorithm
evaluate_time_heu()


#%%This last part (bonus) is here to compare both methods
print("\n\n\n\n\n#################################################\n")
print("                 Conclusion")
print("\n#################################################\n")


# Plotting both graphs on the same sheet
def final():
    print("\n\n\n",timed,"\n",timed2,"\n\n\n")
    plt.plot(timed)
    plt.plot(timed2)
    plt.title("comparaison of both method")
    plt.xlabel("vertices")
    plt.ylabel("time in ms")
    plt.show()
    plt.close()
    
#let's show the comparaison of the two methods
final()




print("\n\n\n")

# Plotting both graphs on the same sheet
def final2():
    timed3=[0, 3, 3, 3.5 ,4.5 , 6, 14, 25, 30, 120, 300, 1925, 4445, 7196, 9867, 11187] # imported manually
    print("\n\n\n",timed,"\n",timed2,"\n",timed3,"\n\n\n")
    plt.plot(timed)
    plt.plot(timed2)
    plt.plot(timed3)
    plt.title("comparaison of 'Brute Force', 'Branch and Bound' and 'Heuristic' method")
    plt.xlabel("vertices")
    plt.ylabel("time in ms")
    plt.show()
    plt.close()
    
#let's show the comparaison of the two methods
final2()




























    