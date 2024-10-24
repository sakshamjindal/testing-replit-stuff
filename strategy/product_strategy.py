from .base_strategy import BaseStrategy
import streamlit as st
import pandas as pd

class ProductStrategy(BaseStrategy):
    def generate_short_term_strategy(self):
        product_short = self.filter_dataframe(
            ((self.df['Categorised'].str.contains("product", case=False)) |
            (self.df['Is Product Specific'] == True)) &
            ((self.df['Intent'].isin(['Transactional', 'Commercial'])) |
            ((self.df['Search Volume Category'].isin(['High', 'Medium'])) &
            (self.df['Keyword Difficulty Category'] == 'Low')) |
            (self.df['CPC Category'].isin(['Medium', 'High'])))
        )        
        product_short = self.add_reason(product_short, [
            (lambda x: x['Is Product Specific'] == True, "Product specific keyword"),
            (lambda x: x['Intent'] in ['Transactional', 'Commercial'], "High purchase intent"),
            (lambda x: x['Search Volume Category'] in ['Medium', 'High'], "Good search volume"),
            (lambda x: x['Keyword Difficulty Category'] in ['Low', 'Medium'], "Low difficulty"),
            (lambda x: x['CPC Category'] in ['Low', 'Medium', 'High'], "Good CPC potential")
        ])
        
        # write the number of keywords in the dataframe
        self.display_dataframe(self.prepare_dataframe(product_short), "Short-Term Product Keywords")
        
        # st.markdown("### Short-Term Product Strategy")
        # st.markdown("""
        # The short-term product strategy focuses on identifying keywords that are product-specific and have high purchase intent. 
        # These keywords are filtered based on their categorization as product-specific, transactional, or commercial intent, 
        # and their search volume and keyword difficulty. The goal is to target keywords with good search volume and low difficulty, 
        # as well as those with good CPC potential.
        # """)

        st.write(f"Number of keywords: {len(product_short)}")

        # Add a new section for short-term long-tail product keywords
        product_short_long_tail = self.filter_dataframe(
            (self.df['Is Long Tail'] == True) &
            (self.df['Is Product Specific'] == True) &
            (self.df['Search Volume Category'].isin(['Low', 'Medium']))
        )
        product_short_long_tail = self.add_reason(product_short_long_tail, [
            (lambda x: x['Is Long Tail'] == True, "Long-tail keyword"),
            (lambda x: x['Is Product Specific'] == True, "Product specific"),
            (lambda x: x['Search Volume Category'] in ['Low', 'Medium'], "Targeted search volume"),
            (lambda x: x['Keyword Difficulty Category'] in ['Low', 'Medium'], "Lower competition")
        ])

        self.display_dataframe(self.prepare_dataframe(product_short_long_tail), "Short-Term Long-Tail Product Keywords")
        st.write(f"Number of long-tail keywords: {len(product_short_long_tail)}")

        # product_long_tail_long = self.filter_dataframe(
        #     (self.df['Is Long Tail'] == True) &
        #     (self.df['Search Volume Category'].isin(['Low']))
        # )
        # product_long_tail_long['Reason'] = "Long-tail keyword with low search volume"
        # self.display_dataframe(self.prepare_dataframe(product_long_tail_long), "Long-tail Product Keywords")

    def generate_long_term_strategy(self):
        product_long = self.filter_dataframe(
            (self.df['Search Volume Category'] == 'Medium') & 
            (self.df['Keyword Difficulty Category'] == 'Medium') & 
            (self.df['CPC Category'] == 'Medium') &
            (self.df['Is Long Tail'] == False)
        )
        product_long = self.add_reason(product_long, [
            (lambda x: x['Search Volume Category'] == 'Medium', "Steady search volume"),
            (lambda x: x['Keyword Difficulty Category'] == 'Medium', "Competitive but achievable"),
            (lambda x: x['CPC Category'] == 'Medium', "Balanced CPC")
        ])
        self.display_dataframe(self.prepare_dataframe(product_long), "Long-Term Product Keywords")

        # Add a new section for long-term long-tail product keywords
        product_long_long_tail = self.filter_dataframe(
            (self.df['Is Long Tail'] == True) &
            (self.df['Is Product Specific'] == True) &
            (self.df['Search Volume Category'].isin(['Medium', 'High'])) &
            (self.df['Keyword Difficulty Category'].isin(['Medium', 'High']))
        )
        product_long_long_tail = self.add_reason(product_long_long_tail, [
            (lambda x: x['Is Long Tail'] == True, "Long-tail keyword"),
            (lambda x: x['Is Product Specific'] == True, "Product specific"),
            (lambda x: x['Search Volume Category'] in ['Medium', 'High'], "Good search potential"),
            (lambda x: x['Keyword Difficulty Category'] in ['Medium', 'High'], "Competitive but valuable")
        ])
        
        self.display_dataframe(self.prepare_dataframe(product_long_long_tail), "Long-Term Long-Tail Product Keywords")
        st.write(f"Number of long-term long-tail keywords: {len(product_long_long_tail)}")

    def prepare_dataframe(self, df):
        # Convert all columns to strings
        for col in df.columns:
            df[col] = df[col].astype(str)
        return df

