import gemini_api
# For testing purposes
if __name__ == "__main__":
    test_prompt = (
    "You are an expert DevOps engineer. Analyze the following CI/CD YAML pipeline configuration "
    "and provide exactly three concise and actionable suggestions in a bullet list. "
    "Each suggestion must be no more than 20 words. Only list the most critical issues. "
    "If no issues exist, output 'No suggestions found.'\n\n"
    f"{pipeline_yaml}"
    )
    print(gemini_api.get_gemini_response(test_prompt))
