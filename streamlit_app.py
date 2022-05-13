import streamlit
streamlit.title('🥣 my parents new healthy diner!')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega & bluberry Oatmeal')
streamlit.text(' 🥗 kale, spinach and rocket smooothie')
streamlit.text('🐔 hard-boiled free-range egg')
streamlit.text('🥑🍞 avacado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("pick some fruits;", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
