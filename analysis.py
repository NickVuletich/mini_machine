# Programmer: Nicholas M. Vuletich
# Date: 01-16-2026
# File: analysis.py

"""
    Version 2 - Updated 01-16-2026

    Risk analsys logic for the Mini Machine project.

    This module evaluates a profile using keyword-based signals
    and returns a structured risk assessment.
"""

import re


def contains_keyword(text: str, keyword: str) -> bool:
    """
    Returns True if keyword is in text.

    - For single words it matches whole words (it prevents "gun" matching "begun")
    - For multi word phrases: it matches as a phrase and is case-insensitive
    """
    keyword = keyword.strip().lower()
    if not keyword:
        return False
    
    # Phrase match
    if " " in keyword:
        return keyword in text
    
    # Whole word match for single words
    return re.search(rf"\b{re.escape(keyword)}\b", text) is not None


def assess_risk(profile: dict, keywords: dict) -> dict:

    """
    Analyzes a profile and determines a risk level based on keyword matches.

    The function scans the profile's activity list and notes field,
    counts keyword matches by category, and assigns a risk level.

    Returns:
    dict: {
        "risk" : str,
        "suspicious_count": int,
        "emotional_count": int,
        "positive_count": int,
        "flags": list[str]
    }
    """
    act = profile.get("activity", []) #array of activity strings
    nts = profile.get("notes", "") #string of notes

    # combines all text into one lowercase string for scanning
    total_string = (" ".join(act) + " " + nts).lower()

    #counters
    suspicious_count = 0
    emotional_count = 0
    positive_count = 0
    flags = []

    # scans keyword categories
    for word in keywords.get("suspicious", []):
        if contains_keyword(total_string, word):
            suspicious_count += 1
            flags.append(f"[SUSPICIOUS] {word}")

    for word in keywords.get("emotional", []):
        if contains_keyword(total_string, word):
            emotional_count += 1
            flags.append(f"[EMOTIONAL] {word}")

    for word in keywords.get("positive", []):
        if contains_keyword(total_string, word):
            positive_count += 1
            flags.append(f"[POSITIVE] {word}")

    for word in keywords.get("behavioral_flags", []):
        if contains_keyword(total_string, word):
            suspicious_count += 1
            flags.append(f"[FLAG] {word}")

    # Determines overall risk
    if suspicious_count >= 4:
        risk = "HIGH"
    elif suspicious_count <= 1 and emotional_count <= 2 and positive_count <= 2:
        risk = "LOW"
    else:
        risk = "MODERATE"
        
    return {
        "risk" : risk,
        "suspicious_count": suspicious_count,
        "emotional_count": emotional_count,
        "positive_count": positive_count,
        "flags": flags
    }

    
def person_info(profile: dict) -> dict:
    """
    Extracts identifying information from a profile.

    Returns:
        dict: {
        "name": str,
        "age": any,
        "height": any,
        "weight": any,
        "ssn": any,
        }
    """
    first_n = profile.get("name_first", "")
    last_n = profile.get("name_last", "")

    return {
        "name": f"{first_n} {last_n}".strip(),
        "age": profile.get("age", ""),
        "height": profile.get("height_in", ""),
        "weight": profile.get("weight_lb", ""),
        "ssn": profile.get("ssn", "")
    }
    
    