# saver.py
import datetime

def save_text(filename, text_to_save):
    """
    指定されたファイルに、文字列を追記（上書きしない）します。

    Args:
        filename (str): 保存先のファイル名 (例: "transcript.txt")
        text_to_save (str): 保存する文字列
    """
    try:
        # 'a' (append) モードでファイルを開く
        # encoding='utf-8' は日本語の文字化けを防ぐため
        with open(filename, 'a', encoding='utf-8') as f:

            # 保存日時も一緒に追加する
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            f.write(f"[{timestamp}] {text_to_save}\n") # 改行も追加

        print(f"{filename} に追記しました。")
    except Exception as e:
        print(f"ファイル保存中にエラーが発生しました: {e}")