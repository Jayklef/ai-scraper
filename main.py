import streamlit as st
from scrape import scrape_website,split_dom_content, clean_data, extract_content


st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL:")


if st.button("Scrape website"):
    st.write("Scraping the website")
    result = scrape_website(url)
    
    body_content = extract_content(result)
    clean_data = clean_data(body_content)
    
    
    st.session_state.dom_content = clean_data
    
    
    # expand to view more content
    with st.expander("View Dom content"):
        st.text_area("Dom content", clean_data, height=300)
   