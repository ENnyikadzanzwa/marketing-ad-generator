import streamlit as st


from json import loads
from requests import post
st.set_page_config(
    page_title = "Emmanuel|Marketing Ad generator",
    page_icon = "🤖",
    layout ="wide"
    )

url = "https://api.openai.com/v1/chat/completions"
openai_api_key = st.secrets("API_KEY")
model_name = "gpt-3.5-turbo"  

headers = {
    "Authorization": f"Bearer {openai_api_key}"
}

def generate_marketing_ad(business_name, country, city, business_type):
    prompt = f"Create a marketing ad for a {business_type} named '{business_name}' located in {city}, {country}."
    data = {
         "model": model_name,
         "messages": [
        {
            "role": "system",
            "content": "Hello, how can I assist you?"
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
   
    
        }
    response = post(url, json=data, headers=headers)
    information = loads(response.text)
    data = information['choices'][0]['message']['content']
    return data

# Streamlit app
st.title("Business Marketing Ad Generator")
column,col2 = st.columns(2)
with column:
    business_name = st.text_input("Enter the business name:")
    country = st.text_input("Enter the country:")
    city = st.text_input("Enter the city:")
    business_type = st.text_input("Enter the type of business:")
    x=st.button("Generate Ad")
with col2:
    if x:
        if business_name and country and city and business_type:
            try:
                ad = generate_marketing_ad(business_name, country, city, business_type)
                st.write(ad)
            except Exception as e:
                st.warning(e)
        else:
            st.write("Please fill in all the fields.")

