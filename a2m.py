from moviepy.editor import AudioFileClip, ImageClip
import sys
import os

def create_video(audio_path, image_path):
    # 音声ファイルの読み込み
    audio_clip = AudioFileClip(audio_path)

    # 音声ファイルの全長を取得
    duration = audio_clip.duration

    # 静止画像の読み込みと音声の長さに合わせる
    image_clip = ImageClip(image_path, duration=duration)

    # 出力動画ファイルのパスを生成
    output_path = os.path.splitext(audio_path)[0] + ".mp4"

    # 静止画像に音声をセット
    video = image_clip.set_audio(audio_clip)

    # ビデオファイルを出力
    video.write_videofile(output_path, fps=24)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python a2m.py <audio_file_path> <image_file_path>")
        sys.exit(1)

    audio_path = sys.argv[1]
    image_path = sys.argv[2]

    create_video(audio_path, image_path)

