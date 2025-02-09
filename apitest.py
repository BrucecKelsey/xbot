import requests

# DeepSeek API URL
API_URL = "https://api.deepseek.com/v1/chat/completions"

# Your API key (replace with actual key)
API_KEY = "sk-c8741294b4bf47669a151cb90aa332c7"

data = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "system", "content": "You are a crypto commenter that loves the crypto community and is very excited to make cryptocurrencies increase in value."},
        {"role": "user", "content": "Give me an exciting and funny crypto comment about the Based cryptocurrency, without necessarily starting with the word 'Based'. Keep it within 5 words."}
    ],
    "temperature": 0.7
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

response = requests.post(API_URL, json=data, headers=headers)

if response.status_code == 200:
    comment = response.json()["choices"][0]["message"]["content"].replace('"', "")
else:
    comment = f"Error: {response.status_code} - {response.text}"

print(comment)