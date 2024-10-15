
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from new_app.forms import LoginRegister, CustomerRegister, CompanyRegister, CustomerDonationForm, FeedbackForm
from new_app.models import Company, Customer, Login, CustomerDonations, Notifications, Feedback


# Create your views here.
def home(request):
    return render(request,'home.html')
def index2(request):
    return render(request,'index2.html')
def adminbase(request):
    return render(request,'admin/adminbase.html')
def customerbase(request):
    return render(request,'customer/customerbase.html')
def organisationbase(request):
    return render(request,'company/organisationbase.html')
def userlogin(request):
    return render(request,'login.html')

#
def Registration_user(request):
    form=UserCreationForm()
    if request.method=='POST':
        form1=UserCreationForm(request.POST)
        if form1.is_valid():
            form1.save()
    return render(request,'reg.html',{'form':form})

def customer_add(request):
    form1=LoginRegister()
    form2=CustomerRegister()
    if request.method=='POST':
        form1=LoginRegister(request.POST)
        form2=CustomerRegister(request.POST)

        if form1.is_valid() and form2.is_valid():
            a=form1.save(commit=False)
            a.is_customer=True
            a.save()
            user1=form2.save(commit=False)
            user1.user=a
            user1.save()
            return redirect('customerbase')
    return render(request,'customer/customeradd.html',{'form1':form1,'form2':form2})

def company_add(request):
    form1=LoginRegister()
    form2=CompanyRegister()
    if request.method=='POST':
        form1=LoginRegister(request.POST)
        form2=CompanyRegister(request.POST)

        if form1.is_valid() and form2.is_valid():
            a=form1.save(commit=False)
            a.is_company=True
            a.save()
            user1=form2.save(commit=False)
            user1.user=a
            user1.save()
            return redirect('organisationbase')
    return render(request,'company/companyadd.html',{'form1':form1,'form2':form2})

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        print(password)
        print(username)
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:

            login(request,user)
            if user.is_staff:
                return redirect('adminbase')
            elif user.is_customer:

                return redirect('customerbase')
            elif user.is_company:
                return redirect('organisationbase')
        else:
            messages.info(request,'Invalid Credentials')
    return render(request,'login.html')

def customer_view(request):
    data=Customer.objects.all()
    return render(request,'customer_view.html',{'data':data})

# delete

def customer_delete(requset,id):
    data=Customer.objects.get(id=id)
    data.delete()
    return redirect('customer_view')
#company view

def company_view(request):
    data=Company.objects.all()
    return render(request, 'organisation_view.html', {'data': data})

#delete


def company_delete(requset,id):
    data=Company.objects.get(id=id)
    data.delete()
    return redirect('company_view')


def donation_view(request):
    if request.method == 'POST':
        form = CustomerDonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_success')
    else:
        form = CustomerDonationForm()

    return render(request, 'customer/donation_form.html', {'form': form})

def donation_success(request):
    return render(request, 'customer/donation_success.html')

def company_approve_donation(request, id):
    donation = get_object_or_404(CustomerDonations, id=id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'approve':
            donation.company_approved = 1  # Approved
            messages.success(request, 'Donation approved by company successfully!')
        donation.save()
        if donation.customer is not None:
            Notifications.objects.create(
                user=donation.customer,
                message=f"Your donation of {donation.amount} has been approved."
            )
        else:
            messages.error(request, 'Customer associated with this donation not found.')
        return redirect('organisationbase')
    return render(request, 'company_approve.html', {'donation': donation})

def admin_approve_donation(request, id):
    donation = get_object_or_404(CustomerDonations, id=id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'approve' and donation.company_approved == 1:
            donation.admin_approved = 1  # Approved
            messages.success(request, 'Donation approved by admin successfully!')
        elif action == 'reject':
            donation.admin_approved = 2  # Rejected
            messages.success(request, 'Donation rejected by admin successfully!')
        donation.save()
        return redirect('adminbase')
    return render(request, 'admin/admin_approve.html', {'donation': donation})

def company_view_all_requests(request):
    donations = CustomerDonations.objects.all()
    return render(request, 'company/view_all_requests.html', {'donations': donations})

def admin_view_all_requests(request):
    donations = CustomerDonations.objects.all()
    return render(request, 'admin/view_all_requests.html', {'donations': donations})

def approved_donations(request):
    donations = CustomerDonations.objects.filter(admin_approved=1)
    return render(request, 'approved_donations.html', {'donations': donations})

def rejected_donations(request):
    donations = CustomerDonations.objects.filter(admin_approved=2)
    return render(request, 'rejected_donations.html', {'donations': donations})


def customer_notifications(request):
    customer = get_object_or_404(Customer, user=request.user)
    notifications = Notifications.objects.filter(user=customer).order_by('-date')
    return render(request, 'notification.html', {'notifications': notifications})

def view_notifications(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
        notifications = Notifications.objects.filter(user=customer).all()
        print(notifications)
        return render(request, 'notification.html', {'notifications': notifications})
    else:
        return redirect('login')

# def view_notifications(request):
#     if request.user.is_authenticated:
#         customer = get_object_or_404(Customer, user=request.user)
#         notifications = Notifications.objects.filter(user=customer).order_by('-date')
#         print(f"Fetched Notifications: {notifications}")
#         return render(request, 'notification.html', {'notifications': notifications})
#     else:
#         return redirect('login')



def feedback(request):
    user=request.user
    customer=Customer.objects.get(user=user)
    print(user)
    data=FeedbackForm()
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            a=form.save(commit=False)
            a.user=customer
            a.save()
            return redirect('customerbase')

    return render(request,'customer/feedback.html',{'form':data})

def feedback_view(request):
    user=request.user
    print(user)
    customer=Customer.objects.get(user=user)
    data = Feedback.objects.filter(user=customer)
    return render(request, 'customer/feedback_view.html', {'data': data})

def feedback_delete(requset,id):
    data=Feedback.objects.get(id=id)
    data.delete()
    return redirect('feedback_view')

def admin_feedback_view(request):
    data = Feedback.objects.all()
    print(data)
    return render(request, 'admin/admin_feedback_view.html', {'data': data})

def replay_to_feedback(request,id):
    feedback=Feedback.objects.get(id=id)
    if request.method== 'POST':
        r=request.POST.get('replay')
        feedback.replay= r
        feedback.save()
        messages.info(request,'Replay send for complaint')
        return redirect('admin_feedback_view')
    return render(request,'admin/replay_to_feedback_view.html',{'feedback':feedback})