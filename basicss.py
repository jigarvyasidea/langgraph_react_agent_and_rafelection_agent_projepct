from typing import List
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph
from chain import generation_chain, reflection_chain



# Now we load the API KEY 

load_dotenv()


# now we dealing with message graph for complex task we deal with stategraph 
graph = MessageGraph()

REFLECT = "reflect"
GENERATE = "generate"

# now we create then first node of langgraph 

def generate_node(state: list[BaseMessage])--> list[BaseMessage]
    responce = generation_chain.invoke({
        "messages": state
    })
    return [HumanMessage(content=response.content)]

def refelction_node(state: list[BaseMessage]) --> list[BaseMessage]
    responce = reflection_chain.invoke({
        "message": state
    })
    retrun [HumanMessage(content=responce.content)]

# task create graph message
# step 2 create nodes ( node ke functin me chain ko invoke karte h )


# now we need to add node to graph 
graph.add_node(GENERATE, generate_node)
graph.add_node(REFLECT ,refelction_node )

# we made the nodes ab humko kya karde h edge banan h isse hum connect kar sate h 


graph.add_edge(GENERATE , REFLECT)
graph.add_edge(REFLECT, END)

graph.set_entry_point(GENERATE)

# ab humk compile karna hai so 

app = graph.compile()


# agar

print(app.get_graph().draw_mermaid())
app.get_graph().print_ascii()



responce = app.invoke([HumanMessage(content="AI agent killing developer")])

print(responce)