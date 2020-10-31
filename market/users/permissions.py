from rest_framework.permissions import BasePermission

from market.products.models import Product


class IsAdminPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff


class IsProductOwnerPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Product):
            return obj.user == request.user


class IsUserOwnerPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class IsAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class IsAuthenticatedOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
