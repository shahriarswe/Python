class Student:
    def __init__(self, name, grade):
        self.name, self.grade = name, grade

@register
def demo_06():
    students = [Student("Ayesha", 90), Student("Rafi", 78), Student("Nabil", 85)]
    best = max(students, key=lambda s: s.grade)
    print("06: top student =", best.name, "with grade", best.grade)
