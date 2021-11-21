from Composite.Company import Company
from Visitors.ConverterVisitor import ConverterVisitor

import json

class JsonConverterVisitor(ConverterVisitor):

    def convert(self, company: Company):
        print('Json: ')
        return json.dumps( company.__dict__ )

