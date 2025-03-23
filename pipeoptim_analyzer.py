import yaml
from gemini_api import get_gemini_response


def analyze_pipeline(pipeline_data: dict) -> list:
    """
    Analyze the CI/CD pipeline configuration using the Gemini API.

    The function converts the pipeline data to YAML, constructs a refined prompt,
    and returns a list of concise, actionable suggestions as bullet points.
    If the API call yields no bullet points, it falls back to a rule-based analysis.
    """
    pipeline_yaml = yaml.dump(pipeline_data)
    prompt = (
        "You are an expert DevOps engineer. Analyze the following CI/CD YAML pipeline configuration "
        "and provide a list of concise, visually appealing, and actionable optimization suggestions. "
        "Focus only on the most critical improvements. Each suggestion should be brief (1-2 sentences) "
        "and start with a dash (-). If there are no issues, simply output 'No suggestions found.'\n\n"
        f"{pipeline_yaml}"
    )

    response_text = get_gemini_response(prompt)

    if response_text.startswith("Error"):
        return rule_based_analysis(pipeline_data)

    # Parse suggestions that start with a dash (-)
    suggestions = [
        line.strip("- ").strip()
        for line in response_text.splitlines()
        if line.strip().startswith("-")
    ]

    # If no bullet points are found but response indicates no issues, return an empty list
    if not suggestions and "No suggestions found" in response_text:
        return []

    if not suggestions:
        return rule_based_analysis(pipeline_data)

    return suggestions


def rule_based_analysis(pipeline_data: dict) -> list:
    """
    A simple fallback analysis that checks for missing caching steps.
    """
    suggestions = []
    jobs = pipeline_data.get('jobs', {})
    for job_name, job in jobs.items():
        steps = job.get('steps', [])
        if not any('cache' in step.get('name', '').lower() for step in steps):
            suggestions.append(f"Job '{job_name}' might benefit from adding a caching step using actions/cache@v3.")
    return suggestions
