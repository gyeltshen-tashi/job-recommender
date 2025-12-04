import fitz # PyMuPDF
import ollama 



def extract_text_from_pdf(uploaded_file):
  """
  Extracts text from PDF file. 
  Args: 
      uploaded_file (str): The path to the PDF File.

  Returns: 
      str: The extracted text.
  """
  doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
  text = ""
  for page in doc: 
    text += page.get_text()
  return text
  

def ask_llm(prompt, max_tokens=500):
    
  """
  Sends a prompt to the LLM and returns the response.
  
  Args:
      prompt(str): The prompt to send to the LLM.
      model(str): The model to use for the request.
      temperature(float): The temperature for the response.
      
  Returns:
      str: The response from the OpenAI API.
  """
  response = ollama.chat(
    model="llama3.2",
    messages=[
      {
        "role":"user",
        "content":prompt
      }
    ],
    options={
      "temperature":0.5,
      "num_predict": max_tokens
    }
  )
  return response.message.content



