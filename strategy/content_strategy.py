from .base_strategy import BaseStrategy
import streamlit as st

class ContentStrategy(BaseStrategy):
    def generate_short_term_strategy(self):
        st.markdown("#### Content Strategy")

        content_short = self.filter_dataframe(
            (self.df['Intent'] == 'Informational') & 
            (self.df['Is Long Tail'] == True) & 
            (self.df['Is Question'] == True)
        )
        content_short = self.add_reason(content_short, [
            (lambda x: x['Intent'] == 'Informational', "Informational content"),
            (lambda x: x['Is Long Tail'], "Specific user intent"),
            (lambda x: x['Is Question'], "Addresses user queries")
        ])
        self.display_dataframe(content_short, "Short-Term Content Keywords")

    def generate_long_term_strategy(self):
        st.markdown("#### Content Strategy")

        content_long = self.filter_dataframe(
            (self.df['Intent'] == 'Informational') & 
            (self.df['Is Long Tail'] == True)
        )
        content_long = self.add_reason(content_long, [
            (lambda x: x['Intent'] == 'Informational', "Informational content"),
            (lambda x: x['Is Long Tail'], "Specific user intent")
        ])
        self.display_dataframe(content_long, "Long-Term Content Keywords")