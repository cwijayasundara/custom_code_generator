from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model_name='gpt-4-1106-preview',
                 streaming=True,
                 callbacks=[StreamingStdOutCallbackHandler()],
                 temperature=0
                 )

prompt = """System: You are an expert engineer in generating python code. Your job is to generate a pydentic class 
definition based on the values in the comma separated string. Don't hesitate to make design choices if the initial 
description doesn't provide enough information. Just generate the pydentic class definition and nothing else!!

Human: {input}

pydentic class:
"""

pydentic_class_def_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)

prompt = """
System: You are an expert engineer in generating python code. Your job is to generate a python class with 
business logic based on the business rules in the comma separated string. 
- break business functionality into multiple functions based on business logic and SOLID principles
- generate unit tests for each function to make sure the function works correctly
- generate a main function that calls all the functions in the correct order
- use the Pydentic class definition generated in the previous step to create the input to the main function
- use the attributes of the Pydentic class to generate the business logic

pydentic class : {pydentic_class} 

Just generate the python code and nothing else!!

generate a python service class to validate the business rules.

Human: {input}

complete python class with business logic:
"""

business_class_def_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)

prompt = """
System: You are an expert engineer in generating python code. Your job is to generate a python class with 
input validations based on input validation rules in the comma separated string.
- create a python class for for all the input validation rules with a function for each rule
- generate unit tests for each function to make sure the functions are working correctly
- use the Pydentic class definition passed as an input
- use the attributes of the Pydentic class to generate the validation logic

pydentic class : {pydentic_class} 

Just generate the python code and nothing else!!

generate a python attribute validation class to validate the attributes.

Human: {input}

complete python class with input validation logic:
"""

input_validator_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)
