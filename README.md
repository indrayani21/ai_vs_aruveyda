🌿 AI vs Ayurveda: Herbal Remedy Comparator
“Blending the intelligence of machines with the wisdom of ancient healing traditions.”

📌 Project Objective
This project explores the intersection of Artificial Intelligence and Ayurveda by building an interactive Streamlit web application that compares AI-suggested herbal remedies with Traditional Ayurvedic treatments based on user-input symptoms.
The goal is to:
->Provide transparent comparison between modern AI-driven predictions and time-tested natural remedies.
->Promote awareness of herbal treatment options and explore how machine learning can adapt traditional wisdom.
->Offer a data-driven perspective on the similarity and uniqueness of each remedy.

📊 Dataset Description
Two CSV datasets are used:
->symptoms_herbal_remedies_1000.csv
->Contains symptom keywords and their AI-generated herbal treatment suggestions.
->Columns: Symptom, Herbal_Remedies
traditional_remedies_1000.csv
->Contains the same symptoms but with Traditional Ayurvedic remedies curated from historical or natural medicine references.
->Columns: Symptom, Traditional_Remedies

These datasets are merged on the Symptom column to create a side-by-side comparison of AI and Traditional remedies.

🚀 Features
🔍 Symptom-based Remedy Finder
->Users can type any symptom (e.g., cough, headache, indigestion).
->The app retrieves both AI and Traditional remedies mapped to that symptom.

🤖 AI vs Ayurveda Comparison
Displays:
->AI-suggested Herbal Remedy
->Traditional Remedy
->Similarity Score based on difflib's sequence comparison algorithm (a measure of textual overlap between the two remedies).

📊 Graphical Visualization
->Bar Chart to compare remedies side-by-side in a visually digestible format.
->Venn Diagram using matplotlib-venn to show overlapping and unique ingredients between AI and traditional remedies.

🧮 Full Remedy Table
->Displays all symptoms with:
->Corresponding AI and Traditional remedies
->Computed Similarity Score (%) for quick scanning and insights

💡 Technologies Used
->Python
->Streamlit – for building the web interface
->Pandas – data handling
->matplotlib & matplotlib-venn – visualization
->difflib – similarity score computation

"Ancient roots, modern insights – unlocking wellness through data." 🌱
