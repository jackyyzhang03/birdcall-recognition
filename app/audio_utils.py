import torch
import torchaudio
import random


class AudioUtils:
    @staticmethod
    def get_format(file):
        formats = {
            'audio/wav': 'WAV',
            'audio/wave': 'WAV',
            'audio/x-wav': 'WAV',
            'audio/x-pn-wav': 'WAV',
            'audio/mpeg': 'MP3',
            'audio/mp3': 'MP3',
            'audio/flac': 'FLAC',
            'audio/ogg': 'OGG/VORBIS',
            'audio/vorbis': 'OGG/VORBIS',
            'audio/opus': 'OPUS'
        }
        format = formats.get(file.mimetype)
        return format

    @staticmethod
    def read(file):
        waveform, sample_rate = torchaudio.load(
            file, format=AudioUtils.get_format(file))
        return waveform, sample_rate

    @staticmethod
    def rechannel(audio):
        waveform, sample_rate = audio
        if waveform.shape[0] == 1:
            return waveform, sample_rate
        waveform = waveform[:1, :]
        return waveform, sample_rate

    @staticmethod
    def resample(audio, sr=32000):
        waveform, sample_rate = audio
        waveform = torchaudio.transforms.Resample(sample_rate, sr)(waveform)
        return waveform, sr

    @staticmethod
    def resize(audio, seconds=10):
        waveform, sample_rate = audio
        length = waveform.shape[1]
        max_length = sample_rate * seconds

        if length > max_length:
            trim_start = random.randint(0, length - max_length)
            trim_end = trim_start + max_length

            waveform = waveform[:, trim_start:trim_end]

        elif length < max_length:
            pad_start_lenght = (max_length - length) // 2
            pad_end_length = max_length - length - pad_start_lenght

            pad_start = torch.zeros((1, pad_start_lenght))
            pad_end = torch.zeros((1, pad_end_length))

            waveform = torch.cat((pad_start, waveform, pad_end), 1)

        return waveform, sample_rate

    @staticmethod
    def high_pass(audio, f_min=1400):
        waveform, sample_rate = audio

        waveform = torchaudio.functional.highpass_biquad(
            waveform, sample_rate, f_min)

        return waveform, sample_rate

    @staticmethod
    def preprocess(file):
        audio = AudioUtils.read(file)
        audio = AudioUtils.rechannel(audio)
        audio = AudioUtils.resample(audio)
        audio = AudioUtils.resize(audio)
        audio = AudioUtils.high_pass(audio)
        return audio

    @staticmethod
    def get_spectrogram(file, n_mels=128, n_fft=1024, hop_len=1024, top_db=80):
        waveform, sample_rate = AudioUtils.preprocess(file)
        spec = torchaudio.transforms.MelSpectrogram(
            sample_rate, n_mels=n_mels, n_fft=n_fft, hop_length=hop_len)(waveform)
        spec = torchaudio.transforms.AmplitudeToDB(top_db=top_db)(spec)

        return spec
