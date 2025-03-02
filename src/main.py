from nlp.processor import NLPProcessor

class Chatbot:
    def __init__(self):
        self.nlp_processor = NLPProcessor()

    def get_response(self, user_input):
        response = self.nlp_processor.extract_information(user_input)
        return response

    def start_chat(self):
        print("Welcome to the Customer Data Platform Support Chatbot!")
        print("Ask me how-to questions related to CDPs. Type 'exit' to end the chat.")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for chatting! Goodbye!")
                break
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.start_chat()