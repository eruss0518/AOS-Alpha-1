import pandas as pd

importList = []

lName = ""

lPoints = ""

lDetach = ""

lGen = ""

lFac = ""

baseData = pd.read_csv("AoSUnits - Sheet1.csv")


class newList:
    def __init__(impLis, playerListName, playerListPoints, playerListDetachment, playerListGeneral, playerListFaction):
        impLis.playerListName = playerListName
        impLis.playerListPoints = playerListPoints
        impLis.playerListDetachment = playerListDetachment
        impLis.playerListGeneral = playerListGeneral
        impLis.playerListFaction = playerListFaction

    

    def listImportName(implLis,):

        #Creates list of all of the unit names
        bdl = baseData.get('unitName').to_list()


        with open("Boop 13901500 pts.txt","r") as newList:
            lines = newList.readlines()
            for line in lines:
                importList.append(line)
        newList.close()


        #new player list


        #Getting the imported lists name
        
        ln = (importList[0])

        ln = ln.split(' ')[0]


        return ln
    
    def listImportPoints(implLis):

        #Creates list of all of the unit names
        bdl = baseData.get('unitName').to_list()


        with open("Boop 13901500 pts.txt","r") as newList:
            lines = newList.readlines()
            for line in lines:
                importList.append(line)
        newList.close()

        lPoints = ""

        #Getting the imported lists points
        flnum = ""
        lnum = (importList[0])

        lnum = lnum.split(' ')[1:2]

        for i in lnum:

            lPoints = lPoints + " " + i

        return lPoints[:-5]
    


    def listImportDetachment(implLis):

        #Creates list of all of the unit names
        #bdl = baseData.get('unitName').to_list()


        with open("Boop 13901500 pts.txt","r") as newList:
            lines = newList.readlines()
            for line in lines:
                importList.append(line)
        newList.close()

        lDetach = ""

        #Getting the imported lists name
        
        ld = (importList[2])

        ldStart = ld.split(' ')[7]

        ldEnd = ld.split(' ')[8]

        lDetach = "" + str(ldStart) + " " + str(ldEnd) + ""

        return lDetach

        #----------------------
    def listImportGeneral(implLis):

        #Creates list of all of the unit names
        #bdl = baseData.get('unitName').to_list()


        with open("Boop 13901500 pts.txt","r") as newList:
            lines = newList.readlines()
            for line in lines:
                importList.append(line)
        newList.close()

        lGen = ""

        #Getting the imported lists General
        
        lg = (importList[6])

        lGen = lg



        return lGen

        #-------------------------------------------

    def listImportFaction(implLis):

        #Creates list of all of the unit names
        #bdl = baseData.get('unitName').to_list()


        with open("Boop 13901500 pts.txt","r") as newList:
            lines = newList.readlines()
            for line in lines:
                importList.append(line)
        newList.close()
        lFac = ""

        #Getting the imported lists Faction
        
        lf = (importList[2])

        lfStart = lf.split(' ')[4]

        lfEnd = lf.split(' ')[5]

        lFac = "" + str(lfStart) + " " + str(lfEnd) + ""


        return lFac


        #npl = newList(lName, lPoints, lDetach, lGen, lFac)






        #lPoints = importList[2]

        lDetach = importList[4]

        lGen = importList[5]

        lFac = importList[6]

        npl = lName + lPoints, lDetach, lGen, lFac

        return npl




#print("Welcom to the game would you like to start a new list?")

#player = newList(lName, lPoints, lDetach, lGen, lFac)

#x = player.listImport()

#print(x)
