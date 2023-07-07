from langchain.chat_models import ChatOpenAI
from langchain.chains import create_tagging_chain, create_tagging_chain_pydantic
from langchain.prompts import ChatPromptTemplate
from langchain.chains  import LLMChain
from UserInfo import PersonalDetails

import streamlit as st
import os

os.environ["OPENAI_API_KEY"] = st.secrets['apikey']
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613", verbose=True)

user_details  = PersonalDetails(first_name="",
                                last_name="",
                                company="",
                                topic="",
                                email="",
                                job_title="",
                                language="")

chain = create_tagging_chain_pydantic(user_details, llm)

def ask_user(text_input, user_details):
    return filter_response(text_input, user_details )

def check_what_is_empty(user_details):
    ask_for = []
    # Check if fields are empty
    for field, value in user_details.dict().items():
        if value in [None, "", 0]:
            print(f"Field '{field}' is empty.")
            ask_for.append(f'{field}')
    return ask_for


def add_non_empty_details(current_details: PersonalDetails, new_details: PersonalDetails):
    non_empty_details = {k: v for k, v in new_details.dict().items() if v not in [None, ""]}
    updated_details = current_details.copy(update=non_empty_details)
    return updated_details

def ask_for_info(ask_for):

    first_prompt = ChatPromptTemplate.from_template(
        "Below is are some things to ask the user for in a conversational way. you should only ask one question at a time even if you don't get all the info \
        don't ask as a list! Don't greet the user! Don't say Hi. If the ask_for list is empty then thank them and let them know that someone will be contcting them shortly.. \n\n \
        ask_for list: {ask_for}"
    )

    # info_gathering_chain
    info_gathering_chain = LLMChain(llm=llm, prompt=first_prompt)
    ai_chat = info_gathering_chain.run(ask_for=ask_for)
    return ai_chat

def filter_response(text_input, user_details ):
    #chain = create_tagging_chain_pydantic(PersonalDetails, llm)
    res = chain.run(text_input)
    # add filtered info to the
    user_details = add_non_empty_details(user_details, res)
    ask_for = check_what_is_empty(user_details)
    return user_details, ask_for
