from Composite.CompanyInterface import CompanyInterface

class Company(CompanyInterface):

    def __init__(self, name: str, nip: str, address: str, yearlyIncome: list, income, contrahents: list):
        self.name = name
        self.nip = nip
        self.address = address
        self.yearlyIncome = yearlyIncome
        self.income = income
        self.contrahents = contrahents

    def getIncome(self):
        return self.income

    def getNip(self):
        return [self.nip]

    def getReward(self):
        return 0

    def convert(self, visitor):
        return visitor.convert(self)