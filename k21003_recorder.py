# k21003_recorder.py
import ffmpeg
import time

# === 設定値 ===
# 録音する時間（秒）
duration = 10

# 出力する音声ファイル名（WAV形式）
output_file = 'python-audio-output.wav'

try:
    print(f"{duration}秒間、マイクからの録音を開始します...")

    # FFmpeg を使用して録音処理を実行する
    # FFmpegの主な指定項目：
    #   format：入力デバイスの種類（OSにより異なる）
    #       - Windows: 'dshow' または 'gdigrab'
    #       - macOS  : 'avfoundation'
    #       - Linux  : 'alsa'
    #   device（第1引数）: 使用するマイクデバイス名
    #       - macOS の例 → ':0'（デフォルトマイク）
    #
    # 出力設定：
    #   acodec='pcm_s16le' → WAV標準の16bit PCM形式で保存
    #   ar='44100' → サンプリングレート 44.1kHz（CD品質）
    #   ac=1 → モノラル録音（1チャンネル）
    (
        ffmpeg
        .input(':0', format='avfoundation', t=duration)  # macOS用設定例として記載
        .output(output_file, acodec='pcm_s16le', ar='44100', ac=1)
        .run(overwrite_output=True)  # 同名ファイルがあれば上書き保存
        #a
    )

    print(f"録音が完了しました。{output_file}に保存されました。")

except ffmpeg.Error as e:
    # FFmpeg 固有のエラー（録音失敗やデバイス認識不可など）
    print(f"エラーが発生しました: {e.stderr.decode()}")

except Exception as e:
    # 想定外のエラー（Python側の例外など）
    print(f"予期せぬエラー: {e}")