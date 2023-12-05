import base64
import requests
import sys

# OpenAI API Key
api_key = "ENTER_YOUR_API_KEY"

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Check if a filename was provided as an argument
if len(sys.argv) < 2:
    print("Usage: python script.py <path_to_image>")
    sys.exit(1)

# Path to your image (from command-line argument)
image_path = sys.argv[1]

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Describe what you can see in the picture."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
response_json = response.json()

# Extracting the text
response_text = response_json['choices'][0]['message']['content'].split("\n\n")[0]

print(f"The response was: {response_text}")
