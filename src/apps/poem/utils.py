import json
import os

from apps.poem.models import AuthorModel, PoemModel


def read_author_2_db(path, dynasty):
    with open(path) as author:
        author = author.read()
        author = json.loads(author)
        for each in author:
            author_obj = AuthorModel()
            author_obj.dynasty = dynasty
            author_obj.name = each.get("name")
            author_obj.desc = each.get("desc")
            author_obj.save()


def read_poem_2_db(path):
    files = os.listdir(path)
    for file in files:
        if not file.startswith("poet"):
            continue

        dynasty = ""

        if "song" in file:
            dynasty = "宋"
        elif "tang" in file:
            dynasty = "唐"
        else:
            pass

        with open(os.path.join(path, file)) as poem:
            poem = poem.read()
            poem = json.loads(poem)
            for each in poem:
                poem_obj = PoemModel()
                poem_obj.title = each.get("title")
                author = each.get("author")
                author_obj = AuthorModel.objects.filter(name=author, dynasty=dynasty)
                if author_obj:
                    author_obj = author_obj.first()
                    poem_obj.author = author_obj
                poem_obj.paragraphs = "\n".join(each.get("paragraphs"))
                poem_obj.strains = "\n".join(each.get("strains"))
                poem_obj.dynasty = dynasty
                poem_obj.save()


if __name__ == '__main__':
    read_author_2_db("/home/loopsun/code/Python/chinese-poetry-master/json/authors.tang.json", "唐代")

