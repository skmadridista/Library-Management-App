from django.urls import path
from . import views
# from git_django_exam.settings import DEBUG, STATIC_URL, STATICFILES_DIRS
from django.conf.urls.static import static

urlpatterns = [
    path('booklist/', views.booklist, name = 'booklist'),
    path('upload/', views.upload, name = 'upload-book'),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book)
    
]

#DataFlair
# if DEBUG:
#     urlpatterns += static(STATIC_URL, document_root = STATICFILES_DIRS)
