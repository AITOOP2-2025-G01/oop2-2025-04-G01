"""
Audio Recorder Module
---------------------

This module provides a reusable function for recording audio from the microphone.

Usage Example:
    from audio_recorder.recorder import record_audio

    file_path = record_audio(duration=10)
    print("Recorded file stored at:", file_path)
"""

import ffmpeg
import datetime
import os


def record_audio(duration: int = 10,
                 output_dir: str = "recordings",
                 device: str = ":0",
                 input_format: str = "avfoundation") -> str:
    """
    Record audio from the system microphone for a specified duration.

    Parameters
    ----------
    duration : int, optional
        Recording duration in seconds. Default is 10.
    output_dir : str, optional
        Directory where the audio file will be saved. Default is 'recordings'.
    device : str, optional
        Name of input audio device. Default works for macOS example (":0").
    input_format : str, optional
        FFmpeg input format. Example:
            macOS: "avfoundation"
            Windows: "dshow"
            Linux : "alsa"

    Returns
    -------
    str
        The filepath of the saved audio file.

    Raises
    ------
    ffmpeg.Error
        If ffmpeg fails to record audio.
    """

    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_dir, f"recording_{timestamp}.wav")

    try:
        (
            ffmpeg
            .input(device, format=input_format, t=duration)
            .output(output_path, acodec="pcm_s16le", ar="44100", ac=1)
            .run(overwrite_output=True)
        )
        print(f"✅ Recording completed. Saved to: {output_path}")
        return output_path

    except ffmpeg.Error as e:
        print(f"❌ FFmpeg Error: {e.stderr.decode()}")
        raise
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        raise