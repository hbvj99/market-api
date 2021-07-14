from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ListRetrieveUpdateViewSetMixin(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    pass


class ListRetrieveViewSetMixin(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    pass


class RetrieveUpdateViewSetMixin(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    pass


class ListCreateViewSetMixin(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    pass


class ListViewSetMixin(
    mixins.ListModelMixin,
    GenericViewSet
):
    pass


class ListCreateRetrieveDestroyViewSetMixin(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    pass
