import gemini_api
import os

def code_refactorting(files):
    #TODO: Implement code refactoring prompt for Gemini
    with open(files[0], "r") as f:
        text = f.read()

def test_cases(file):
    with open(file, "r") as f:
        text = f.read()

    prompt = (f"Here is my code. Write me test cases. Make sure that only one file is generated, and that file only has test cases. "
              f"DO NOT have any of the original code in the file. Make sure that the cases compile and run correctly."
              f"{text}")
    response = gemini_api.get_gemini_response(prompt)

    with open(f"test_cases_{os.path.basename(file)}", "w") as f:
        for line in response.split("\n"):
            if line == "```" or line == "```python":
                continue
            else:
                f.write(line + "\n")
    print("Generated Test Cases. Check the file test_cases_" + os.path.basename(file) + ". \nRemember to review the test cases before running them.")

def code_analysis(files):
    #TODO: Implement code analysis prompt for Gemini
    with open(files[0], "r") as f:
        text = f.read()
