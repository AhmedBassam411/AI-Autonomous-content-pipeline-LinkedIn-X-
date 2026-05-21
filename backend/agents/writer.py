from groq import Groq
from config import GROQ_API_KEY


client = Groq(api_key=GROQ_API_KEY)


class WriterAgent:

    def run(self, topic, research):

        prompt = f'''
        Write a detailed SEO optimized blog.

        Topic:
        {topic}

        Research:
        {research}

        Requirements:
        - Professional
        - Technical
        - 1500+ words
        - Headings
        - Bullet points
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