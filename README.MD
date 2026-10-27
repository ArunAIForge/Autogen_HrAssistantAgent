AutoGen HR Assistant Agent

A lightweight AI agent application built using the Microsoft AutoGen v0.4 asynchronous architecture (autogen-agentchat). The application initializes an AssistantAgent configured with an HR persona that generates a concise, 5-line job description for a Junior Python Developer using streaming console output.

Features

Asynchronous AutoGen v0.4 Pipeline: Built natively on Python asyncio for non-blocking execution and event-driven agent interaction.

Persona-Driven Agent: Configured with a dedicated system_message="You are an HR assistant." to shape tone, priorities, and requirements.

Streaming Output: Employs AutoGen's Console UI to stream responses directly to the terminal as tokens are generated.

Explicit Prompt Disambiguation: Formats the request into 5 distinct, single-sentence bullet points to avoid ambiguous line wrapping.

Secure Configuration: Uses python-dotenv to safely load API credentials from .env without exposing them in source code.

Resource Management: Ensures clean lifecycle management by shutting down HTTP connection pools via await model_client.close().

Project Structure

.
├── .env                  # Local environment file (contains API keys; untracked)
├── .gitignore            # Git exclusion rules for virtual environments and secrets
├── hr_agent.py           # Main application script containing the async agent
├── README.md             # Project documentation and setup guide
└── requirements.txt      # Python package dependencies


Prerequisites

Python 3.10+

OpenAI API Key: Obtainable from the OpenAI Platform.

Installation

Clone or download this repository:

git clone <repo-url>
cd <repo-folder>


Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Configuration

Create a .env file in the root directory (or update the existing one) with your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key_here


Usage

Run the agent script:

python hr_agent.py


Expected Output

The Console utility will stream the response from the hr_assistant agent into the terminal:

---------- user ----------
Write a job description for a Junior Python Developer. Format the output strictly as 5 bullet points (exactly 5 lines, one concise sentence per line):
1. Role Overview
2. Primary Responsibilities
3. Required Technical Skills
4. Desirable Qualifications
5. What We Offer
---------- hr_assistant ----------
* Role Overview: We are looking for an enthusiastic Junior Python Developer to collaborate with our engineering team in building and maintaining backend services.
* Primary Responsibilities: You will write clean, well-tested Python code, assist with API integrations, and contribute to continuous codebase improvements.
* Required Technical Skills: Proficiency in foundational Python, familiarity with Git version control, and basic comprehension of RESTful architecture are required.
* Desirable Qualifications: Prior exposure to modern frameworks like FastAPI or Django, as well as relational database queries, is a strong plus.
* What We Offer: We provide competitive compensation, comprehensive healthcare coverage, dedicated mentorship, and abundant professional development opportunities.


Design Highlights

Clean HTTP Shutdown: The OpenAI HTTP client maintains an active connection pool. Invoking await model_client.close() inside a finally block prevents terminal hanging and connection leaks.

Deterministic Prompting: LLMs interpret "5 lines" variably (paragraphs, bullet lists, or summary sentences). Defining clear categories in the task prompt ensures consistent single-sentence outputs.