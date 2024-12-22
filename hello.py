from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    print("Hello LangChain!")
    print(os.environ["OPENAI_API_KEY"])
