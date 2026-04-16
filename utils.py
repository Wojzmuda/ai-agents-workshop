from google.genai.types import GenerateContentResponse

def print_token_usage(response: GenerateContentResponse):
    # TODO: Zadanie 2
    if response and response.usage_metadata:
        print(f"Prompt tokens: {'TODO'}") # type: ignore
        print(f"Reponse tokens: {'TODO'}") # type: ignore