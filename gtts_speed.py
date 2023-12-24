from gtts import gTTS
from pydub import AudioSegment
import sys
import os

def text_to_speech(text, language, filename):
    text2speech = gTTS(text, lang=language)
    text2speech.save(filename)
    return filename

def change_speed(file_path, output_path, speed=1.2):
    audio = AudioSegment.from_file(file_path)
    new_audio = audio.speedup(playback_speed=speed)
    new_audio.export(output_path, format="mp3")
    return output_path

def main(file_path, speed=1.2):
    # ファイルからテキストを読み込む
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # 対応言語
    language = "ja"

    # 一時オーディオファイルのパスを生成
    temp_audio_file = os.path.splitext(file_path)[0] + "_temp.mp3"

    # 最終的な出力ファイルのパスを生成
    output_file = os.path.splitext(file_path)[0] + ".mp3"

    # 音声に変換
    text_to_speech(text, language, temp_audio_file)

    # 速度調整して最終ファイルを保存
    change_speed(temp_audio_file, output_file, speed)

    # 一時ファイルを削除
    os.remove(temp_audio_file)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python gtts_speed.py <input_text_file> [speed]")
        sys.exit(1)

    input_text_file = sys.argv[1]
    speed = float(sys.argv[2]) if len(sys.argv) > 2 else 1.2

    main(input_text_file, speed)
