import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
# import pandas_gbq as pd_gbq
import json

# # Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)

project_id = credentials.project_id
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

st.write(project_id)
st.caption('test')
# Perform query.
# query = """SELECT * FROM bt4301.ttao.salaries LIMIT 10"""

# salary_df = pd_gbq.read_gbq(query, project_id= project_id)
# st.dataframe(salary_df)

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    query_job = client.query(query)
    df = query_job.to_dataframe()
    return df
# def run_query(query):
#     query_job = client.query(query)
#     rows_raw = query_job.result()
#     # Convert to list of dicts. Required for st.cache_data to hash the return value.
#     rows = [dict(row) for row in rows_raw]
#     return rows


df = run_query("""SELECT * FROM bt4301.ttao.salaries LIMIT 10""")
st.dataframe(df)
# # Print results.
# st.write("Some wise words from Shakespeare:")
# for row in rows:
#     st.write(row)