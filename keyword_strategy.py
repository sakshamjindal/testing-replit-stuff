import streamlit as st
from strategy import (
    ProductStrategy,
    CategoryStrategy,
    LandingPageStrategy,
    FacebookStrategy,
    GoogleStrategy,
    ContentStrategy
)

def generate_keyword_strategy(df):
    st.subheader("Keyword Strategy")

    # st.markdown("### Product, Category, and Landing Pages")
    # Short-Term Focus
    st.markdown("### Short-Term Focus")

    LandingPageStrategy(df).generate_short_term_strategy()
    CategoryStrategy(df).generate_short_term_strategy()
    ProductStrategy(df).generate_short_term_strategy()


    st.markdown("### Facebook and Google Ads")
    FacebookStrategy(df).generate_short_term_strategy()
    GoogleStrategy(df).generate_short_term_strategy()

    st.markdown("### Content Strategy")
    ContentStrategy(df).generate_short_term_strategy()

    # Long-Term Focus
    st.markdown("## Long-Term Focus")

    st.markdown("### Product, Category, and Landing Pages")
    ProductStrategy(df).generate_long_term_strategy()
    CategoryStrategy(df).generate_long_term_strategy()
    LandingPageStrategy(df).generate_long_term_strategy()

    st.markdown("### Facebook and Google Ads")
    FacebookStrategy(df).generate_long_term_strategy()
    GoogleStrategy(df).generate_long_term_strategy()

    st.markdown("### Content Strategy")
    ContentStrategy(df).generate_long_term_strategy()