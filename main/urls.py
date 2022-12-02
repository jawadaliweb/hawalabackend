from django.urls import path, include
from rest_framework_nested import routers
from accounts import views as accountView
from customer import views as customerView

router = routers.DefaultRouter()
router.register('customers', customerView.CustomerViewSet, basename='customers')
router.register('accounts', accountView.AccountViewSet, basename='accounts')
router.register('transaction', accountView.TransactionViewSet,basename='transaction')

# items_routers = routers.NestedDefaultRouter(router, 'customer', lookup='customer')
# items_routers.register('items',views.customer_list, basename='order-items')


urlpatterns = [
    path('', include(router.urls)),
    # path('', include(items_routers.urls)),
]
