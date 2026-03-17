# healthfetal
A hybrid Fetal Health Monitoring System combining a Random Forest Classifier with expert-defined medical safety overrides.A framework that monitors the health of a child while still in the mother's womb

# Fetal Health Monitoring System (AI + Expert Rules)

A Python-based diagnostic tool that combines a **Random Forest Classifier** with **Hard-Coded Safety Overrides** to monitor fetal well-being based on clinical vitals.

### Key Features:
- **Safety-First Logic:** Expert medical rules override AI predictions for critical vitals (e.g., Heart Rate < 100).
- **Machine Learning:** Uses Scikit-Learn's Random Forest for "gray area" classifications.
- **Data Logging:** Automatically saves every session to `fetal_health_history.txt`.
- **Clean UI:** Color-coded terminal output (Green/Yellow/Red) for quick diagnosis.

### Tech Stack:
- Python, Pandas, Scikit-Learn, NumPy
