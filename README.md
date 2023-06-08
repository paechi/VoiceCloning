# VoiceCloning
This repository provides a quick research on current state-fo-the-art methods on Voice 
Cloning. My task is to do the voice cloning on the audio in any language (for 
simplicity, it can be only English) and generate new audio samples based the given text 
in any language. So far, I have found several models that promise a very impressive 
text synthesis with just a minute or even seconds of reference audio.

- [x] **TortoiseTTS**: SOTA model in the open source, which incorporates DALL-E and 
Diffusion models for TTS task. It performs very well, but only for English language. 
You can check my experiments in [![Open In 
Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1tpaTRWY24A8ADcR0IyGKHqUM_Kg3EM9i?authuser=2#scrollTo=Bsu_u1x5BCb7)
- [x] **Multi-Tacotron Voice Cloning**: Multi-Tacotron Voice Cloning repo is a phonemic 
multilingual (Russian-English) implementation based on Real-Time-Voice-Cloning. It is a 
four-stage deep learning framework that allows to create a numerical representation of 
a voice from a few seconds of audio, and to use it to condition a text-to-speech model. 
The results are not bad, especially for bilingual(Russian-English) text. But the model 
is considered to be quite outdated, so it might be better to consider more sota models. 
You can check my experiments in [![Open In 
Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1wpCL69vTnQfcFud45-HtCMjy5qsoH1rZ#scrollTo=6ZCIPpnozOWu)
- [x] **ToucanTTS**: Multilingual multi-speaker TTS model which proves Language 
Agnostic Meta Learning (LAML) method to be effective. I tested their ToucanTTS + 
HifiGAN models on test audio and the results are mediocre. Perhaps, extra finetuning on 
longer reference audios, could improve the performance. You can check my experiments in 
[![Open In 
Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ngV-503Ph5fTxf0gDQMFW9NkbDKkH5jv#scrollTo=_HXlWoXNxYZh)
- [x] **CoquiTTS/YourTTS**: A powerful toolkit which provides TTS models on 20+ 
languages and various scripts for voice cloning and conversion. It had multilingual 
YourTTS model, but for now it only supports 3 languages. Text synthesis, especially for 
VITS models, is quite well, but for every language you have to create a new model and 
do the separate voice cloning and text synthesis. You can check my experiments in 
[![Open In 
Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kRJCZ2n-UV2lAqTS0Gxa_0FAmonI9c4v#scrollTo=dgsHPRj3UrTw)
- [ ] **VALL-E**: The authors claim that they need just 3 seconds of audio to 
synthesize a text. The problem is that even though there is an unofficial code 
implementation available, the pretrained model is not released yet. This model seems to 
be the most promising, but there is not much can be done.

To conclude, for the given task, Multi-Tacotron Voice Cloning model seems to be the 
most stable, even though the performance is pretty low. ToucanTTS and YourTTS models 
are performing quite well, but the former doesn't clone the voice, but rather just the 
style of the speaker and the latter has a limited language choice. I think, the easiest 
and quickest solution for this task is to finetune YourTTS for Russian and other 
languages of need. For TortoiseTTS and VALL-E, we would need lots of resources, so it 
might not be the best option in case of limited computational power.

