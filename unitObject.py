import pandas as pd

importList = []

baseData = pd.read_csv("AoSUnits - Sheet1.csv")

class units:
    def __init__(un, unitName, unitMovement, unitCurrentMovement, unitTotalMovement, unitHealth, unitCurrentHealth, unitTotalHealth, unitRangeDamage, unitMeleeDamage, unitTotalDamage, unitNumModels, unitNumModelsCurrent, unitDamageTaken):
        un.unitName = unitName
        un.unitMovement = unitMovement
        un.unitCurrentMovement = unitCurrentMovement
        un.unitTotalMovement = unitTotalMovement
        un.unitHealth = unitHealth
        un.unitCurrentHealth = unitCurrentHealth
        un.unitTotalHealth = unitTotalHealth
        un.unitRangeDamage = unitRangeDamage
        un.unitMeleeDamage = unitMeleeDamage
        un.unitTotalDamage = unitTotalDamage
        un.unitNumModels = unitNumModels
        un.unitNumModelsCurrent = unitNumModelsCurrent
        un.unitDamageTaken = unitDamageTaken

    def __str__(un):
        return '\nUnit Name: ' + str(un.unitName) + '\nMovement: ' + str(un.unitMovement) + '\nUnit Health: ' + str(un.unitHealth) + '\nNumber of models in unit: ' + str(un.unitNumModels)
    
    def Move(un):
        return str(un.unitMovement)
    
    def Move_Current(un):
        return str(un.unitCurrentMovement)
    
    def Move_Total(un):
        return str(un.unitTotalMovement)
    
    def Name(un):
        return str(un.unitName)
    
    def Health(un):
        return str(un.unitHealth)
    
    def Health_Current(un):
        return str(un.unitCurrentHealth)
    
    def Health_Total(un):
        return str(un.unitTotalHealth)
    
    def NumModels(un):
        return str(un.unitNumModels)
    
    def Damage_Delt(un):
        return str(un.unitTotalDamage)
    
    def Damage_Taken(un):
        return str(un.unitDamageTaken)
    
    def unitRangeStatus(un):
        return str(un)
    

        
