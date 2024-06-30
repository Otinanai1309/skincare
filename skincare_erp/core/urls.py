from django.urls import path
from .views import (
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView,
    BudgetListView, BudgetDetailView, BudgetCreateView, BudgetUpdateView, BudgetDeleteView,
    TransactionListView, TransactionDetailView, TransactionCreateView, TransactionUpdateView, TransactionDeleteView,
    CashFlowListView, CashFlowDetailView, CashFlowCreateView, CashFlowUpdateView, CashFlowDeleteView,
    SupplierListView, SupplierDetailView, SupplierCreateView, SupplierUpdateView, SupplierDeleteView,
    PurchaseOrderListView, PurchaseOrderDetailView, PurchaseOrderCreateView, PurchaseOrderUpdateView, PurchaseOrderDeleteView,
    InventoryForecastListView, InventoryForecastDetailView, InventoryForecastCreateView, InventoryForecastUpdateView, InventoryForecastDeleteView,
    home
)

urlpatterns = [
    path('', home, name='home'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/new/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/new/', OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('orders/<int:pk>/edit/', OrderUpdateView.as_view(), name='order_update'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),

    path('budgets/', BudgetListView.as_view(), name='budget_list'),
    path('budgets/new/', BudgetCreateView.as_view(), name='budget_create'),
    path('budgets/<int:pk>/', BudgetDetailView.as_view(), name='budget_detail'),
    path('budgets/<int:pk>/edit/', BudgetUpdateView.as_view(), name='budget_update'),
    path('budgets/<int:pk>/delete/', BudgetDeleteView.as_view(), name='budget_delete'),

    path('transactions/', TransactionListView.as_view(), name='transaction_list'),
    path('transactions/new/', TransactionCreateView.as_view(), name='transaction_create'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction_detail'),
    path('transactions/<int:pk>/edit/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('transactions/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),

    path('cashflows/', CashFlowListView.as_view(), name='cashflow_list'),
    path('cashflows/new/', CashFlowCreateView.as_view(), name='cashflow_create'),
    path('cashflows/<int:pk>/', CashFlowDetailView.as_view(), name='cashflow_detail'),
    path('cashflows/<int:pk>/edit/', CashFlowUpdateView.as_view(), name='cashflow_update'),
    path('cashflows/<int:pk>/delete/', CashFlowDeleteView.as_view(), name='cashflow_delete'),
 
    # Supplier URLs
    path('suppliers/', SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/new/', SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('suppliers/<int:pk>/edit/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),

    # PurchaseOrder URLs
    path('purchaseorders/', PurchaseOrderListView.as_view(), name='purchaseorder_list'),
    path('purchaseorders/new/', PurchaseOrderCreateView.as_view(), name='purchaseorder_create'),
    path('purchaseorders/<int:pk>/', PurchaseOrderDetailView.as_view(), name='purchaseorder_detail'),
    path('purchaseorders/<int:pk>/edit/', PurchaseOrderUpdateView.as_view(), name='purchaseorder_update'),
    path('purchaseorders/<int:pk>/delete/', PurchaseOrderDeleteView.as_view(), name='purchaseorder_delete'),

    # InventoryForecast URLs
    path('inventoryforecasts/', InventoryForecastListView.as_view(), name='inventoryforecast_list'),
    path('inventoryforecasts/new/', InventoryForecastCreateView.as_view(), name='inventoryforecast_create'),
    path('inventoryforecasts/<int:pk>/', InventoryForecastDetailView.as_view(), name='inventoryforecast_detail'),
    path('inventoryforecasts/<int:pk>/edit/', InventoryForecastUpdateView.as_view(), name='inventoryforecast_update'),
    path('inventoryforecasts/<int:pk>/delete/', InventoryForecastDeleteView.as_view(), name='inventoryforecast_delete'),
]
