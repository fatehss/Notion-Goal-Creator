from setuptools import setup, find_packages

setup(
    name="notion-goal-creator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "notion-client",
        "python-dotenv",
        "langgraph",
        "groq",
        "pydantic",
    ],
    entry_points={
        "console_scripts": [
            "notion_goal_create=app.cli:main",
        ],
    },
) 