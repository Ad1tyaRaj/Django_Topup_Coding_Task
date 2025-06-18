from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TopUpOrderSerializer
from .models import TopUpOrder, TopUpProduct
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, Sum
from django.utils.timezone import now, timedelta
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib import auth




#Apis showing in postman

class TopUpOrderAPIView(APIView):
    def get(self, request):
        return Response({ "message": " Only POST method allowed. Use Postman or curl to create a top-up order. GET is not supported on this endpoint."})

    def post(self, request):
        serializer = TopUpOrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response({
                "message": "Top-Up Order Created ✅",
                "order_id": order.id
            }, status=201)
        return Response(serializer.errors, status=400)
    
    
    
#Homepage   
def Base(request):
    return render(request, 'Home/Base.html')


#Login 
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
        return redirect('/')
    else:
        return render(request, 'Home/Login.html')
#Signup
def Signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request, 'Password Not Matching...')
            return redirect('signup')
        return redirect('/')
    else:
        return render(request, 'Home/Signup.html')   

#Dashboard
def Dashboard(request):
    if request.user.is_authenticated:
        # Top 5 most purchased
        top_products = (
            TopUpProduct.objects
            .annotate(total=Count('topuporder'))
            .order_by('-total')[:5]
        )

        # Daily revenue for last 7 days
        today = now().date()
        last_7_days = [today - timedelta(days=i) for i in range(7)]
        daily_revenue = []

        for day in reversed(last_7_days):
            total = (
                TopUpOrder.objects
                .filter(status='success', created_at__date=day)
                .aggregate(Sum('product__price'))['product__price__sum'] or 0
            )
            daily_revenue.append({"date": day.strftime("%Y-%m-%d"), "total": total})

        # Failed payments in this month
        failed_payments = TopUpOrder.objects.filter(
            status='failed',
            created_at__month=now().month,
            created_at__year=now().year
        ).count()

        return render(request, 'Home/Dashboard.html', {
            'top_products': top_products,
            'daily_revenue': daily_revenue,
            'failed_payments': failed_payments
        })
    else:
        return redirect('login')

#Logout
def Logout(request):
    auth.logout(request)
    return redirect('/')