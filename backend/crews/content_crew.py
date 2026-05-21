from agents.strategist import StrategistAgent
from agents.researcher import ResearchAgent
from agents.writer import WriterAgent
from agents.seo_optimizer import SEOAgent
from agents.social_adapter import SocialAgent
from agents.reviewer import ReviewerAgent


class ContentPipelineCrew:

    def __init__(self, topic, audience):

        self.topic = topic
        self.audience = audience

        self.strategist = StrategistAgent()
        self.researcher = ResearchAgent()
        self.writer = WriterAgent()
        self.seo = SEOAgent()
        self.social = SocialAgent()
        self.reviewer = ReviewerAgent()

    def run(self, platform):

        strategy = self.strategist.run(
            self.topic,
            self.audience
        )

        research = self.researcher.run(
            self.topic
        )

        blog = self.writer.run(
            self.topic,
            research
        )

        seo = self.seo.run(blog)

        social = self.social.run(blog, platform)

        review = self.reviewer.run(blog)

        return {
            "social": social,
        }