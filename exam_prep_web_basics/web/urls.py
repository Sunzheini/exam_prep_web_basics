"""
•	http://localhost:8000/ - home page
•	http://localhost:8000/album/add/ - add album page
•	http://localhost:8000/album/details/<id>/ - album details page
•	http://localhost:8000/album/edit/<id>/ - edit album page
•	http://localhost:8000/album/delete/<id>/ - delete album page
•	http://localhost:8000/profile/details/ - profile details page
•	http://localhost:8000/profile/delete/ - delete profile page

"""
from django.urls import path, include

from exam_prep_web_basics.web.views import index, add_album, details_album, edit_album, delete_album, details_profile, \
    delete_profile, add_profile

urlpatterns = (
    # http://localhost:8000/
    path('', index, name='index'),

    path('album/', include([
        # http://localhost:8000/album/add/
        path('add/', add_album, name='add album'),
        # http://localhost:8000/album/details/<id>/
        path('details/<int:pk>/', details_album, name='details album'),
        # http://localhost:8000/album/edit/<id>/
        path('edit/<int:pk>/', edit_album, name='edit album'),
        # http://localhost:8000/album/delete/<id>/
        path('delete/<int:pk>/', delete_album, name='delete album'),
    ])),

    path('profile/', include([
        path('add/', add_profile, name='add profile'),
        # http://localhost:8000/profile/details/
        path('details/', details_profile, name='details profile'),
        # http://localhost:8000/profile/delete/
        path('delete/', delete_profile, name='delete profile'),
    ])),
)
