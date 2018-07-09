#!/usr/bin/python
import operator
GIG = {'Q':['URU','BEL','FRA','SPA','SWI','DEN','GER','COL'],
       'S':['BEL','DEN','FRA','GER'],'F':['GER','FRA'],'p':64,'t':0}
KAR = {'Q':['URU','PER','BRA','SEN','SPA','FRA','GER','BEL'],
       'S':['PER','BRA','FRA','GER'],'F':['GER','FRA'],'p':22,'t':0}
JOA = {'Q':['POR','BRA','FRA','ENG','ARG','GER','BEL','SPA'],
       'S':['ARG','ENG','FRA','GER'],'F':['ARG','FRA'],'p':58,'t':0}
JUL = {'Q':['URU','CRO','BRA','GER','SPA','FRA','COL','BEL'],
       'S':['URU','BRA','SPA','GER'],'F':['GER','BRA'],'p':57,'t':0}
#ROD = {'Q':['POL','ITA','ALL','ESP','FRA','ANG','AUT','BEL'],
#       'S':['ALL','ANG','BEL','FRA'],'F':['FRA','ANG'],'p':1,'t':0}
H=[['URU','POR'],['FRA','ARG'],['BRA','MEX'],['BEL','JAP'],
   ['SPA','RUS'],['CRO','DEN'],['SWE','SWI'],['COL','ENG']]

GIGp = {}
JOAp = {}
JULp = {}
RODp = {}
KARp = {}

SC = []
DC = []
FC = []
i = 0
PTS = {'GIG':0,'KAR':0,'JOA':0,'JUL':0}
prob = {}
tot = 0
while i <256:
    I = '{0:08b}'.format(i)
    i+=1
    ddS = [H[0][int(I[0])],H[1][int(I[1])], H[2][int(I[2])],H[3][int(I[3])], H[4][int(I[4])],H[5][int(I[5])], H[6][int(I[6])],H[7][int(I[7])]]
    S   =[[H[0][int(I[0])],H[1][int(I[1])]], [H[2][int(I[2])],H[3][int(I[3])]], [H[4][int(I[4])],H[5][int(I[5])]], [H[6][int(I[6])],H[7][int(I[7])]]]
    check = 0
    for win in SC:
        if win in ddS:
            check += 1
    if check != len(SC): continue
    ii=0
    while ii < 16:
        II = '{0:04b}'.format(ii)
        ii+=1
        ddD = [S[0][int(II[0])],S[1][int(II[1])], S[2][int(II[2])],S[3][int(II[3])]]
        check = 0
        for win in DC:
            if win in ddD:
                check += 1
        if check != len(DC): continue
        F =  [[S[0][int(II[0])],S[1][int(II[1])]], [S[2][int(II[2])],S[3][int(II[3])]]]
        iii = 0
        while iii < 4:
            tot+=1
            III = '{0:02b}'.format(iii)
            iii+=1
            ddF = [F[0][int(III[0])],F[1][int(III[1])]]
            check = 0
            for win in FC:
                if win in ddF:
                    check += 1
            if check != len(FC): continue
            PTS['GIG'] = GIG['p']+2*len(set(ddS).intersection(GIG['Q']))
            PTS['KAR'] = KAR['p']+2*len(set(ddS).intersection(KAR['Q']))
            PTS['JOA'] = JOA['p']+2*len(set(ddS).intersection(JOA['Q']))
            PTS['JUL'] = JUL['p']+2*len(set(ddS).intersection(JUL['Q']))
            PTS['GIG'] += 3*len(set(ddD).intersection(GIG['S']))
            PTS['KAR'] += 3*len(set(ddD).intersection(KAR['S']))
            PTS['JOA'] += 3*len(set(ddD).intersection(JOA['S']))
            PTS['JUL'] += 3*len(set(ddD).intersection(JUL['S']))
            PTS['GIG'] += 4*len(set(ddF).intersection(GIG['F']))
            PTS['KAR'] += 4*len(set(ddF).intersection(KAR['F']))
            PTS['JOA'] += 4*len(set(ddF).intersection(JOA['F']))
            PTS['JUL'] += 4*len(set(ddF).intersection(JUL['F']))
            sorted_PTS = sorted(PTS.items(),key=operator.itemgetter(1))
            if PTS['JUL'] in JULp:
                JULp[PTS['JUL']] += 1
            else:
                JULp[PTS['JUL']] = 1
            if PTS['GIG'] in GIGp:
                GIGp[PTS['GIG']] += 1
            else:
                GIGp[PTS['GIG']] = 1
            if PTS['JOA'] in JOAp:
                JOAp[PTS['JOA']] += 1
            else:
                JOAp[PTS['JOA']] = 1
            if PTS['KAR'] in KARp:
                KARp[PTS['KAR']] += 1
            else:
                KARp[PTS['KAR']] = 1
            if sorted_PTS[len(sorted_PTS)-1][1]>sorted_PTS[len(sorted_PTS)-2][1]:
                key =  sorted_PTS[len(sorted_PTS)-1][0]
                if key in prob:
                    prob[key]+=1
                else:
                    prob[key]=1
            if sorted_PTS[len(sorted_PTS)-1][1]==sorted_PTS[len(sorted_PTS)-2][1] and sorted_PTS[len(sorted_PTS)-2][1]>sorted_PTS[len(sorted_PTS)-3][1]:
                key =  sorted_PTS[len(sorted_PTS)-1][0]+"+"+sorted_PTS[len(sorted_PTS)-2][0]
                if key in prob:
                    prob[key]+=1
                else:
                    prob[key]=1
            if sorted_PTS[len(sorted_PTS)-1][1]==sorted_PTS[len(sorted_PTS)-2][1] and sorted_PTS[len(sorted_PTS)-2][1]==sorted_PTS[len(sorted_PTS)-3][1] and sorted_PTS[len(sorted_PTS)-3][1]>sorted_PTS[len(sorted_PTS)-4][1]:
                key =  sorted_PTS[len(sorted_PTS)-1][0]+"+"+sorted_PTS[len(sorted_PTS)-2][0]+"+"+sorted_PTS[len(sorted_PTS)-3][0]
                if key in prob:
                    prob[key]+=1
                else:
                    prob[key]=1
            if sorted_PTS[len(sorted_PTS)-1][1]==sorted_PTS[len(sorted_PTS)-2][1] and sorted_PTS[len(sorted_PTS)-2][1]==sorted_PTS[len(sorted_PTS)-3][1] and sorted_PTS[len(sorted_PTS)-3][1]==sorted_PTS[len(sorted_PTS)-4][1] and sorted_PTS[len(sorted_PTS)-4][1]>sorted_PTS[len(sorted_PTS)-5][1]:
                key =  sorted_PTS[len(sorted_PTS)-1][0]+"+"+sorted_PTS[len(sorted_PTS)-2][0]+"+"+sorted_PTS[len(sorted_PTS)-3][0]+"+"+sorted_PTS[len(sorted_PTS)-4][0]
                if key in prob:
                    prob[key]+=1
                else:
                    prob[key]=1




