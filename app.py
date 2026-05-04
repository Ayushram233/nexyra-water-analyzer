import streamlit as st

# Page setup
st.set_page_config(page_title="Nexyra", page_icon="💧", layout="centered")

# Title
st.title("💧 Nexyra Water Analyzer")
st.write("Analyze water quality using key scientific parameters.")

st.write("---")

# Inputs
st.subheader("Enter Water Parameters")

ph = st.number_input("pH", value=7.0)
tds = st.number_input("TDS (mg/L)", value=300.0)
turbidity = st.number_input("Turbidity (NTU)", value=2.0)
hardness = st.number_input("Hardness (mg/L)", value=100.0)
do = st.number_input("Dissolved Oxygen (mg/L)", value=6.0)

st.write("---")

# Button
if st.button("🔍 Analyze Water"):

    score = 100
    issues = []

    # Logic
    if ph < 6.5 or ph > 8.5:
        issues.append("pH out of safe range")
        score -= 20

    if tds > 500:
        issues.append("High TDS")
        score -= 20

    if turbidity > 5:
        issues.append("High turbidity")
        score -= 20

    if hardness > 200:
        issues.append("High hardness")
        score -= 20

    if do < 5:
        issues.append("Low dissolved oxygen")
        score -= 20

    st.write("---")

    # Result
    if score >= 80:
        st.success("🟢 Excellent Water Quality")
    elif score >= 50:
        st.warning("🟡 Moderate Water Quality")
    else:
        st.error("🔴 Poor Water Quality")

    # Score display
    st.subheader(f"🌊 Water Quality Score: {score}/100")
    st.progress(score / 100)

    # Issues
    if issues:
        st.write("### ⚠️ Issues Found:")
        for i in issues:
            st.write("-", i)

    st.write("---")

    # Clean parameter display (simple, not messy)
    st.write("### 📊 Parameter Values")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"pH: {ph}")
        st.write(f"TDS: {tds}")
        st.write(f"Turbidity: {turbidity}")

    with col2:
        st.write(f"Hardness: {hardness}")
        st.write(f"Dissolved Oxygen: {do}")

st.bar_chart({
    "Values": [ph, tds, turbidity, hardness, do]
})

if 'score' in locals(): # Only run this if score exists
    if score < 80:
        st.write("Score is low!")
