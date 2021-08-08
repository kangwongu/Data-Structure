class Stack:
    def __init__(self):
        self.stack_list = list()

    def push(self, data):
        self.stack_list.append(data)

    def pop(self):
        if len(self.stack_list) == 0:
            print("empty")
            return
        data = self.stack_list[-1]
        del self.stack_list[-1]
        return data
