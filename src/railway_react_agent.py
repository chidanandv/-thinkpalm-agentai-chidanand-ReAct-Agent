
# Railway ReAct Agent

## Project Overview

This project demonstrates a minimal Python ReAct Agent for a Railway Tracking System.

The agent:
- Accepts user queries
- Thinks step-by-step
- Calls a tool
- Returns final railway tracking information

The project uses 10 dummy train datasets.

---

# Folder Structure

/Railway-ReAct-Agent
│
├── /src
│   └── railway_react_agent.py
│
├── /screenshots
│   ├── output1.png
│   ├── output2.png
│   └── output3.png
│
├── README.md
│
└── requirements.txt

---

# Tools Used

- Python
- Google Colab
- ReAct Agent Pattern

---

# Features

- Interactive train search
- Railway tracking tool
- ReAct reasoning steps
- Dummy railway database
- Continuous search option

---

# How to Run

## Step 1

Open Google Colab:

https://colab.research.google.com

## Step 2

Upload or paste:

src/railway_react_agent.py

## Step 3

Run the Python file

## Step 4

Enter train number

Example:

12006

## Step 5

View railway tracking result

---

# Sample Query

Track train 12006

---

# Sample Output

Train Number   : 12006
Train Name     : Kerala Express
From           : Trivandrum
To             : Delhi
Current Station: Kochi
Status         : Running On Time

---

# Observations

- ReAct pattern helps agents think step-by-step
- Tool calling makes the system modular
- Dummy railway data simulates real-world train tracking
- The agent can continuously accept new queries

---

# Future Improvements

- Add live railway API
- Add station search
- Add ETA prediction
- Add GUI interface
- Connect with database
