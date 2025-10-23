import os
import time
from typing import Optional

# SpeechRecognitionライブラリを使用（要インストール: pip install SpeechRecognition）
# 依存ライブラリがない場合でも、モック機能によりプログラムは実行可能です。
try:
    import speech_recognition as sr
except ImportError:
    # ライブラリがない場合は、エラーメッセージを表示し、モックデータに戻します
    sr = None

def transcribe_audio(audio_filepath: str) -> Optional[str]:
    """
    指定された音声ファイルを文字起こしします。

    Args:
        audio_filepath: 文字起こしを行う音声ファイルのパス（例: 'temp/audio.wav'）。

    Returns:
        文字起こしされたテキスト (str)。処理に失敗した場合は None。
    """
    print("--- 作業者2: 音声ファイルの文字起こしを開始します ---")
    
    # 1. 事前確認: ファイルが存在しない場合は処理を中断
    if not audio_filepath or not os.path.exists(audio_filepath):
        print(f"エラー: 指定された音声ファイルが見つかりません: {audio_filepath}")
        return None

    # 2. 実際の文字起こし処理（SpeechRecognitionが利用可能な場合）
    if sr:
        r = sr.Recognizer()
        
        try:
            with sr.AudioFile(audio_filepath) as source:
                print("音声ファイルを読み込み中...")
                # ファイル全体を読み込みます
                audio = r.record(source) 
            
            print("Google Web Speech APIを使用して文字起こしを試行中...")
            # 日本語で認識を試みる
            text = r.recognize_google(audio, language='ja-JP')
            
            print("文字起こしが完了しました。")
            return text
            
        except sr.UnknownValueError:
            error_msg = "Google Web Speech APIが音声を理解できませんでした（音声認識失敗）。"
            print(f"警告: {error_msg}")
            return f"【音声認識失敗】{error_msg}"
        except sr.RequestError as e:
            error_msg = f"Google Web Speech APIへの接続に失敗しました（インターネット接続またはAPI制限）。エラー: {e}"
            print(f"警告: {error_msg}")
            return f"【接続エラー】{error_msg}"
        except Exception as e:
            error_msg = f"音声ファイルの処理中に予期せぬエラーが発生しました: {e}"
            print(f"致命的エラー: {error_msg}")
            return None
    
    else:
        # 3. SpeechRecognitionが利用できない場合のフォールバック（モックデータ）
        print("警告: SpeechRecognitionライブラリが見つかりません。モックデータを使用します。")
        time.sleep(2) # 処理時間のシミュレーション
        
        transcribed_text = (
            "【モックデータ】この度はグループワークにご協力いただきありがとうございます。\n"
            "これは10秒間の録音をシミュレーションした結果の文字起こしです。\n"
            "プログラム分散開発の練習を通じて、コミュニケーション能力を養いましょう。"
        )
        return transcribed_text

# main.pyから直接実行されることを想定し、他のファイルに影響しないようにする
if __name__ == '__main__':
    # テスト環境のセットアップ
    TEMP_DIR = "temp"
    if not os.path.exists(TEMP_DIR): os.makedirs(TEMP_DIR)
    
    # 作業者1と取り決めたファイル名 'audio.wav' を利用してテスト
    dummy_path = os.path.join(TEMP_DIR, "audio.wav") 
    
    # 実際の音声ファイルがない場合は、ダミーファイルを作成
    if not os.path.exists(dummy_path):
         with open(dummy_path, 'w') as f:
             f.write("dummy content")
         print(f"警告: 実際の音声ファイルがないため、ダミーファイル '{dummy_path}' を作成しました。")

    # 文字起こし実行
    result = transcribe_audio(dummy_path)
    
    # 結果表示
    if result:
        print("\n--- 文字起こし結果の確認 ---")
        print(result)
