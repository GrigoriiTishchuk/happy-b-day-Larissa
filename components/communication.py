import streamlit as st
import plotly.express as px
from utils.texts_parser import parse_texts, enrich_messages
from utils.kpi_engine import build_texts_df, compute_basic_metrics

def render_communication_tab():
    st.title("Communication Analytics")
    # LOAD DATA
    messages = parse_texts("data/texts.txt")
    messages_enriched = enrich_messages(messages)
    df = build_texts_df(messages_enriched)
    metrics = compute_basic_metrics(df)
    # KPIS
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Messages", metrics["total_messages"])
    col2.metric("Active Days", metrics["unique_days"])
    col3.metric("Msgs / Day", round(metrics["messages_per_day"], 2))
    st.markdown("---")
    # MESSAGE TREND
    daily = df.groupby("date").size().reset_index(name="count")
    fig1 = px.line(
        daily,
        x="date",
        y="count",
        title="Message Volume Over Time"
    )
    st.plotly_chart(fig1, use_container_width=True)

    # HEATMAP (hour vs day)
    heatmap_data = df.groupby(["date", "hour"]).size().reset_index(name="count")
    fig2 = px.density_heatmap(
        heatmap_data,
        x="hour",
        y="date",
        z="count",
        title="Communication Heatmap"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # PIE CHART (balance)
    balance = df["sender"].value_counts().reset_index()
    balance.columns = ["sender", "count"]
    fig3 = px.pie(
        balance,
        names="sender",
        values="count",
        title="Communication Balance"
    )
    st.plotly_chart(fig3, use_container_width=True)

    # HOURLY ACTIVITY
    hourly = df.groupby("hour").size().reset_index(name="count")
    fig4 = px.bar(
        hourly,
        x="hour",
        y="count",
        title="Hourly Activity Distribution"
    )
    st.plotly_chart(fig4, use_container_width=True)