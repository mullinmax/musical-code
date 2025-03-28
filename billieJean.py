class Person:
    def __init__(self, relationship):
        self.relationship = relationship

BillieJean = Person("just a girl")

i = 0
if BillieJean.relationship != "lover":
    print("Billie Jean is not my lover")
    print(f"She's: {BillieJean.relationship}")
    assert i == 1
else:
    print("Billie Jean is my lover")

