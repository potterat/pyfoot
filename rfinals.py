#!/usr/bin/python2
import operator
FRE = {'Q':['BRL','ANG','ESP','CIV','NIG','GER','ARG','POR'],'S':['GER','BRL','ARG','ESP'],'p':29,'t':0}
ROD = {'Q':['BRL','ANG','ESP','URG','SUI','GER','BEL','FRA'],'S':['ANG','URG','SUI','BEL'],'p':34,'t':0}
RAH = {'Q':['BRL','ITA','ESP','ANG','FRA','GER','ARG','POR'],'S':['BRL','ESP','ARG','POR'],'p':33,'t':0}
PAO = {'Q':['BRL','ITA','NED','URG','BOS','GER','POR','ARG'],'S':['ITA','BOS','URG','ARG'],'p':34,'t':0}
H=[['BRL','CHI'],['COL','URG'],['FRA','NIG'],['GER','ALG'],['NED','MEX'],['CRC','GRE'],['ARG','SUI'],['BEL','USA']]
K = 0
K1 = 0
KK = 0
i = 0
PTS = {'FRE':0,'ROD':0,'RAH':0,'PAO':0}
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
        PTS['FRE'] = FRE['p']+len(set(ddS).intersection(FRE['Q']))
        PTS['ROD'] = ROD['p']+len(set(ddS).intersection(ROD['Q']))
        PTS['RAH'] = RAH['p']+len(set(ddS).intersection(RAH['Q']))
        PTS['PAO'] = PAO['p']+len(set(ddS).intersection(PAO['Q']))
        PTS['FRE'] += len(set(ddD).intersection(FRE['S']))
        PTS['ROD'] += len(set(ddD).intersection(ROD['S']))
        PTS['RAH'] += len(set(ddD).intersection(RAH['S']))
        PTS['PAO'] += len(set(ddD).intersection(PAO['S']))
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
