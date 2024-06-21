import streamlit as st


@st.cache_resource
def get_looker_studio_url():
    # Replace this with the actual Looker Studio embed URL
    return "https://lookerstudio.google.com/embed/reporting/1c31c6d5-230f-4cac-acdb-81ae1f4b49b8/page/ApJ2D"

looker_studio_url = get_looker_studio_url()

st.title("Employee Churn Dashboard")

# Embed Looker Studio dashboard using an iframe
st.components.v1.html(
    f"""
    <iframe width="100%" height="800" src="{looker_studio_url}" frameborder="0" style="border:0" allowfullscreen></iframe>
    """,
    height=800,
)
