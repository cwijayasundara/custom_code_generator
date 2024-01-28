from chains import pydentic_class_def_chain, business_class_def_chain, input_validator_chain
from util.util import trade_attributes, trade_attribute_validations, trade_business_rules, safe_write

trade_fields = trade_attributes()
trade_attribute_validations = trade_attribute_validations()
trade_business_rules = trade_business_rules()

print(trade_fields)
print(trade_business_rules)
print(trade_attribute_validations)

dir_path = 'pydentic_class'

pydentic_class_def = pydentic_class_def_chain.run(trade_fields)
safe_write(dir_path, pydentic_class_def)
print(pydentic_class_def)

dir_path = 'attribute_validations'
attribute_validations = input_validator_chain.run({'pydentic_class': pydentic_class_def,
                                                   'input': trade_attribute_validations})
safe_write(dir_path, attribute_validations)
print(attribute_validations)

dir_path = 'business_validations'

business_validations = business_class_def_chain.run({'pydentic_class': pydentic_class_def,
                                                     'input': trade_business_rules})
safe_write(dir_path, business_validations)
print(business_validations)
