from groq import Groq
from config import GROQ_API_KEY


client = Groq(api_key=GROQ_API_KEY)


class ReviewerAgent:

    def run(self, blog):

        prompt = f'''
        Review this blog.

        Check:
        - grammar
        - technical accuracy
        - SEO quality
        - readability

        Give a quality score out of 10.

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