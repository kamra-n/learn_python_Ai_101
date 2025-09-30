from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import os
from dotenv import load_dotenv
import pdfplumber


class PDFExtractor:
    """Handles PDF text extraction."""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract_text(self) -> str:
        all_content = ""
        with pdfplumber.open(self.file_path) as pdf:
            for page in pdf.pages:
                all_content += page.extract_text() or ""  # Handle empty pages safely
        return all_content


class AIModelConfig:
    """Configures the external AI client and model."""

    def __init__(self, api_key_env: str = "GEMINI_API_KEY"):
        load_dotenv()
        self.api_key = os.getenv(api_key_env)

        self.external_client = AsyncOpenAI(
            api_key=self.api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        )

        self.model = OpenAIChatCompletionsModel(
            model="gemini-2.0-flash",
            openai_client=self.external_client
        )

        self.config = RunConfig(
            model=self.model,
            model_provider=self.external_client,
            tracing_disabled=True
        )


class BookAssistant:
    """Main class to interact with the AI for book-related queries."""

    def __init__(self, config: AIModelConfig):
        self.config = config
        self.agent = Agent(
            name="Assistant",
            instructions="You are a helpful assistant helping in extracting the books"
        )

    def ask(self, query: str) -> str:
        result = Runner.run_sync(self.agent, query, run_config=self.config.config)
        return result.final_output


if __name__ == "__main__":
    # Step 1: Extract PDF text
    pdf_reader = PDFExtractor("poem.pdf")
    content = pdf_reader.extract_text()

    # Step 2: Configure AI Model
    ai_config = AIModelConfig()

    # Step 3: Ask AI about the content
    assistant = BookAssistant(ai_config)
    answer = assistant.ask(f"Who is the author: {content}")

    print("\n--- AI Response ---")
    print(answer)
