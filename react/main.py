from dotenv import load_dotenv
from langchain.agents import tool
from langchain_core.prompts import PromptTemplate
from langchain.tools.render import render_text_description
from langchain_openai import ChatOpenAI

load_dotenv()


@tool
def get_text_length(text: str) -> int:
    """Returns the length of a text by characters"""
    print(f"get_text_length enter with {text=}")
    text = text.strip("'\n").strip('"')
    return len(text)


if __name__ == "__main__":
    print("Hello ReAct Langchain!")
    # print(get_text_length.description)
    # print(get_text_length.invoke(input={"text": "Sample"}))

    tools = [get_text_length]
    template = """
    Answer the following questions as best you can. You have access to the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    Begin!

    Question: {input}
    Thought:
    """

    prompt = PromptTemplate.from_template(template=template).partial(
        tools=render_text_description(tools),
        tool_names=", ".join([t.name for t in tools]),
    )

    llm = ChatOpenAI(temperature=0, stop=["\nObservation"])
    agent = {"input": lambda x: x["input"]} | prompt | llm

    invoke_result = agent.invoke(
        {"input": "What is the text length of 'Doggie' in characters?"}
    )
    print(invoke_result)
