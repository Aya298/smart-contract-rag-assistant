def calculate_confidence(result):
    sources = result.get("source_documents", [])
    confidence = len(sources) / 3
    return round(confidence, 2)