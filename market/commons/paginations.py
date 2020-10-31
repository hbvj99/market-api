from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    def get_page_size(self, request):
        page_size = 10
        if request.query_params and request.query_params.get('page_size'):
            page_size = request.query_params.get('page_size')

        return page_size
