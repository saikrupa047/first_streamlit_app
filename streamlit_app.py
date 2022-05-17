import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

# import streamlit
streamlit.title('🥣 my parents new healthy diner!')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega & bluberry Oatmeal')
streamlit.text(' 🥗 kale, spinach and rocket smooothie')
streamlit.text('🐔 hard-boiled free-range egg')
streamlit.text('🥑🍞 avacado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("pick some fruits;", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error('please select a fruit to get information')
  else:
    fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  sreamlit.error()
streamlit.stop()


# import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("Hello from Snowflake:")
streamlit.dataframe(my_data_rows)

fruit_choice2 = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanks for adding',fruit_choice2)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
