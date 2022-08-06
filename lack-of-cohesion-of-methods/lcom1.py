# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 02:19:07 2018

@author: Spikee
"""

import re
import copy
import nltk

read_lines=list()
lines=list()
methods=0
noOfVariables=0


Variables=list()

tokens=list()

graph=[]


def parseData():
    for line in file.readlines():
        read_lines.append(line)
    
    file.close()
    
    removeSpace()
    
    
# preprocessing of the file to remove extra spaces
def removeSpace():
    lines.clear() #To clear the initial Lines list
    for line in read_lines:
        if len(line)==0: 
            continue
        lines.append(re.sub(r'\s+',' ',line).strip()) # using Regular expression to replace all the Whitespaces with a single space
    
    CheckLines() # After Preprocessing Calling the Check

def CheckLines():
    i=0
    global methods
    size=len(lines)
    while i<size :
        #print(lines[i])
        if lines[i].endswith("{"):
            if lines[i].endswith("){"):
             
                methods+=1
                i+=1
                
                temp=" "
                
                while lines[i].endswith("}")==False:
                    temp+=lines[i]
                    i+=1
                
                tokens=nltk.word_tokenize(temp)
                
                print("Tokens",tokens)
                temp1=list()
                
                for j in range(len(Variables)):
                    #print(Variables)
                    if Variables[j] in tokens:
                        temp1.append(1)
                    else:
                        temp1.append(0)
                
                graph.append(temp1)
                print(graph)
                
            else:
                
                tokens=nltk.word_tokenize(lines[i])
                #print(tokens)
                for token in tokens:
                    #print(token)
                    if token is 'class':
                        i+=1
                        
                    
        elif lines[i].endswith(";"):
            tokens=lines[i].split(" ")
            
            q=1
            
            while q<len(tokens):
                if tokens[q] is ",":
                    q+=1
                elif tokens[q] is '=':
                    q+=2
                elif tokens[q] is ';':
                    break
                else:
                    Variables.append(tokens[q])
                    q+=1
        i+=1
        
            
        
    
    print("\nNumber of variables",len(Variables))
    print("Methods",methods)
    
    
    graph_f =[[0 for x in range(len(graph[1]))]for x in range(len(graph))]
    
    for i in range(len(graph)):
        for j in range(len(graph[1])):
            graph_f[i][j]=graph[i][j]
    
    graph_f=copy.deepcopy(graph)  
    
    cal(graph_f)

def cal(graph_f):
    graph_transpose=transpose(graph_f)
    multi=multiply(graph_f,graph_transpose)
    n=methods
    score=(n*(n-1))//2
        
    for i in range(len(multi)):
        for j in range(i+1,len(multi[1])):
            
            if multi[i][j] is not 0:
                score-=1
                
    print("LCOM1= ",score)

def transpose(graph_f):
    
    trans=[[0 for x in range(len(graph_f))]for x in range(len(graph_f[1]))]
    
    for i in range(len(graph_f[1])):
        for j in range (len(graph_f)):        
            trans[i][j]=graph_f[j][i]
    
    return trans

def multiply(graph_f,graph_transpose):
    
    c=[[0 for x in range(len(graph_f))]for x in range(len(graph_transpose[0]))]
        
    for i in range(len(c)):
        for j in range(len(c[0])):
            c[i][j]=0
            for k in range(len(graph_transpose)):
                c[i][j]+=graph_f[i][k]*graph_transpose[k][i]
    
    return c


file=open("test_lcom.java","r")
parseData()

