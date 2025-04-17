import os
import random

def monitor():
    # Simulate monitoring logic (placeholder for actual metrics)
    accuracy = random.uniform(0.6, 1.0)
    threshold = 0.75

    if accuracy < threshold:
        print(f"⚠️ Accuracy dropped! Current: {accuracy:.2f}")
    else:
        print(f"✅ Accuracy is healthy: {accuracy:.2f}")
