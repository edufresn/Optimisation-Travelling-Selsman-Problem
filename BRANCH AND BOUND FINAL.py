# -*- coding: utf-8 -*-
"""
Projecto Final em Otimização de Grafos 

O problemo do TSP

Erwan Dufresne 

Novembro 2018
"""

# all global variable and impot needed

import numpy as np
import itertools
import matplotlib.pyplot as plt
import time 
from random import randint

global x
global y
global mat_init
global mat_original
global mat_red
#global path
global best_path
global best_somme_path
global somme_path
global debut



#For time calculating
timed3=np.arange(20)*0
time1 = time.time()


def remise_mat():
    "create a save matrix from the initial random creating city localisation"
    global mat_original
    for i in range (0,x,1):
        for y in range (0,x,1):
            mat_original[i][y]=mat_init[i][y]
    #print(mat_original)


def init_bb(valeur):
    "initialisation needed for the beginning"
    global x
    global y
    global mat_init
    global mat_original
    #global path
    global best_path
    global best_somme_path
    global somme_path
    global debut
    global mat_red

    #number of cities
    x= valeur
    #max value of the cost of a single trip between two cities
    y=15 
    #matriz identidad com 1000 (infinity)
    mat_init=np.eye(x,x)*1000
    best_somme_path=100000    
    #generatção matriz aleatoiria com distancia entre 1 e y
    for i in range (0,x,1):
        for i2 in range (i,x,1):
            if i!=i2:
                mat_init[i][i2]=randint(1,y)
                mat_init[i2][i]=mat_init[i][i2]          
    #print (mat2)
    mat_original=np.eye(x,x)*0
    mat_red=np.eye(x,x)*0
    #cost camino
    somme_path = 0
    debut = 0  
    remise_mat()



#do the initialisation
init_bb(5)                          # change here the value of the number of cities si needed


def somme_ligne(lig,ma):
    "adition of number of a line"
    som_ligne=0
    for i in range (0,x,1):
        if (ma[lig][i]) < 200:
            som_ligne = som_ligne + ma[lig][i]
    return som_ligne
    
    
def somme_column(col,ma):
    "adition of number of a column"
    som_col=0
    for i in range (0,x,1):
        if (ma[i][col]) < 200:
            som_col = som_col + ma[i][col]
    return som_col
        
#print(somme_column(0,mat_init))
#print(somme_ligne(1,mat_original))



def brouille_col(col,ma):
    "give the value 'infinity' to a column"
    for i in range (0,x,1):
        ma[i][col]=1000
    
    
def brouille_lig(lig,ma):
    "give the value 'infinity' to a line"
    for i in range (0,x,1):
        ma[lig][i]=1000
        
        
def brouille_valeur(lig,col,ma):
    "give the value 'infinity' to a value of the matrix in parameter"
    ma[lig][col]=1000


#brouille_col(0,mat_init)
#brouille_lig(1,mat_original)
#brouille_valeur(0,0,mat_init)
    
    
    
    
def find_mini_lig(lig,ma):
    "find the minimum of a line of a matrix"
    mini=1002
    for i in range(0,x):
        if ma[lig][i]<mini:
            mini=ma[lig][i]
    return mini



def find_mini_col(col,ma):
    "find the minimum of a column of a matrix"
    mini=1002
    for i in range(0,x):
        if ma[i][col]<mini:
            mini=ma[i][col]
    return mini


#print(find_mini_col(0,mat_init))
#print(find_mini_lig(1,mat_original))




def substract_col(sub,col,ma):
    "soustract a value on each value of a column of the matrix"
    for i in range (0,x):
        ma[i][col]=(ma[i][col])-sub


def substract_lig(sub,lig,ma):
    "soustract a value on each value of a line of the matrix"
    for i in range (0,x):
        ma[lig][i]=(ma[lig][i])-sub


#substract_lig(5,0,mat_init)
#substract_col(20,1,mat_original)



def reducing_matrix(ma):
    "apply the reduction needed to do the Branch and Bound Algorithm"
    global mat_red
    global mat_original
    tudo=0
    for i in range (0,x,1):
        for y in range (0,x,1):
            mat_red[i][y]=ma[i][y]
    for i in range (0,x):
        aux=find_mini_lig(i,mat_red)
        if aux!=0 and aux<200:
            substract_lig(aux,i,mat_red)
            tudo=tudo+aux
    for u in range (0,x):
        aux2=find_mini_col(u,mat_red)
        if aux2!=0 and aux2<200:
            substract_col(aux2,u,mat_red)
            tudo=tudo+aux2
    return tudo   
      
