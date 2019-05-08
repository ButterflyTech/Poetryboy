
from pydub import AudioSegment


def combined_audio(tts_path, bgm_path, filename):
    # 人声
    tts = AudioSegment.from_file(tts_path)

    # BGM
    bgm = AudioSegment.from_file(bgm_path)

    # 头尾添加３秒空白
    two_second_silence = AudioSegment.silent(duration=3000)

    tts = two_second_silence.append(tts)

    tts = tts.append(two_second_silence)

    # 减少BGM 振幅
    tts_dbfs = tts.dBFS

    bgm_dbfs = tts.dBFS

    dbfs_offset = tts_dbfs - bgm_dbfs

    if dbfs_offset < 0:
        bgm = bgm.apply_gain(-5.7 + dbfs_offset)

    # 合并人声与BGM
    combined = tts.overlay(bgm)

    # 添加首尾淡入淡出
    combined = combined.fade_in(3000).fade_out(3000)

    # 输出音频

    out_path = "media/{}.mp3".format(filename)

    combined.export(
        out_path,
        format='mp3',
        tags={
            'artist': 'Poetry Boy',
            'album': 'Best of 2019',
            'comments': 'This album is awesome!'
        }
    )

    return out_path


if __name__ == '__main__':
    combined_audio(
        "/home/loopsun/code/Python/Poetryboy/src/audio/hts00000107@dx17fe102e15956f2300.wav",
        "/home/loopsun/code/Python/Poetryboy/src/audio/bgm1.mp3")
