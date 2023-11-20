import streamlit as st
from generate_text import generate_summary

def main():
    st.title('Özet Çıkarma')

    input_text = st.text_area('Metni buraya yaz...')

    if st.button("Özetiliyor...."):
        # Process the input text
        processed_text = generate_summary(input_text, 3)

        # Display the processed text
        st.subheader("Processed Text:")
        st.write(processed_text)


if __name__ == '__main__':
    main()