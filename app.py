import streamlit as st
import pandas as pd
from difflib import SequenceMatcher
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
data=pd.read_csv('symptoms_herbal_remedies_1000.csv')
traditional_df=pd.read_csv('traditional_remedies_1000.csv')
merged_df = pd.merge(data,traditional_df, on="Symptom")
print("Merged columns:", merged_df.columns.tolist())
st.set_page_config(page_title="AI vs Ayurveda", layout="centered")

st.title("🌿 AI vs Ayurveda: Herbal Remedy Predictor")
st.write("Enter a symptom to compare AI-suggested herbal remedies with traditional Ayurvedic solutions.")
symptom_input = st.text_input("🔍 Enter your symptom:")
if symptom_input:
    # Lowercase the input for comparison
    symptom_input_lower = symptom_input.lower()

    # Try to match the symptom in your dataset
    match = merged_df[merged_df['Symptom'].str.lower() == symptom_input_lower]

    if not match.empty:
        herbal = match.iloc[0]['Herbal_Remedies']
        traditional = match.iloc[0]['Traditional_Remedies']
        # Similarity Score
        score = SequenceMatcher(None, str(herbal), str(traditional)).ratio()
        percent = round(score * 100, 2)

        # Display Results
        st.subheader("💡 Results:")
        st.markdown(f"**AI Suggested Remedy:** {herbal}")
        st.markdown(f"**Traditional Remedy:** {traditional}")
        st.markdown(f"**Similarity Score:** `{percent}%`")

        # Optional: Comparison Graph
        st.subheader("📊 Visual Similarity Score")
        fig, ax = plt.subplots()
        ax.bar(["Similarity Score"], [score], color="skyblue")
        ax.set_ylim(0, 1)
        ax.set_ylabel("Score (0 to 1)")
        ax.set_title("Similarity Between AI and Traditional Remedies")
        st.pyplot(fig) 
        set1 = set(str(herbal).replace(',', '').lower().split())
        set2 = set(str(traditional).replace(',', '').lower().split())
        st.subheader("🔍 Remedy Ingredient Overlap")
        fig2, ax2 = plt.subplots()
        venn2([set1, set2], set_labels=('AI Remedies', 'Traditional Remedies'))
        st.pyplot(fig2)

    else:
        st.warning("Symptom not found. Please try another.")

# Optional: Show Table for Summary
st.markdown("---")
st.subheader("📋 Full Remedy Comparison Table")

# Calculate similarity for all (using merged_df instead of data)
def compute_similarity(row):
    return round(SequenceMatcher(None, str(row['Herbal_Remedies']), str(row['Traditional_Remedies'])).ratio() * 100, 2)

merged_df["Similarity (%)"] = merged_df.apply(compute_similarity, axis=1)
st.dataframe(merged_df[["Symptom", "Herbal_Remedies", "Traditional_Remedies", "Similarity (%)"]])
