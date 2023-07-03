"""Module for plotting the IP addresses."""
import pandas as pd
import plotly.express as px


def plot_bar_addresses(ip_data: pd.DataFrame, title: str, ylabel: str, xlabel: str):
    bar_dest = px.bar(ip_data, y=ip_data.index[:], x=ip_data['length'][:] / 1e3,
                      title=title,
                      opacity=0.8,
                      color_discrete_sequence=['#e5b769'],
                      text_auto=True,
                      template='plotly_white',
                      width=800,
                      height=400)
    bar_dest.update_layout(
        yaxis_title_text=ylabel,
        xaxis_title_text=xlabel)  # gap between bars of adjacent location coordinates
    bar_dest.update_yaxes(tickfont_family="Arial Black")
    bar_dest.update_traces(textfont_size=9, textangle=0, textposition="outside", cliponaxis=False)
    bar_dest.show()
