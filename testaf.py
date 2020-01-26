import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import csv

#s = input("Enter Speed:(-1 to leave Open):" )
#h = input("Enter Hardness:(-1 to leave Open):" )
#w = input("Enter Width:(-1 to leave Open):" )
#f = input("Enter Feed:(-1 to leave Open):" )
#Input Variables
speed = ctrl.Antecedent(np.arange(1,100,1),'speed')
hardness = ctrl.Antecedent(np.arange(30,40,1),'hardness')
width = ctrl.Antecedent(np.arange(0.05,0.20,0.01),'width')
feed = ctrl.Antecedent(np.arange(1,5,1),'feed')
amr = ctrl.Antecedent(np.arange(0,5000,50),'amr')

#Output Variables
energy = ctrl.Consequent(np.arange(0,500,5), 'energy')
scenergy = ctrl.Consequent(np.arange(0,10,0.1),'scenergy')
mrr = ctrl.Consequent(np.arange(0,1000,5),'mrr')
vb = ctrl.Consequent(np.arange(0,0.2,0.0005),'vb')
vb3= ctrl.Consequent(np.arange(0,0.2,0.0005),'vb3')
avgstatcutforce = ctrl.Consequent(np.arange(0,1500,10),'avgstatcutforce')
avgdynfeedforce = ctrl.Consequent(np.arange(0,1300,10),'avgdynfeedforce')


#input fuzzysets
#speed
speed['slow'] = fuzz.trapmf(speed.universe, [1, 1, 28, 57])
speed['medium'] = fuzz.trimf(speed.universe, [28,57,89])
speed['fast'] = fuzz.trapmf(speed.universe,[57,89,100,100])
#feed
feed['small'] = fuzz.trapmf(feed.universe, [0.05, 0.05, 0.07, 0.12])
feed['medium'] = fuzz.trimf(feed.universe, [0.07,0.12,0.17])
feed['large'] = fuzz.trapmf(feed.universe,[0.12,0.17,0.20,0.20])
#width
width['narrow'] = fuzz.trapmf(width.universe, [1,1,2,3])
width['medium'] = fuzz.trimf(width.universe, [2,3,4])
width['wide'] = fuzz.trapmf(width.universe,[3,4,5,5])
#hardness
hardness['soft'] = fuzz.trapmf(hardness.universe, [30, 30, 31, 38])
hardness['hard'] = fuzz.trapmf(hardness.universe,[31,38,40,40])
#amr
amr['less'] = fuzz.trapmf(amr.universe, [0, 0, 1500, 3000])
amr['medium'] = fuzz.trimf(amr.universe, [1500,3000,4500])
amr['high'] = fuzz.trapmf(amr.universe,[3000,4500,5000,5000])

