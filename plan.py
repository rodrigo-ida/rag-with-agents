# CRIAR UM RAG

# CRIACAO DO VECTOR DB
#     pega os arquivos da pasta onde as infos estao
#     quebra elas em chunks
        # chunks sao criados enviando o arquivo inteiro a llm com um
        # prompt para devolver com structured output em formato de chunk
        #     formato de chunk pode ser o seguinte

        #         class Result(BaseModel):
        #             page_content: str
        #             metadata: dict

        #         class Chunk(BaseModel):
        #             headline: str = Field(
        #                 description="A brief heading for this chunk, typically a few words, that is most likely to be surfaced in a query",
        #             )
        #             summary: str = Field(
        #                 description="A few sentences summarizing the content of this chunk to answer common questions"
        #             )
        #             original_text: str = Field(
        #                 description="The original text of this chunk from the provided document, exactly as is, not changed in any way"
        #             )
        #             def as_result(self, document):
        #                 metadata = {"source": document["source"], "type": document["type"]}
        #                 return Result(
        #                     page_content=self.headline + "\n\n" + self.summary + "\n\n" + self.original_text,
        #                     metadata=metadata,
        #                 )
#     faca o processo de embbeding
#     embeda elas
#     salva no chroma

# CRIAR O RAG

#     pega a pergunta do usuario
#     pede pra llm pegar os chunks relativos a pergunta
#     coloca os chunks recuperados como contexto e inclui a pergunta
#     responde com base na pergunta

# CRIA MECANISMO DE HISTORICO

#     isso eh plussss