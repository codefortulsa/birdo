from rest_framework.pagination import LimitOffsetPagination


class BirdoPagination(LimitOffsetPagination):
    default_limit = 50
    max_limit = 100
