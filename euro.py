#!/usr/bin/python2
import operator
TOM = {'Q':['POL','ESP','FRA','AUT','ALL','ANG','BEL','ITA'],'S':['BEL','ITA','FRA','ESP'],'F':['ESP','FRA'],'p':42,'t':0}
CED = {'Q':['POL','ESP','FRA','AUT','ALL','ANG','BEL','ITA'],'S':['ANG','ALL','FRA','ESP'],'F':['ALL','FRA'],'p':41,'t':0}
JOA = {'Q':['POL','ESP','FRA','AUT','ALL','ANG','BEL','POR'],'S':['ALL','ANG','FRA','ESP'],'F':['ESP','FRA'],'p':41,'t':0}
LAN = {'Q':['POL','CRO','ITA','ALL','ESP','FRA','POR','ANG'],'S':['CRO','ANG','ESP','FRA'],'F':['ESP','ANG'],'p':41,'t':0}
H=[['SUI','POL'],['CRO','ISL'],['PDG','IRN'],['POR','ITA'],['ALL','SLO'],['BEL','ESP'],['FRA','IRL'],['ANG','HON']]
K = 0
K1 = 0
KK = 0
i = 0
PTS = {'TOM':0,'CED':0,'JOA':0,'LAN':0}
prob = {}
while i < 256:
    I = '{0:08b}'.format(i)
    i+=1
    ddS = [H[0][int(I[0])],H[1][int(I[1])], H[2][int(I[2])],H[3][int(I[3])], H[4][int(I[4])],H[5][int(I[5])], H[6][int(I[6])],H[7][int(I[7])]]
    S = [[H[0][int(I[0])],H[1][int(I[1])]], [H[2][int(I[2])],H[3][int(I[3])]], [H[4][int(I[4])],H[5][int(I[5])]], [H[6][int(I[6])],H[7][int(I[7])]]]
    ii=0
    while ii < 16:
        II = '{0:04b}'.format(ii)
        ii+=1
        ddD = [S[0][int(II[0])],S[1][int(II[1])], S[2][int(II[2])],S[3][int(II[3])]]
        PTS['TOM'] = TOM['p']+len(set(ddS).intersection(TOM['Q']))
        PTS['CED'] = CED['p']+len(set(ddS).intersection(CED['Q']))
        PTS['JOA'] = JOA['p']+len(set(ddS).intersection(JOA['Q']))
        PTS['LAN'] = LAN['p']+len(set(ddS).intersection(LAN['Q']))
        PTS['TOM'] += len(set(ddD).intersection(TOM['S']))
        PTS['CED'] += len(set(ddD).intersection(CED['S']))
        PTS['JOA'] += len(set(ddD).intersection(JOA['S']))
        PTS['LAN'] += len(set(ddD).intersection(LAN['S']))
        sorted_PTS = sorted(PTS.iteritems(),key=operator.itemgetter(1), reverse=True)
        KK+=1
        fact = 40.96
        #fact -=25.6
        if sorted_PTS[len(sorted_PTS)-1][1]<sorted_PTS[len(sorted_PTS)-2][1]:
            key =  sorted_PTS[len(sorted_PTS)-1][0]
            K+=1
            if key in prob:
                prob[key]+=1./fact
            else:
                prob[key]=1./fact
        if sorted_PTS[len(sorted_PTS)-1][1]==sorted_PTS[len(sorted_PTS)-2][1] and sorted_PTS[len(sorted_PTS)-2][1]<sorted_PTS[len(sorted_PTS)-3][1]:
            K+=1
            key =  sorted_PTS[len(sorted_PTS)-1][0]+"+"+sorted_PTS[len(sorted_PTS)-2][0]
            if key in prob:
                prob[key]+=1./fact
            else:
                prob[key]=1./fact
            print "magic"
            print ddS
            print ddD
        if sorted_PTS[len(sorted_PTS)-1][1]==sorted_PTS[len(sorted_PTS)-2][1] and sorted_PTS[len(sorted_PTS)-2][1]==sorted_PTS[len(sorted_PTS)-3][1] and sorted_PTS[len(sorted_PTS)-3][1]<sorted_PTS[len(sorted_PTS)-4][1]:
            K+=1
            key =  sorted_PTS[len(sorted_PTS)-1][0]+"+"+sorted_PTS[len(sorted_PTS)-2][0]+"+"+sorted_PTS[len(sorted_PTS)-3][0]
            if key in prob:
                prob[key]+=1./fact
            else:
                prob[key]=1./fact




sorted_prob = sorted(prob.iteritems(),key=operator.itemgetter(1),reverse=True)
print sorted_prob
