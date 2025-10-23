from k24005_audio import transcribe_audio
from k24007_save import save_text_new_file
from recorder import record_audio  

if __name__ == '__main__': 
    print("=== 作業者1: 録音を開始します ===")
    audio_filepath = record_audio(duration=10)  # 10秒間録音
    result = transcribe_audio(audio_filepath)
    if result:
        save_text_new_file(result, basename="output_text")
        print("\n=== 文字起こし結果が保存されました ===")