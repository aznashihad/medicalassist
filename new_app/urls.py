from django.urls import path

from new_app import views

urlpatterns=[
    path('home',views.home,name='home'),
    path('index2', views.index2, name='index2'),
    path('adminbase', views.adminbase, name='adminbase'),
    path('customerbase', views.customerbase, name='customerbase'),
    path('organisationbase', views.organisationbase, name='organisationbase'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('Registration_user', views.Registration_user, name='Registration_user'),
    path('customer_add', views.customer_add, name='customer_add'),
    path('company_add', views.company_add, name='company_add'),
    path('login_view', views.login_view, name='login_view'),
    path('customer_view', views.customer_view, name='customer_view'),
    path('customer_delete/<int:id>/', views.customer_delete, name='customer_delete'),
    path('company_view', views.company_view, name='company_view'),
    path('company_delete/<int:id>/', views.company_delete, name='company_delete'),
    path('donation_view', views.donation_view, name='donation_view'),
    path('donation_success', views.donation_success, name='donation_success'),
    path('company_approve/<int:id>/', views.company_approve_donation, name='company_approve'),
    path('admin_approve/<int:id>/', views.admin_approve_donation, name='admin_approve'),
    path('company_view_all_requests/', views.company_view_all_requests, name='company_view_all_requests'),
    path('admin_view_all_requests/', views.admin_view_all_requests, name='admin_view_all_requests'),

    # path('company_donation_list', views.company_donation_list, name='company_donation_list'),
    path('approved_donations/', views.approved_donations, name='approved_donations'),
    path('rejected_donations/', views.rejected_donations, name='rejected_donations'),
    path('customer_notifications', views.customer_notifications, name='customer_notifications'),
    path('view_notifications', views.view_notifications, name='view_notifications'),
    # path('create_feedback', views.create_feedback, name='create_feedback'),
    path('feedback', views.feedback, name='feedback'),
    path('feedback_view', views.feedback_view, name='feedback_view'),
    path('feedback_delete/<int:id>/', views.feedback_delete, name='feedback_delete'),
    path('admin_feedback_view', views.admin_feedback_view, name='admin_feedback_view'),
    path('update/<int:id>/', views.replay_to_feedback, name='update'),





]