#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Function penambahan dan perkalian
def addition(*tup):
    result = 0
    for t in tup:
        result += t
    return result

def multiplication(*tup):
    result = 1
    for t in tup:
        result *= t
    return result

def division(*tup):
    [result, *sisa] = tup
    for t in sisa:
        result /= t
    return result

