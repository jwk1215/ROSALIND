#! /usr/bin/env python

txt = """
Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat
"""

splitted = txt.split('\n')
print(splitted)

for i in range(0,len(splitted),2):
    print(splitted[i])
    


