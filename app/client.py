from notion_client import Client
from dotenv import load_dotenv
import os
import json

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

# Build the request body as a Python dictionary
# body = {
#     "cover": {
#         "type": "external",
#         "external": {
#             "url": "https://upload.wikimedia.org/wikipedia/commons/6/62/Tuscankale.jpg"
#         }
#     },
#     "icon": {
#         "type": "emoji",
#         "emoji": "🥬"
#     },
#     "parent": {
#         "type": "database_id",
#         "database_id": os.getenv("NOTION_DATABASE_ID")
#     },
#     "properties": {
#         "Name": {
#             "title": [
#                 {
#                     "text": {
#                         "content": "Tuscan kale"
#                     }
#                 }
#             ]
#         },
#     },
#     "children": [
#         {
#             "object": "block",
#             "heading_2": {
#                 "rich_text": [
#                     {
#                         "text": {
#                             "content": "Lacinato kale"
#                         }
#                     }
#                 ]
#             }
#         },
#         {
#             "object": "block",
#             "paragraph": {
#                 "rich_text": [
#                     {
#                         "text": {
#                             "content": (
#                                 "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, "
#                                 "especially that of Tuscany. It is also known as Tuscan kale, Italian kale, "
#                                 "dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm."
#                             ),
#                             "link": {
#                                 "url": "https://en.wikipedia.org/wiki/Lacinato_kale"
#                             }
#                         },
#                         "href": "https://en.wikipedia.org/wiki/Lacinato_kale"
#                     }
#                 ],
#                 "color": "default"
#             }
#         }
#     ]
# }

body = {
    "parent": {"database_id": database_id},
    "properties": {
        "Project": {
            "title": [
                {"text": {"content": "Minimal task"}}  # Required title property
            ]
        },
        "icon": {
            "type": "emoji",
            "emoji": "🗞️"
        },
        "Tags": {
                    "id": "oHBv",
                    "type": "multi_select",
                    "multi_select": [
                        {
                            "id": "3b5ffaf3-d517-4652-b893-fb77b95d31d5",
                            "name": "Task",
                            "color": "orange"
                        },
                    ]
        }
    }
}




# Use the low-level request method to create the page
response = notion.request(
    path="/pages",
    method="POST",
    body=body
)

# print(response)


# notion.request(
#     path="/v1/pages",
#     method="POST",
#     body={
#         # fill in the body HERE
#     }
# )

# print(json_response)
