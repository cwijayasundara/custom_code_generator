import warnings
import streamlit as st

from chains import (pydentic_chain, attribute_validation_chain, business_validation_chain, controller_chain,
                    repository_chain)
from util.util import attributes, attribute_validations, business_rules

warnings.filterwarnings("ignore")

attribute_set = attributes()
attribute_validations_set = attribute_validations()
business_rules_set = business_rules()

""" convert the list of strings to a comma separated string """
attribute_set = ', '.join(attribute_set)
print("converted attribute set is", attribute_set)

business_rules_set = ', '.join(business_rules_set)
print("converted business validation set is", business_rules_set)

st.title("Code Generator")

language = st.radio("Select Language:", ["Python"])

submit = st.button("submit", type="primary")

if language and submit:

    pydentic_class_def = pydentic_chain.run({'input': attribute_set})
    st.markdown(""" :blue[Pydentic Class Definition : ] """, unsafe_allow_html=True)
    st.markdown(pydentic_class_def)

    attribute_validation_class_def = attribute_validation_chain.run({'input': attribute_validations_set,
                                                                     'pydentic_class': pydentic_class_def})
    st.markdown(""" :blue[Attribute Validations Class Definition : ] """, unsafe_allow_html=True)
    st.markdown(attribute_validation_class_def)

    business_validation_class_def = business_validation_chain.run({'input': business_rules_set,
                                                                   'pydentic_class': pydentic_class_def})
    st.markdown(""" :blue[Business Rules Class Definition : ] """, unsafe_allow_html=True)
    st.markdown(business_validation_class_def)

    controller_class_def = controller_chain.run({'pydentic_class': pydentic_class_def})
    st.markdown(""" :blue[Controller Class Definition : ] """, unsafe_allow_html=True)
    st.markdown(controller_class_def)

    repository_class_def = repository_chain.run({'pydentic_class': pydentic_class_def})
    st.markdown(""" :blue[Repository Class Definition : ] """, unsafe_allow_html=True)
    st.markdown(repository_class_def)
