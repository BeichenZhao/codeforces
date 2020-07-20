# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:07:51 2020

@author: Beichen Zhao
"""
def f(s,n):
    ss='abacaba'
    ans=0
    for i in range(n-7+1):
        flag=True
        for j in range(7):
            if s[i+j]!=ss[j]:
                flag=False
                break
        if flag==True:
            ans+=1
    return ans




t=int(input())
for case in range(t):
    n=int(input())
    s=input()
    ss='abacaba'
    index=[]
    for i in range(n-7+1):
        flag=True
        for j in range(7):
            if s[i+j]!=ss[j] and s[i+j]!='?':
                flag=False
                break
        if flag==True:
            index.append(i)
    flag=False
    for i in index:
        st=s[:i]+ss+s[i+7:]
        while '?' in st:
            st=st.replace('?', 'z')
        if f(st,n)==1:
            print('Yes')
            print(st)
            flag=True
            break
    if flag==False:
        print('No')
        
        
    