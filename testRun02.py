import pandas as pd
import os
from importList import newList
from unitObject import units
import subprocess


baseData = pd.read_csv("AoSUnits - Sheet1.csv")

battleRound = 1

p1CurrentList = []

p1ActiveList = []

q = os.getlogin()

print(q)

createImportFolder = '[IO.Directory]::CreateDirectory("C:\\Program Files\\importFolder")'

createArchiveFolder = '[IO.Directory]::CreateDirectory("C:\\Program Files\\archiveFolder")'

uif = "C:\\Users\\" + q + "\\Documents\\importFolder"

uaf = "C:\\Users\\" + q + "\\Documents\\archiveFolder"

if not os.path.isdir(uif):
    os.makedirs(uif)


if not os.path.isdir(uaf):
    os.makedirs(uaf)



x = 0
while x < 1:
    #number of players based off of the number of files in the import folder
    np = 0

    fcp = '(Get-Childitem -Path' + uif + '-File).count'


    fileCount = fcp

    fc = subprocess.run(['powershell.exe', '-Command', fileCount], capture_output=True, text=True)

    t = 1

    fnp = 'Get-Childitem -Path "C:\\Users\\' + q + '\\Documents\\importFolder" -Name'

    fileName = fnp

    fn = subprocess.run(['powershell.exe', '-Command', fileName], capture_output=True, text=True)

    z = fn.stdout

    
    if t == 1:
        tempName = ""
        tempPoints = ""
        tempDet = ""
        tempGen = ""
        tempFac = ""

        pln = tempName
        plp = tempPoints
        pld = tempDet
        plg = tempGen
        plf = tempFac

        #player Unit List
        pun = []

        pln = pln

        p1 = newList(pln, plp, pld, plg, plf)

        p1.playerListName = p1.listImportName()

        #print(p1.playerListName) Worked

        p1.playerListPoints = p1.listImportPoints()

        #print(p1.playerListPoints)

        p1.playerListDetachment = p1.listImportDetachment()

        #print(p1.playerListDetachment) Worked

        p1.playerListGeneral = p1.listImportGeneral()

        #print(p1.playerListGeneral) Worked needs refinement

        p1.playerListFaction= p1.listImportFaction()

        #print(p1.playerListFaction) #Worked

        with open(str(z)[:-1],"r") as newList:
            lines = newList.readlines()
        for line in lines:
            temp = ""
            temp += line
            temp = temp[:-7]
            str(temp)
            pun.append(temp)

        ToF = baseData.get('unitName').to_list()

        p1List = []



        unList = frozenset(ToF).intersection(pun)

        for cu in unList:
            p1List.append(cu)



        
        else:
            print("Noop noop")
    
    print(p1.playerListName)
    print(p1.playerListPoints)
    print(p1.playerListDetachment)
    print(p1.playerListGeneral)
    print(p1.playerListFaction)
    print(p1List)

    pul = {
        'unit_name': ['temp_Name',],
        'unit_movement': [0,],
        'unit_currentMovement': [0,],
        'unit_totalMovement': [0,],
        'unit_health': [0,],
        'unit_currentHealth': [0,],
        'unit_totalHealth': [0,],
        'unit_numModels': [0,],
        'unit_numModelsCurrent': [0,],
        'unit_damageTaken': [0,],
        'unit_damageGiven': [0,],
        'unit_numRange': [0,],
        'unit_rangeDamage': [0,],
        'unit_totalRangeDamage': [0,],
        'unit_numMelee': [0,],
        'unit_meleeDamage': [0,],
        'unit_totalMeleeDamage': [0,]
        
        
    }

    p1df = pd.DataFrame(pul)



    uList = []

    for l in p1List:
        uList.append(l)

    
        


        
    tum = 0

    ind = 1

    pl = len(p1List)

    for u in p1List:

        

        un = baseData[baseData['unitName'] == u].index[0]

        fun = baseData.loc[un, 'unitName']

        #Creates unit name for player list
        p1df.loc[ind, 'unit_name'] = fun

        fum = baseData.loc[un, 'Move']

        #Creates unit movement stat
        p1df.loc[ind, 'unit_movement'] = fum


        fuh = baseData.loc[un, 'Health']

        #Creates unit movement stat
        p1df.loc[ind, 'unit_health'] = fuh


        funm = baseData.loc[un, 'numModels']

        #Creates unit movement stat
        p1df.loc[ind, 'unit_numModels'] = funm

        #Game creation stat
        gcs = 0

        p1df.loc[ind, 'unit_currentMovement'] = gcs

        p1df.loc[ind, 'unit_totalMovement'] = gcs

        p1df.loc[ind, 'unit_currentHealth'] = gcs

        p1df.loc[ind, 'unit_totalHealth'] = gcs

        fcnm = baseData.loc[un, 'numModels']

        p1df.loc[ind, 'unit_numModelsCurrent'] = fcnm

        p1df.loc[ind, 'unit_damageTaken'] = gcs

        p1df.loc[ind, 'unit_damageGiven'] = gcs

        fnrw = baseData.loc[un, 'numRangeWeapons']

        p1df.loc[ind, 'unit_numRange'] = fnrw

        frd = baseData.loc[un, 'rDamage']

        p1df.loc[ind, 'unit_rangeDamage'] = frd

        p1df.loc[ind, 'unit_totalRangeDamage'] = gcs

        fnmw = baseData.loc[un, 'numMeleeWeapons']

        p1df.loc[ind, 'unit_numMelee'] = fnmw

        p1df.loc[ind, 'unit_meleeDamage'] = gcs

        p1df.loc[ind, 'unit_totalMeleeDamage'] = gcs



        ind += 1

        
        tum += 1
    

    while battleRound < 5:

        #movement phase
        mlistCount = 1
        for m in range(len(p1df) - 1):
            mi = input(print("Will " + str(p1df.loc[mlistCount, 'unit_name']) + " move its: " + str(p1df.loc[mlistCount, 'unit_movement']) + " this turn?"))

            if mi == "y":
                ncm = p1df.loc[mlistCount, 'unit_movement'] + p1df.loc[mlistCount, 'unit_currentMovement']

                p1df.loc[mlistCount, 'unit_currentMovement'] = ncm
            else:
                print("noop noop")
            mlistCount += 1

        print('------------------------------------------------')
        print(p1df)

        #Shooting Phase
        rlistCount = 1
        for r in range(len(p1df) - 1):

            run = int(p1df.loc[rlistCount, 'unit_numRange'])


            if run > 0:

                ri = input(print("Will " + str(p1df.loc[rlistCount, 'unit_name']) + " fire its: " + str(p1df.loc[rlistCount, 'unit_numRange']) + " this turn?"))

                if ri == "y":
                    ncr = p1df.loc[rlistCount, 'unit_rangeDamage'] * p1df.loc[rlistCount, 'unit_numModelsCurrent']


                    p1df.loc[rlistCount, 'unit_totalRangeDamage'] += ncr
                else:
                    print("noop noop")
            else:
                print(str(p1df.loc[rlistCount, 'unit_name']) + " does not have a ranged weapon.")
            rlistCount += 1
        print('------------------------------------------------')
        print(p1df)


        #Melee
        melistCount = 1
        for me in range(len(p1df) - 1):
            mun = int(p1df.loc[melistCount, 'unit_numMelee'])


            if mun > 0:

                ri = input(print("Will " + str(p1df.loc[melistCount, 'unit_name']) + " fire its: " + str(p1df.loc[melistCount, 'unit_numMelee']) + " this turn?"))

                if ri == "y":
                    ncme = p1df.loc[melistCount, 'unit_meleeDamage'] * p1df.loc[melistCount, 'unit_numModelsCurrent']

                    cd = p1df.loc[melistCount, 'unit_totalMeleeDamage']


                    p1df.loc[melistCount, 'unit_totalMeleeDamage'] = ncme + cd
                else:
                    print("noop noop")
            else:
                print(str(p1df.loc[melistCount, 'unit_name']) + " does not have a melee weapon.")
            melistCount += 1

        print('------------------------------------------------')
        print(p1df)







        battleRound = 5

        #for u in p1List:




x += 1