class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
while True:
    input_line = input()
    if input_line == "Stop":
        break
    sender, receiver, content = [x for x in input_line.split(" ")]
    email = Email(sender, receiver, content)
    emails.append(email)

indexes = [int(x) for x in input().split(", ")]

[emails[i].send() for i in indexes]
# for i in indexes:
#     emails[i].send()
[print(email.get_info()) for email in emails]
# for email in emails:
#     print(email.get_info())
