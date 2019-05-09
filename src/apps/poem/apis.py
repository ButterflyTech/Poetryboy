import os
import random

from django.db.models import Max
from django.forms import model_to_dict
from django.http import HttpResponse, StreamingHttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.poem.models import PoemModel
from apps.tts.utils.tts_convert import TTSConvert


class RandomPoemView(APIView):

    def get(self, request, format=None):
        poem = self.get_random_poem()

        tc = TTSConvert()
        if not poem.audio:
            audio_path = tc.convert(poem.paragraphs, poem.id)
            poem.audio.name = audio_path
            poem.save()

        poem_dict = model_to_dict(poem, exclude=["audio"])
        poem_dict["author"] = poem.author.name
        return Response(poem_dict)

    def get_random_poem(self):
        max_id = PoemModel.objects.all().aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = random.randint(1, max_id)
            poem = PoemModel.objects.filter(pk=pk).first()
            if poem:
                return poem


class PoemAudioView(APIView):

    def get(self, *args, **kwargs):

        id = kwargs.get("id")

        poem = PoemModel.objects.filter(pk=id).first()

        def file_iterator(file_name, chunk_size=512):
            with open(file_name, 'rb') as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break

        file_name = poem.audio.path
        response = StreamingHttpResponse(file_iterator(file_name))
        response['Content-Type'] = 'audio/mp3'
        response['Content-Disposition'] = "attachment; filename=%s" % \
                                          (poem.audio.name.replace(' ', '-'),)
        response['Content-Length'] = os.path.getsize(file_name)
        return response

