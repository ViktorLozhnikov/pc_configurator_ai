import openai

# OpenAI API інтеграція
def chat_with_ai(user_message):
    try:
        openai.api_key = "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"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a PC building assistant. Provide advice on PC components and builds."},
                {"role": "user", "content": user_message}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Помилка у чаті з AI: {e}"
