# Support Chatbot for Customer Data Platforms (CDPs)

This project is a support chatbot designed to assist users with "how-to" questions related to Customer Data Platforms (CDPs). The chatbot utilizes Natural Language Processing (NLP) techniques to understand user queries and provide relevant information.

## Project Structure

```
suppChatbot
├── src
│   ├── main.py          # Entry point of the chatbot application
│   └── nlp
│       └── processor.py # NLP processing for user queries
├── requirements.txt     # List of project dependencies
├── setup.py             # Project packaging and metadata
└── README.md            # Project documentation
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd suppChatbot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the chatbot, execute the following command:
```
python src/main.py
```
To run the chatbot web application, execute the following command:
```
python src/app.py
```
The chatbot will prompt you for questions related to CDPs and provide answers based on the information processed from the documentation.

## Features

- NLP processing to understand user queries.
- Ability to fetch and provide information from CDP documentation.
- User-friendly interaction for resolving common queries.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
