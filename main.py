import os
import google.generativeai as genai

# --- Configuration ---
GEMINI_API_KEY = "AIzaSyBwZrK6Vvhi0mjVtkHdqVokIDjhMlAJ1uo"

if not GEMINI_API_KEY:
    print("Error: Gemini API key not set.")
    exit()

genai.configure(api_key=GEMINI_API_KEY)

MODEL_NAME = 'gemini-1.5-flash-latest'  # or 'gemini-1.5-pro-latest'

# --- Define local tool (function) ---

def get_current_weather(location: str) -> str:
    """
    Simulate getting current weather for a location.
    """
    print(f"\n--- Calling get_current_weather for: {location} ---")
    location = location.lower()
    if location == "chennai":
        return "The current weather in Chennai is 32°C and partly cloudy with high humidity. Expect some scattered showers."
    elif location == "london":
        return "The current weather in London is 15°C and rainy."
    elif location == "new york":
        return "The current weather in New York is 22°C and sunny."
    else:
        return f"Weather data for {location} is not available."

# --- Main Application Logic ---

def main():
    print("Gemini Function Calling Example (Python)")
    print("Type 'exit' to quit.")

    # Initialize model with tools
    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        tools=[get_current_weather]
    )

    # Start chat session
    chat = model.start_chat(history=[])

    while True:
        user_input = input("\nUser: ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            response = chat.send_message(user_input)

            # Go through each part
            for part in response.candidates[0].content.parts:
                if hasattr(part, 'function_call') and part.function_call:
                    function_call = part.function_call
                    function_name = function_call.name
                    args = {k: v for k, v in function_call.args.items()}

                    print(f"\n--- Gemini wants to call function: {function_name} with args: {args} ---")

                    if function_name == "get_current_weather":
                        location = args.get("location")
                        if location:
                            result = get_current_weather(location)
                            print(f"--- Function result: {result} ---")

                            # Send result back to Gemini for final answer
                            follow_up = chat.send_message(
                                f"The weather in {location} is: {result}"
                            )
                            print(f"\nGemini: {follow_up.text}")
                        else:
                            print("Error: No 'location' provided in function call.")

                elif hasattr(part, 'text') and part.text:
                    # Gemini responded directly
                    print(f"\nGemini: {part.text}")

        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Please check your API key, model name, and internet connection.")

if __name__ == "__main__":
    main()
