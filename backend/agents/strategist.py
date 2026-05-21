from groq import Groq
from config import GROQ_API_KEY


client = Groq(api_key=GROQ_API_KEY)


class StrategistAgent:

    def run(self, topic, audience):

        prompt = f'''
        Create a blog strategy for:

        Topic: {topic}
        Audience: {audience}

        Include:
        - Blog title
        - Outline
        - Tone
        - Key sections
        '''

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content