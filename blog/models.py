from django.db import models
# api imports


class Author(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.name


	class Meta:
		db_table = 'author'

class Article(models.Model):
	title = models.CharField(max_length=200, blank=True, null=True)
	author = models.ForeignKey('Author', max_length=200, blank=True, null=True, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	sub_heading_1 = models.CharField(max_length=200, blank=True, null=True)
	body_one = models.TextField(blank=True, null=True)
	img_one = models.FileField(upload_to='uploads/', blank=True, null=True)
	sub_heading_2 = models.CharField(max_length=200, blank=True, null=True)
	code_one = models.TextField(blank=True, null=True)
	body_two = models.TextField(blank=True, null=True)

	sub_heading_3 = models.CharField(max_length=200, blank=True, null=True)
	body_three = models.TextField(blank=True, null=True)
	img_two = models.FileField(upload_to='uploads/', blank=True, null=True)
	sub_heading_4 = models.CharField(max_length=200, blank=True, null=True)
	code_two = models.TextField(blank=True, null=True)
	body_four = models.TextField(blank=True, null=True)

	sub_heading_5 = models.CharField(max_length=200, blank=True, null=True)
	body_five = models.TextField(blank=True, null=True)
	img_three = models.FileField(upload_to='uploads/', blank=True, null=True)
	sub_heading_6 = models.CharField(max_length=200, blank=True, null=True)
	code_three = models.TextField(blank=True, null=True)
	body_six = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.title

	class Meta:
		db_table = 'article'

class Comments(models.Model):
	article =  models.ForeignKey('Article', on_delete=models.CASCADE, blank=True, null=True)
	comment_body = models.TextField(blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	comment_owner = models.ForeignKey('Comment_owner', on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.comment_body


	class Meta:
		db_table = 'comments'

class Comment_owner(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.name


	class Meta:
		db_table = 'comment_owner'
			

