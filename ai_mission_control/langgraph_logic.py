from typing import TypedDict, Annotated, Sequence
import operator
from langgraph.graph import StateGraph, END

# 1. Define the State (Shared Memory)
class SatelliteMissionState(TypedDict):
    messages: Annotated[list[str], operator.add]
    telemetry_alert: str
    validation_status: str

# 2. Define the Agent Nodes
def mission_controller_agent(state: SatelliteMissionState):
    print("🤖 [Controller] Analyzing telemetry anomaly...")
    return {"messages": ["Controller: Delegated to RAG for manual lookup."]}

def rag_specialist_agent(state: SatelliteMissionState):
    print("📚 [RAG Agent] Querying technical manuals...")
    solution = "Protocol Alpha: Initiate auxiliary power routing."
    return {"messages": [f"RAG Agent: Found solution - {solution}"]}

def safety_validator_agent(state: SatelliteMissionState):
    print("🛡️ [Validator] Simulating protocol safety checks...")
    return {"validation_status": "Passed", "messages": ["Validator: Maneuver is within safety thresholds."]}

# 3. Compile the Graph (Strict Linear Flow)
workflow = StateGraph(SatelliteMissionState)

workflow.add_node("Controller", mission_controller_agent)
workflow.add_node("RAG", rag_specialist_agent)
workflow.add_node("Validator", safety_validator_agent)

workflow.set_entry_point("Controller")

# Explicitly tell LangGraph the exact path to take
workflow.add_edge("Controller", "RAG")
workflow.add_edge("RAG", "Validator")
workflow.add_edge("Validator", END)

# Export the compiled application
satellite_ai_app = workflow.compile()