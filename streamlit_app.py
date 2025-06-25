# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests


cnx=st.connection("snowflake")
session=cnx.session()


# Write directly to the app
st.title(f"Customize Your Smoothie!:cup_with_straw:")
st.write(
  """
  **Choose the fruits you want in your Custom Smoothie !**.
  """
)




name_on_order = st.text_input("Name on Smoothie")
st.write("The name on your smoothie will be : ", name_on_order)


my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))


ingredient_list = st.multiselect(
    "Choisir le top 5 des ingredients",
    my_dataframe,
    max_selections=5
)

if ingredient_list:

    ingredient_string=''
    
    for fruit_chosen in ingredient_list :
        ingredient_string += fruit_chosen + ' '
        st.subheader(fruit_chosen + 'Nutrition Information')
        smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/" + fruit_chosen)
#st.text(smoothiefroot_response.json())
        sf_df=st.dataframe(data=smoothiefroot_response.json(),use_container_width=True)

   # st.write(ingredient_string)
  


    my_insert_stmt = """ 
    
                            insert into smoothies.public.orders(ingredients, name_on_order)
                            values ('""" + ingredient_string + """', '"""+name_on_order+ """')
                      
                      """
    # st.write(my_insert_stmt)
    # st.stop()

    time_to_insert=st.button('Submit order')

    if time_to_insert :
        session.sql(my_insert_stmt).collect()
        
        st.success('Votre smoothie a été commandé,name_on_order', icon="✅")

#st.write(my_insert_stmt)









    
