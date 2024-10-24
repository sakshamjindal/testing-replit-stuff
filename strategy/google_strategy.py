from .base_strategy import BaseStrategy
import streamlit as st

class GoogleStrategy(BaseStrategy):
    def generate_short_term_strategy(self):
        # st.markdown("### Google Ads Strategy - Short-Term Focus")

        google_short = self.filter_dataframe(
            (self.df['Intent'] == 'Transactional') & 
            (self.df['Keyword Difficulty Category'] == 'Low') & 
            (self.df['Is Long Tail'] == True)
        )
        google_short = self.add_reason(google_short, [
            (lambda x: x['Intent'] == 'Transactional', "High purchase intent"),
            (lambda x: x['Keyword Difficulty Category'] == 'Low', "Lower competition"),
            (lambda x: x['Is Long Tail'], "Specific user intent")
        ])
        self.display_dataframe(google_short, "Short-Term Google Ad Keywords")

    def generate_long_term_strategy(self):
        # st.markdown("### Google Ads Strategy - Long-Term Focus")

        google_long = self.filter_dataframe(
            (self.df['Intent'] == 'Transactional') & 
            (self.df['Search Volume Category'] == 'High') & 
            (self.df['Keyword Difficulty Category'] == 'High')
        )
        google_long = self.add_reason(google_long, [
            (lambda x: x['Intent'] == 'Transactional', "High purchase intent"),
            (lambda x: x['Search Volume Category'] == 'High', "High-volume keywords"),
            (lambda x: x['Keyword Difficulty Category'] == 'High', "Competitive but valuable")
        ])
        self.display_dataframe(google_long, "Long-Term Google Ad Keywords")