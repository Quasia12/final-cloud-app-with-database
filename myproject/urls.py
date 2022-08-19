from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('onlinecourse/', include('onlinecourse.urls')),
    path('<int:course_id>/submit/', views.submit, name="submit"),
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name="exam_result"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
