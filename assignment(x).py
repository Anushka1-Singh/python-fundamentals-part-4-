class User:
    def __init__(self,user_id):
        self.user_id=user_id
        self.text=None
    def message(self):
       self.text = input("enter your text : ")
       return f"You entered: {self.text}"
class Message(User):
    #To share data between methods or classes, 
    #variables must be stored as instance attributes using self.
    def display_message(self): 
        return self.text
class ChatRoom(Message):
    def __init__(self, user_id, join_time, leave_time):
        super().__init__(user_id)
        self.join_time=join_time
        self.leave_time=leave_time
    def chat_history(self):
        return self.text
c = ChatRoom(101, "10:00", "11:00")

print(c.message())
print(c.display_message())
print(c.join_time, c.leave_time)
print(c.chat_history())



# Problem: Design a simple chat system using multilevel inheritance where
# a User sends a message, the Message class displays it, and the ChatRoom
# class extends the behavior by adding chat context (join and leave time).


    


