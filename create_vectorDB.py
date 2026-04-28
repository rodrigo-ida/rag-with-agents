from pathlib import Path

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
                    'meta': file_path.parent.name
                })
            except Exception as e:
                print(f"Erro ao ler o arquivo {file_path}: {e}")
    
    return files