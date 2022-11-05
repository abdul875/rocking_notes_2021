from django.urls import path
from practiceapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup', views.UserSignUp),
    path('signin', views.UserSignIn),
    path('create_note', views.CreateNote),
    path('fetch_note', views.FetchNote),
    path('update_note', views.UpdateNote),
    path('delete_note', views.DeleteNote),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
