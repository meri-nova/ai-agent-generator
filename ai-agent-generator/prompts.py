def create_agent_prompt(skills, interests, goals):
    return f"""You are an AI product strategist. Based on the user's profile, generate exactly 3 unique AI agent product ideas.

User Profile:
- Skills: {skills}
- Interests: {interests}
- Goals: {goals}

For each AI agent idea, provide:
1. Name: A catchy, memorable name for the AI agent
2. Problem: The specific problem it solves (1-2 sentences)
3. Architecture: High-level technical architecture summary (2-3 sentences)
4. Tech Stack: Recommended tools, frameworks, and technologies

Return your response as a JSON array with exactly 3 objects, each containing "name", "problem", "architecture", and "tech_stack" fields.

Example format:
[
  {{
    "name": "Example Agent",
    "problem": "Solves a specific problem for users.",
    "architecture": "Uses a microservices architecture with API gateway and vector database.",
    "tech_stack": "Python, FastAPI, OpenAI API, Pinecone, Docker"
  }}
]

Generate creative, practical ideas that align with the user's skills and interests."""