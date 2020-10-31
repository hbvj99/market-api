"""
v1 API url
"""

from django.urls import include, path

urlpatterns = [
    path('auth/', include('market.authentications.api.v1.urls')),
    path('users/', include('market.users.api.v1.urls')),
    path('products/', include('market.products.api.v1.urls'))
]
