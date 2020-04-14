# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:37:38 2020

@author: kazum
"""

class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        self.items == []
        
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last = len(self.items)-1
        return(self.items(last))
        
    def size(self):
        return len(self.items)
    
stack = Stack()
for c in "yesterday":
    stack.push(c)
reverse = ""    
while stack.size():
    reverse += stack.pop()
    
print(reverse)

reverse = ""
list = [1,2,3,4,5]
for c in list:
    stack.push(c)
i = 0
while stack.size():
    list[i] = stack.pop()
    i += 1
print(list)