






class ToDoList:
    

    def __init__(self):
        self.tasks = []

    def add_task(self,task): #adds new task to the list
        self.tasks.append(task)
        

    def complete_task(self,task):
       print(f'{self.tasks[1]} has been completed')
        
    def display_task(self):
        for task in self.tasks:
            print(f"{task} has been completed")
        
message = ToDoList()

message.add_task("pray")
message.add_task("cleaning")
message.add_task("fishing")
#I used multiple (message.add_task) so that each member of the list will bear the completion message
message.complete_task(1)
message.display_task()


