from .base_strategy import BaseStrategy
import streamlit as st

class CategoryStrategy(BaseStrategy):
    def __init__(self, df):
        super().__init__(df)

    def generate_short_term_strategy(self):
        # st.markdown(f"#Category Page Strategy (for '{self.category_name}') - Short-Term Focus")
        # st.markdown("#### Category Page Strategy")

        category_short = self.filter_dataframe(
            (self.df['Categorised'].str.contains("category", case=False)) &
            ((self.df['Search Volume Category'].isin(['Medium', 'High'])) &
            (self.df['Keyword Difficulty Category'].isin(['Low', 'Medium'])))
        )
        category_short = self.add_reason(category_short, [
            (lambda x: x['Search Volume Category'] in ['Medium', 'High'], "Good search volume"),
            (lambda x: x['Keyword Difficulty Category'] in ['Low', 'Medium'], "Low difficulty")
        ])

        self.display_dataframe(category_short, "Short-Term Category Keywords")
        # write the number of keywords in the dataframe
        st.write(f"Number of keywords: {len(category_short)}")

    def generate_long_term_strategy(self):
        # st.markdown("#### Category Page Strategy")

        category_long = self.filter_dataframe(
            (self.df['Search Volume Category'] == 'High') & 
            (self.df['Keyword Difficulty Category'] == 'High') & 
            (self.df['CPC Category'].isin(['Medium', 'High']))
        )
        category_long = self.add_reason(category_long, [
            (lambda x: x['Search Volume Category'] == 'High', "High search volume"),
            (lambda x: x['Keyword Difficulty Category'] == 'High', "Competitive but valuable"),
            (lambda x: x['CPC Category'] in ['Medium', 'High'], "Good CPC potential")
        ])
        self.display_dataframe(category_long, "Long-Term Category Keywords")