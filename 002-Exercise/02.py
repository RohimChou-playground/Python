from datetime import datetime

def readAllLines(filePath):
    with open(filePath, 'r') as file:
        return file.read().splitlines()

def getTimeStamp():
    timestampStr = datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f')
    return timestampStr[:-5] # chop last 5 mili sec digits

class User:
    def __init__(self, id, name, cityId):
        self.id = id
        self.name = name
        self.cityId = cityId

class SickLeave:
    def __init__(self, id, userId, date):
        self.id = id
        self.userId = userId
        self.date = date

print(f'{getTimeStamp()} Start reading 02-user.csv')
users = []
allUserLines = readAllLines('02-user.csv')
print(f'{getTimeStamp()} {len(allUserLines)} lines are read')
for i, line in enumerate(allUserLines):
    splits = line.split(',')
    if i > 0 and len(splits) >= 3:
        users.append(User(splits[0], splits[1].strip('\"'), splits[2]))

print(f'{getTimeStamp()} Start reading 02-sickleaves.csv')
sickLeaves = []
allSickLeaveLines = readAllLines('02-sickleaves.csv')
print(f'{getTimeStamp()} {len(allSickLeaveLines)} lines are read')
for i, line in enumerate(allSickLeaveLines):
    splits = line.split(',')
    if i > 0 and len(splits) >= 3:
        sickLeaves.append(SickLeave(splits[0], splits[1].strip('\"'), splits[2]))

print(f'{getTimeStamp()}')
print('===================================')
print(f'{getTimeStamp()} {datetime.now().strftime("%Y/%m")} Sick Leaves stats')
