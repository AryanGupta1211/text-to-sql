from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from db import query_db
import streamlit as st

data_analyst_prompt = '''
You are a data analyst working with a database named "customers". This database has a single table named "customers" with the following columns:

customer_id: INT (Primary Key)
first_name: VARCHAR(50)
last_name: VARCHAR(50)
email: VARCHAR(100)
phone: VARCHAR(15)
address: VARCHAR(255)
city: VARCHAR(50)
join_date: DATE
Your task is to translate the following prompt {prompt} into a single, accurate SQL query that retrieves relevant data from the "customers" table. Please do not generate explanations or additional information. If the prompt is irrelevant to the data available, notify me.

'''

data_analyst_template = PromptTemplate(
    input_variables=["prompt"],
    template=data_analyst_prompt
)

gemma = Ollama(model="gemma")

llm_chain = LLMChain(llm=gemma, prompt=data_analyst_template) 

def query_llm(prompt):
    print(llm_chain.invoke({"prompt":prompt})["text"])
    
def extract_sql_code(input_string):
    sql_code = input_string.replace("```sql", "").replace("```", "").strip()
    return sql_code


st.title("Data Query Expert")
user_input = st.text_input("Enter the Prompt....")

if st.button("Extract Data"):
    result = query_llm(user_input)
    sql_query = extract_sql_code(result)
    st.table(query_db(sql_query))