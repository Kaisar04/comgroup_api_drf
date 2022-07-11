# comgroup_api_drf

Запускаем проект по команде (python manage.py runserver)

Переходим http://127.0.0.1:8000/api/ (локалка)

Сначала запускаем api/seed.py для заполнения таблицы 

Далее...

Запросы:

		'List':'/api/emp-list/',
		'Detail View':'/api/emp-detail/<str:pk>/',
		'Create':'/api/emp-create/',
		'Update':'/api/emp-update/<str:pk>/',
		'Delete':'/api/emp-delete/<str:pk>/',
