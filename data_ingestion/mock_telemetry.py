import json
import time
import random
from kafka import KafkaProducer

def generate_telemetry():
    print("🚀 Satellite B-1 Online. Beginning telemetry transmission...")
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    while True:
        # 10% chance to simulate a critical voltage drop
        is_anomaly = random.random() > 0.90
        voltage = random.uniform(15.0, 18.0) if is_anomaly else random.uniform(22.0, 24.0)
        
        data = {
            "satellite_id": "SAT-B1",
            "timestamp": time.time(),
            "component": "Solar Array B",
            "voltage": round(voltage, 2),
            "status": "ANOMALY" if is_anomaly else "NOMINAL"
        }
        
        if is_anomaly:
            print(f"⚠️  [ALERT] Voltage drop: {data['voltage']}V. Transmitting anomaly to ground station!")
        else:
            print(f"✅ [NOMINAL] Voltage: {data['voltage']}V")
            
        producer.send('satellite-telemetry', value=data)
        time.sleep(2) 

if __name__ == "__main__":
    generate_telemetry()