from notion_client import Client
from dotenv import load_dotenv
import os
import json
from pydantic import BaseModel
from typing import Optional, List
from langchain_core.output_parsers import JsonOutputParser
from groq import Groq
from app.prompts.goal_parser_prompt import GOAL_PARSER_PROMPT
load_dotenv()

notion = Client(auth=os.getenv("NOTION_API_KEY"))
database_id = os.getenv("NOTION_DATABASE_ID")

def get_all_pages(database_id: str):
    return notion.databases.query(database_id=database_id)


# response = get_all_pages(database_id)

# json_response = json.dumps(response, indent=4)
# # save to file
# with open("response.json", "w") as f:
#     f.write(json_response)  
# Initialize the client with your integration token

def create_page(tag: str, title: str, parent_item = None, tags: Optional[List[str]] = None):
    tag_to_emoji = {
        "Task": "🗞️",
        "Goal": "🏟️",
        "Sub-Goal": "🎯",
    }

    all_tags = [{"name": tag}]
    if tags:
        all_tags.extend([{"name": t} for t in tags])


    body = {
        # Icon should be at the top level, not in properties
        "icon": {
            "type": "emoji",
            "emoji": tag_to_emoji[tag]
        },
        "parent": {"database_id": os.getenv("NOTION_DATABASE_ID")},
        "properties": {
            "Project": {
                "title": [
                    {"text": {"content": title}}  # Required title property
                ]
            },
            "Tags": {
                "type": "multi_select",
                "multi_select": all_tags
            },
            "Status": {
                "type": "select",
                "select": {
                    "name": "Not started",
                }
            }
            
        }
    }

    if parent_item:
        body["properties"]["Parent item"] = {
            "relation": [
                {
                    "id": parent_item  # This must be a valid page ID
                }
            ]
        }
    
    # Use the low-level request method to create the page
    response = notion.request(
        path="pages",
        method="POST",
        body=body
    )
    
    print(response)
    return response['id']

def parse_goals_subgoals_tasks(input: str):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    parser = JsonOutputParser()
    completion = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL"),
        messages=[
            {"role": "system", "content": GOAL_PARSER_PROMPT},
            {"role": "user", "content": input}
        ],
        reasoning_format="hidden",
        response_format={"type": "json_object"}
    )
    return parser.parse(completion.choices[0].message.content)

class PageNode(BaseModel):
    title: str
    children: Optional[List["PageNode"]] = None


def create_page_tree(response: dict, tags: Optional[List[str]] = None):
    # create a page tree from the response
    # the response is a dictionary with a goal key, which has a title and subgoals key, which has a list of subgoal dictionaries, which have a title and tasks key, which has a list of task strings
    # we need to create a tree of PageNode objects from the response
    # the tree should have the following structure:
    created_pages = []
    goal = response["goal"]

    goal_page = create_page("Goal", goal["title"], tags=tags)
    created_pages.append(goal_page)
    for subgoal in goal["subgoals"]:
        subgoal_page = create_page("Sub-Goal", subgoal["title"], goal_page, tags=tags)
        created_pages.append(subgoal_page)
        for task in subgoal["tasks"]:
            task_page = create_page("Task", task, subgoal_page, tags=tags)
            created_pages.append(task_page)
    return created_pages


def trash_pages(page_ids: List[str]):
    for page_id in page_ids:
        notion.request(
            path=f"pages/{page_id}",
            method="PATCH",
            body={"archived": True}
        )
# def parse_goals_subgoals_tasks(response: dict):

# # notion.request(
# #     path="/v1/pages",
# #     method="POST",
# #     body={
# #         # fill in the body HERE
# #     }
# # )

# print(json_response)

