from google.genai.types import GenerateContentResponse

def print_token_usage(response: GenerateContentResponse):
    # TODO: Zadanie 2
    if response and response.usage_metadata:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}") # type: ignore
        print(f"Reponse tokens: {response.usage_metadata.total_token_count}") # type: ignore