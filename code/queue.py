class Queue:
    def __init__(self):
        self.queue_list = list()

    def enqueue(self, data):
        self.queue_list.append(data)

    def dequeue(self):
        if len(self.queue_list) == 0:
            print("empty")
            return
        data = self.queue_list[0]
        del self.queue_list[0]
        return data

