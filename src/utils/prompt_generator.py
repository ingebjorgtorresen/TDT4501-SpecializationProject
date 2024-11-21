def generate_prompt(labels):
    prompt = ""
    if "melancholic" in labels:
        prompt += "a dark, soft scene with muted colors, "
    if "intense" in labels:
        prompt += "a dramatic landscape with vivid contrasts, "
    # Add other conditions based on labels
    return prompt.strip(", ")
