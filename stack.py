class Stack:
    def __init__(self):
        self.l = []
        self.top = -1
    def push(self, x):
        self.top += 1
        self.l.append(x)
    def pop(self):
        self.top -= 1
        return(self.l.pop())
    def display(self):
        print(self.l)

st = Stack()
st.push(8)
st.display()
st.push(9)
st.display()
st.pop()
st.display()
