# chat_app.py

class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"User: {self.username}"


class Manager(User):
    def __init__(self, username, department):
        super().__init__(username)
        self.department = department

    def __str__(self):
        return f"Manager: {self.username}, Dept: {self.department}"


class Message:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def __str__(self):
        return f"{self.sender.username} ➜ {self.receiver.username}: {self.content}"


# Simulating a simple chat flow
if __name__ == "__main__":
    user1 = User("areeba")
    manager1 = Manager("admin", "Support")

    # Create messages
    msg1 = Message(user1, manager1, "Hello sir, I have a question.")
    msg2 = Message(manager1, user1, "Sure, go ahead.")

    # Store messages in a chat list
    chat_log = [msg1, msg2]

    # Display chat history
    print("📨 Chat History:\n")
    for msg in chat_log:
        print(msg)
