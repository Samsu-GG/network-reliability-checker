from numpy.ma.core import append

import utils
from src.utils import nodeName


class Nodes:

    def __init__(self, type, name,reliability,cost):
        self.Type = type
        self.Name = name
        self.Reliability = reliability
        self.Cost = cost
        self.route=[]
    def add_edge(self, edge):
        self.route.append(edge)
    def set_critical_score(self,impact):
        self.imapct=impact
        self.Score=(1-self.Reliability)*impact


network={
    name: Nodes(utils.Node["Type"][i],utils.Node["Name"][i],utils.Node["Reliability"][i],utils.Node["Cost"][i]) for i,name in zip(range(utils.nodeNumber), nodeName)}


for i in utils.edge:
        # print(i[0],i[1])

        network[i[0]].add_edge(i[1])
        network[i[1]].add_edge(i[0])
        # print(network[i[0]].route)

if __name__ == "__main__":

    for i in network:
        print(
        str(network[i].Type) + " " +
        str(network[i].Name) + " " +
        str(network[i].Reliability) + " " +
        str(network[i].Cost)
    )
    for i in network:
        print(
            str(network[i].Name) + " "
            )
        print(network[i].route)
    print(network["CSE"].Cost)



