from database import database
import itertools

def setTwitterGraphDB(tlink,*argument):
    db = database('twitter')
    uid = db.getUniqueID(tlink)
    db.createTable(uid,"Date","Rt","Fav")

    rtData = argument[0]
    favData = argument[1]
    dateData = argument[2]

    for x in range(0,len(rtData)):
        data = []
        data.append(dateData[x])
        data.append(rtData[x])
        data.append(favData[x])
        db.insertTable(data,uid,'Date','Rt','Fav')

def getTwitterGraphDB(tlink):
    db = database('twitter')
    uid = db.getUniqueID(tlink)
    dateData = db.getTableData(uid,'Date')
    dateData = list(itertools.chain(*dateData))
    dateData.reverse()
    rtData = db.getTableData(uid,'Rt')
    rtData = list(itertools.chain(*rtData))
    favData = db.getTableData(uid,'Fav')
    favData = list(itertools.chain(*favData))
    return rtData,favData,dateData


#main
tlink = 'https://twitter.com/BarackObama'
rtData,favData,dateData = getTwitterGraphDB(tlink)
print(rtData)
print(favData)
print(dateData)
