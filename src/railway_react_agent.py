# ==========================================
# INTERACTIVE PYTHON REACT AGENT
# RAILWAY TRACKING SYSTEM
# ==========================================

# ---------- DUMMY TRAIN DATABASE ----------
trains = [
    {"train_no": "12001", "name": "Shatabdi Express", "from": "Delhi", "to": "Bhopal", "status": "Running On Time", "current_station": "Agra"},
    {"train_no": "12002", "name": "Rajdhani Express", "from": "Mumbai", "to": "Delhi", "status": "Delayed by 20 mins", "current_station": "Kota"},
    {"train_no": "12003", "name": "Duronto Express", "from": "Kolkata", "to": "Delhi", "status": "Running On Time", "current_station": "Kanpur"},
    {"train_no": "12004", "name": "Garib Rath", "from": "Chennai", "to": "Bangalore", "status": "Arrived", "current_station": "Bangalore"},
    {"train_no": "12005", "name": "Intercity Express", "from": "Hyderabad", "to": "Vijayawada", "status": "Running Late", "current_station": "Warangal"},
    {"train_no": "12006", "name": "Kerala Express", "from": "Trivandrum", "to": "Delhi", "status": "Running On Time", "current_station": "Kochi"},
    {"train_no": "12007", "name": "Mangalore Mail", "from": "Mangalore", "to": "Chennai", "status": "Delayed by 15 mins", "current_station": "Kannur"},
    {"train_no": "12008", "name": "Tejas Express", "from": "Goa", "to": "Mumbai", "status": "Running On Time", "current_station": "Ratnagiri"},
    {"train_no": "12009", "name": "Jan Shatabdi", "from": "Pune", "to": "Nagpur", "status": "Cancelled", "current_station": "No Service"},
    {"train_no": "12010", "name": "Vande Bharat", "from": "Delhi", "to": "Varanasi", "status": "Running On Time", "current_station": "Prayagraj"},
]


# ---------- TOOL ----------
def railway_tracking_tool(train_number):

    for train in trains:
        if train["train_no"] == train_number:
            return train

    return None


# ---------- REACT AGENT ----------
def react_agent(user_query):

    print("\n==============================")
    print("USER QUERY:")
    print(user_query)
    print("==============================\n")

    # THOUGHT
    print("Thought:")
    print("User wants railway tracking information.")
    print("I should extract the train number and call the railway tracking tool.\n")

    # EXTRACT TRAIN NUMBER
    words = user_query.split()

    train_number = None

    for word in words:
        if word.isdigit():
            train_number = word
            break

    # ACTION
    print("Action:")
    print(f"Calling railway_tracking_tool('{train_number}')\n")

    # OBSERVATION
    observation = railway_tracking_tool(train_number)

    print("Observation:")
    print(observation)
    print()

    # FINAL ANSWER
    print("Final Answer:")

    if observation is None:
        print("Train not found.\n")
    else:
        print(f'''
Train Number   : {observation['train_no']}
Train Name     : {observation['name']}
From           : {observation['from']}
To             : {observation['to']}
Current Station: {observation['current_station']}
Status         : {observation['status']}
''')


# ---------- MAIN LOOP ----------
while True:

    print("\nAvailable Train Numbers:")
    for t in trains:
        print(t["train_no"], "-", t["name"])

    user_input = input("\nEnter Train Number (or type exit): ")

    if user_input.lower() == "exit":
        print("\nExiting Railway Tracking Agent...")
        break

    query = f"Track train {user_input}"

    react_agent(query)

    again = input("\nDo you want to search again? (yes/no): ")

    if again.lower() != "yes":
        print("\nThank you for using Railway Tracking Agent.")
        break
