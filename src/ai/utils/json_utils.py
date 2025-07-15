import re

def extract_json(response: str) -> str:
    """
    Extract the first JSON object from a possibly messy LLM response.
    
    Args:
        response (str): Raw string output from LLM

    Returns:
        str: Extracted JSON string (or raw if no match)
    """
    match = re.search(r"\{.*\}", response, re.DOTALL)
    return match.group(0) if match else response
