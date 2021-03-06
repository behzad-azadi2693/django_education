from django.urls import path
from django.urls.conf import include
from .cart import send_request, verify
from .sitemaps import CourseSitemap, BookSitemap
from django.contrib.sitemaps.views import sitemap
from .views import (
    index, contact,book_single, cartview,
    courses, course_single, book_store,cart, 
    teachercourse, newsletters,tag_search,
    search,panel,myorder,send_email,create_book,
    create_category,create_course,create_coursevideo,
    edit_course,edit_coursevideo,edit_book,
    delete_course,delete_coursevideo,delete_book,
)


app_name = 'education'


sitemaps = {
    'movie':CourseSitemap,
    'serial':BookSitemap,
}


create_urlpatterns = [
    path('category/',create_category, name='create_category'),
    path('coursevideo/<int:pk>/',create_coursevideo, name='create_coursevideo'),
    path('course/',create_course, name='create_course'),
    path('book/',create_book, name='create_book'),
]
edit_urlpatterns = [
    path('coursevideo/<int:pk>/',edit_coursevideo, name='edit_coursevideo'),
    path('course/<int:pk>/',edit_course, name='edit_course'),
    path('book/<int:pk>/',edit_book, name='edit_book'),
]
delete_urlpatterns = [
    path('coursevideo/<int:pk>/',delete_coursevideo, name='delete_coursevideo'),
    path('course/<int:pk>/',delete_course, name='delete_course'),
    path('book/<int:pk>/',delete_book, name='delete_book'),
]
urlpatterns = [
    path('', index , name="index"),
    path('page-contact/', contact , name="contact"),
    
    path('search/', search ,name='search'),
    path('myorder/', myorder, name='myorder'),
    path('cartview/', cartview, name='cartview'),
    path('tagsearch/<str:name>/', tag_search, name='tag'),
    path('cart/<str:name>/<int:pk>/', cart , name='cart'), 
    path('send/request/', send_request , name='send_request'), 
    path('verify/<int:order_id>/', verify , name='verify'),
    path('contact/', contact, name='contact'),
    path('newsletters/', newsletters , name="newsletters"),
    path('send_email/', send_email , name="send_email"),
    path('teahercourse/<str:slug>/', teachercourse , name="teachercourse"),
    path('coursesingle/<str:slug>/', course_single , name="coursesingle"),
    path('coureses/', courses , name="coureses"),
    path('bookstore/', book_store , name="book_store"),
    path('book-single/<str:slug>/', book_single , name='book_single'),
    path('panel/', panel, name='panel'),
    path('create/', include(create_urlpatterns)),
    path('edit/', include(edit_urlpatterns)),
    path('delete/', include(delete_urlpatterns)),
    path('sitemap/', sitemap, {'sitemaps':sitemaps}, name="sitemap"),
]
