# posts/serializers.py
from rest_framework import serializers
from anime.models import Anime
from manga.models import Title,Manga,Author,Publisher,Demographic,MangaType,Genre

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ['original_name', 'english_name', 'russian_name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name','surname','photo']



class DemographicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demographic
        fields = ['name']


class MangaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangaType
        fields = ['name']
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class MangaSerializer(serializers.ModelSerializer):
    author=AuthorSerializer()
    publisher=serializers.StringRelatedField(many=True)
    genres=serializers.StringRelatedField(many=True)
    themes=serializers.StringRelatedField(many=True)
    magazine=serializers.StringRelatedField(many=True)
    demographic=serializers.StringRelatedField()
    type=serializers.StringRelatedField()
    title  = TitleSerializer()
    class Meta:
        model = Manga
        fields = ['id','title','type','author','publisher','premiere','volumes','chapters','genres','demographic','themes','image','magazine','description']
    
 


class AnimeSerializer(serializers.ModelSerializer):
    title  = TitleSerializer()
    source=MangaSerializer()
    author=AuthorSerializer()
    genres=serializers.StringRelatedField(many=True)
    themes=serializers.StringRelatedField(many=True)
    type=serializers.StringRelatedField()
    studio=serializers.StringRelatedField(many=True)

    class Meta:
        model = Anime
        fields = ('id','title','source','type', 'author', 'studio','premiere','episodes','genres','themes','image','description',)


