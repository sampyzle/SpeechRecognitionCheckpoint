import streamlit as st
import speech_recognition as sr

def transcribe_speech(api_choice, language_choice):
    # Initialize recognizer class
    r = sr.Recognizer()

    try:
        # Reading Microphone as source
        with sr.Microphone() as source:
            st.info("Speak now...")
            
            # listen for speech and store in audio_text variable
            audio_text = r.listen(source)

            st.info("Transcribing...")

            try:
                if api_choice == "Google Speech Recognition":
                    # using Google Speech Recognition
                    text = r.recognize_google(audio_text, language=language_choice)
                elif api_choice == "Sphinx":
                    # using CMU Sphinx
                    text = r.recognize_sphinx(audio_text, language=language_choice)
                else:
                    text = "Unsupported API"
                return text
            except sr.UnknownValueError:
                return "Sorry, I did not understand the audio."
            except sr.RequestError as e:
                return f"Sorry, there was an error with the API request; {e}"
            except Exception as e:
                return f"An error occurred: {e}"
    except Exception as e:
        return f"An error occurred with microphone access: {e}"

def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    # Add a dropdown to select the speech recognition API
    api_choice = st.selectbox("Select Speech Recognition API", ["Google Speech Recognition", "Sphinx"])

    # Add a dropdown to choose language for speech recognition
    language_choice = st.selectbox("Choose Language", ["en-US", "es-ES", "fr-FR", "de-DE", "it-IT"])

    # Add a button to trigger speech recognition
    if st.button("Start Recording"):
        text = transcribe_speech(api_choice, language_choice)
        st.write("Transcription: ", text)

        # Add option to save the transcribed text to a file
        save_option = st.button("Save to file")
        if save_option:
            with open("transcription.txt", "w") as file:
                file.write(text)
            st.success("Transcription saved to 'transcription.txt'")

if __name__ == "__main__":
    main()
