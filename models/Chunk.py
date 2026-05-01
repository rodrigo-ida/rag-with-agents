from pydantic import BaseModel, Field

class Result(BaseModel):
    page_content: str
    metadata: dict

class Chunk(BaseModel):
    headline: str = Field(
            description="A consise heading for this chunk. A short sentence explaining what this chunk is about"
    )
    summary: str = Field(
            description="the summary of this chunks. this should answer some surface common questions about the topic"
    )
    original_text: str = Field(
        description="The original text of this chunk from the provided document, exactly as is, not changed in any way"
    )
    
    def as_result(self, document):
        metadata = {"source": document["source"], "type": document["type"]}
        return Result(
            page_content=self.headline + "\n\n" + self.summary + "\n\n" + self.original_text,
            metadata=metadata,
        )
    















# sdk_http_response=HttpResponse(
#   headers=<dict len=12>
# ) candidates=[Candidate(
#   content=Content(
#     parts=[
#       Part(
#         text="""{
#   "headline": "Overview of Insurellm Company History and Growth",
#   "summary": "Insurellm was founded in 2015 by Avery Lancaster as an insurance tech startup, initially launching Markellm. It grew rapidly until 2020, expanding its product portfolio to include Carllm, Homellm, and Rellm, reaching 200 employees and 12 offices.",
#   "original_text": "# About Insurellm\n\nInsurellm was founded by Avery Lancaster in 2015 as an insurance tech startup designed to disrupt an industry in need of innovative products. Its first product was Markellm, the marketplace connecting consumers with insurance providers.\n\nThe company experienced rapid growth in its first five years, expanding its product portfolio to include Carllm (auto insurance portal), Homellm (home insurance portal), and Rellm (enterprise reinsurance platform). By 2020, Insurellm had reached a peak of 200 employees with 12 offices across the US."
# }
# ```"""
#       ),
#     ],
#     role='model'
#   ),
#   finish_reason=<FinishReason.STOP: 'STOP'>,
#   index=0
# )] create_time=None model_version='gemma-4-31b-it' prompt_feedback=None response_id='2-XzacSoPKudz7IP8rmG2Q4' usage_metadata=GenerateContentResponseUsageMetadata(
#   candidates_token_count=234,
#   prompt_token_count=854,
#   prompt_tokens_details=[
#     ModalityTokenCount(
#       modality=<MediaModality.TEXT: 'TEXT'>,
#       token_count=854
#     ),
#   ],
#   total_token_count=1088
# ) model_status=None automatic_function_calling_history=[] parsed=None










#  text='{\n  
#     "headline": "Overview of Insurellm\'s founding and early growth",\n  
#     "summary": "Insurellm was founded in 2015 by Avery Lancaster, starting with the Markellm marketplace and expanding to include Carllm, Homellm, and Rellm, reaching 200 employees by 2020.",\n  
#     "original_text": "# About Insurellm\\n\\nInsurellm was founded by Avery Lancaster in 2015 as an insurance tech startup designed to disrupt an industry in need of innovative products. Its first product was Markellm, the marketplace connecting consumers with insurance providers.\\n\\nThe company experienced rapid growth in its first five years, expanding its product portfolio to include Carllm (auto insurance portal), Homellm (home insurance portal), and Rellm (enterprise reinsurance platform). By 2020, Insurellm had reached a peak of 200 employees with 12 offices across the US."\n
# }
# \n```' thought=None thought_signature=None video_metadata=None tool_call=None tool_response=None part_metadata=None