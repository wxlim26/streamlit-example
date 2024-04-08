import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
import pandas_gbq as pd_gbq

# # Create API client.
# credentials = service_account.Credentials.from_service_account_info(
#     st.secrets["gcp_service_account"]
# )
# client = bigquery.Client(credentials=credentials)


# directory to privatekey.json
cred = "secrets/privatekey.json"
credentials = service_account.Credentials.from_service_account_file(f"{cred}")
client = bigquery.Client(credentials=credentials, project=credentials.project_id)
project_id = credentials.project_id

# Perform query.
query = """SELECT * FROM bt4301.ttao.salaries LIMIT 10"""

salary_df = pd_gbq.read_gbq(query, project_id= project_id)
st.dataframe(salary_df)