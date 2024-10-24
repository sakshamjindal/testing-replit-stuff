import streamlit as st
import pandas as pd
from utils import add_reason

class BaseStrategy:
    def __init__(self, df):
        self.df = df

    def display_dataframe(self, filtered_df, title, description=""):
        st.markdown(f"##### {title}")
        if description: 
            st.markdown(description)
        
        # Reset index and start from 1
        display_df = filtered_df.reset_index(drop=True)
        display_df.index += 1
        
        st.dataframe(display_df[['Keyword', 'Volume', 'Keyword Difficulty', 'CPC (INR)', 'Reason']])

    def filter_dataframe(self, conditions):
        return self.df[conditions].sort_values('Volume', ascending=False)

    def add_reason(self, filtered_df, reason_conditions):
        filtered_df['Reason'] = add_reason(filtered_df, reason_conditions)
        return filtered_df

    def generate_strategy(self):
        raise NotImplementedError("Subclasses must implement generate_strategy method")