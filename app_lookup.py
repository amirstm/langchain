from typing import Tuple
from dotenv import load_dotenv
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from output_parsers import summary_parser, Summary


def custom_lookup(name: str) -> Tuple[Summary, str]:
    linkedin_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_url, mock=True
    )

    summary_template = """\
Given the information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
{format_instructions}
"""

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    chain = summary_prompt_template | llm | summary_parser
    res: Summary = chain.invoke(input={"information": linkedin_data})

    return res, linkedin_data["profile_pic_url"]


if __name__ == "__main__":
    load_dotenv()
    print("Hello langchain!")

    custom_lookup("Amir Zare Physics Olympiad")
