class patient:
    def __init__(self, id, province, city):
        #存储病人的相关信息
        self.id = id
        self.province = province
        self.diagnoseTime = None
        self.city = city
        self.pos = set()

    def insertArea(self, pos):
        self.pos.add(pos)

    def insertDiagnoseTime(self,time):
        self.diagnoseTime = time


