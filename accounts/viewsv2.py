from .serializers import AccountSerializer
from .models import Account


from utils.generic_sets_views import (
    ListCreateGenericView,
    RetrieveUpdateDestroyGenericView,
)


# MRO - Method Resolution Order
class AccountView(ListCreateGenericView):
    view_queryset = Account.objects.all()
    view_serializer = AccountSerializer


class AccountDetailView(RetrieveUpdateDestroyGenericView):
    view_queryset = Account.objects.all()
    view_serializer = AccountSerializer
    url_params_name = "account_id"
