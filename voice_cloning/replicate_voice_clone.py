import replicate

voice_file = "path_to_your_voice_file.wav"  # Replace with the path to your voice file
# Clone the voice
clone_output = replicate.run(
    "minimax/voice-cloning",
    input={
        "voice_file": open(voice_file, "rb"),
        "model": "speech-02-turbo"  # or "speech-02-hd"
    }
)

voice_id = clone_output["voice_id"]
print("Cloned voice ID:", voice_id)