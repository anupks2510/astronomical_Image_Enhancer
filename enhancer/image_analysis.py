import os
import base64
import openai
from django.conf import settings

def analyze_astronomical_image(image_path):
    """
    Analyze enhanced image using ChatGPT's Vision API
    Returns analysis text or None
    """
    try:
        # Encode image to base64
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')

        # Prepare prompt
        prompt = """You are a professional astronomer. Analyze this astronomical image in detail. 
        Describe the celestial objects, phenomena, and any notable features visible. 
        Include scientific interpretations and potential research significance.
        The image resolution is {width}x{height} pixels and format is {format}."""

        # Get image metadata
        file_format = os.path.splitext(image_path)[1][1:].upper()

        response = openai.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
            max_tokens=500,
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"Analysis error: {str(e)}")
        return None