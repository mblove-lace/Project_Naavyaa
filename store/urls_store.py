from store.views import index
from store import views
app_name = 'store'
urlpatterns = [
    path("", views.index, name='index'),
]
