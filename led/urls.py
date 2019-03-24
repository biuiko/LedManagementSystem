from django.urls import path
from . import views

app_name = 'led'

urlpatterns = [
	path('',views.index,name ='index'),
	path('<int:user_id>/choice/',views.choice_page,name='choice'),
	path('movie/',views.movie_show,name='movie'),
	path('check/',views.check,name ='check'),
	path('<int:user_id>/add_led/',views.add_led,name='add_led'),
	path('<int:user_id>/add_led_data/',views.add_led_data,name='add_led_data'),
	path('<int:user_id>/led_operation/',views.led_operation,name='led_operation'),
	path('<int:led_id>/<int:user_id>/led_update/',views.led_update,name='led_update'),
]