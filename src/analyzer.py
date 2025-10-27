import utils
from pyvis.network import Network
import networkx as nx
import webbrowser

g = nx.Graph()
for i in utils.nodeName:
    g.add_node(i)
for i in utils.edge:
    g.add_edge(i[0], i[1])

# Create PyVis network
net = Network(
    notebook=False,
    width="100%",
    height="100vh",
    bgcolor="#222222",
    font_color="white",
    cdn_resources='in_line',
)

net.title = "Network Reliability System"
net.from_nx(g)


net.set_options("""
var options = {
  "configure": {
    "enabled": false
  },
  "physics": {
    "enabled": true,
    "stabilization": {"iterations": 100}
  }
}
""")

html_file = "sad.html"
html_content = net.generate_html()


html_content = html_content.replace('height="800px"', 'height="100vh"')
html_content = html_content.replace('style="', 'style="margin: 0; padding: 0; ')

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Graph saved successfully as {html_file}")
webbrowser.open("sad.html")