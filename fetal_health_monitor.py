import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import warnings

# Suppress annoying warnings to keep your terminal clean
warnings.filterwarnings("ignore", category=UserWarning)

# --- COLOR DEFINITIONS ---
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'

def generate_medical_data():
    np.random.seed(42)
    records = 2000
    data = {
        'heart_rate': np.random.normal(135, 10, records),
        'movement': np.random.uniform(0, 0.5, records),
        'contractions': np.random.uniform(0, 0.01, records),
        'accelerations': np.random.uniform(0, 0.01, records),
        'target': np.random.choice([1, 2, 3], records, p=[0.75, 0.15, 0.10])
    }
    return pd.DataFrame(data)

def save_to_history(hr, mov, con, acc, result_text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"Date: {timestamp}\nVitals -> HR: {hr}, Mov: {mov}, Con: {con}, Acc: {acc}\nAI Diagnosis: {result_text}\n{'-'*30}\n"
    with open("fetal_health_history.txt", "a") as file:
        file.write(log_entry)

def run_fetal_health_system():
    stats = {"normal": 0, "suspect": 0, "pathological": 0}
    df = generate_medical_data()
    
    # Feature names are stored here
    feature_names = ['heart_rate', 'movement', 'contractions', 'accelerations']
    X = df[feature_names]
    y = df['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train_scaled, y_train)

    print(f"{BOLD}✅ System Ready: AI + Hard-Coded Safety Rules active.{END}")
    
    while True:
        print("\n" + "-" * 50)
        print(f"{BOLD}--- NEW PATIENT CHECK (Type 'exit' to quit) ---{END}")
        
        try:
            val = input("Enter Baseline Heart Rate: ")
            if val.lower() == 'exit': break
            hr = float(val)
            mov = float(input("Enter Fetal Movement Score: "))
            con = float(input("Enter Contraction Score: "))
            acc = float(input("Enter Acceleration Score: "))

            # --- 1. THE SAFETY OVERRIDE (CRITICAL RULES) ---
            # We check these FIRST. If these are met, we don't even ask the AI.
            if hr < 100 or hr > 180 or (mov == 0 and acc == 0):
                prediction = 3  # FORCE Pathological
                reason = "CRITICAL: Vitals are in the danger zone."
            elif hr < 110 or hr > 160 or mov < 0.05:
                prediction = 2  # FORCE Suspect
                reason = "WARNING: Vitals are outside normal range."
            else:
                # --- 2. THE AI PREDICTION (For 'Gray Area' cases) ---
                user_input_df = pd.DataFrame([[hr, mov, con, acc]], columns=feature_names)
                user_data_scaled = scaler.transform(user_input_df)
                prediction = model.predict(user_data_scaled)[0]
                reason = "AI Analysis: Vitals appear stable."

            # --- 3. THE DISPLAY LOGIC ---
            if prediction == 1:
                color, label = GREEN, "normal; baby health is reassuring"
                stats["normal"] += 1
            elif prediction == 2:
                color, label = YELLOW, "suspect; monitor closely"
                stats["suspect"] += 1
            else:
                color, label = RED, "pathological; urgent review needed"
                stats["pathological"] += 1

            print(f"\n{BOLD}DIAGNOSIS:{END} {color}{label}{END}")
            print(f"Details: {reason}")

            save_to_history(hr, mov, con, acc, label)
            print(f"📂 Result logged to 'fetal_health_history.txt'")

        except ValueError:
            print(f"{RED}❌ Error: Please enter numbers or 'exit'.{END}")

    print(f"\n📊 SESSION SUMMARY: Normal: {stats['normal']}, Suspect: {stats['suspect']}, Pathological: {stats['pathological']}")

if __name__ == "__main__":
    run_fetal_health_system()