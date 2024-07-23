import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms.ctransformers import CTransformers

### llama2 function
def getllamaresponse(input_text,no_words,blog_style):
    llm= CTransformers(model='model-chat-llama2\\llama-2-7b-chat.ggmlv3.q8_0.bin', # type: ignore
                      model_type ='llama',
                      config={'max_new_tokens':256,
                                 'temperature':0.01})
    ##prompt temp
    template = """
    Write a blog for {blog_style}
    job profile for a topic {input_text}
    within {no_words} words.
            """
    prompt = PromptTemplate(input_variables=["blog_style","input_text",'no_words'],template=template)
    response = llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response

st.set_page_config(page_title="Generate Blogs",
                   page_icon='✍️✍️✍️',
                   layout='centered',
                   initial_sidebar_state='collapsed')
st.header("Generate Blogs")

input_text = st.text_input("Enter the Topic")

### 

col1,col2 = st.columns([5,5])
with col1:
    no_words = st.text_input('No of words')
with col2:
    blog_style = st.selectbox('Writing the blog for',('Common people','Data Scientist','Researchers'),index=1)
submit = st.button("Generate")

if submit:
    st.write(getllamaresponse(input_text,no_words,blog_style))