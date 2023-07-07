import streamlit as st
from conversational_form_service import ask_user, ask_for_info
from UserInfo import PersonalDetails

if "user_details" not in st.session_state:
    st.session_state['user_details'] = PersonalDetails(first_name="",
                                last_name="",
                                company="",
                                topic="",
                                email="",
                                job_title="",
                                language="english")

# define the UI containers
header_container = st.container()
chat_output_container = st.container()
chat_container = st.container()
contact_form = st.container()
with header_container:
    st.header("Contact Us")
    st.subheader("What may I assist you with?")

with chat_output_container:
    st.write(":robot_face:  Tell me what information you are looking for. Please provide your contact information.")

with chat_container:
    #_user_input = st.empty()
    user_text = st.text_input(label='', placeholder="Send a message", label_visibility='hidden')
    if user_text:
        user_details, ask_for = ask_user(user_text, st.session_state['user_details'])
        if user_details is not None:
            #chat_output_container.write(user_details)
            st.session_state['user_details'] = user_details
            question = ask_for_info(ask_for)
            st.session_state.user_prompt = question
            chat_output_container.write(f":computer: {user_text}")
            chat_output_container.write(f":robot_face:  {question}")
    # else:
    #     st.warning("Please enter a topic to proceed.")

with st.expander("View Contact Form"):
    st.write(f"I am intested in : {st.session_state.user_details.topic}")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"First Name: {st.session_state.user_details.first_name}")
        st.write(f"Company:    {st.session_state.user_details.company}")
        st.write(f"Job Title:  {st.session_state.user_details.job_title}")

    with col2:
        st.write(f"Last Name: {st.session_state.user_details.last_name}")
        st.write(f"email (work): {st.session_state.user_details.email}")

with st.sidebar:
    st.title('About')
    st.markdown('''
        The goal of 'Contact Us' is to provide a way for users to 
        use natural language to fill out a web form. I have been testing using English, Spanish, and French user entries. 

         -This is a Proof Of Concept (POC). 

     ''')
    st.title('Technology')
    st.markdown('''
        Developed by Jorge Duenas using:
        - [OpenAI GPT-3.5 API](https://openai.com/product)
        - [Streamlit.io](https://streamlit.io/)
        - [LangChain](https://python.langchain.com/en/latest/index.html)
        - [Python](https://www.python.org/)
        - [Anaconda](https://www.anaconda.com/)   
        - [Pycharm IDE](https://www.jetbrains.com/pycharm/) 
 
    ''')