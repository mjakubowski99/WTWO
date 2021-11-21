from Composite.CompanyInterface import CompanyInterface

class CompanyComposite(CompanyInterface):

    def __init__(self):
        self.firms = []

    def add(self, firm: CompanyInterface):
        self.firms.append(firm)

    def getIncome(self):
        income = 0
        for firm in self.firms:
            income += firm.getIncome()

        return income

    def getNip(self):
        nips = []

        for firm in self.firms:
            nips = nips + firm.getNip()

        return nips 

    def getReward(self):
        return 0