import subprocess
import sys
import gemini_api
import os

def test_cases(file):
    def generate_tests(input_file):
        _, ext = os.path.splitext(input_file)
        basename = os.path.basename(input_file)
        if basename == "requirements.txt" or basename == "README.md" or basename.startswith("test_cases") or basename.startswith("__"):
            print("Skipping File: " + os.path.basename(input_file))
            return
        if ext in (".txt", ".docx", ".md"):
                type_of_file = "requirements"
        else:
            type_of_file = "code"


        with open(input_file, "r", encoding='utf-8') as f:
            text = f.read()

        prompt = (f"Here is my {type_of_file} file. Write me test cases. Make sure that only one file is generated, and that file only has test cases. "
                  f"DO NOT have any of the original code in the file. Do not use phrases like 'DO NOT MODIFY THIS CLASS' and your_code. "
                  f"Make sure that the cases compile and run correctly.\n"
                  f"The file name is {os.path.basename(input_file)}. and the {type_of_file} is:\n"
                  f"{text}")
        response = gemini_api.get_gemini_response(prompt)

        folder = os.path.dirname(input_file)
        test_cases_file_name = f"test_cases_{os.path.splitext(os.path.basename(input_file))[0]}.py"
        with open(os.path.join(folder, test_cases_file_name), "w") as f:
            for line in response.split("\n"):
                if "```" in line:
                    continue
                else:
                    f.write(line + "\n")
        print(f"Generated Test Cases. Check the file {test_cases_file_name}. "
              f"\nRemember to review the test cases before running them.")

    if os.path.isdir(file):
        for item in os.listdir(file):
            generate_tests(os.path.join(file, item))
    else:
        generate_tests(file)

def diff_test_cases():
    diff = subprocess.run(['git', 'diff'], capture_output=True, text=True)

    prompt = (f"Here is my current git diff, write me test cases. Make sure that all the differences are on the test cases. "
              f"Make sure that only one file is generated, and that file only has test cases."
              f"DO NOT have any of the original code in the file. Do not use phrases like 'DO NOT MODIFY THIS CLASS' and your_code."
              f"{diff.stdout}")
    response = gemini_api.get_gemini_response(prompt)

    with open("test_cases_git_diff.py", "w") as f:
        for line in response.split("\n"):
            if "```" in line:
                continue
            else:
                f.write(line + "\n")
    print(f"Generated Test Cases on the most recent changes. Check the file test_cases_git_diff.py. "
          f"\nRemember to review the test cases before running them.")
    
if __name__ == "__main__":
    low_token = sys.argv[1]
    if low_token == "true":
        output = diff_test_cases()
    else:
        output = test_cases(sys.argv[2])
    print(output)