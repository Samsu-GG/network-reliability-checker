import utils
from pyvis.network import Network
import webbrowser
import webbrowser


def map_data():
    g=Network(notebook='false',height='1500px',width='100%',bgcolor='#222222',font_color='white')
    for i in utils.nodeName:
        g.add_node(i)
    for i in utils.edge:
        g.add_edge(i[0], i[1])

    g.show("sad.html")

if __name__ == "__main__":
    map_data()
    webbrowser.open("sad.html")



