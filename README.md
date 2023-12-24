# TextToVoice

TextToVoiceは、テキストを音声に変換し、必要に応じてその音声の速度を調整することができるPythonスクリプトのコレクションです。また、音声ファイルと静止画像から動画を生成する機能も提供します。

## 機能

- `ttsx3.py`: `pyttsx3` ライブラリを使用してテキストファイルを音声に変換します。日本語対応の音声エンジンを使用し、音声のピッチと速度を調整することができます。

- `gtts_speed.py`: Google Text-to-Speech (gTTS) ライブラリを使用してテキストを音声に変換し、`pydub` ライブラリでその速度を調整します。

- `a2m.py`: `moviepy` ライブラリを使用して音声ファイルと静止画像から動画を生成します。音声ファイルの全長に基づいて動画の長さを設定し、指定された出力パスに動画を保存します。
`moviepy`は様々な外部ツールを使うため、ローカル環境でのセットアップが面倒です。そんなときはGoogle Colabを使うとよいでしょう。


## 使い方

### ttsx3.py

```bash
python ttsx3.py <input_text_file_path> <output_audio_file_path>
```

### gtts_speed.py

```bash
python gtts_speed.py <input_text_file_path> [speed]
```

### a2m.py

```bash
python a2m.py <audio_file_path> <image_file_path>
```

## ライセンス

このプロジェクトは [MITライセンス](LICENSE) の下で提供されています。

