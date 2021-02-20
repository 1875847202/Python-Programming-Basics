#!/usr/bin/env python
# coding: utf-8

# In[6]:


number = 1090
name = '张三'

def add(*args):
    if len(args)>1:
        sum = 0
        for i in args:
            sum += i
        return sum
    else:
        return 0

