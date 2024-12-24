from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from third_parties.linkedin import scrape_linkedin_profile
import os

if __name__ == "__main__":
    print("Starting LangChain App!")

    load_dotenv()

    summary_template = """\
Given the Linkedin information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
"""

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOllama(model="llama3")

    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_data = scrape_linkedin_profile(None, mock=True)
    res = chain.invoke(input={"information": linkedin_data})

    print(res)
