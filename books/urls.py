
from django.urls import path
from books.views import get_uuids_a, get_uuids_b, get_argument_from_path, get_arguments_from_query, \
    check_http_query_type, get_headers, raise_error_for_fun, AuthorListBaseView, CategoryListBaseTemplateView, \
    BookListView, BookDetailsView, CategoryCreateFormView

urlpatterns = [
    path('uuids-a',get_uuids_a),
    path('uuids-b',get_uuids_b),
    path('path-args/<int:x>/<str:y>/<slug:z>',get_argument_from_path, name="get_from_path"),
    path('query-args',get_arguments_from_query, name="get_from_query"),
    path('query-type',check_http_query_type, name="check_query_type"),
    path('get-header',get_headers, name="get_headers"),
    path('raise-error',raise_error_for_fun, name="raise_error"),
    path('author-list',AuthorListBaseView.as_view(), name="author_list"),
    path('category-list',CategoryListBaseTemplateView.as_view(), name="category_list"),
    path('book-list',BookListView.as_view(), name="book_list"),
    path('book-detail/<int:pk>',BookDetailsView.as_view(), name="book_detail"),
    path('category-create',CategoryCreateFormView.as_view(), name="category_create")

]