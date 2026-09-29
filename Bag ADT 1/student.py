class student:
    def __init__(self, first, last, ssn, email, age):
        self.first = first
        self.last = last
        self.ssn = ssn
        self.email = email
        self.age = age
    # init first name, last name, ssn, email, age
    def __eq__(self, rhs):
        return self.ssn == rhs.ssn