#output fuzzysets
#energy
energy['EEL'] = fuzz.trapmf(energy.universe, [0, 0, 100, 140])
energy['EVL'] = fuzz.trimf(energy.universe, [100,130,160])
energy['VL'] = fuzz.trimf(energy.universe, [135,160,175])
energy['L'] = fuzz.trimf(energy.universe, [160,175,190])
energy['SL'] = fuzz.trimf(energy.universe, [175,200,225])
energy['SH'] = fuzz.trimf(energy.universe, [200,240,270])
energy['H'] = fuzz.trimf(energy.universe, [240,270,300])
energy['VH'] = fuzz.trimf(energy.universe, [270,310,350])
energy['EVH'] = fuzz.trimf(energy.universe, [310,355,400])
energy['EEH'] = fuzz.trapmf(energy.universe,[360,430,500,500])
#mrr
mrr['EVL'] = fuzz.trapmf(mrr.universe, [0, 0, 50, 125])
mrr['VL'] = fuzz.trimf(mrr.universe, [50,125,175])
mrr['L'] = fuzz.trimf(mrr.universe, [125,200,275])
mrr['SL'] = fuzz.trimf(mrr.universe, [200,250,295])
mrr['SH'] = fuzz.trimf(mrr.universe, [250,300,375])
mrr['H'] = fuzz.trimf(mrr.universe, [305,405,500])
mrr['VH'] = fuzz.trimf(mrr.universe, [405,590,735])
mrr['EVH'] = fuzz.trapmf(mrr.universe,[525,950,1000,1000])
#scenergey
scenergy['EEL'] = fuzz.trapmf(scenergy.universe, [0, 0,1, 1.8])
scenergy['EVL'] = fuzz.trimf(scenergy.universe, [1,1.8,2.6])
scenergy['VL'] = fuzz.trimf(scenergy.universe, [1.8,2.4,3])
scenergy['L'] = fuzz.trimf(scenergy.universe, [2.4,3,3.6])
scenergy['SL'] = fuzz.trimf(scenergy.universe, [3,3.5,4])
scenergy['SH'] = fuzz.trimf(scenergy.universe, [3.5,4,4.5])
scenergy['H'] = fuzz.trimf(scenergy.universe, [4,4.4,4.8])
scenergy['VH'] = fuzz.trimf(scenergy.universe, [4.4,5,5.6])
scenergy['EVH'] = fuzz.trimf(scenergy.universe, [4.8,6.4,8])
scenergy['EEH'] = fuzz.trapmf(scenergy.universe,[6.4,8,10,10])
#vb
vb['EEL'] = fuzz.trapmf(vb.universe, [0, 0, 0.03, 0.04])
vb['EVL'] = fuzz.trimf(vb.universe, [0.03,0.04,0.05])
vb['VL'] = fuzz.trimf(vb.universe, [0.04,0.045,0.055])
vb['L'] = fuzz.trimf(vb.universe, [0.045,0.055,0.06])
vb['SL'] = fuzz.trimf(vb.universe, [0.055,0.06,0.07])
vb['SH'] = fuzz.trimf(vb.universe, [0.06,0.0725,0.08])
vb['H'] = fuzz.trimf(vb.universe, [0.075,0.0875,0.0975])
vb['VH'] = fuzz.trimf(vb.universe, [0.0985,0.105,0.12])
vb['EVH'] = fuzz.trimf(vb.universe, [0.105,0.13,0.155])
vb['EEH'] = fuzz.trapmf(vb.universe,[0.14,0.16,0.2,0.2])
#vb3
vb3['EEL'] = fuzz.trapmf(vb3.universe, [0, 0, 0.05, 0.065])
vb3['EVL'] = fuzz.trimf(vb3.universe, [0.05,0.065,0.0775])
vb3['VL'] = fuzz.trimf(vb3.universe, [0.065,0.075,0.085])
vb3['L'] = fuzz.trimf(vb3.universe, [0.075,0.0825,0.090])
vb3['SL'] = fuzz.trimf(vb3.universe, [0.085,0.090,0.095])
vb3['SH'] = fuzz.trimf(vb3.universe, [0.0925,0.0975,0.1025])
vb3['H'] = fuzz.trimf(vb3.universe, [0.10,0.11,0.1175])
vb3['VH'] = fuzz.trimf(vb3.universe, [0.11,0.1225,0.135])
vb3['EVH'] = fuzz.trimf(vb3.universe, [0.125,0.145,0.16])
vb3['EEH'] = fuzz.trapmf(vb3.universe,[0.145,0.165,0.2,0.2])
#avgstatcutforce
avgstatcutforce['EEL'] = fuzz.trapmf(avgstatcutforce.universe, [0, 0, 660, 740])
avgstatcutforce['EVL'] = fuzz.trimf(avgstatcutforce.universe, [690,740,790])
avgstatcutforce['VL'] = fuzz.trimf(avgstatcutforce.universe, [740,790,830])
avgstatcutforce['L'] = fuzz.trimf(avgstatcutforce.universe, [790,880,970])
avgstatcutforce['SL'] = fuzz.trimf(avgstatcutforce.universe, [880,930,990])
avgstatcutforce['SH'] = fuzz.trimf(avgstatcutforce.universe, [930,990,1030])
avgstatcutforce['H'] = fuzz.trimf(avgstatcutforce.universe, [990,1040,1100])
avgstatcutforce['VH'] = fuzz.trimf(avgstatcutforce.universe, [1040,1120,1200])
avgstatcutforce['EVH'] = fuzz.trimf(avgstatcutforce.universe, [1120,1220,1320])
avgstatcutforce['EEH'] = fuzz.trapmf(avgstatcutforce.universe,[1220,1330,1500,1500])
#avgdynfeedforce
avgdynfeedforce['EEL'] = fuzz.trapmf(avgdynfeedforce.universe, [0, 0, 300, 400])
avgdynfeedforce['EVL'] = fuzz.trimf(avgdynfeedforce.universe, [300,420,540])
avgdynfeedforce['VL'] = fuzz.trimf(avgdynfeedforce.universe, [420,500,580])
avgdynfeedforce['L'] = fuzz.trimf(avgdynfeedforce.universe, [500,580,660])
avgdynfeedforce['SL'] = fuzz.trimf(avgdynfeedforce.universe, [580,620,680])
avgdynfeedforce['SH'] = fuzz.trimf(avgdynfeedforce.universe, [640,700,750])
avgdynfeedforce['H'] = fuzz.trimf(avgdynfeedforce.universe, [780,810,930])
avgdynfeedforce['VH'] = fuzz.trimf(avgdynfeedforce.universe, [900,950,1000])
avgdynfeedforce['EVH'] = fuzz.trimf(avgdynfeedforce.universe, [950,1030,1110])
avgdynfeedforce['EEH'] = fuzz.trapmf(avgdynfeedforce.universe,[1030,1120,1500,1500])
x=0
rule1 = ctrl.Rule(hardness['soft'] & speed['slow']&width['narrow']&feed['small']&amr['less'],vb['EEL'])

for h in ['soft','hard']:
    for s in ['slow','medium','fast']:
        for w in ['narrow','medium','wide']:
            for f in ['small','medium','large']:
                for a in ['less','medium','high']:
                    print('Enter Data for '+h+' hardness, '+s+' speed, '+w+' width, '+f+' feed, '+a+' amr')
                    v = input("Enter VB:")
                    fc = input("Enter avgstatcutforce:")
                    df = input("Enter avgdynfeedforce:")
                    sce = input("Enter sceenergy:") 

