class A:
    def show(self):
        print("Class A method")

class B(A):
    def show(self):
        print("Class B method")

class C(A):
    def show(self):
        print("Class C method")

class D(B, C):
    pass

# Usage
d = D()
d.show()  # Check which show() is called due to MRO
