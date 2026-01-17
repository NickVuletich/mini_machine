#AI



def assess_risk(profile, keywords):
    act = [] #array of activity strings
    nts = "" #string of notes

    if "activity" in profile:
        act = profile.get("activity", [])

    if "notes" in profile:
        nts = profile.get("notes", "")

    total_string = " ".join(act) + " " + nts
    total_string = total_string.lower()

    #counters
    suspicious_count = 0;
    emotional_count = 0
    positive_count = 0
    flags = [] # holds exact keywords and matches their type

    for word in keywords.get("suspicious", []):
        if word in total_string:
            suspicious_count += 1
            flags.append(f"[SUSPICIOUS] {word}")

    for word in keywords.get("emotional", []):
        if word in total_string:
            emotional_count += 1
            flags.append(f"[EMOTIONAL] {word}")

    for word in keywords.get("positive", []):
        if word in total_string:
            positive_count += 1
            flags.append(f"[POSITIVE] {word}")

    for word in keywords.get("behavioral_flags", []):
        if word in total_string:
            suspicious_count += 1
            flags.append(f"[FLAG] {word}")

    if suspicious_count >= 4:
        return {
            "risk" : "HIGH",
            "suspicious_count" : suspicious_count,
            "emotional_count" : emotional_count,
            "positive_count" : positive_count,
            "flags" : flags
        }

    elif suspicious_count <=1 and emotional_count <=2 and positive_count <=2:
        return {
            "risk" : "LOW",
            "suspicious_count" : suspicious_count,
            "emotional_count" : emotional_count,
            "positive_count" : positive_count,
            "flags" : flags
        }
    else:
        return {
            "risk" : "MODERATE",
            "suspicious_count" : suspicious_count,
            "emotional_count" : emotional_count,
            "positive_count" : positive_count,
            "flags" : flags
        }

    
def person_info(profile):
    if "name_first" in profile:
        first_n = profile.get("name_first", "")

    if "name_last" in profile:
        last_n = profile.get("name_last", "")

    if "age" in profile:
        age = profile.get("age", "")

    if "height_in" in profile:
        height = profile.get("height_in", "")

    if "weight_lb" in profile:
        weight = profile.get("weight_lb", "")

    if "ssn" in profile:
        ssn = profile.get("ssn", "")

    return {
        "name" : first_n + " " + last_n,
        "age" : age,
        "height" : height,
        "weight" : weight,
        "ssn" : ssn
    }
    
    