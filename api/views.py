# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from stories.models import StrArticle, StrUser

def api_index(request):
	return render(request, 'api/index.html')

def render_json(data):
	return JsonResponse(data, json_dumps_params={'indent': 2})

def stories(request):

	# Обработка параметров фильтрации
	
	# период дат
	date_from = request.GET.get('date_from', None)
	date_to = request.GET.get('date_to', None)

	# автор
	author_first_name = request.GET.get('author_first_name', None)
	author_last_name = request.GET.get('author_last_name', None)

	# набор тегов
	# (пока не ясно с ними)

	# ---

	param_filters = dict()

	if author_first_name and author_last_name:
		# ищем пользователей с таким именем в системе
		users = StrUser.objects.filter(first=author_first_name, last=author_last_name).all()
		user_ids = [u.id for u in users]

		param_filters['user__in'] = user_ids

	# фильтруем по дате
	if date_from or date_to:
		if date_from:
			param_filters['date__gte'] = date_from

		if date_to:
			param_filters['date__lte'] = date_to

	# получаем к-во объектов и сами объекты по заданным параметрам
	count = StrArticle.objects.filter(**param_filters).count()
	items = StrArticle.objects.filter(**param_filters).all()

	# ---

	data = {}
	data['count'] = count
	data['items'] = []

	for story in items:
		created_by = StrUser.objects.get(id=story.user)

		item = {
			'id': story.id,
			'name': story.name,
			'text': story.text,
			'created_at': story.date,
			'user': {
				'id': created_by.id,
				'first_name': created_by.first,
				'last_name': created_by.last,
			}
		}
		data['items'].append(item)
	
	return render_json(data)
