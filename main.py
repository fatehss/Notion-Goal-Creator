from app.client import parse_goals_subgoals_tasks, create_page_tree, trash_pages

if __name__ == "__main__":
    # create_page("Task", "Some random task asdfasdf", "1b48041cec6680db84eee61e1506c57b")
    input = f"""
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
"""
    
    response = parse_goals_subgoals_tasks(input)
    pages = create_page_tree(response)
    trash_pages(pages)