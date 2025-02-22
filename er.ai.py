# Simple ER AI by Grok - No coding experience needed
def analyze_patient():
    # Ask user for input
    age = input("Enter patient age (e.g., 30): ")
    symptoms = input("Enter symptoms (e.g., chest pain, fever): ").lower().split(", ")
    heart_rate = input("Enter heart rate (e.g., 100): ")

    # Basic logic to suggest diagnoses, plan, disposition
    result = {"Differential": "", "Plan": "", "Disposition": ""}
    
    if "chest pain" in symptoms and int(heart_rate) > 90:
        result["Differential"] = "1. Heart attack, 2. Pneumonia"
        result["Plan"] = "Do ECG, chest X-ray, blood test"
        result["Disposition"] = "Admit to hospital"
    elif "fever" in symptoms and int(heart_rate) > 100:
        result["Differential"] = "1. Sepsis, 2. Flu"
        result["Plan"] = "Blood tests, IV fluids"
        result["Disposition"] = "Admit to ICU if worsening"
    else:
        result["Differential"] = "Unsure - need more info"
        result["Plan"] = "Check more symptoms and vitals"
        result["Disposition"] = "Reassess later"

    # Show results
    print("\nResults:")
    for key, value in result.items():
        print(f"{key}: {value}")

# Run the program
analyze_patient()