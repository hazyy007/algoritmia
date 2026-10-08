import math
import numpy as np
def init_cd(n: int)-> np.ndarray: 
    lst = n*[-1]
    np1 = np.array(lst)
    return np1
def find(ind: int, p_cd: np.ndarray)-> int:
    while p_cd[ind]>=0:
        ind= p_cd[ind]
    return ind   
def union(rep_1: int, rep_2: int, p_cd: np.ndarray)-> int:
    a=find(rep_1,p_cd)
    b=find(rep_2,p_cd)
    """if a==b:
        return None"""
    if p_cd[a]<p_cd[b]:
        p_cd[b]=a
        return a
    elif p_cd[a]>p_cd[b]:
            p_cd[a]=b
            return b
    else:
        p_cd[b]=a
        p_cd[a]-=1
        return a
def cd_2_dict(p_cd)-> dict:
    resultado={}
    for i in range(len(p_cd)):
        raiz = i
        while p_cd[raiz]>=0:
            raiz=p_cd[raiz]
        if raiz not in resultado:
            resultado[raiz]=[]
        resultado[raiz].append(i)
    return resultado        
def ccs(n:int,l:list)->dict:
    cd=init_cd(n)
    for u,v in l:
        if find(u,cd)!=find(v,cd):
            union(u,v,cd)
    res=cd_2_dict(cd)
    return res