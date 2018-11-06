import math


#EXERCICE 1


#params : valeur de l'angle, ordre approx
def approx_sinus(angle, n):    
    res = angle
    for i in range(1,n+1):
        res = res + pow(-1, i)*pow(angle, 2*i+1) / math.factorial(2*i+1)
    return res


#recherche de l'ordre n donnant une erreur fixée
def error_order(angle, n, err):
    exact_sin  = math.sin(angle)
    approx_sin = approx_sinus(angle, 0)
    delta      = exact_sin - approx_sin
    
    while(abs(delta) > err):
        n += 1
        approx_sin = approx_sinus(angle, n)
        delta = exact_sin - approx_sin

    return n


###################################################################################

#EXERCICE 2


#conversion de base 8 à base 10
#params : nombre en base 8
def conv_oct_dec(n8):
    str_n8 = str(n8)
    res = 0
    
    for i in range(0, len(str_n8)):
        res += int(str_n8[i])*8**i

    return res

####################################################################################

#EXERCICE 3

#maximum dans une liste
def max_list(_list):
    res = 0;
    pos = 0;
    for i in range(0, len(_list)):
        if(_list[i] > res):
            res = _list[i]
            pos = i

    return [res, i]


#tri par selection
def sort_list(_list):
    tri = max_list(_list)
    



















