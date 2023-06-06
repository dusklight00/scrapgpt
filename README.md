# ScrapGPT

ScrapGPT is a simple yet powerful library that allows developers to easily interact with the ChatGPT by scraping the website. It provides a convenient interface to send messages to the website and receive responses, making it easy to integrate ChatGPT into your own applications.

## Installation

You can install ScrapGPT using pip, the Python package manager. Open your command-line interface and execute the following command:

```python
pip install scrapgpt
```

## Getting Started

To get started, use the following simple 3 line code.

```python
from scrapgpt import ScrapGPT

# Open AI Login Credentials
EMAIL = "..."
PASSWORD = "..."

chatgpt = ScrapGPT(EMAIL, PASSWORD)
response = chatgpt.ask("How are you?")

print(response)

# As an AI language model, I don't have
# feelings or emotions, but I'm here to
# help you with any questions or information
# you need. How can I assist you today?
```
