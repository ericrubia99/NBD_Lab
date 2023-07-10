import plotly.express as px


def plot_protocol_count(grouped_flows):
    num_protocols = grouped_flows.Protocol.nunique()
    bar_protocol = px.bar(grouped_flows["Protocol"], y=grouped_flows.Protocol.value_counts().index,
                          x=grouped_flows.Protocol.value_counts().values,
                          title=f'Top {num_protocols} Protocols used',
                          opacity=0.8,
                          color_discrete_sequence=['#2a9d8f'],
                          text_auto=True,
                          template='plotly_white',
                          width=800,
                          height=400)

    bar_protocol.update_layout(
        yaxis_title_text='Protocols',
        xaxis_title_text='Count')
    bar_protocol.update_yaxes(tickfont_family="Arial Black")
    bar_protocol.update_traces(textfont_size=9, textangle=0, textposition="outside", cliponaxis=False)
    bar_protocol.show()
