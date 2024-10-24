from .base_strategy import BaseStrategy
import streamlit as st

class FacebookStrategy(BaseStrategy):
    def generate_short_term_strategy(self):
        # st.markdown("#### FB Ads Strategy")

        facebook_short = self.filter_dataframe(
            (self.df['Intent'].isin(['Commercial', 'Informational'])) & 
            (self.df['Search Volume Category'].isin(['Medium', 'High']))
        )
        facebook_short = self.add_reason(facebook_short, [
            (lambda x: x['Intent'] in ['Commercial', 'Informational'], "Suitable for awareness"),
            (lambda x: x['Search Volume Category'] in ['Medium', 'High'], "Popular topics")
        ])
        self.display_dataframe(facebook_short, "Short-Term Facebook Ad Keywords")

    def generate_long_term_strategy(self):
        # st.markdown("#### FB Ads Strategy")

        facebook_long = self.filter_dataframe(
            (self.df['Intent'].isin(['Commercial', 'Informational'])) & 
            (self.df['Search Volume Category'] == 'High') & 
            (self.df['Keyword Difficulty Category'] == 'High')
        )
        facebook_long = self.add_reason(facebook_long, [
            (lambda x: x['Intent'] in ['Commercial', 'Informational'], "Build brand awareness"),
            (lambda x: x['Search Volume Category'] == 'High', "High-volume topics"),
            (lambda x: x['Keyword Difficulty Category'] == 'High', "Competitive but valuable")
        ])
        self.display_dataframe(facebook_long, "Long-Term Facebook Ad Keywords")

# Add this line at the end of the file
__all__ = ['FacebookStrategy']