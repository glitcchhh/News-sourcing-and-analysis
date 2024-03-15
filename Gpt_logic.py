from openai import OpenAI
import os

class GP_Generate:
    """
    A class for generating text using the OpenAI API.

    Attributes:
        api_key (str): The API key used to authenticate with the OpenAI API.
        client (OpenAI): An instance of the OpenAI class for making API requests.
        conversation_history (list): A list to store conversation history.
    """

    def __init__(self, api_key):
        """
        Initializes the Generate class with the provided API key.

        Args:
            api_key (str): The API key used to authenticate with the OpenAI API.
        """
        self.client = OpenAI(api_key=api_key)
        self.conversation_history = []

    def ask(self):
        """
        Generates text based on the provided message using the OpenAI API.

        Returns:
            str: The generated text containing answers to user queries.
        """
        while True:
            message = input("\nEnter STOP to stop the program\nContinuous running will cause credit to decrease\nEnter Your Query:\n")
            if message.upper() == "STOP":
                break
            query = "\nNew query: " + message
            self.conversation_history.append({"role": "user", "content": message})  # Add user query to conversation history
            context = [{"role": "system", "content": query}]
            context.extend(self.conversation_history[-5:])  # Include last 5 messages in the context
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",  # Specify the GPT model
                messages=context
            )
            response = completion.choices[0].message.content
            self.conversation_history.append({"role": "assistant", "content": response})  # Add AI response to conversation history with role 'assistant'
            print("AI:", response)

# Retrieve the API key from environment variables
api_key = os.getenv("API_KEY")

# Create an instance of the Generate class
generator = GP_Generate(api_key)

# Start conversation
generator.ask()
