import json
import ai_analysis
import time

def type_out(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# you can replace red.json with any json file aslong as it keeps the same format as the provided json files
j = open("profiles/red.json")
profile = json.load(j)

f = open("data/poi_keywords.json")
keywords = json.load(f)

result = ai_analysis.assess_risk(profile, keywords)

info = ai_analysis.person_info(profile)

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
type_out(f"SSN: {info['ssn']}")
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
    
