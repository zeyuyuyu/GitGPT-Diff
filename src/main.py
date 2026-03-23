import os
import difflib
import openai

openai.api_key = os.environ['OPENAI_API_KEY']

def generate_code_diff(base_code, new_code):
    """Generate an AI-powered code diff between two code snippets."""
    prompt = f"""Generate a detailed code diff between the following two code snippets:
    
    Base code:
    {base_code}
    
    New code:
    {new_code}
    
    Provide the diff in the standard unified diff format, with clear explanations for each change."""
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    return response.choices[0].text.strip()

if __name__ == "__main__":
    base_code = """import os
import sys

def main():
    print("Hello, world!")

if __name__ == "__main__":
    main()"""
    new_code = """import os
import sys

def main():
    print("Hello, GPT!")
    print("This is a new feature.")

if __name__ == "__main__":
    main()"""
    
    diff = generate_code_diff(base_code, new_code)
    print(diff)