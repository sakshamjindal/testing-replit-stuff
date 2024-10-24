def add_reason(df, conditions):
    reasons = []
    for _, row in df.iterrows():
        reason = []
        for condition, explanation in conditions:
            if condition(row):
                reason.append(explanation)
        reasons.append("; ".join(reason) if reason else "Meets multiple criteria")
    return reasons