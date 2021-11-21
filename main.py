
from Composite.CompanyComposite import CompanyComposite
from Composite.Company import Company
from Decorators.FullRewardDecorator import FullRewardDecorator

from Visitors.JsonConverterVisitor import JsonConverterVisitor
from Visitors.XmlConverterVisitor import XmlConverterVisitor

holding = CompanyComposite()

company1 = Company(
    "facebook",
    "9999999999",
    "Wall street 3",
    [ 1000000 for x in range(0,10) ],
    10000000,
    ["Test1", "Test2"]
)

company2 = Company(
    "google",
    "12345678",
    "Wall street 4",
    [ 2000000 for x in range(0,10) ],
    20000000,
    ["Test3", "Test4"]
)

holding.add( company1 )
holding.add( company2 )

print("-----------Nagrody firm-------------")
fullRewardDecorator = FullRewardDecorator(company1)
print("Nagroda firmy {}:".format(company1.name) , fullRewardDecorator.getReward() )

fullRewardDecorator.decorate(company2)
print("Nagroda firmy {}:".format(company2.name), fullRewardDecorator.getReward() )

fullRewardDecorator.decorate(holding)
print("Nagroda holdingu firm:", fullRewardDecorator.getReward() )


print("\n\n-----------------Wyniki konwertowania: ---------------------")
print( company1.convert(JsonConverterVisitor()) )
print( company2.convert(XmlConverterVisitor()) )







