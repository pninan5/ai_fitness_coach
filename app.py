import streamlit as st
from prompt_template import build_prompt
from llm_api import call_openrouter

st.set_page_config(page_title="AI Fitness Coach", layout="centered")
st.title("🏋️ AI Fitness Coach")
st.markdown("Generate a personalized weekly workout plan using a free open-source LLM via OpenRouter.")

with st.form("input_form"):
    goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Endurance", "Flexibility"])
    duration = st.slider("Workout Duration (minutes)", 15, 90, 30)
    frequency = st.slider("Workouts per Week", 1, 7, 4)
    equipment = st.text_input("Equipment Available", "Bodyweight only")
    constraints = st.text_area("Injuries or Limitations", "None")
    api_key = st.text_input("OpenRouter API Key", type="password")
    submitted = st.form_submit_button("Generate Plan")

if submitted:
    with st.spinner("Building your custom fitness plan..."):
        user_input = {
            "goal": goal,
            "duration": duration,
            "frequency": frequency,
            "equipment": equipment,
            "constraints": constraints
        }
        prompt = build_prompt(user_input)
        try:
            output = call_openrouter(prompt, api_key)
            st.success("✅ Here is your plan!")
            st.text(output)
        except Exception as e:
            st.error(f"❌ Error: {e}")