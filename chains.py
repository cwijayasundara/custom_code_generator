from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# gpt-4-0125-preview
# gpt-3.5-turbo-0125

llm = ChatOpenAI(model_name='gpt-4-0125-preview',
                 streaming=True,
                 callbacks=[StreamingStdOutCallbackHandler()],
                 temperature=0
                 )

prompt = """

System: 

You are an expert Python engineer and your job is to generate a fully functional pydentic class based on the
values in the comma separated string.

ONLY RETURN THE FULLY FUNCTIONAL PYDENTIC CLASS AND NOTHING ELSE !

input: {input}

pydentic class:

"""

pydentic_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)

prompt = """

System: 

You are an expert Python engineer and your job is to generate a fully functional attribute validation class based on the
values in a list of strings {input}.

Convert the list of strings to a comma separated string and use that as the input to generate the attribute validation.

YOU ARE PROVIDED WITH THE PYDENTIC CLASS DEFINITION {pydentic_class} AND IMPORT
THAT FROM YOUR ATTRIBUTE VALIDATION CLASS AND DO NOT GENERATE THE PYDENTIC CLASS DEFINITION AGAIN !!

ONLY RETURN THE FULLY FUNCTIONAL ATTRIBUTE VALIDATION CLASS AND NOTHING ELSE !

input: {input}

pydentic_class: {pydentic_class}

attribute validation class:

"""

attribute_validation_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)

prompt = """

System: 

You are an expert Python engineer and your job is to generate a fully functional business validation class based on the
values in the comma separated string {input}.

YOU ARE PROVIDED WITH THE PYDENTIC CLASS DEFINITION {pydentic_class} AND IMPORT
THAT FROM YOUR ATTRIBUTE VALIDATION CLASS AND DO NOT GENERATE THE PYDENTIC CLASS DEFINITION AGAIN !!

ONLY RETURN THE FULLY FUNCTIONAL BUSINESS VALIDATION CLASS AND NOTHING ELSE !

input: {input}

pydentic_class: {pydentic_class}

business validation class:

"""

business_validation_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)

prompt = """System:

You are an expert Python engineer and your job is to develop a fully functional microservice to manage the provided 
business entity class {pydentic_class}.

Can you generate fully functional code for a RESTful controller class for the provided entity class {pydentic_class}?

YOU ARE PROVIDED WITH THE PYDENTIC CLASS DEFINITION {pydentic_class} AND IMPORT
THAT FROM YOUR ATTRIBUTE VALIDATION CLASS AND DO NOT GENERATE THE PYDENTIC CLASS DEFINITION AGAIN !!

ONLY RETURN THE FULLY FUNCTIONAL RESTFUL CONTROLLER CLASS AND NOTHING ELSE !

pydentic_class: {pydentic_class}

controller class:

"""

controller_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)

prompt = """System:

You are an expert Python engineer and your job is to develop a fully functional microservice to manage the provided 
business entity class {pydentic_class}.

Can you generate fully functional code for a data persistence  class for the provided entity class {pydentic_class}?

YOU ARE PROVIDED WITH THE PYDENTIC CLASS DEFINITION {pydentic_class} AND IMPORT
THAT FROM YOUR ATTRIBUTE VALIDATION CLASS AND DO NOT GENERATE THE PYDENTIC CLASS DEFINITION AGAIN !!

ONLY RETURN THE FULLY FUNCTIONAL DATA PERSISTENCE CLASS AND NOTHING ELSE !

pydentic_class: {pydentic_class}

repository class:

"""

repository_chain = LLMChain.from_string(
    llm=llm,
    template=prompt
)
