
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/auth/', include('users.urls')),
#     path('api/', include('products.urls')),
#     path('api/', include('orders.urls')),
#     path('api/payments/', include('payments.urls')),
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








# ecommerce_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request):
    return Response({
        'message': 'Ecommerce API is running successfully! 🚀',
        'endpoints': {
            'admin': '/admin/',
            'auth_register': '/api/auth/register/',
            'auth_login': '/api/auth/login/',
            'products': '/api/products/',
            'categories': '/api/categories/',
            'orders': '/api/orders/',
            'cart': '/api/cart/',
            'payments': '/api/payments/'
        },
        'status': 'active'
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/', include('products.urls')),
    path('api/', include('orders.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/', api_root, name='api-root'),  # Add this line for /api/
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)