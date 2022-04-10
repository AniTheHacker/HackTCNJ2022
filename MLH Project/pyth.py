from quickstart import getVals

def getScores():
    NumPlants = float(getVals(0)[3])
    MonPlants = float(getVals(0)[4])
    MilesCar = float(getVals(0)[5])
    MPGCar = float(getVals(0)[6])
    NumTrashbag = float(getVals(0)[7])
    VolTrashbag = float(getVals(0)[8])
    NumRecycleBin = float(getVals(0)[9])
    VolBin = float(getVals(0)[10])
    KwGen = float(getVals(0)[11])
    KwUse = float(getVals(0)[12])
    MinShower = float(getVals(0)[13])
    MilesBus = float(getVals(0)[14])
    MilesBike = float(getVals(0)[15])


    CarCo2 = (MilesCar/MPGCar) * 8887
    BusCo2 = (MilesBus/10) * 8887
    Co2Saved = (MilesBike/MPGCar) * 52 * 8887
    OxygenProd = NumPlants * MonPlants * 27
    NetCo2 = (CarCo2 + BusCo2 - Co2Saved - OxygenProd)
    GreyScore = 0

    if NetCo2 <= 4200000:
        GreyScore = 10
    elif 4200000 <= NetCo2 < 4300000:
        GreyScore = 9
    elif 4300000 <= NetCo2 < 4400000:
        GreyScore = 8
    elif 4400000 <= NetCo2 < 4500000:
        GreyScore = 7
    elif 4500000 <= NetCo2 < 4600000:
        GreyScore = 6 
    elif 4600000 <= NetCo2 < 4700000:
        Greyscore = 5 
    elif 4700000 <= NetCo2 < 4700000:
        GreyScore = 4
    elif 4800000 <= NetCo2 < 4900000:
        GreyScore = 3 
    elif 4900000 <= NetCo2 < 5000000:
        GreyScore = 2 
    else:
        GreyScore = 1

    GalWater = MinShower * 2.1 * 365.25
    GalTrash = NumTrashbag * VolTrashbag * 52
    GalRecycle = NumRecycleBin * VolBin * 52
    NetTrash = GalTrash - GalRecycle + GalWater
    BlueScore = 0

    if NetTrash <= 300:
        BlueScore = 10
    elif 300 <= NetTrash < 500:
        BlueScore = 9
    elif 500 <= NetTrash < 700:
        BlueScore = 8 
    elif 700 <= NetTrash < 900:
        BlueScore = 7
    elif 900 <= NetTrash < 1100:
        BlueScore = 6
    elif 1100 <= NetTrash < 1300:
        BlueScore = 5
    elif 1300 <= NetTrash < 1500:
        BlueScore = 4 
    elif 1500 <= NetTrash < 1700:
        BlueScore = 3
    elif 1700 <= NetTrash < 1900:
        BlueScore = 2
    else:
        BlueScore = 1

    NetKwh = (KwUse -KwGen) * 52
    YellowScore = 0

    if NetKwh <= 8000:
        YellowScore = 10
    elif 8000 <= NetKwh < 8300:
        YellowScore = 9
    elif 8300 <= NetKwh < 8600:
        YellowScore = 8
    elif 8600 <= NetKwh < 8900:
        YellowScore = 7
    elif 8900 <= NetKwh < 9200:
        YellowScore = 6
    elif 9200 <= NetKwh < 9500:
        YellowScore = 5
    elif 9500 <= NetKwh < 9800:
        YellowScore = 4
    elif 9800 <= NetKwh < 10100:
        YellowScore = 4
    elif 10100 <= NetKwh < 10400:
        YellowScore = 3
    elif 10400 <= NetKwh < 10700:
        YellowScore = 2
    else:
        YellowScore = 1


    rStr = ("Grey Score: %i/10\nBlue Score: %i/10\nYellow Score: %i/10\n" % (GreyScore, BlueScore, YellowScore))
    rStr += ("Green Score: %i/30" % (GreyScore+BlueScore+YellowScore))
    return rStr

getScores()