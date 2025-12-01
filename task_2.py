import speech_recognition as sr
from datetime import datetime

def capture_voice():
    recognizer = sr.Recognizer()

    with sr.Microphone() as mic:
        print("\n Speak any time...")

        recognizer.adjust_for_ambient_noise(mic)

        try:
            audio_data = recognizer.listen(mic, timeout=5)
            text_output = recognizer.recognize_google(audio_data)
            return text_output.lower()

        except Exception:
            return None


def run_assistant():
    print("=== Interactive Voice Assistant ===")
    print("Say 'stop', 'goodbye', or 'end' to finish the session.")

    running = True

    while running:
        user_voice = capture_voice()

        if not user_voice:
            continue

        print(f"User said: {user_voice}")

        # Greeting responses
        if "hey" in user_voice or "hello" in user_voice:
            print("Assistant: Hello! How can I support you today?")

        # Identity response
        elif "who are you" in user_voice or "name" in user_voice:
            print("Assistant: I'm your custom-made Python voice helper.")

        # Status response
        elif "how are you" in user_voice:
            print("Assistant: I'm operating smoothly. Thanks for asking!")

        # Time response
        elif "time" in user_voice or "clock" in user_voice:
            now = datetime.now().strftime("%H:%M %p")
            print(f"Assistant: The time right now is {now}.")

        # Location response
        elif "where are you" in user_voice or "location" in user_voice:
            print("Assistant: I'm running inside your system's memory.")

        # Joke response
        elif "joke" in user_voice or "funny" in user_voice:
            print("Assistant: Why was the computer cold? Because it forgot to close its Windows!")

        # School/College conversation
        elif "study" in user_voice or "school" in user_voice:
            print("Assistant: Education opens the door to creating programs like me!")

        # Exit conditions
        elif any(exit_word in user_voice for exit_word in ["stop", "end", "goodbye"]):
            print("Assistant: Ending program. See you soon!")
            running = False

        # Unknown input
        else:
            print("Assistant: Hmm, I'm not sure what that means.")

if __name__ == "__main__":
    run_assistant()
