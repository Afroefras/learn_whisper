import whisper
from pathlib import Path

MODEL = "small"


class FullTranscription:
    def __init__(self, model_size: str) -> None:
        self.model_name = model_size
        self.get_model()

    def get_model(self) -> None:
        self.model = whisper.load_model(self.model_name)
        print(f"\nWhisper's {self.model_name} model imported successfully!\n")

    def transcript_audio(self, audio_dir: str) -> dict:
        transcription = self.model.transcribe(audio_dir)
        return transcription

    def audio_to_txt(self, audio_dir: str) -> None:
        file_name = Path(audio_dir).stem

        transcription = self.transcript_audio(audio_dir)

        output_dir = f"transcripted_files/{file_name}.txt"
        with open(output_dir, "w") as txt:
            txt.write(transcription["text"])

        print(f"\n{output_dir} saved succesfully!\n")


ft = FullTranscription(MODEL)
ft.audio_to_txt(audio_dir="files_to_transcript/sync_dash_test.mp3")
