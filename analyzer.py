import os
from gemini_api import get_gemini_response
import tracemalloc
import runpy


def measure_memory_usage(file_path):
    
    tracemalloc.start()
    print(file_path, "currently running:\n")
    runpy.run_path(file_path, run_name="__main__")
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(file_path, "\nfinished running.\n")
    return current, peak


# def analyze_code_with_memory(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
#             code = f.read()
#     except Exception as e:
#         print(f"Error reading {file_path}: {e}")
#         return None

#     # Measure memory usage by running the file without altering it.
#     current, peak = measure_memory_usage(file_path)
#     memory_report = f"Current memory usage: {current/1024:.2f} KB\nPeak memory usage: {peak/1024:.2f} KB"

#     # Construct a prompt for Gemini that includes both the code and the memory metrics.
#     prompt = f"""
#         You are an expert software engineer. Analyze the following Python code for memory management issues such as leaks or inefficient usage. Use the provided memory metrics to support your analysis, and suggest possible optimizations.
#         Also make the response consise and a max of 150 words per file and do not print the file in the response.

#         Memory Metrics:
#         {memory_report}

#         Code:
#         ```python
#         {code}
#         """
#     analysis = get_gemini_response(prompt)
#     return analysis

def analyze_code_with_gemini(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            code = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

    prompt = f"""
    You are an expert software engineer. Analyze the time and space complexity of the following Python code, and format
    the results like this:
    
    ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
    │               Classes               │               Functions               │ Time Complexity │ Space Complexity │
    ├──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
    │             Book                    │              readBook                 │     O(1)        │       O(n)       │
    │                                     │              getTitle                 │     O(1)        │       O(1)       │
    │                                     │              setAuthor                │     O(1)        │       O(1)       │
    ├──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
    │             Library                 │              addBook                  │     O(1)        │       O(1)       │
    │                                     │              removeBook               │     O(n)        │       O(1)       │
    │                                     │              findBookByTitle          │     O(n)        │       O(1)       │
    ├──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
    │             Reader                  │              borrowBook               │     O(1)        │       O(1)       │
    │                                     │              returnBook               │     O(1)        │       O(1)       │
    │                                     │              listBorrowedBooks        │     O(n)        │       O(n)       │
    └──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

    All box text contents have to be in the middle of the box. DO NOT SAY ANYTHING ELSE BESIDES OUTPUTTING THIS BOX.
    
    
    {code}
    """
    
    analysis = get_gemini_response(prompt)
    return analysis

def analyze_repo_performance(repo_path):
    results = []
    for root, dirs, files in os.walk(repo_path):
        # Skip directories that are unlikely to contain source code
        if any(skip in root for skip in ['.git', 'node_modules', '__pycache__', 'venv', '.gitignore', 'analyzer.py', 'gemini_api.py']):
            continue
        for filename in files:
            if filename.endswith('.py'):
                file_path = os.path.join(root, filename)
                analysis = analyze_code_with_gemini(file_path)
                if analysis:
                    results.append(analysis)
    return results