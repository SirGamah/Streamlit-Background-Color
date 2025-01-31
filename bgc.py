import streamlit as st 


st.markdown( """ 
            <style>
                /* Target the expander header */
                div[data-testid="stExpander"] > details > summary {
                    background-color: #FAEBD7;
                    color: black;
                    font-size: 16px;
                    font-weight: bold;
                }
                /* Target the expander content */
                div[data-testid="stExpander"] > details > div {
                    background-color: white;
                    color: blue;
                    padding: 10px;
                    border: 1px solid #FAEBD7;
                }
            </style>
            """, 
            unsafe_allow_html=True )

with st.expander("*Gamah Upload Image*"): 
    st.write("Users can upload microscope slide images containing red blood cells (RBCs). The application supports various image formats for ease of use.") 
