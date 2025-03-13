A simple notion tool that allows me to add goals, subgoals, and tasks into my Notion kanban board from natural language text.

<img width="1044" alt="image" src="https://github.com/user-attachments/assets/7a956eba-ff40-4a9e-ad14-4e50e7d9b2ed" />

This was the input prompt:
```
✅ Goal: Backend/ML Learning - Week 2
🟩 Subgoal 1: GraphQL & gRPC APIs
Task 1 (2 hours, Conceptual):

Learn GraphQL basics (queries, mutations, schemas). Watch introductory videos or read the official docs briefly, then summarize in your notes.
Task 2 (3 hours, Practical):

Create a simple GraphQL API using FastAPI + Strawberry, serving basic data (e.g., users or quizzes). Test using GraphQL Playground.
Task 3 (1.5 hours, Conceptual):

Explore what gRPC is (read docs/watch tutorials). Note key concepts like Protocol Buffers (.proto) and RPC calls.
Task 4 (2.5 hours, Practical):

Implement a basic gRPC API in Python (grpcio), defining simple RPC methods (like getQuiz, submitAnswer). Run a basic client-server example.
🟦 Subgoal 2: Linear & Logistic Regression
Task 1 (1 hour, Conceptual):

Understand the intuition behind Linear Regression (videos/articles). Summarize how it works and where it’s used.
Task 2 (2 hours, Practical):

Build a Linear Regression model using scikit-learn on a simple dataset. Interpret results (RMSE, R²).
Task 3 (1 hour, Conceptual):

Learn Logistic Regression basics: how it differs from linear regression, where it's useful, and basic concepts of classification.
Task 4 (2 hours, Practical):

Build a simple Logistic Regression classifier in Python on a provided dataset. Evaluate using Accuracy and F1-score metrics.

```

## Setup

Requires a little configuration on the notion part - you need to create an integration, then link it to a database, then get the Notion API key and set it in the .env, along with the ID of the database you want to modify. After this, you need the following properties on notion: Tags (multi-select) with fields of **Goal**, **Sub-Goal**, **Task**, and Parent-item enabled. 

<img width="683" alt="image" src="https://github.com/user-attachments/assets/40b627fb-652b-4c4b-955e-35d97cb405d3" />

Once you have this configured, you can download the source files.

Run `pip install -e .` to install!

Packaged using Poetry.
