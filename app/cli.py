#!/usr/bin/env python
import argparse
import sys
from typing import Optional
import json
from app.client import parse_goals_subgoals_tasks, create_page_tree, trash_pages

def get_user_input() -> str:
    """Prompt the user for input and collect it until they enter an empty line."""
    print("Enter your goal description (press Enter twice when finished):")
    lines = []
    while True:
        line = input()
        if not line and lines and not lines[-1]:  # Two empty lines in a row
            break
        lines.append(line)
    return "\n".join(lines)

def confirm(prompt: str) -> bool:
    """Ask user for confirmation."""
    response = input(f"{prompt} (y/n): ").lower().strip()
    return response in ("y", "yes")

def display_parsed_goals(parsed_goals: dict) -> None:
    """Display the parsed goals in a readable format."""
    print("\n=== PARSED GOALS ===")
    goal = parsed_goals["goal"]
    print(f"GOAL: {goal['title']}")
    
    for i, subgoal in enumerate(goal["subgoals"], 1):
        print(f"\nSubgoal {i}: {subgoal['title']}")
        print("Tasks:")
        for j, task in enumerate(subgoal["tasks"], 1):
            print(f"  {j}. {task}")
    
    print("\n==================")

def main() -> int:
    """Main CLI function."""
    parser = argparse.ArgumentParser(description="Create structured goals in Notion")
    parser.add_argument("--input-file", type=str, help="Path to input file instead of interactive input")
    args = parser.parse_args()
    
    try:
        # Get input either from file or user
        if args.input_file:
            try:
                with open(args.input_file, 'r') as f:
                    user_input = f.read()
            except FileNotFoundError:
                print(f"Error: File '{args.input_file}' not found.")
                return 1
        else:
            user_input = get_user_input()
        
        if not user_input.strip():
            print("Error: Empty input. Please provide goal information.")
            return 1
        
        # Parse the goals
        print("Parsing goals...")
        parsed_goals = parse_goals_subgoals_tasks(user_input)
        
        # Display the parsed goals
        display_parsed_goals(parsed_goals)
        
        # Ask for confirmation
        if not confirm("Do you want to create these pages in Notion?"):
            print("Operation cancelled.")
            return 0
        
        # Create the pages
        print("Creating pages in Notion...")
        created_pages = create_page_tree(parsed_goals)
        print(f"Successfully created {len(created_pages)} pages in Notion!")
        
        # Ask if user wants to revert
        if confirm("Do you want to revert these changes (trash the created pages)?"):
            print("Trashing pages...")
            trash_pages(created_pages)
            print("Pages have been moved to trash.")
        
        return 0
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 