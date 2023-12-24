from moviepy.editor import AudioFileClip, ImageClip

def create_video(audio_path, image_path, duration, output_path):
    # 音声ファイルの読み込み
    audio_clip = AudioFileClip(audio_path)

    # 静止画像の読み込みと音声の長さに合わせる
    image_clip = ImageClip(image_path, duration=duration)

    # 静止画像に音声をセット
    video = image_clip.set_audio(audio_clip)

    # ビデオファイルを出力
    video.write_videofile(output_path, fps=24)

# 使用例
audio_path = 'vvox_makura.wav'  # 音声ファイルのパス
image_path = 'image03.png'  # 静止画像ファイルのパス
duration = 10  # 静止画像の表示時間（秒）
output_path = 'vvox_makura.mp4'  # 出力する動画ファイルのパス

create_video(audio_path, image_path, duration, output_path)
