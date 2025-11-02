from src.node import network
import node

type_scores = {
    "Server": 5,
    "Router": 4,
    "Faculty": 3,
    "Department": 2,
    "PC" : 1
}


def DFS(source):
    impact=0
    isvisted={network[i].Name:False for i in network}
    q=[source]
    isvisted[source]=True
    while q:
        u=q.pop(0)
        # print(u)

        for i in network[u].route :
            if not isvisted[i] and type_scores[network[u].Type]>=type_scores[network[i].Type]:
                q.append(i)
                isvisted[i]=True
                if type_scores[network[i].Type]==1:
                    impact += 1

    return impact

def find_score():
    for name in network:
        impact=DFS(name)
        network[name].set_critical_score(impact)


def get_critical_score():
    find_score()
    Critical_score = []
    for name in network:
        score = float(network[name].Score)
        score = round(score, 2)
        Critical_score.append((name,network[name].imapct,network[name].Reliability,score))
        print(network[name].imapct)

    return Critical_score


if __name__=="__main__":
    x = input("Enter node Name: ")
    # print(DFS(x))
    find_score()
    # for i in network:
    #         print(
    #             str(network[i].Name) + " "+
    #             str("%.2f" % network[i].Score)
    #         )
    get_critical_score()