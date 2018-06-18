#!/usr/bin/python
import operator
TOM = {'Q':['POL','ESP','FRA','AUT','ALL','ANG','BEL','ITA'],
       'S':['BEL','ITA','FRA','ESP'],'F':['ESP','FRA'],'p':44,'t':0}
CED = {'Q':['POL','ESP','FRA','AUT','ALL','ANG','BEL','ITA'],
       'S':['ANG','ALL','FRA','ESP'],'F':['ALL','FRA'],'p':44,'t':0}
JOA = {'Q':['POL','ESP','FRA','AUT','ALL','ANG','BEL','POR'],
       'S':['ALL','ANG','FRA','ESP'],'F':['ESP','FRA'],'p':42,'t':0}
LAN = {'Q':['POL','CRO','ITA','ALL','ESP','FRA','POR','ANG'],
       'S':['CRO','ANG','ESP','FRA'],'F':['ESP','ANG'],'p':44,'t':0}
ROD = {'Q':['POL','ITA','ALL','ESP','FRA','ANG','AUT','BEL'],
       'S':['ALL','ANG','BEL','FRA'],'F':['FRA','ANG'],'p':41,'t':0}
H=[['SUI','POL'],['CRO','POR'],['PDG','IRN'],['HON','BEL'],['ALL','SLO'],['ITA','ESP'],['FRA','IRL'],['ANG','ISL']]

TOMp = {}
JOAp = {}
LANp = {}
RODp = {}
CEDp = {}

SC = []
DC = []
FC = []
i = 0
PTS = {'TOM':0,'CED':0,'JOA':0,'LAN':0, 'ROD':0}
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
            PTS['TOM'] = TOM['p']+len(set(ddS).intersection(TOM['Q']))
            PTS['CED'] = CED['p']+len(set(ddS).intersection(CED['Q']))
            PTS['JOA'] = JOA['p']+len(set(ddS).intersection(JOA['Q']))
            PTS['LAN'] = LAN['p']+len(set(ddS).intersection(LAN['Q']))
            PTS['TOM'] += len(set(ddD).intersection(TOM['S']))
            PTS['CED'] += len(set(ddD).intersection(CED['S']))
            PTS['JOA'] += len(set(ddD).intersection(JOA['S']))
            PTS['LAN'] += len(set(ddD).intersection(LAN['S']))
            PTS['TOM'] += len(set(ddF).intersection(TOM['F']))
            PTS['CED'] += len(set(ddF).intersection(CED['F']))
            PTS['JOA'] += len(set(ddF).intersection(JOA['F']))
            PTS['LAN'] += len(set(ddF).intersection(LAN['F']))
            PTS['ROD'] = ROD['p']+len(set(ddS).intersection(ROD['Q']))
            PTS['ROD'] += len(set(ddD).intersection(ROD['S']))
            PTS['ROD'] += len(set(ddF).intersection(ROD['F']))
            sorted_PTS = sorted(PTS.items(),key=operator.itemgetter(1))
            if PTS['LAN'] in LANp:
                LANp[PTS['LAN']] += 1
            else:
                LANp[PTS['LAN']] = 1
            if PTS['TOM'] in TOMp:
                TOMp[PTS['TOM']] += 1
            else:
                TOMp[PTS['TOM']] = 1
            if PTS['JOA'] in JOAp:
                JOAp[PTS['JOA']] += 1
            else:
                JOAp[PTS['JOA']] = 1
            if PTS['ROD'] in RODp:
                RODp[PTS['ROD']] += 1
            else:
                RODp[PTS['ROD']] = 1
            if PTS['CED'] in CEDp:
                CEDp[PTS['CED']] += 1
            else:
                CEDp[PTS['CED']] = 1
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
xn = ["TOM","LAN","CED","JOA","ROD"]
x = [0,1,2,3,4,5]
x1 = [0.5,1.5,2.5,3.5,4.5,5]
from pylab import *
y = [41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57]
zz = []
for key in y:
    z = []
    if key in TOMp:
        z = z+[TOMp[key]/fullproba]
    else:
        z = z+ [0]
    if key in LANp:
        z = z+[LANp[key]/fullproba]
    else:
        z = z+ [0]
    if key in CEDp:
        z = z+[CEDp[key]/fullproba]
    else:
        z = z+ [0]
    if key in JOAp:
        z = z+[JOAp[key]/fullproba]
    else:
        z = z+ [0]
    if key in RODp:
        z = z+[RODp[key]/fullproba]
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
