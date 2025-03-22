import gemini_api
import os

def code_refactorting(files):
    #TODO: Implement code refactoring prompt for Gemini
    with open(files[0], "r") as f:
        text = f.read()

def test_cases(file):
    #TODO: Implement test cases prompt for Gemini
    with open(file, "r") as f:
        text = f.read()
        print(text)

    prompt = (f"Here is my code. Write me test cases. Make sure that only one file is generated, and that file only has test cases. "
              f"DO NOT have the original code in the file. Make sure that the cases compile and run correctly."
              f"{text}")
    response = gemini_api.get_gemini_response(prompt)
    with open(f"test_cases_{os.path.basename(file)}", "w") as f:
        f.write(response)

def code_analysis(files):
    #TODO: Implement code analysis prompt for Gemini
    with open(files[0], "r") as f:
        text = f.read()
