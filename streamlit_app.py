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
my_fruit_list=my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("pick some fruits;", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/watermelon")

streamlit.text(fruityvice_response)
