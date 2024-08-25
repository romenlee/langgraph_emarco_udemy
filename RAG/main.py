from dotenv import load_dotenv
import os
load_dotenv()
os.environ["LANGCHAIN_PROJECT"] = 'lenggraph RAG'
from pprint import pprint
from graph.graph import app

question1 = "What are the types of agent memory?"
# question1 = "What is agent memory?"
# question1 = "What to make pizza?"
inputs = {"question": question1}
pprint(app.invoke(input=inputs))
for output in app.stream(inputs, config={"configurable": {"thread_id": "2"}}):
    for key, value in output.items():
        pprint(f"Finished running: {key}:")
pprint(value["generation"])
