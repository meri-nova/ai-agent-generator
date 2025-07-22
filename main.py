#!/usr/bin/env python3

import argparse
import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from openai_client import OpenAIClient

console = Console()

def collect_user_input():
    """Collect user skills, interests, and goals through interactive prompts"""
    console.print(Panel.fit(
        "[bold blue]AI Agent Idea Generator[/bold blue]\n"
        "Let's create personalized AI agent product ideas based on your profile!",
        title="Welcome"
    ))
    
    console.print("\n[yellow]Please provide information about yourself:[/yellow]\n")
    
    skills = Prompt.ask(
        "[cyan]What are your technical skills?[/cyan] "
        "(e.g., Python, JavaScript, Machine Learning, Data Analysis)"
    )
    
    interests = Prompt.ask(
        "[cyan]What are your interests or domains you're passionate about?[/cyan] "
        "(e.g., Healthcare, Education, Finance, Gaming, Productivity)"
    )
    
    goals = Prompt.ask(
        "[cyan]What are your goals or what do you want to achieve?[/cyan] "
        "(e.g., Build a SaaS product, Automate workflows, Help businesses, Create content)"
    )
    
    return skills.strip(), interests.strip(), goals.strip()

def display_agent_ideas(agent_ideas):
    """Display the generated AI agent ideas in a formatted way"""
    console.print("\n[bold green]🚀 Your AI Agent Ideas:[/bold green]\n")
    
    for i, idea in enumerate(agent_ideas, 1):
        panel_content = (
            f"[bold yellow]Problem:[/bold yellow] {idea['problem']}\n\n"
            f"[bold cyan]Architecture:[/bold cyan] {idea['architecture']}\n\n"
            f"[bold magenta]Tech Stack:[/bold magenta] {idea['tech_stack']}"
        )
        
        console.print(Panel(
            panel_content,
            title=f"[bold white]{i}. {idea['name']}[/bold white]",
            border_style="bright_blue"
        ))
        console.print()

def main():
    parser = argparse.ArgumentParser(
        description="Generate AI agent product ideas based on your skills, interests, and goals"
    )
    parser.add_argument(
        "--version", 
        action="version", 
        version="AI Agent Idea Generator 1.0.0"
    )
    
    args = parser.parse_args()
    
    try:
        # Collect user input
        skills, interests, goals = collect_user_input()
        
        if not all([skills, interests, goals]):
            console.print("[red]Error: All fields are required![/red]")
            sys.exit(1)
        
        # Generate ideas
        console.print("\n[yellow]🤖 Generating your personalized AI agent ideas...[/yellow]")
        
        client = OpenAIClient()
        agent_ideas = client.generate_agent_ideas(skills, interests, goals)
        
        # Display results
        display_agent_ideas(agent_ideas)
        
        console.print("[green]✨ Happy building! Choose an idea and start creating your AI agent.[/green]")
        
    except ValueError as e:
        console.print(f"[red]Configuration Error: {e}[/red]")
        console.print("[yellow]Make sure you have set your OPENAI_API_KEY in a .env file[/yellow]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)

if __name__ == "__main__":
    main()