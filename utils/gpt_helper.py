import openai

openai.api_key = "your-openai-key"

def explain_field(field_name, content):
    prompt = f"This is the field '{field_name}' with value '{content}'. Explain what it means in a document."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
