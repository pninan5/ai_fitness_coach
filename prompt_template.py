def build_prompt(user_input):
    return f"""
You are a certified personal fitness trainer. Create a 7-day personalized workout plan.

Goal: {user_input['goal']}
Duration: {user_input['duration']} minutes per session
Frequency: {user_input['frequency']} days/week
Equipment: {user_input['equipment']}
Constraints: {user_input['constraints']}

Please include:
- Daily workout breakdown
- Exercises, sets, and reps
- Rest intervals and motivational notes
"""