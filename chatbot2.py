def greet():
    print("Welcome to QuickSupport Chatbot!")
    print("How can I help you today?")
    print("You can ask about:")
    print("- Product Information")
    print("- Order Status")
    print("- Refund Policy")
    print("- Technical Support")
    print("- Exit")

def get_response(user_input):
    user_input = user_input.lower()

    if "product" in user_input:
        return "We offer a wide range of products including electronics, home appliances, and clothing. Please visit our website for more details."

    elif "order" in user_input or "status" in user_input:
        return "To check your order status, please visit 'My Orders' section on our website or app."

    elif "refund" in user_input or "return" in user_input:
        return "Our refund policy allows returns within 30 days of purchase. Refunds are processed within 5-7 business days after approval."

    elif "technical" in user_input or "support" in user_input:
        return "Please describe your technical issue. Our support team will assist you shortly."

    elif "exit" in user_input or "bye" in user_input:
        return "Thank you for contacting QuickSupport! Have a great day."

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def chatbot():
    greet()
    while True:
        user_input = input("\nYou: ")
        response = get_response(user_input)
        print(f"Bot: {response}")
        if "thank you" in user_input.lower() or "exit" in user_input.lower() or "bye" in user_input.lower():
            break

if __name__ == "__main__":
    chatbot()
