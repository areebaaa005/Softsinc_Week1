class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def is_valid_email(self):
        return "@" in self.email

    def __str__(self):
        return f"User: {self.name}, Email: {self.email}"


class Intern(User):
    def __init__(self, name, email, university):
        super().__init__(name, email)
        self.university = university

    def __str__(self):
        return f"Intern: {self.name}, Email: {self.email}, University: {self.university}"


class Mentor(User):
    def __init__(self, name, email, expertise):
        super().__init__(name, email)
        self.expertise = expertise

    def __str__(self):
        return f"Mentor: {self.name}, Email: {self.email}, Expertise: {self.expertise}"


# Sample usage:
if __name__ == "__main__":
    user1 = User("Areeba", "areeba@example.com")
    intern1 = Intern("Ali", "ali@uni.edu", "FAST University")
    mentor1 = Mentor("Zain", "zain@gmail.com", "Python & AI")

    print(user1)
    print("Is valid email?", user1.is_valid_email())

    print(intern1)
    print(mentor1)
