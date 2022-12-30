class Person:
    def __init__(self, name: str, surname: str):
        self.surname = surname
        self.name = name

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __repr__(self):
        return f"{self.name} {self.surname}"

    
class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)
    
    def __add__(self, other):
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __getitem__(self, index):
        return f"Person {index}: {str(self.people[index])}"

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(str(x) for x in self.people)}"
