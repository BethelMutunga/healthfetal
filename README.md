#  HealthFetal: Hybrid Fetal Health Monitoring System

**HealthFetal** is a diagnostic framework designed to monitor the well-being of a child in the womb by analyzing clinical vitals. It uniquely bridges the gap between pure Machine Learning and clinical safety by employing a **"Safety-First" architecture.**

---

##  The Hybrid Approach
Unlike standard AI models that can sometimes make "uncertain" guesses in critical moments, this system uses a two-tier verification process:

1.  **Expert System (Priority):** Hard-coded medical thresholds immediately flag critical vitals (e.g., Heart Rate < 100 or > 180) before the AI is even consulted.
2.  **AI Analysis (Random Forest):** For vitals within "gray areas," a trained **Scikit-Learn** model predicts the health status based on historical patterns.

## Key Features
* **Safety-First Logic:** Clinical rules override AI predictions for high-risk vitals to ensure zero-latency alerts for urgent cases.
* **Intelligent Classification:** Utilizes a **Random Forest Classifier** to handle complex interactions between fetal movement and contractions.
* **Automated Medical Logging:** Every diagnostic session is timestamped and saved to `fetal_health_history.txt` for future clinical review.
* **Intuitive Terminal UI:** Features color-coded output (**Green**, **Yellow**, **Red**) for immediate visual diagnosis.

##  Tech Stack
* **Language:** Python 3.x
* **Data Handling:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Random Forest, StandardScaler)

##  How to Run
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/BethelMutunga/healthfetal.git
    ```
2.  **Navigate to the folder:**
    ```bash
    cd FetalHealthProject
    ```
3.  **Run the monitor:**
    ```bash
    python3 fetal_health_monitor.py
    ```
