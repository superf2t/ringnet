'''
Created on Dec 19, 2012

@author: Yutao
'''

def debug(out):
    try:
        print "[DEBUG]"+str(out)
    except Exception,e:
        print e
        