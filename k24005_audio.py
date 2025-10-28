# -*- coding: utf-8 -*-
"""
音声ファイルを受け取り、文字起こしを実行するモジュール (作業者2担当)

依存関係:
    - SpeechRecognition: 音声認識ライブラリ
      (pip install SpeechRecognition)
    - pydub: .wav以外の形式を扱う場合や、処理の補助に必要になることがあります
      (pip install pydub)
    - Google Web Speech API を使用するため、インターネット接続が必要です。
"""
import speech_recognition as sr
import os
import time

def transcribe_audio_file(audio_filepath: str) -> str:
    """
    指定されたファイルパスの音声ファイル（WAV形式を想定）を文字起こしします。

    **グループとの取り決め事項:**
    1.  **入力形式:** ファイルパス（文字列）を受け取ります。
    2.  **出力形式:** 文字起こし結果の文字列を返します。
    3.  **音声ファイル名:** 作業者1のプログラムで生成される 'python-audio-output.wav' を想定しています。
    4.  **依存ライブラリ:** SpeechRecognition を使用します。

    Args:
        audio_filepath (str): 文字起こしを行う音声ファイル（例: 'python-audio-output.wav'）のパス。

    Returns:
        str: 文字起こしされたテキスト。認識できなかった場合は空文字列を返します。
    """
    # 認識器 (Recognizer) インスタンスの作成
    recognizer = sr.Recognizer()

    # ファイルの存在確認
    if not os.path.exists(audio_filepath):
        print(f"エラー: 指定された音声ファイルが見つかりません: {audio_filepath}")
        return ""

    # 音声ファイルを読み込み
    try:
        # AudioFileオブジェクトとして音声ファイルをオープン
        with sr.AudioFile(audio_filepath) as source:
            print(f"音声ファイル '{audio_filepath}' を読み込み中...")
            # recognizer.record() や recognizer.listen() とは異なり、
            # ファイル全体をメモリにロードします。
            audio_data = recognizer.record(source) 
            print("音声データの読み込み完了。認識処理を開始します...")

    except Exception as e:
        print(f"音声ファイルの読み込み中にエラーが発生しました: {e}")
        return ""

    # Google Web Speech API を使用して文字起こしを実行
    try:
        # 日本語 (ja-JP) を指定して認識
        # 古いバージョンでエラーになる 'timeout' 引数を削除しました。
        start_time = time.time()
        text = recognizer.recognize_google(audio_data, language="ja-JP")
        end_time = time.time()
        print(f"認識処理完了 (所要時間: {end_time - start_time:.2f}秒)")
        return text

    except sr.UnknownValueError:
        print("Google Web Speech API は音声を理解できませんでした。ノイズが多い可能性があります。")
        return ""
    except sr.RequestError as e:
        # APIキーがない、ネットワークエラー、クォータ超過など
        print(f"Google Web Speech API へのリクエストに失敗しました; {e}")
        return ""
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")
        return ""


if __name__ == '__main__':
    # --- 動作確認用のサンプルコード ---
    # 作業者1のプログラムの出力ファイル名に合わせて変更します
    TEST_FILE = "python-audio-output.wav"

    print(f"--- 動作確認開始 (この処理では、'{TEST_FILE}' が存在することを前提とします) ---")
    
    # ここに、仮の 'python-audio-output.wav' ファイルを作成する処理があるべきです。
    
    # ファイルが存在しない場合のテスト
    transcribed_result = transcribe_audio_file(TEST_FILE)
    print("\n[テスト結果 (ファイル非存在)]")
    print(f"文字起こし結果: '{transcribed_result}'")

    # 実際には、WAVファイルを配置し、再テストしてください。
    
    print("\n--- 動作確認終了 ---")
