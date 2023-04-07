from django.shortcuts import render, redirect


def home(request):
    user = request.user.is_authenticated # 사용자가 로그인 되어있는지 알려주는 함수
    if user:
        return redirect('/tweet')
    else:
        return redirect('/log-in')
    

def tweet(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'tweet/home.html')
        else:
            return redirect('/log-in')
    
