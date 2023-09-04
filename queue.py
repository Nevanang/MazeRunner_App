class Queue():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items == []
    def get(self):
        return self.items[0]
    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.isEmpty():
            return None
        else: return self.items.pop(0)
    def __str__(self):
        output = '<'
        for i in range( len(self.items) ):
            item = self.items[i]
            if i < len(self.items)-1 :
                output += f'{str(item)}, '
            else:
                output += f'{str(item)}'
        output += '>'
        return output