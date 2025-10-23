# k24007_save.py
import datetime

def save_text_new_file(text_to_save, basename="transcript"):
    """
    文字起こし結果を、タイムスタンプ付きの「新しい」ファイルに保存します。
    (例: transcript_20251023_152030.txt)

    Args:
        text_to_save (str): 保存する文字列
        basename (str): ファイル名の基礎 (例: "transcript")
    """
    if not text_to_save:
        print("保存するテキストが空です。スキップします。")
        return

    try:
        # タイムスタンプでユニークなファイル名を生成
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{basename}_{timestamp}.txt"
        
        # 'w' (write) モードで新しいファイルを作成
        # encoding='utf-8' は日本語の文字化けを防ぐため
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text_to_save + "\n") # 改行も追加
            
        print(f"'{filename}' に新しく保存しました。")
        
    except Exception as e:
        print(f"ファイル保存中にエラーが発生しました: {e}")