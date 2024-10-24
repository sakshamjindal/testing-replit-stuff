import streamlit as st
import pandas as pd
import numpy as np


def perform_additional_analysis(df):
    st.subheader("Additional Keyword Analysis")

    # Display the top 10 keywords by volume
    st.write("Top 10 Keywords by Volume:")
    top_10_volume = df.nlargest(10, 'Volume')[['Keyword', 'Volume']]
    st.table(top_10_volume)

    # Create a scatter plot of Volume vs Keyword Difficulty
    # fig = px.scatter(df, x='Keyword Difficulty', y='Volume', hover_data=['Keyword'])
    # st.plotly_chart(fig)

    # Display the distribution of intent
    st.write("Distribution of Intent:")
    intent_distribution = df['Intent'].value_counts()
    st.bar_chart(intent_distribution)

    # Display the average CPC by intent
    st.write("Average CPC by Intent:")
    avg_cpc_by_intent = df.groupby('Intent')['CPC (INR)'].mean().sort_values(ascending=False)
    st.bar_chart(avg_cpc_by_intent)

    # Display the correlation matrix
    st.write("Correlation Matrix:")
    correlation_matrix = df[['Volume', 'Keyword Difficulty', 'CPC (INR)', 'Competitive Density']].corr()
    st.table(correlation_matrix)

    # Display the filtered dataframe
    st.dataframe(df[['Keyword', 'Volume', 'Keyword Difficulty', 'CPC (INR)']])

    # SERP Feature Analysis
    # analyze_serp_features(df)

def analyze_serp_features(df):
    st.subheader("SERP Feature Analysis")

    # Check if the 'SERP Features' column exists
    if 'SERP Features' not in df.columns:
        st.warning("The 'SERP Features' column is missing from the data. SERP analysis cannot be performed.")
        return

    # Extract unique SERP features
    serp_features = df['SERP Features'].fillna('').str.split(',', expand=True).stack().unique()

    # Create a dictionary to store the analysis results
    serp_analysis = {}

    # Analyze each SERP feature
    for feature in serp_features:
        if feature:  # Skip empty strings
            feature_keywords = df[df['SERP Features'].fillna('').str.contains(feature, case=False, na=False)]
            serp_analysis[feature] = {
                'Count': len(feature_keywords),
                'Average Volume': feature_keywords['Volume'].mean(),
                'Average Keyword Difficulty': feature_keywords['Keyword Difficulty'].mean(),
                'Average CPC': feature_keywords['CPC (INR)'].mean()
            }

    # Display the analysis results
    for feature, stats in serp_analysis.items():
        st.write(f"**{feature}**")
        st.write(f"Count: {stats['Count']}")
        st.write(f"Average Volume: {stats['Average Volume']:.2f}")
        st.write(f"Average Keyword Difficulty: {stats['Average Keyword Difficulty']:.2f}")
        st.write(f"Average CPC: {stats['Average CPC']:.2f}")
        st.write("---")
