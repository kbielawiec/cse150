'''
Created on Jan 11, 2016

@author: jonny

Jonathan McAlexander, jmmcalex@ucsd.edu
Katherine Bielawiec, kbielawi@ucsd.edu
'''

#Find if the initial input is a goal state
#Goal state if both rooms are clean (0) and vacuum is in a valid state (0 or 1)

import fileinput

CLEAN = 0
DIRTY = 1
NUMROOM = 1


for line in fileinput.input():
    params = line.replace(' ','').replace('\n', '').split(',') # Get rid of whitespace and create list of input

    for num in range (0,NUMROOM+2):                                  #cast all to ints
        params[num] = int(params[num])

    #print(params[0], params[1], params[2])
    # Check if all input is valid

    for num in params:
        # room number invalid
        if params[NUMROOM+1]>NUMROOM:
            print("invalid input")
            break
        # room dirty/clean invalid
        if ((params[0] !=0 and params[0] !=1) or (params[1] != 0 and params[1] != 1)):
            print ("invalid input")
            break
        #both rooms clean
        elif (params[0] == 0 and params[1] == 0):
            print ("True")
            break
        # at least one room dirty
        else:
            print ("False")
            break