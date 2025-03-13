from notion_client import Client
from dotenv import load_dotenv
import os
import json
from pydantic import BaseModel
from typing import Optional, List
load_dotenv()
print(f"NOTION_API_KEY: {os.getenv('NOTION_API_KEY')}")
notion = Client(auth=os.getenv("NOTION_API_KEY"))
database_id = os.getenv("NOTION_DATABASE_ID")

def get_all_pages(database_id: str):
    return notion.databases.query(database_id=database_id)


response = get_all_pages(database_id)

json_response = json.dumps(response, indent=4)
# save to file
with open("response.json", "w") as f:
    f.write(json_response)  

# create a page


from notion_client import Client

# Initialize the client with your integration token
notion = Client(auth=os.getenv("NOTION_API_KEY"))



def create_page(tag: str, title: str, parent_item = None):
    tag_to_emoji = {
        "Task": "🗞️",
        "Goal": "🏟️",
        "Sub-Goal": "🎯",
    }


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
                "multi_select": [
                    {
                        "name": tag,
                    }
                ]
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


class PageNode(BaseModel):
    title: str
    children: Optional[List["PageNode"]] = None


# def parse_goals_subgoals_tasks(response: dict):

# # notion.request(
# #     path="/v1/pages",
# #     method="POST",
# #     body={
# #         # fill in the body HERE
# #     }
# # )

# print(json_response)

if __name__ == "__main__":
    # create_page("Task", "Some random task asdfasdf", "1b48041cec6680db84eee61e1506c57b")
    x = PageNode(title="Some random task asdfasdf", children=[PageNode(title="Some random task asdfasdf")])