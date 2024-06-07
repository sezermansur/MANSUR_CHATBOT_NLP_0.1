MANSUR_CHATBOT_NLP_0.1 Turkish Chat Bot

This project aims to create a Turkish chat bot that responds to user inputs and improves over time. The bot analyzes user messages, searches the database for the most appropriate response, and updates its responses based on user feedback.
Table of Contents

    Features
    Installation
    Usage
    Functions

Features

    Preprocesses user messages.
    Selects the most appropriate response using TF-IDF and cosine similarity.
    Updates and improves its responses based on user feedback.
    Stores responses in a JSON file for persistence.

Installation

To run this project, follow these steps:

    Clone this repository:

    bash

git clone https://github.com/sezermansur/MANSUR_CHATBOT_NLP_0.1.git
cd MANSUR_CHATBOT_NLP_0.1

Install the required Python packages:

bash

pip install -r requirements.txt

Download the NLTK data files:

python

    import nltk
    nltk.download('stopwords')

Usage

To start the chat bot, use the following commands:

    Run the Python script:

    bash

python main.py

Start a conversation and see the bot's responses:

text

You: Merhaba
MANSUR: Merhaba! Size nasıl yardımcı olabilirim?

Confirm the bot's response or provide a new response:

text

Is my answer correct? (Y/N): Y

To update the response:

text

    Is my answer correct? (Y/N): N
    Please enter the correct answer: How are you?

Functions
save_responses()

Writes the learned_responses dictionary to the learned_responses.json file.
preprocess_message(message)

Preprocesses the given message: converts to lowercase, removes words with 1-2 characters, reduces multiple spaces to a single space, and removes stop words.
message_similarity(message1, message2)

Calculates the similarity between two messages using TF-IDF vectorizer and cosine similarity.
check_all_messages(message)

Checks the similarity of the given message with all learned responses and returns the response with the highest similarity score.
update_response(question, old_response, new_response)

Updates the old response for the given question with the new response.
