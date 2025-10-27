import node
import utils
from node import network



for i in utils.edge:
        # print(i[0],i[1])

        network[i[0]].add_edge(i[1])
        network[i[1]].add_edge(i[0])
        # print(network[i[0]].route)

#
if __name__=='__main__':
    for i in network:
        print(

        str(network[i].Name) + " "
    )
        print(network[i].route)
