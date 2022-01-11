import collections

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def union(self, node1, node2):
        self.parent[self.find(node1)]  = self.find(node2)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return  self.parent[node]


class patientRelationGraph:
    def __init__(self):
        self.graph = {}
        self.patient = []
        self.size = 0
    def insertPatient(self, relations):
        for r in relations:
            if r[0] not in self.graph:
                self.graph[r[0]] = [r[1]]
            else:
                self.graph[r[0]].append(r[1])

            if r[1] not in self.graph:
                self.graph[r[1]] = [r[0]]
            else:
                self.graph[r[1]].append(r[0])

            if r[0] not in self.patient:
                self.patient.append(r[0])
                self.size += 1

            if r[1] not in self.patient:
                self.patient.append(r[1])
                self.size += 1
    def findSource(self):
        #查询当前疫情的源头，是否是一条传播链
        uf = UnionFind(self.size)
        for k, values in self.graph.items():
            for v in values:
                uf.union(self.patient.index(k), self.patient.index(v))
        chains = 0
        for p in range(len(uf.parent)):
            if p == uf.parent[p]:
                chains += 1
        if chains == 1:
            print('当前疫情传播链清晰，源头可溯')
            return True
        else:
            print('当前疫情存在多条传播链')
            return False
    def findNumOfChian(self):
        #查看当前疫情有几条传播链
        uf = UnionFind(self.size)
        for k,values in self.graph.items():
            for v in values:
                uf.union(self.patient.index(k), self.patient.index(v))
        chains = 0
        for p in range(len(uf.parent)):
            if p == uf.parent[p]:
                chains += 1
        print('当前疫情有' + str(chains) + '条传播链')
        return chains
    def findMaxInfectPatient(self):
        #查找最多传播的人
        maxInfectNums = 0
        patient = []
        for k,v in self.graph.items():
            if len(v) > maxInfectNums:
                patient = [k]
                maxInfectNums = len(v)
            elif len(v) == maxInfectNums:
                patient.append(k)
        print('超级传播者为：' + str(patient), '与他接触过确诊人数为：'+ str(maxInfectNums))
        return patient, maxInfectNums


prg = patientRelationGraph()
prg.insertPatient([['A','B'], ['B','C'], ['C','D'],['D','E'], ['X','E'], ['Y','E'], ['F','G'],['G','Z']])
prg.findNumOfChian()
prg.findMaxInfectPatient()
prg.insertPatient([['E','F']])
prg.findNumOfChian()