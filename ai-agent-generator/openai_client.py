import json
from openai import OpenAI
from config import Config
from prompts import create_agent_prompt

class OpenAIClient:
    def __init__(self):
        Config.validate()
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        self.model = Config.OPENAI_MODEL
    
    def generate_agent_ideas(self, skills, interests, goals):
        try:
            prompt = create_agent_prompt(skills, interests, goals)
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful AI product strategist that responds with valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=2000
            )
            
            content = response.choices[0].message.content.strip()
            
            # Parse JSON response
            agent_ideas = json.loads(content)
            
            if not isinstance(agent_ideas, list) or len(agent_ideas) != 3:
                raise ValueError("Expected exactly 3 agent ideas")
            
            return agent_ideas
            
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse AI response as JSON: {e}")
        except Exception as e:
            raise RuntimeError(f"OpenAI API error: {e}")