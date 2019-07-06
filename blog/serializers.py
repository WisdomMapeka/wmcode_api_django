from rest_framework import serializers
from blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'pub_date', 'sub_heading_1', 
        	'body_one', 'code_one')

# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=200)
#     body_one = serializers.CharField(style={'base_template': 'textarea.html'})

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.body_one = validated_data.get('body_one', instance.body_one)
#         instance.save()
#         return instance



 #         title = models.CharField(max_length=200, blank=True, null=True)
	# author = models.ForeignKey('Author', max_length=200, blank=True, null=True, on_delete=models.CASCADE)
	# pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	# sub_heading_1 = models.CharField(max_length=200, blank=True, null=True)
	# body_one = models.TextField(blank=True, null=True)
	# img_one = models.FileField(upload_to='uploads/', blank=True, null=True)
	# sub_heading_2 = models.CharField(max_length=200, blank=True, null=True)
	# code_one = models.TextField(blank=True, null=True)
	# body_two = models.TextField(blank=True, null=True)

	# sub_heading_3 = models.CharField(max_length=200, blank=True, null=True)
	# body_three = models.TextField(blank=True, null=True)
	# img_two = models.FileField(upload_to='uploads/', blank=True, null=True)
	# sub_heading_4 = models.CharField(max_length=200, blank=True, null=True)
	# code_two = models.TextField(blank=True, null=True)
	# body_four = models.TextField(blank=True, null=True)

	# sub_heading_5 = models.CharField(max_length=200, blank=True, null=True)
	# body_five = models.TextField(blank=True, null=True)
	# img_three = models.FileField(upload_to='uploads/', blank=True, null=True)
	# sub_heading_6 = models.CharField(max_length=200, blank=True, null=True)
	# code_three = models.TextField(blank=True, null=True)
	# body_six = models.TextField



