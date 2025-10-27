import pandas as pd


# Use the absolute path to your file
Node = pd.read_csv("F:/Python/network_reliability_system/data/Node.csv")
Edge= pd.read_csv("F:/Python/network_reliability_system/data/Edge.csv")

# print("Node data head:")
# print(Node.head())
# print("Edge data head:")
# print(Edge.head())

nodeName=list(Node["Name"])
nodeNumber = len(Node)
edge=[]
for i in range(len(Edge["Source"])):
    edge.append((Edge.iloc[i]["Source"],Edge.iloc[i]["Target"]))



if __name__=="__main__":
    print(nodeNumber)
    print(edge)


