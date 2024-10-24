from .base_strategy import BaseStrategy
import streamlit as st

class LandingPageStrategy(BaseStrategy):
    def generate_short_term_strategy(self):
        # st.markdown("### Landing Page Strategy - Short-Term Focus")

        landing_short = self.filter_dataframe(
            ((self.df['Intent'] == 'Transactional') &
            (self.df['Search Volume Category'] == 'Medium') & 
            (self.df['Keyword Difficulty Category'] == 'Medium') & 
            (self.df['CPC Category'].isin(['Medium', 'High']))) |
            (self.df['Contains Location'] == True)
        )
        landing_short = self.add_reason(landing_short, [
            (lambda x: x['Intent'] == 'Transactional', "High intent"),
            (lambda x: x['Search Volume Category'] == 'Medium', "Moderate search volume"),
            (lambda x: x['Keyword Difficulty Category'] == 'Medium', "Moderate difficulty"),
            (lambda x: x['CPC Category'] in ['Medium', 'High'], "Good CPC potential"),
            (lambda x: x['Contains Location'], "Location-specific keyword")
        ])
        self.display_dataframe(landing_short, "Short-Term Landing Page Keywords")

    def generate_long_term_strategy(self):
        # st.markdown("### Landing Page Strategy - Long-Term Focus")

        landing_long = self.filter_dataframe(
            (self.df['Intent'] == 'Informational') | 
            (self.df['Search Volume Category'] == 'High') |
            (self.df['Keyword Difficulty Category'] == 'High') |
            (self.df['CPC Category'] == 'Low')
        )
        landing_long = self.add_reason(landing_long, [
            (lambda x: x['Intent'] == 'Informational', "Informational content"),
            (lambda x: x['Search Volume Category'] == 'High', "High search volume"),
            (lambda x: x['Keyword Difficulty Category'] == 'High', "Competitive but valuable"),
            (lambda x: x['CPC Category'] == 'Low', "Build authority")
        ])
        self.display_dataframe(landing_long, "Long-Term Landing Page Keywords")