import random

from django.db.models import Max
from django.forms import model_to_dict
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
        return Response(poem_dict)

    def get_random_poem(self):
        max_id = PoemModel.objects.all().aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = random.randint(1, max_id)
            poem = PoemModel.objects.filter(pk=pk).first()
            if poem:
                return poem


class PoemAudioView(APIView):

    def get(self, request, format=None):
        poem = self.get_random_poem()

        tc = TTSConvert()
        if not poem.audio:
            audio_path = tc.convert(poem.paragraphs, poem.id)
            poem.audio.name = audio_path
            poem.save()

        poem_dict = model_to_dict(poem, exclude=["audio"])
        return Response(poem_dict)
