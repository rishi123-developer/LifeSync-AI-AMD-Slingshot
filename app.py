import time
import random

# Simulating AMD Ryzen AI Integration
# In a real scenario, we would import libraries like 'tensorflow-rocm' or 'pytorch-directml'
class AMD_Ryzen_AI_Engine:
    def __init__(self):
        self.device = "AMD NPU (Neural Processing Unit)"
        self.status = "Active"
        print(f"[System Init] Initializing {self.device} for local inference...")

    def run_inference(self, user_data):
        """
        Simulates running a machine learning model locally on AMD hardware.
        This avoids sending sensitive user data to the cloud.
        """
        start_time = time.time()
        
        # Simulating complex matrix multiplication for recommendation
        # Optimized for AMD ROCm architecture
        preferences = user_data.get('interests', [])
        
        # Fake Logic: processing data
        recommendations = []
        if 'Sci-Fi' in preferences:
            recommendations.append({'type': 'Movie', 'title': 'Project Hail Mary', 'match': '99%'})
        if 'Tech' in preferences:
            recommendations.append({'type': 'Event', 'title': 'AMD AI Hackathon', 'location': 'Vadodara'})
            
        end_time = time.time()
        latency = (end_time - start_time) * 1000  # Convert to ms
        
        return {
            'recommendations': recommendations,
            'latency_ms': f"{latency:.4f}",
            'hardware_used': 'AMD Ryzen AI NPU'
        }

# --- Main Application Logic ---

def get_recommendations(user_id):
    # User Profile (Mock Data)
    user_profile = {
        'id': user_id,
        'location': 'Vadodara, India',
        'interests': ['Sci-Fi', 'Tech', 'Cricket', 'Sustainable Fashion']
    }
    
    # Initialize AI Engine
    engine = AMD_Ryzen_AI_Engine()
    
    # Run Prediction
    print("Processing user context locally...")
    result = engine.run_inference(user_profile)
    
    return result

if __name__ == "__main__":
    # Test the system
    output = get_recommendations(user_id="Rishi_001")
    print("\n--- Recommendation Output ---")
    print(output)
