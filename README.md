# comgroup_api_drf

Тестовое задание (КоммерцGroup)

Запускаем проект по команде (python manage.py runserver)

Переходим http://127.0.0.1:8000/api/ (локалка)

Сначала запускаем api/seed.py для заполнение таблицы в postgresql (в моем случае, я развернул локальную базу)

Далее...

Запросы:

		'List':'/api/emp-list/',
		'Detail View':'/api/emp-detail/<str:pk>/',
		'Create':'/api/emp-create/',
		'Update':'/api/emp-update/<str:pk>/',
		'Delete':'/api/emp-delete/<str:pk>/',
