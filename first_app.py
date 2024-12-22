from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

information = """\
Chester Charles Bennington (March 20, 1976 – July 20, 2017) was an American singer who was the lead vocalist of the rock band Linkin Park. He was also the lead vocalist of Grey Daze, Dead by Sunrise, and Stone Temple Pilots at various points.

Bennington first gained prominence as a vocalist following the release of Linkin Park's debut album, Hybrid Theory (2000), which was a worldwide commercial success. The album was certified Diamond by the Recording Industry Association of America in 2005, making it the bestselling debut album of the decade, as well as one of the few albums ever to achieve that many sales.[2] He continued as the band's lead vocalist for their next six studio albums, from Meteora (2003) to One More Light (2017), with each charting within the top three spots of the Billboard 200.[3][4]

Bennington formed his own band, Dead by Sunrise, as a side project in 2005. The band's debut album, Out of Ashes, was released on October 13, 2009. He became the lead singer of Stone Temple Pilots in 2013 to release the extended play record High Rise on October 8, 2013, via their own record label, Play Pen, but left in 2015 to focus solely on Linkin Park. As an actor, he appeared in films such as Crank (2006), Crank: High Voltage (2009), and Saw 3D (2010).

Bennington struggled with depression and substance abuse for most of his life, starting in his childhood. On July 20, 2017, he was found dead at his home in Palos Verdes Estates, California. The coroner concluded that his death was a result of suicide by hanging. Hit Parader magazine placed Bennington at number 46 on their list of the "Top 100 Metal Vocalists of All Time."[5] Bennington has been ranked by several publications as one of the greatest rock vocalists of his generation.[6] Writing for Billboard, Dan Weiss stated that Bennington "turned nu-metal universal."[7]
"""
model_name = "gpt-3.5-turbo"

if __name__ == "__main__":
    print("Starting LangChain App!")

    load_dotenv()

    summary_template = """\
Given the information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
"""

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name=model_name)

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})

    print(res)
