from pathlib import Path
from models.Chunk import Chunk
from prompts.create_vector import create_chunks_prompt
from constants import CHUNK_SIZE, OVERLAP
from gemini_api import call_llm, transform_doc_in_chunk

def get_files_from_knowledge_base():
    """
    Função que percorre a pasta knowledge-base e retorna uma lista de dicionários
    contendo o caminho e o conteúdo de cada arquivo.
    """
    knowledge_base_path = Path("knowledge-base")
    files = []
    
    for file_path in knowledge_base_path.rglob("*"):
        if file_path.is_file():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                files.append({
                    'path': str(file_path),
                    'content': content,
                    'meta_data': file_path.parent.name
                })
            except Exception as e:
                print(f"Erro ao ler o arquivo {file_path}: {e}")
    
    return files

def create_chunk(document):
    prompt = create_chunks_prompt.format(
        chunk_size=CHUNK_SIZE,
        overlap=OVERLAP,
        document=document
    )

    # print("oioioioiioioioio")
    # print(prompt)

    docs_transformed_in_chunks = transform_doc_in_chunk(prompt)

    # print(docs_transformed_in_chunks)


    return docs_transformed_in_chunks



if __name__ == "__main__":
    docs = get_files_from_knowledge_base()
    chunks = create_chunk(docs[0])

    print(chunks)