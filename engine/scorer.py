def score_log(log_text: str) -> float:
    # Simple scoring: if 'unauthorized' in log, score 0.9 else 0.2
    if "unauthorized" in log_text.lower():
        return 0.9
    return 0.2
