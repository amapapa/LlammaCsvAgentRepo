import streamlit as st
from langchain_experimental.agents import (
    create_csv_agent,
    create_pandas_dataframe_agent,
)
import pandas as pd
from langchain_community.llms import OpenAI

# from langchain.llms import OpenAI
from dotenv import load_dotenv


def main():
    load_dotenv()

    st.set_page_config(
        page_title="CsvAgentRepo-TM ", page_icon=":chart:", layout="wide"
    )
    st.header("Ask Your CSV :chart:")
    # print("Hello, this is a test for the LlamaCsvAgentRepo.")

    user_csv = st.file_uploader("Upload your CSV file", type=["csv"])

    if user_csv is not None:
        user_question = st.text_input("Ask a question about your CSV file")

        llm = OpenAI(temperature=0)
        agent = create_csv_agent(
            llm=llm,
            path=user_csv,
            # df=pd.read_csv(user_csv),
            verbose=True,
            agent_type="openai-tools",
            allow_dangerous_code=True,  # Set to True to allow dangerous code execution
        )

        if user_question is not None and user_question != "":
            st.write("You asked: ", user_question)
            response = agent.run(user_question)
            st.write("Agent response: ", response)


if __name__ == "__main__":
    main()
