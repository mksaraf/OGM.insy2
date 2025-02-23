from braintrust import Eval
from autoevals import LevenshteinScorer

# cd 'OGM.insy/src/app/steps/step13_evaluation/'
# BRAINTRUST_API_KEY=sk-S5lD2KPQpxF4D6PXDJbLWjMQgvd3L4n31VPIelurEdKXQEZa braintrust eval eval_braintrust.py

Eval(
  "Say Hi Bot",
  data=lambda: [
      {
          "input": "Foo",
          "expected": "Hi Foo",
      },
      {
          "input": "Bar",
          "expected": "Hello Bar",
      },
  ],  # Replace with your eval dataset
  task=lambda input: "Hi " + input,  # Replace with your LLM call
  scores=[LevenshteinScorer],
)

