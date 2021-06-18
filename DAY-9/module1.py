#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import emoji

import pyttsx3

import camelcase



def call(s):
    s=s
    if s != s.lower() and s != s.upper() and "_" not in s:
        
        return emoji.emojize("It is in camel Case :thumbsup:", use_aliases=True)
    
    else:
        p=pyttsx3.init()
        y=camelcase.CamelCase()
        z=y.hump(s)
        p.say("Successfully converted string into camel Case")
        p.runAndWait()

