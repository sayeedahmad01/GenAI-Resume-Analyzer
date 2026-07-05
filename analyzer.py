import ollama
from prompts import PROMPT

print("ANALYZER FILE LOADED")

def analyze_resume(resume_text):
    prompt = PROMPT.format(resume=resume_text)

    print("MODEL = qwen2.5:3b")

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]