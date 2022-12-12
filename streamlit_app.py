import streamlit
import pandas

streamlit.title('My Parents New Healty Diner')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')

streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')

streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index[0]),['Avocado', 'Strawberries'])
#fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.columns[0]),['Avocado', 'Strawberries'])
#streamlit.dataframe(my_fruit_list.index[0])
#fruits_selected = streamlit.multiselect("Pick some fruits:", ['Mango', 'Avocado', 'Strawberries', 'Banana'],['Avocado', 'Strawberries'])

# Display the table on the page.
#streamlit.dataframe(my_fruit_list)
