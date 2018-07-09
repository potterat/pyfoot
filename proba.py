#!/usr/bin/python
import operator
import sys, getopt
from os import listdir
from os.path import isfile, join
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

class player:

    def __init__(self):
        self.name = ""
        self.points = 0
        self.tmppts = 0
        self.eighth = []
        self.quarter = []
        self.semi = []
        self.final = []
        self.winner = []
        self.nb_test = 0
        self.nb_win = {}
        self.prob_point = {}


    def __init__(self, fname = ""):
        self.name = ""
        self.points = 0
        self.tmppts = 0
        self.eighth = []
        self.quarter = []
        self.semi = []
        self.final = []
        self.winner = []
        self.read(fname)
        self.nb_test = 0
        self.nb_win = {}
        self.prob_point = {}
    '''
    file format:
    name: john doe
    pts: 45
    eighth: team0, team1, team2, team3, team4 ...
    quarter: team0, team1, team2, team3, team4 ...
    semi: team0, team1, team2, team3, team4
    final: team0, team1
    winner: team0
    '''
    def read(self, fname = ""):
        with open(fname) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        for item in content:
            splititems = item.split(':')
            cleanitem  = splititems[1].split(",")
            cleanitem  = [x.strip(' ') for x in cleanitem]
            if splititems[0] == "name":
                self.name = cleanitem[0]
            if splititems[0] == "points":
                self.points = int(cleanitem[0])
                self.tmppts = int(cleanitem[0])
            if splititems[0] == "eighth":
                self.eighth = cleanitem
            if splititems[0] == "quarter":
                self.quarter = cleanitem
            if splititems[0] == "semi":
                self.semi = cleanitem
            if splititems[0] == "final":
                self.final = cleanitem
            if splititems[0] == "winner":
                self.winner = cleanitem



class results:

    def __init__(self):
        self.eighth = []
        self.quarter = []
        self.semi = []
        self.final = []
        self.winner = []
        self.nb_test = 0
        self.winners = {}
    def __init__(self, fname = ""):
        self.eighth = []
        self.quarter = []
        self.semi = []
        self.final = []
        self.winner = []
        self.read(fname)
        self.nb_test = 0
        self.winners = {}
    '''
    file format:
    eighth: team0, team1, team2, team3, team4 ...
    take care team1 vs team2 etc..

    team0                                       team8
    team1                                       team9
            win0                        win4
            win1                        win5
    team2                                       team10
    team3                                       team11
                win8    win12-win13 win10
                win9      winner    win11
    team4                                       team12
    team5                                       team13
            win2                        win6
            win3                        win7
    team6                                       team14
    team7                                       team15

    quarter: team0, team1, team2, team3, team4 ...
    semi: team0, team1, team2, team3, team4
    final: team0, team1
    winner: team0
    '''
    def read(self, fname = ""):
        with open(fname) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        for item in content:
            splititems = item.split(':')
            cleanitem  = splititems[1].split(",")
            cleanitem  = [x.strip(' ') for x in cleanitem]
            if splititems[0] == "eighth":
                self.eighth = cleanitem
            if splititems[0] == "quarter":
                self.quarter = cleanitem
            if splititems[0] == "semi":
                self.semi = cleanitem
            if splititems[0] == "final":
                self.final = cleanitem
            if splititems[0] == "winner":
                self.winner = cleanitem


senarii = [{'qpts':1, 'spts': 1, 'fpts': 1, 'wpts': 1},
           {'qpts':2, 'spts': 2, 'fpts': 2, 'wpts': 2},
           {'qpts':2, 'spts': 3, 'fpts': 4, 'wpts': 5},
           {'qpts':2, 'spts': 4, 'fpts': 6, 'wpts': 8},
           {'qpts':2, 'spts': 4, 'fpts': 8, 'wpts': 16},
           ]

