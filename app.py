import streamlit as st
import pandas as pd
import plotly.express as px
import time

# Set page configuration
st.set_page_config(page_title="NIT Kurukshetra Info App", layout="wide")

# Custom CSS for snow effect
snow_css = """
<style>
.snowflake {
  position: fixed;
  top: 0;
  color: white;
  opacity: 0.8;
  font-size: 10px;
  animation: fall linear infinite;
}
@keyframes fall {
  0% { transform: translateY(0px); }
  100% { transform: translateY(100vh); }
}
</style>
<script>
function createSnowflakes() {
    for (let i = 0; i < 30; i++) {  // Adjust number of snowflakes
        let snowflake = document.createElement("div");
        snowflake.innerHTML = "❄";
        snowflake.classList.add("snowflake");
        snowflake.style.left = Math.random() * 100 + "vw";
        snowflake.style.animationDuration = (Math.random() * 3 + 2) + "s"; 
        document.body.appendChild(snowflake);
        setTimeout(() => snowflake.remove(), 5000);
    }
}
</script>
"""

# Title with animation
st.title("🏛️ NIT Kurukshetra Information Portal")
st.markdown("---")

# Sidebar navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Campus Life", "Feedback"])

# Campus Life Section
if page == "Campus Life":
    st.header("🏕️ Campus Life at NIT Kurukshetra")
    clubs = ["Coding Club", "Robotics Club", "Music and Dance Society", "Sports Club", "Entrepreneurship Cell", "Aeromodelling Club"]
    st.write("### Active Clubs:")
    st.write(", ".join(clubs))
    
    club_choice = st.radio("Which club interests you the most?", clubs)
    if st.button("Vote"):
        st.success(f"Thank you for voting for {club_choice}!")
        st.markdown(snow_css, unsafe_allow_html=True)
        st.markdown('<script>createSnowflakes();</script>', unsafe_allow_html=True)
