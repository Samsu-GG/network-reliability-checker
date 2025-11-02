import os
import sys
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd


sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src import graph, analyzer, node, utils

st.set_page_config(
    page_title="Network Reliability System",
    layout="wide"
)

st.markdown(
    """
    <h1 style='text-align: center; color: #4B8BBE;'> NETWORK RELIABILITY SYSTEM & BUDGET OPTIMIZER</h1>
    <p style='text-align: center; color: #306998;'>Made by: Shamsul Islam Fahim & Md Mahfuz Hossain Antor</p>
    """, unsafe_allow_html=True
)
st.markdown("---")

st.markdown("### Load Graph")
if st.button("Load Graph"):
    graph.map_data()
    st.success("Graph loaded successfully!")
    html_file = "sad.html"
    if os.path.exists(html_file):
        with open(html_file, "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=1200, scrolling=True)
    else:
        st.error("Graph file not found!")

st.markdown("---")
st.markdown("### ⚙️ Reliability Test")

if st.button("Run Reliability Test"):
    critical_score = analyzer.get_critical_score()
    critical_score_sorted = sorted(critical_score, key=lambda x: x[3], reverse=True)
    top5 = critical_score_sorted[:5]

    st.success("Top 5 Critical Nodes Calculated!")

    df_top5 = pd.DataFrame(top5, columns=["Node Name", "Impact", "Reliability", "Score"])
    df_top5["Score"] = df_top5["Score"].map("{:.2f}".format)
    df_top5["Reliability"] = df_top5["Reliability"].map("{:.2f}".format)
    df_top5.index = df_top5.index + 1

    styled_df = df_top5.style.set_properties(**{
        'text-align': 'center',
        'font-family': 'Arial, sans-serif',
        'border-color': 'black',
        'border-style': 'solid'
    }).set_table_styles([
        {'selector': 'th', 'props': [('text-align', 'center'), ('background-color', '#4CAF50'), ('color', 'white'), ('font-weight', 'bold')]},
        {'selector': 'td', 'props': [('padding', '8px')]}
    ])

    st.dataframe(styled_df, use_container_width=True)

st.markdown("---")

st.markdown("Budget Optimization")
if st.button("Run Budget Optimization"):
    st.warning("Work in progress!")

st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>© 2025 Network Reliability System. All rights reserved.</p>",
    unsafe_allow_html=True
)
