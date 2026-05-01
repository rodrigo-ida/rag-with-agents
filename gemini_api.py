from google import genai
import os
from dotenv import load_dotenv
from constants import LLM_MODEL
from models.Chunk import Chunk

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def call_llm(contents, config=None):

    params = {
        "model": LLM_MODEL,
        "contents": contents
    }

    if config is not None:
        params["config"] = config
    # print("oioioioiioioioio222222222222222")
    # print(params)

    response = client.models.generate_content(**params)

    


    return response

def transform_doc_in_chunk(contents):

    config={
        'response_mime_type': 'application/json',
        'response_schema': Chunk,
    }
    response = call_llm(contents,config)

    # print("oioioioiioioioio2222222222222223333333333333433434344")
    # print(response.candidates[0].content.parts[0].text)

    return response.candidates[0].content.parts[0].text