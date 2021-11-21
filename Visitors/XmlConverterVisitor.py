from Composite.Company import Company
from Visitors.ConverterVisitor import ConverterVisitor

class XmlConverterVisitor(ConverterVisitor):

    def convert(self, company: Company):
        print('Xml: ')
        return self.object_to_xml(company.__dict__)

    def object_to_xml(self,data, root='object'):
        xml = f'<{root}>'
        if isinstance(data, dict):
            for key, value in data.items():
                xml += self.object_to_xml(value, key)

        elif isinstance(data, (list, tuple, set)):
            for item in data:
                xml += self.object_to_xml(item, 'item')

        else:
            xml += str(data)

        xml += f'</{root}>'
        return xml
