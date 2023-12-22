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
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
# Generated on: Python 3.9.18
asn1crypto==1.5.1
certifi==2023.11.17
cffi==1.16.0
charset-normalizer==3.3.2
cryptography==41.0.7
filelock==3.13.1
idna==3.6
packaging==23.2
platformdirs==3.11.0
pycparser==2.21
PyJWT==2.8.0
pyOpenSSL==23.3.0
pytz==2023.3.post1
requests==2.31.0
sortedcontainers==2.4.0
tomlkit==0.12.3
typing_extensions==4.8.0
urllib3==1.26.18
snowflake-connector-python==3.6.0

#import connector
import snowflake.connector
