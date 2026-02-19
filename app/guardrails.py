def check_not_found(result):
    sources = result.get("source_documents", [])
    if not sources:
        return "Not found in the document."
    return result["answer"]