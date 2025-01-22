import streamlit as st 


st.markdown( """ 
            <style>
                /* Target the expander header */
                div[data-testid="stExpander"] > div:first-child {
                    background-color: #FAEBD7;
                    color: black;
                    font-size: 16px;
                    font-weight: bold;
                }
                /* Target the expander content */
                div[data-testid="stExpander"] > div:nth-child(2) {
                    background-color: red;
                    color: blue;
                    padding: 10px;
                    border: 1px solid #FAEBD7;
                }
            </style>
            """, 
            unsafe_allow_html=True )

with st.expander("*Gamah Upload Image*"): 
    st.write("Users can upload microscope slide images containing red blood cells (RBCs). The application supports various image formats for ease of use.") 