import pyttsx3
import sys

def text_to_speech(file_path, output_file):
    # テキストファイルからテキストを読み込む
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # pyttsx3エンジンの初期化
    engine = pyttsx3.init()

    # 日本語対応のための設定（システムによって異なる場合がある）
    voices = engine.getProperty('voices')
    for voice in voices:
        print(voice)
        if 'japanese' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    # テキストを音声に変換し、ファイルに保存
    engine.setProperty('pitch', 80)
    engine.setProperty('rate', 170) #速度を150に設定
    engine.save_to_file(text, output_file)

    # 変換の完了を待つ
    engine.runAndWait()

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file_path> <output_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    output_file = sys.argv[2]

    text_to_speech(file_path, output_file)

if __name__ == "__main__":
    main()
