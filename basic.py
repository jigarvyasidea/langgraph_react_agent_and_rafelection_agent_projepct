from typing import List
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph
from chain import generation_chain, reflection_chain

load_dotenv()

# Create MessageGraph
graph = MessageGraph()


REFLECT = "reflect"
GENERATE = "generate"

def should_continue(state):
    if len(state) > 4:
        return END
    return REFLECT

# Generate node
def generate_node(state: List[BaseMessage]) -> List[BaseMessage]:
    response = generation_chain.invoke({
        "messages": state
    })
    return [HumanMessage(content=response.content)]

# Reflect node
def reflection_node(state: List[BaseMessage]) -> List[BaseMessage]:
    response = reflection_chain.invoke({
        "messages": state
    })
    return [HumanMessage(content=response.content)]

# Add nodes to graph
graph.add_node(GENERATE, generate_node)
graph.add_node(REFLECT, reflection_node)

# Define flow (unconditional edges; if you want to use should_continue, integrate per MessageGraph API)
graph.add_edge(GENERATE, REFLECT)
graph.add_edge(REFLECT, END)
graph.add_edge(GENERATE, END)

# Set entry point
graph.set_entry_point(GENERATE)

# Compile app
app = graph.compile()

# Visualize graph
print(app.get_graph().draw_mermaid())
app.get_graph().print_ascii()

# Run
response = app.invoke([HumanMessage(content="AI Agent taking over content creation")])
print(response)
