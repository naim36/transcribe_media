import os
import whisper

def find_media_files(directory, extensions=(".mp3", ".wav", ".mp4", ".mkv", ".avi")):
    media_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(extensions):
                media_files.append(os.path.join(root, file))
    return media_files

def transcribe_files(directory, output_folder):
    model = whisper.load_model("tiny")
    media_files = find_media_files(directory)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file in media_files:
        print(f"Transcribing: {file}")
        result = model.transcribe(file)
        text_output_path = os.path.join(output_folder, os.path.basename(file) + ".txt")
        
        with open(text_output_path, "w", encoding="utf-8") as f:
            f.write(result["text"])
        print(f"Saved: {text_output_path}")
    
    print("All files processed!")

if __name__ == "__main__":
    input_directory = input("Enter the folder path containing media files: ")
    output_directory = os.path.join(input_directory, "transcriptions")
    transcribe_files(input_directory, output_directory)
