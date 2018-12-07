
"""
Created on Mon Nov 24 13:16:00 2018

@author: Spikee
"""

import re
from pythonds.basic.stack import Stack

read_lines=list()
lines=list()

stack=Stack()

num=Stack()
breakFlags=Stack()
continueFlags=Stack()
ifFlag=Stack()



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
        lines.append(re.sub(r'\s+',' ',line).strip())
    
    CheckLines()
              
def CheckLines():
    line_num=0
    endif=0
    endelse=0
    size=len(lines)
    matrix=[[0 for x in range(size)]for x in range(size)]

    while (line_num<size):
        if "#" in lines[line_num]:
            matrix[line_num][line_num+1]=1
            
        elif "if" in lines[line_num]:
            matrix[line_num][line_num+1]=1
            stack.push('if')
            num.push(line_num)
            ifFlag.push(line_num)
        
        elif 'else if' in lines[line_num]:
            matrix[line_num][line_num+1]=1
            stack.push('else if')
            num.push(line_num)
            ifFlag.push(line_num)
        
        elif "else" in lines[line_num]:
            matrix[line_num][line_num+1]=1
            stack.push('else')
            num.push(line_num)
        
        elif "while" in lines[line_num]:
            matrix[line_num][line_num+1]=1
            stack.push('while')
            num.push(line_num)
        
        elif "do" in lines[line_num]:
            matrix[line_num][line_num+1]=1
            stack.push('do')
            num.push(line_num)
            
        elif "for" in lines[line_num]:
            matrix[line_num][line_num+1]=1
            stack.push('for')
            num.push(line_num)
        
        elif "switch" in lines[line_num]:
            matrix[line_num][line_num+1]=1
            stack.push('switch')
            num.push(line_num)
            
        elif "case" in lines[line_num]:
            matrix[line_num][line_num+1]=1
            matrix[num.peek()][line_num]=1
        
        elif "default " in lines[line_num] or 'default:' in lines[line_num] :
            matrix[line_num][line_num+1]=1
            matrix[num.peek()][line_num]=1
        
        elif "break" in lines[line_num]:
            breakFlags.push(line_num)
            
        elif "continue" in lines[line_num]:
            continueFlags.push(line_num)
        
        elif "{" in lines[line_num]:
            matrix[line_num][line_num+1]=1
            
            
        elif "}" in lines[line_num]:
            if line_num==size-1 :
                 break
            
            s=stack.peek()
             
            if breakFlags.isEmpty()== False:
                 if s is not 'if' and s is not 'else' and s is not 'else if':
                     matrix[breakFlags.pop()][num.peek()]=1
            
            if continueFlags.isEmpty()== False:
                 if s is not 'if' and s is not 'else' and s is not 'else if':
                     matrix[continueFlags.pop()][num.peek()]=1
            
            if stack.isEmpty()== False:
                if s is 'else':   
                    num.pop()
                    stack.pop()
               
                    
                else:
                    matrix[num.pop()][line_num+1]=1
                    stack.pop()
            
            if s=='if':
                endif=line_num
            
         
                
            if s=='else':
                endelse=line_num+1
                matrix[endif][endelse]=1
                matrix[line_num][line_num+1]=1
        
            
            #if '}while' and stack.peek() is 'do':
             #   matrix[line_num][num.pop()]=1
              #  stack.pop()
            
            
        elif ')' in lines[line_num]:
            matrix[line_num][line_num+1]=1
        
        elif ';' in lines[line_num]:
            matrix[line_num][line_num+1]=1
        
        line_num+=1
        
    printMatrix(matrix)
            
            
    
    
# To Print the Adjacency
def printMatrix(matrix):
    print("PRINTING...")
    i=1
    size=len(matrix)

    for k in range(1,size+1):
        print(k,end=" ")
    
    print()
        
    for row in matrix:
        out.write(str(row)+"\n")
    
        for j in row:
            print(j,end=" " )
        print(i)
        i+=1
        
    out.close()
   
file=open("test_while.c","r")

out=open("output_while.txt","w")

parseData()




