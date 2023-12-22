import streamlit

streamlit.title("My Mom's New Healthy Dinner")

streamlit.header('Breakfast favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import streamlit as st
import pandas as pd
import requests

# Assuming my_fruit_list is a pandas DataFrame
my_fruit_list = pd.DataFrame({'Fruit': ['Apple', 'Banana', 'Orange']})

# Display the table on the page.
st.dataframe(my_fruit_list)

# New Section to display fruityvice api response
st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input('What fruit would you like information about?', 'Kiwi')
st.write('The user entered ', fruit_choice)

# Make the API request and check for success
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
if fruityvice_response.status_code == 200:
    # Import the pandas module and normalize the JSON response
    import pandas as pd
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    # Display the normalized data
    st.dataframe(fruityvice_normalized)
else:
    st.write(f"Fruityvice API request failed with status code: {fruityvice_response.status_code}")

# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = st.multiselect("Pick some fruits:", my_fruit_list['Fruit'].tolist(), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list[my_fruit_list['Fruit'].isin(fruits_selected)]

# Display the table on the page.
st.dataframe(fruits_to_show)

# New section to display fruityvice api response
st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input('What fruit would you like information about?', 'Kiwi')
st.write('The user entered ', fruit_choice)

# import Snowflake connector
import snowflake.connector


