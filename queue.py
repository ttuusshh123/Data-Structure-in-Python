class Queue:
    def __init__(self, size):
        self.rear = -1
        self.front = -1
        self.size = size
        self.l = [None]*size

    def enqueue(self, data):
        if self.rear == -1 and self.front == -1:
            self.front += 1
            self.rear = self.rear + 1
            self.l[self.rear] = data
        else:
        	if self.isfull():
        		print("queue is full")
        	else:
        		self.rear += 1
        		self.l[self.rear] = data

    def isempty(self):
        return((self.rear == -1 and self.front == -1) or (self.front > self.rear))

    def isfull(self):
        return(self.rear == self.size-1)

    def display(self):
        i = self.front
        while(i<=self.rear):
            print(self.l[i],end = " ")
            i+=1
        print()

    def dequeue(self):
        if self.rear == -1 and self.front == -1:
            print("Empty queue")
        elif self.front > self.rear:
            print("Empty queue")
        else:
            # self.l[self.front]
            self.front+=1
q = Queue(3)
# print(q.isempty())
# q.dequeue()
q.enqueue(5)
q.enqueue(3)
q.enqueue(9)
# q.enqueue(19)
q.display()
# q.dequeue()

# q.display()