def myrun(path):

    players = []
    mypath = path+"./players/"
    playerstxt = [join(mypath,f) for f in listdir(mypath) if isfile(join(mypath,f))]
    for f in playerstxt:
        players.append(player(f))


    result =  results(path+"./results/results.txt")


    def calPropSenario(current):
        qi=0
        while qi < 256:
            QI = '{0:08b}'.format(qi)
            qi+=1
            testquarter= []
            for it in range(len(QI)):
                testquarter.append(result.eighth[it*2+(int(QI[it]))])
            #test if already some games
            if(len(set(result.quarter) & set(testquarter)) < len(result.quarter)):
                continue
            si = 0
            while si < 16:
                SI = '{0:04b}'.format(si)
                si+=1
                testsemi= []
                for it in range(len(SI)):
                    testsemi.append(testquarter[it*2+(int(SI[it]))])
                    #test if already some games
                if(len(set(result.semi) & set(testsemi)) < len(result.semi)):
                    continue
                fi = 0
                while fi < 4:
                    FI = '{0:02b}'.format(fi)
                    fi+=1
                    testfinal= []
                    for it in range(len(FI)):
                        testfinal.append(testsemi[it*2+(int(FI[it]))])
                    if(len(set(result.final) & set(testfinal)) < len(result.final)):
                        continue
                    wi = 0
                    while wi < 2:
                        WI = '{0:01b}'.format(wi)
                        wi+=1
                        testwinner= []
                        for it in range(len(WI)):
                            testwinner.append(testfinal[it*2+(int(WI[it]))])
                        if(len(set(result.winner) & set(testwinner)) < len(result.winner)):
                            continue
                        for ply in players:
                            ply.tmppts += senarii[current]['qpts']* len(set(ply.quarter) & set(testquarter))
                            ply.tmppts += senarii[current]['spts']* len(set(ply.semi)    & set(testsemi))
                            ply.tmppts += senarii[current]['fpts']* len(set(ply.final)   & set(testfinal))
                            ply.tmppts += senarii[current]['wpts']* len(set(ply.winner)  & set(testwinner))
                            if ply.tmppts in ply.prob_point:
                                ply.prob_point[ply.tmppts] +=1
                            else:
                                ply.prob_point[ply.tmppts] =1

                        bestplys  = [players[0]]
                        bestplysN = [players[0].name]
                        for ply in players[1:]:
                            if ply.tmppts == bestplys[0].tmppts:
                                bestplys.append(ply)
                                bestplysN.append(ply.name)
                            elif ply.tmppts > bestplys[0].tmppts:
                                bestplys  = [ply]
                                bestplysN = [ply.name]
                            else: continue
                        for ply in players: ply.tmppts = ply.points

                        names=", ".join(bestplysN)
                        result.nb_test += 1
                        if names in result.winners:
                            result.winners[names] += 1
                        else:
                            result.winners[names] = 1
                        for ply in bestplys:
                            if current in ply.nb_win:
                                ply.nb_win[current] += 1
                            else:
                                ply.nb_win[current] = 1



    i_test=0
    for cur in range(len(senarii)):
        for ply in players:
            if cur not in ply.nb_win:
                ply.nb_win[cur] = 0


        calPropSenario(cur)
        sorted_prob = sorted(result.winners.items(),key=operator.itemgetter(1),reverse=True)


        print (senarii[cur])
        print ("number of possibilities", result.nb_test)
        print ("winners probability:")
        for tup in sorted_prob:
            if(len(tup[0])>12):
                print (tup[0], '\t', round(100*tup[1]/result.nb_test,2), "%")
            elif(len(tup[0])>8):
                print (tup[0], '\t\t', round(100*tup[1]/result.nb_test,2), "%")
            elif(len(tup[0])>3):
                print (tup[0], '\t\t\t', round(100*tup[1]/result.nb_test, 2), "%")
            else:
                print (tup[0],'\t\t\t\t', round(100*tup[1]/result.nb_test,2), "%")
        i_test = float(result.nb_test)
        result.nb_test=0
        result.winners = {}

    x  = []
    ys = []
    xticks = []
    for iy in range(len(players)):
        ys.append([])
    for ix in range(len(senarii)):
        x.append(1+ix)
        xticks.append(str(senarii[ix]['qpts'])+","+str(senarii[ix]['spts'])+","+str(senarii[ix]['fpts'])+","+str(senarii[ix]['wpts']))
        for iy in range(len(players)):
            ys[iy].append(100*(float(players[iy].nb_win[ix])/i_test))


    print(x)
    print(ys)




    for iy in range(len(players)):
        plt.plot(x,ys[iy], label=players[iy].name)


    plt.xticks(x,xticks)
    plt.legend()
    #plt.show()
    savefig(path+"prob.png")







def main(argv):
    thepath = ''
    try:
        opts, args = getopt.getopt(argv,"hp:",["path="])
    except getopt.GetoptError:
        print ('probFoot.py -p <path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('probFoot.py -p <path>')
            sys.exit()
        elif opt in ("-p", "--path"):
            thepath = arg
    myrun(thepath)


if __name__ == "__main__":
   main(sys.argv[1:])
