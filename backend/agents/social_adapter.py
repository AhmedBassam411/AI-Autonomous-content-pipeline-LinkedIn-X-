from groq import Groq
from config import GROQ_API_KEY


client = Groq(api_key=GROQ_API_KEY)


class SocialAgent:

    def run(self, blog, platform):

        if platform == "linkedin":
            prompt = f"""
            Convert this blog into a professional LinkedIn post.

            Requirements:
            - formal tone
            - structured paragraphs
            - include insights
            - add hashtags at the end

            Blog:
            {blog}
            """

        else:  # twitter
            prompt = f"""
            Convert this blog into a Twitter/X thread.

            Requirements:
            - short tweets
            - engaging hooks
            - thread format (1/..., 2/...)
            - include hashtags

            Blog:
            {blog}
            """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content