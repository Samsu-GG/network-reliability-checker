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


network={
    name: Nodes(utils.Node["Type"][i],utils.Node["Name"][i],utils.Node["Reliability"][i],utils.Node["Cost"][i]) for i,name in zip(range(utils.nodeNumber), nodeName)}


if __name__ == "__main__":

    for i in network:
        print(
        str(network[i].Type) + " " +
        str(network[i].Name) + " " +
        str(network[i].Reliability) + " " +
        str(network[i].Cost)
    )