#print(reducing_matrix(mat_init))      




#Creation of the dictionary
global dic
dic={}

def dict_init():
    "initialisation of the dictionnary to save data"
    global dic
    dic['0']=[(reducing_matrix(mat_init))]  # cost initial
    dic['0'].append(mat_init)               # the reduced matrix
    dic['0'].append('free')                 # 'free' if the nodes haven't been explored yet, 'done' if already explored

#print(dic)
    



#do the initialisation of the dico
dict_init()


  


def find_minimum_from_dict():
    "find the minimum reduction cost of the dictionnary"
    my_min=99999
    my_key=''
    for key in dic:
        if dic[key]!=[] and dic[key][2]=='free':
            if dic[key][0]<my_min :
                my_min=dic[key][0]
                my_key=key
    #print("my min is :",my_min," with a key of ",my_key)
    return my_key

#find_minimum_from_dict()




def brouille_all(liste_de_city,param,mat):
    "give infinity value to all the value wich need it"
    brouille_valeur(param,0,mat)
    for i in liste_de_city:
        brouille_lig(int(i),mat)
        brouille_valeur(int(i),0,mat)
    brouille_col(param,mat)
    brouille_valeur(param,0,mat)
        
#print(mat_red)
#brouille_all(1,mat_red)




global list_city

def BnB():
    "Branch and Bound Algorithm"
    global best_path
    global best_somme_path
    global mat_red
    global mat_original
    global list_city
    key_mini_dict=find_minimum_from_dict()
    list_city=key_mini_dict.split(' ')
    costo_mat_antes=dic[key_mini_dict][0]
    rest_to_visit=[]
    if len(list_city)==x:
        best_path=key_mini_dict
        best_somme_path=dic[key_mini_dict][0]
        return 99
    for i in range (0,x):
        if str(i) in list_city:
            useless=1
            #print("here :",i)
        else:
            #print("not here :",i)
            rest_to_visit.append(i)
    for v in range(0,len(rest_to_visit)):
        for i in range (0,x,1):
            for y in range (0,x,1):
                mat_original[i][y]=(dic[key_mini_dict][1])[i][y]
        brouille_all(list_city,rest_to_visit[v],mat_original)
        costo_mat_agora=reducing_matrix(mat_original)
        last_elem_of_path=int(list_city[int((len(list_city)-1))])
        valeur_cc=(dic[key_mini_dict][1])[last_elem_of_path][rest_to_visit[v]]
        total_costo=0
        total_costo = costo_mat_agora + valeur_cc + costo_mat_antes
        path_som=key_mini_dict+' '+str(rest_to_visit[v])
        dic[path_som]=[]
        dic[path_som].append(total_costo)
        mat_or=np.eye(x,x)*0
        for i in range (0,x,1):
            for y in range (0,x,1):
                mat_or[i][y]=mat_red[i][y]
        dic[path_som].append(mat_or)
        dic[path_som].append('free')
    dic[key_mini_dict][2]='done'
    BnB()
    exit




global cost_of_the_final_path

def costo_cam(cami):
    "give the cost of a path between different city"
    global cost_of_the_final_path
    costo=0
    for u in range(0,x-1):
        abs=int(cami[u])
        ord=int(cami[u+1])
        costo=costo+mat_init[abs][ord]
        #print("eu ;",mat2[abs][ord])
    abs=int(cami[x-1])
    ord=int(cami[0])
    costo=costo+mat_init[abs][ord]
    cost_of_the_final_path=costo
    return costo




#Let's run the Algorithm

BnB()
print("\n\n\nwith a total cost of ",costo_cam(list_city))
print("we got the best path possible :",best_path," with a reduction cost of ",best_somme_path,"\n")



#For time calculating
time2 = time.time()
tim3=(time2-time1)*1000.0
print("time : ",tim3)

#list of time (manually done)
timed3=[0, 3, 3, 3.5 ,4.5 , 6, 14, 25, 30, 120, 300, 1925, 4445, 7196, 9867, 11187]


#ploting the resultas
print("\n\n\n\n\n differents time depending numbers of vertices, by BnB : ",timed3,"\n\n\n")
plt.plot(timed3)
plt.title("time for BnB")
plt.xlabel("vertices")
plt.ylabel("time in ms")
plt.show()
plt.close()













   



