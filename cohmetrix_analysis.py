# cohmetrix_analysis.py
# A basic script for extracting linguistic features (mock version)

def analyze_text(text):
    result = {
        "mean_sentence_length": len(text.split()) / max(text.count('.'), 1),
        "lexical_diversity": len(set(text.split())) / len(text.split()),
        "cohesion_index": 0.45  # Dummy value
    }
    return result

sample_text = "ChatGPT is a helpful tool. It provides suggestions. Students can revise their essays based on it."
features = analyze_text(sample_text)

print("Linguistic features extracted:")
for key, value in features.items():
    print(f"{key}: {value}")
