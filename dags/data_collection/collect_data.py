import os
from datetime import datetime

def collect():
    # Simulate real-time data collection
    sample_data = "Breaking: AI takes over the world... again 😄"

    # Timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/raw_data/data_{timestamp}.txt"

    # Make sure directory exists
    os.makedirs("data/raw_data", exist_ok=True)

    # Save the data
    with open(filename, "w", encoding="utf-8") as f:
        f.write(sample_data)

    print(f"✅ Data collected and saved to: {filename}")

# Optional: Run the function if script is executed directly
if __name__ == "__main__":
    collect()
