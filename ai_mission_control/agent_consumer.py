import json
import sys
import os

# Ensure Python can find the langgraph_logic file
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from langgraph_logic import satellite_ai_app 
from kafka import KafkaConsumer

def start_ground_station():
    print("📡 Ground Station AI initialized. Listening to Kafka topic 'satellite-telemetry'...")
    consumer = KafkaConsumer(
        'satellite-telemetry',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:
        telemetry = message.value
        
        if telemetry['status'] == 'ANOMALY':
            print(f"\n" + "="*50)
            print(f"🚨 ANOMALY DETECTED: {telemetry['satellite_id']} - {telemetry['component']}")
            print(f"📉 Voltage: {telemetry['voltage']}V. Waking up Multi-Agent System...")
            print("="*50)
            
            initial_state = {
                "messages": [],
                "telemetry_alert": f"Voltage drop to {telemetry['voltage']}V",
                "current_assignee": "Controller",
                "validation_status": "Pending"
            }
            
            # Execute the LangGraph Agents
            result = satellite_ai_app.invoke(initial_state)
            
            print(f"\n✅ [RESOLUTION COMPLETE]")
            for msg in result['messages']:
                print(f" - {msg}")
            print("="*50 + "\n")

if __name__ == "__main__":
    start_ground_station()