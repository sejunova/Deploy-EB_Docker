from rest_framework.pagination import PageNumberPagination


class PostListResultPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page_size'
