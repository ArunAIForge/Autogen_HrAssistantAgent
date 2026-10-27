import asyncio
import os
import sys

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv


async def main() -> None:
    # 1. Load environment variables from a local .env file
    load_dotenv()

    # 2. Retrieve the OpenAI API key securely
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print(
            "Error: OPENAI_API_KEY not found in environment or .env file.\n"
            "Please create a .env file with the following line:\n"
            "OPENAI_API_KEY=your_openai_api_key_here",
            file=sys.stderr,
        )
        sys.exit(1)

    # 3. Initialize the OpenAI model client
    # OpenAIChatCompletionClient manages connections to the OpenAI API
    model_client = OpenAIChatCompletionClient(
        model="gpt-4o",
        api_key=api_key,
    )

    try:
        # 4. Create the AssistantAgent with the exact system message required
        # Note: In AutoGen v0.4, AssistantAgent acts as a core conversational agent
        agent = AssistantAgent(
            name="hr_assistant",
            model_client=model_client,
            system_message="You are an HR assistant.",
        )

        # 5. Define the task prompt
        # Disambiguating "5 lines": We explicitly instruct the model to produce
        # exactly 5 bullet points (one sentence per bullet) covering essential job dimensions.
        task = (
            "Write a job description for a Junior Python Developer. "
            "Format the output strictly as 5 bullet points (exactly 5 lines, one concise sentence per line):\n"
            "1. Role Overview\n"
            "2. Primary Responsibilities\n"
            "3. Required Technical Skills\n"
            "4. Desirable Qualifications\n"
            "5. What We Offer"
        )

        # 6. Run the agent stream and render messages using the built-in Console UI
        await Console(agent.run_stream(task=task))

    finally:
        # 7. Ensure the model client connection pool is cleanly closed to prevent script hanging
        await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())