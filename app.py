import streamlit as st
import pandas as pd
import os
import sys
from keyword_categorization import categorize_keywords
from keyword_analysis import perform_additional_analysis
from keyword_strategy import generate_keyword_strategy
from additional_keyword_filter import additional_keyword_filter  # Import analyze_serp_features

# Set page configuration to wide layout
st.set_page_config(layout="wide")

# Custom CSS to center content and position the rerun button
st.markdown("""
<style>
    .reportview-container .main .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 2rem;
    }
    .stButton button {
        position: fixed;
        top: 0.5rem;
        right: 0.5rem;
        z-index: 999;
    }
    #rerun-shortcut {
        display: none;
    }
</style>
<script>
    document.addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.key === 'r') {
            e.preventDefault();
            document.querySelector('.stButton button').click();
        }
    });
</script>
""", unsafe_allow_html=True)

def rerun_script():
    st.rerun()

def main():
    # Add the rerun button to the top right corner
    st.button("Rerun App (Ctrl+R)", on_click=rerun_script, key="rerun-button")
    
    # Use a container to center the content
    container = st.container()
    
    with container:
        st.title("Keyword Data Analysis")

        # Add a button to rerun the app
        if st.button("Rerun App"):
            rerun_script()

        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                
                # Check if all required columns are present
                required_columns = ['Keyword', 'Volume', 'Keyword Difficulty', 'CPC (INR)', 'Competitive Density']
                missing_columns = [col for col in required_columns if col not in df.columns]
                
                if missing_columns:
                    st.error(f"The following required columns are missing: {', '.join(missing_columns)}")
                    return

                # Perform categorization
                df = categorize_keywords(df)  # Removed the category_name argument

                st.subheader("Keyword Data Analysis")
                st.dataframe(df)

                # Create tabs
                tab1, tab2, tab3, tab4 = st.tabs(["Keyword Statistics", "Additional Analysis", "Keyword Strategy", "Keyword Filter"])

                with tab1:
                    st.subheader("Keyword Statistics")
                    
                    for category in ['Search Volume Category', 'Keyword Difficulty Category', 'CPC Category', 'Competitor Density Category', 'Intent']:
                        st.write(f"{category} Distribution:")
                        st.write(df[category].value_counts())

                with tab2:
                    perform_additional_analysis(df)

                with tab3:
                    generate_keyword_strategy(df)

                with tab4:
                    additional_keyword_filter(df)

            except Exception as e:
                st.error(f"An error occurred while processing the file: {str(e)}")
                st.error("Please make sure your CSV file has the correct format and column names.")

if __name__ == "__main__":
    main()