# Programmer: Nicholas M. Vuletich
# Date: 01-16-2026
# File: main.py


import json
import analysis
import time

PROFILE_PATH = "profiles/red.json"
KEYWORDS_PATH = "keywords.json"


def type_out(text: str, delay: float = 0.05) -> None:
    """Prints out text with a typewriter effect."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def load_json(path: str) -> dict:
    """Loads JSON from a file path."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def main() -> None:

    profile = load_json(PROFILE_PATH)
    keywords = load_json(KEYWORDS_PATH)
    
    result = analysis.assess_risk(profile, keywords)
    info = analysis.person_info(profile)

    type_out("Initializing...")
    time.sleep(1.0)
    type_out("Running risk analysis...")
    time.sleep(1.0)

    type_out(f"Name: {info['name']}")
    time.sleep(0.2)
    type_out(f"Age: {info['age']}")
    time.sleep(0.2)
    type_out(f"Height: {info['height']} in")
    time.sleep(0.2)
    type_out(f"Weight: {info['weight']} lbs")
    time.sleep(0.2)

    # SSN is redacted for a public demo
    type_out("SSN: [REDACTED]")
    # Prints fake ssn from profile
    #type_out(f"SSN: {info['ssn']}")
    time.sleep(0.2)

    print()
    time.sleep(0.2)

    type_out(f"RISK LEVEL: {result['risk']}")
    time.sleep(0.2)
    type_out(f"Suspicious: {result['suspicious_count']}")
    time.sleep(0.2)
    type_out(f"Emotional: {result['emotional_count']}")
    time.sleep(0.2)
    type_out(f"Positive: {result['positive_count']}")
    time.sleep(0.2)

    type_out("Flags:")
    time.sleep(0.2)
    for flag in result["flags"]:
        type_out(f"   - {flag}", 0.02)

if __name__ == "__main__":
    main()
    
