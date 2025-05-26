import streamlit as st

st.set_page_config(page_title="Growth Mindset Tracker", page_icon="🌱", layout="centered")

st.title("🌱 Growth Mindset Challenge")
st.subheader("Welcome to your journey of self-growth!")

st.markdown("""
A **growth mindset** means believing you can improve with effort.  
Set goals, face challenges, and become better every day. 💪  
""")

st.markdown("---")

# Input section
st.header("🎯 Set Your Learning Goals")
goals = st.text_area("Write your goals here (one per line)", height=150)

# Show entered goals as checklist
if goals:
    st.markdown("#### ✅ Track Your Progress")
    goal_list = goals.strip().split("\n")
    completed = []
    for goal in goal_list:
        done = st.checkbox(goal)
        if done:
            completed.append(goal)

    st.markdown("---")

    if len(completed) == len(goal_list) and goal_list != [""]:
        st.success("🎉 You completed all your goals! Keep going!")
    elif completed:
        st.info(f"🔥 You’ve completed **{len(completed)}** out of **{len(goal_list)}** goals.")
else:
    st.warning("✍️ Please enter at least one goal to begin tracking.")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
