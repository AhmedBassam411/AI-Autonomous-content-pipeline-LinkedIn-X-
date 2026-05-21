from groq import Groq
from config import GROQ_API_KEY


client = Groq(api_key=GROQ_API_KEY)


class SEOAgent:

    def run(self, blog):

        prompt = f'''
        Optimize this blog for SEO.

        Generate:
        - Meta title
        - Meta description
        - Keywords
        - Slug

        Blog:
        {blog}
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