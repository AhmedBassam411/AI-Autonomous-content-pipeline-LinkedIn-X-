from groq import Groq
from config import GROQ_API_KEY


client = Groq(api_key=GROQ_API_KEY)


class ResearchAgent:

    def run(self, topic):

        prompt = f'''
        Research latest trends and best practices about:

        {topic}

        Include:
        - statistics
        - examples
        - modern technologies
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