sorted_prob = sorted(prob.items(),key=operator.itemgetter(1),reverse=True)
fullproba = 0.
print (tot)
for tup in sorted_prob:
    fullproba += tup[1]

print ("with the following 1/8:")
print (H)
print ("number of possibilities", fullproba)
print ("winners probability:")
for tup in sorted_prob:
    if(len(tup[0])>12):
        print (tup[0], round(100*tup[1]/fullproba,2), "%")
    elif(len(tup[0])>8):
        print (tup[0], '\t', round(100*tup[1]/fullproba,2), "%")
    elif(len(tup[0])>3):
        print (tup[0], '\t', round(100*tup[1]/fullproba,2), "%")
    else:
        print (tup[0],'\t\t', round(100*tup[1]/fullproba,2), "%")

from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np

# normal distribution center at x=0 and y=5
xn = ["GIG","JUL","KAR","JOA"]
x = [0,1,2,3,4]
x1 = [0.5,1.5,2.5,3.5,4.5]
from pylab import *
y = [41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,
     58,59,60,61,62,63,64,65,66,67,68,69,70]
zz = []
for key in y:
    z = []
    if key in GIGp:
        z = z+[GIGp[key]/fullproba]
    else:
        z = z+ [0]
    if key in JULp:
        z = z+[JULp[key]/fullproba]
    else:
        z = z+ [0]
    if key in KARp:
        z = z+[KARp[key]/fullproba]
    else:
        z = z+ [0]
    if key in JOAp:
        z = z+[JOAp[key]/fullproba]
    else:
        z = z+ [0]
    zz = zz + [z]

X = np.array(x)
Y = np.array(y)
Z = np.array(zz)
set_cmap('viridis')

plt.pcolor(X,Y,Z)
plt.xticks(x1, xn)
plt.colorbar()
savefig("pts.png")
