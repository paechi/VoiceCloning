import os
import torch
import sys
from InferenceInterfaces.ToucanTTSInterface import ToucanTTSInterface


def read_texts(model_id, sentence, filename, device="cpu", language="en", 
speaker_reference=None, faster_vocoder=False):
    tts = ToucanTTSInterface(device=device, tts_model_path=model_id, 
faster_vocoder=faster_vocoder)
    tts.set_language(language)
    if speaker_reference is not None:
        tts.set_utterance_embedding(speaker_reference)
    if type(sentence) == str:
        sentence = [sentence]
    tts.read_to_file(text_list=sentence, file_location=filename)
    del tts


def clone_voice(version, text, speaker_reference, model_id="Meta", exec_device="cpu", 
speed_over_quality=True):
    os.makedirs("audios", exist_ok=True)

    read_texts(model_id=model_id,
               sentence=[text],
               filename="audios/" + speaker_reference.split('/')[-1].split('.')[0] + 
'_cloned.wav',
               device=exec_device,
               language="en",
               speaker_reference=speaker_reference,
               faster_vocoder=speed_over_quality)


if __name__ == '__main__':
    text = sys.argv[1]
    audio_filepath = sys.argv[2]

    exec_device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"running on {exec_device}")

    clone_voice(version="MetaBaseline",
                text=text,
                speaker_reference=audio_filepath,
                model_id="Meta",
                exec_device=exec_device,
                speed_over_quality=exec_device != "cuda")
