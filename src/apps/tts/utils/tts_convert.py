import base64
import hashlib
import json
import time

import requests

from apps.audio_editor.utils.bound import combined_audio
from apps.tts.models import TTSProviderModel


class TTSConvert:
    AUE = "raw"

    def __init__(self):
        self.tts_provider = TTSProviderModel.objects.first()
        if not self.tts_provider:
            raise RuntimeError("需要配置一个语音合成提供商, 暂且只支持讯飞")

    def get_header(self):
        curTime = str(int(time.time()))
        # ttp=ssml
        param = {
            "aue": self.AUE,
            "auf": "audio/L16;rate=16000",
            # "voice_name": "x_xiaofeng",
            "voice_name": "x_mengmengneutral",
            "engine_type": "intp65",
            "speed": "45",
        }
        param = json.dumps(param)

        param_base64 = str(base64.b64encode(param.encode('utf-8')), 'utf-8')

        m2 = hashlib.md5()
        m2.update((self.tts_provider.app_key + curTime + param_base64).encode('utf-8'))

        check_sum = m2.hexdigest()

        header = {
            'X-CurTime': curTime,
            'X-Param': param_base64,
            'X-Appid': self.tts_provider.app_id,
            'X-CheckSum': check_sum,
            'X-Real-Ip': '127.0.0.1',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        }
        print(header)
        return header

    def get_body(self, text):
        data = {'text': text}
        return data

    def write_file(self, file, content):
        with open(file, 'wb') as f:
            f.write(content)
        f.close()

    def convert(self, text, poem_id):
        #  待合成文本内容
        r = requests.post(self.tts_provider.api_url, headers=self.get_header(), data=self.get_body(text))

        contentType = r.headers['Content-Type']
        if contentType == "audio/mpeg":
            sid = r.headers['sid']
            if self.AUE == "raw":
                # print(r.content)
                #   合成音频格式为pcm、wav并保存在audio目录下
                tts_path = "audio/" + sid + ".wav"
                self.write_file(tts_path, r.content)
                audio_path = combined_audio(tts_path, "audio/bgm1.mp3", poem_id)
                return audio_path
            else:
                # print(r.content)
                #   合成音频格式为mp3并保存在audio目录下
                self.write_file("audio/" + "xiaoyan" + ".mp3", r.content)
            # print("success, sid = " + sid)
        else:
            #   错误码链接：https://www.xfyun.cn/document/error-code （code返回错误码时必看）
            print(r.text)



