#!/usr/bin/python2
import operator
CED = {'Q':['BRL','ANG','ESP','URG','FRA','GER','BEL','ARG'],'S':['GER','BRL','ARG','ESP'],'p':53,'t':0}
TOM = {'Q':['BRL','ANG','NED','URG','FRA','GER','BEL','ARG'],'S':['GER','URG','ARG','BRL'],'p':52,'t':0}
JES = {'Q':['BRL','URG','ESP','ANG','FRA','GER','ARG','POR'],'S':['GER','ESP','ARG','POR'],'p':47,'t':0}
BAR = {'Q':['ESP','ANG','NED','ITA','FRA','GER','BEL','ARG'],'S':['ESP','NED','GER','BEL'],'p':47,'t':0}
JUL = {'Q':['BRL','ESP','FRA','ITA','URG','GER','BEL','ARG'],'S':['BRL','ESP','GER','BEL'],'p':47,'t':0}
SHA = {'Q':['BRL','COL','FRA','GER','ESP','ITA','BEL','ARG'],'S':['GER','ESP','ARG','BRL'],'p':46,'t':0}
#GIG = {'Q':['BRL','URG','ESP','ITA','GER','ARG','BEL','FRA'],'S':['GER','ESP','BEL','BRL'],'p':44,'t':0}
GIG = {'Q':['BRL','ITA','FRA','GER','ESP','URG','ARG','POR'],'S':['GER','ESP','ARG','BRL'],'p':44,'t':0}
H=[['BRL','CHI'],['COL','URG'],['FRA','NIG'],['GER','ALG'],['NED','MEX'],['CRC','GRE'],['ARG','SUI'],['BEL','USA']]
K = 0
K1 = 0
KK = 0
i = 0
maxCED = 0
minGIG = 99
maxGIG = 0
PTS = {'TOM':0,'CED':0,'JES':0,'BAR':0,'JUL':0,'SHA':0}
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
        PTS['CED'] = CED['p']+len(set(ddS).intersection(CED['Q']))
        PTS['TOM'] = TOM['p']+len(set(ddS).intersection(TOM['Q']))
        PTS['JES'] = JES['p']+len(set(ddS).intersection(JES['Q']))
        PTS['BAR'] = BAR['p']+len(set(ddS).intersection(BAR['Q']))
        PTS['JUL'] = JUL['p']+len(set(ddS).intersection(JUL['Q']))
        PTS['SHA'] = SHA['p']+len(set(ddS).intersection(SHA['Q']))
        PTS['CED'] += len(set(ddD).intersection(CED['S']))
        PTS['TOM'] += len(set(ddD).intersection(TOM['S']))
        PTS['JES'] += len(set(ddD).intersection(JES['S']))
        PTS['BAR'] += len(set(ddD).intersection(BAR['S']))
        PTS['JUL'] += len(set(ddD).intersection(JUL['S']))
        PTS['SHA'] += len(set(ddD).intersection(SHA['S']))
        sorted_PTS = sorted(PTS.iteritems(),key=operator.itemgetter(1))
        if PTS['CED']>maxCED:
            maxCED = PTS['CED']
        KK+=1
        fact = 40.96
#        fact -=25.6
        if sorted_PTS[len(sorted_PTS)-1][1]>sorted_PTS[len(sorted_PTS)-2][1]:
            key =  sorted_PTS[len(sorted_PTS)-1][0]
            K+=1
            if key in prob:
                prob[key]+=1./fact
            else:
                prob[key]=1./fact
        if sorted_PTS[len(sorted_PTS)-1][1]==sorted_PTS[len(sorted_PTS)-2][1] and sorted_PTS[len(sorted_PTS)-2][1]>sorted_PTS[len(sorted_PTS)-3][1]:
            K+=1
            key =  sorted_PTS[len(sorted_PTS)-1][0]+"+"+sorted_PTS[len(sorted_PTS)-2][0]
            if key in prob:
                prob[key]+=1./fact
            else:
                prob[key]=1./fact
        if sorted_PTS[len(sorted_PTS)-1][1]==sorted_PTS[len(sorted_PTS)-2][1] and sorted_PTS[len(sorted_PTS)-2][1]==sorted_PTS[len(sorted_PTS)-3][1] and sorted_PTS[len(sorted_PTS)-3][1]>sorted_PTS[len(sorted_PTS)-4][1]:
            K+=1
            key =  sorted_PTS[len(sorted_PTS)-1][0]+"+"+sorted_PTS[len(sorted_PTS)-2][0]+"+"+sorted_PTS[len(sorted_PTS)-3][0]
            if key in prob:
                prob[key]+=1./fact
            else:
                prob[key]=1./fact




sorted_prob = sorted(prob.iteritems(),key=operator.itemgetter(1),reverse=True)
print sorted_prob
print K,KK, maxCED, minGIG, maxGIG
