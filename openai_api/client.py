import openai

def get_car_ai_bio(model, brand, year):
    prompt = f"Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 250 caracteres. Fale coisas específicas desse modelo."
    
    openai.api_key = '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'
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "Você é um assistente especializado em descrições de vendas de carros."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=250,
        temperature=0.7,
        top_p=1
    )
    return response['choices'][0]['message']['content'].strip()
