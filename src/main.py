import os
import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')

def generate_code(prompt):
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def analyze_diff(old_code, new_code):
    prompt = f"""Analyze the changes between the following two code snippets:
Old code:
{old_code}

New code: 
{new_code}

Provide a detailed summary of the key changes, including any new functionality, refactors, or bug fixes."""

    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def main():
    print("Welcome to GitGPT-Diff!")
    print("Enter 'q' to quit.")
    
    while True:
        user_input = input("Enter a prompt to generate new code: ")
        if user_input.lower() == 'q':
            break
        new_code = generate_code(user_input)
        print("\
Generated code:\
")
        print(new_code)
        
        old_code = """# Previous version of the code
        print('Hello, world!')
        """
        diff_analysis = analyze_diff(old_code, new_code)
        print("\
Diff analysis:\
")
        print(diff_analysis)

if __name__ == "__main__":
    main()