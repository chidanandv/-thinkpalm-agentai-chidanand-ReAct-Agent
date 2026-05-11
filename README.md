# Railway ReAct Agent

## Name
Chidanand

## Track
Agent AI

## Lab Name
Railway Tracking ReAct Agent

## What It Does
This project demonstrates a minimal Python ReAct Agent for a Railway Tracking System using dummy railway data.

The agent accepts a user query or train number as input and follows the ReAct (Reason + Act) pattern:
1. Understands the user request
2. Thinks step-by-step
3. Calls a railway tracking tool
4. Retrieves train information
5. Returns the final answer to the user

The project contains 10 dummy train datasets with details such as:
- Train Number
- Train Name
- Source Station
- Destination Station
- Current Station
- Train Status

The system supports interactive searching, allowing users to repeatedly check train tracking information until they exit the application.

This project demonstrates:
- Basic AI agent workflow
- Tool calling in Python
- Step-by-step reasoning
- Interactive command-line execution
- Railway tracking simulation

---

# How to Run

## Step 1
Open Google Colab or any Python IDE.

## Step 2
Upload or copy the file:

src/railway_react_agent.py

## Step 3
Run the Python program.

## Step 4
Enter a train number when prompted.

Example:

12006

## Step 5
View the train tracking result.

## Step 6
Choose whether to search again or exit the program.

---

# Tools Used

- Python
- Google Colab
- ReAct Agent Pattern
- Dummy Railway Dataset

---

# Observations

- ReAct agents improve problem-solving by thinking step-by-step.
- Tool calling makes the application modular and reusable.
- Dummy railway data helps simulate real-world train tracking.
- Interactive input allows continuous searching without restarting the program.
- The project demonstrates the basic workflow of an AI agent system.
