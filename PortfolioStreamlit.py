import streamlit as st

def main():
    st.title("Embedded HTML Portfolio")

    # Replace the URL with the actual URL of your HTML file or hosted website
    html_url = "https://github.com/VishRIV03/VishRIV03/blob/49d806f7e111fab5344b4f5ad17469f4131f9014/PORTFOLIO.html"

    # Use iframe to embed the HTML content
    st.markdown(f'<iframe src="{html_url}" width="800" height="600"></iframe>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
