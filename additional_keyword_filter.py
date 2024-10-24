import streamlit as st
import pandas as pd

def additional_keyword_filter(df, category_name):
    st.subheader("Additional Keyword Filter")
    
    # Search Volume filter
    st.subheader("Search Volume")
    sv_options = ['Low', 'Medium', 'High']
    sv_filter = st.multiselect("Select Search Volume", sv_options, default=sv_options)
    
    # Keyword Difficulty filter
    st.subheader("Keyword Difficulty")
    kd_options = ['Low', 'Medium', 'High']
    kd_filter = st.multiselect("Select Keyword Difficulty", kd_options, default=kd_options)
    
    # CPC filter
    st.subheader("CPC")
    cpc_options = ['Low', 'Medium', 'High']
    cpc_filter = st.multiselect("Select CPC", cpc_options, default=cpc_options)
    
    # Category Keyword filter
    st.subheader("Category Keyword")
    category_filter_options = ["All", "Category Only", "Broad Category Only"]
    category_filter = st.radio("Filter category keywords", category_filter_options)
    
    # Apply filters
    filtered_df = df[
        (df['Search Volume Category'].isin(sv_filter)) &
        (df['Keyword Difficulty Category'].isin(kd_filter)) &
        (df['CPC Category'].isin(cpc_filter))
    ]
    
    # Display filtered results
    st.subheader("Filtered Keywords")
    
    # Convert boolean 'Is Long Tail' to 'Yes'/'No' for better readability
    filtered_df['Long Tail'] = filtered_df['Is Long Tail'].map({True: 'Yes', False: 'No'})
    
    st.dataframe(filtered_df[['Keyword', 'Volume', 'Keyword Difficulty', 'CPC (INR)', 'Intent', 'Long Tail', 'Is Category Keyword']])
    
    # Download filtered results as CSV
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download filtered keywords as CSV",
        data=csv,
        file_name="filtered_keywords.csv",
        mime="text/csv",
    )