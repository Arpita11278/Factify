from analyzer import FactifyAnalyzer

print("Initializing Factify Analyzer...")
analyzer = FactifyAnalyzer()

# Test sample text
sample_text = "URGENT: Forward this message to 10 people to win a free smartphone immediately!"

print("\n--- Running Analysis ---")
result = analyzer.analyze(sample_text)

print("\n--- Test Result ---")
for key, value in result.items():
    print(f"{key}: {value}")