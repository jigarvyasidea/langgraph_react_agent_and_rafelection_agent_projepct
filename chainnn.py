from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI



initial_doctor = ChatPromptTemplate.from_messages(
    [
        (
            "system"
            "You are extern docotr understand the patient desisiens understand what kind recide they have "
            "if you found desisi by undersing contnet ands report you need to give disess name "
        )
    ]
)


final_doctor = ChatPromptTemplate.from_message(
    [
        (
            "System"
            "you are expert docotr in genral disess like fever etc you neeed to genrate detail ans about that "
        )
    ]
)

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


# task 1 --> created  prompt --> done 

# task 2 ---> we need llm to guide on that perticular prompt --> done llm too 

# now we need to execute it so we do with the help of chain 


init_dr = initial_doctor | llm

fin_dr = final_doctor | llmm



