import json
from random import randint


class IncidentGenerator:

    def __init__(self):

        self.idlist = {}
        with open('metadata.json') as json_data:
                self.idlist = json.load(json_data)

        self.total = 0
        for key,item in self.idlist.items():
                self.total += item['count']

    def generate(self):
        num = randint(0, self.total)
        temp = 0
        id = ''
        desc = ''
        time1 = 0
        time2 = 0
        time3 = 0
        time4 = 0
        out = False
        for key,item in self.idlist.items():
            for x in range (temp, temp + item['count']):
                temp += 1
                if (temp >= num):
                    out = True
                    id = key
                    desc = item['description']
                    time1 = item['callTime']
                    time2 = item['leaveTime']
                    time3 = item['travelTime']
                    time4 = item['eventTime']
                    break

            if out:
                break
        return {"id":id, "description":desc, "callTime":time1, "leaveTime":time2, "travelTime":time3, "eventTime":time4}
