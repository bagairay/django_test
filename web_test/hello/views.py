# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm
from .models import Friend
from django.shortcuts import redirect

# Create your views here.

def index(request):
    data=Friend.objects.all()
    params = {
       # 'sample' :'お腹すいた' ,
       # 'sentence' :'djangoむずい',
       # 'memo' : '次のページ',
       # 'nextpagesukinabunn' :'test',
       'title' :'hello/Home' ,
       #'message' : 'わっつゆあねいむ',
       #'form' : HelloForm()
       'data' : data,
    }
    #if(request.method == 'POST'):
       # params['message'] = '名前:' +request.POST['name'] + '<br>メール:'+request.POST['mail']+'<br>年齢:'+request.POST['age']
       # params['form'] = HelloForm(request.POST)
    return render(request, 'hello/index.html',params)#段落はきちんと分ける

def test(request):
    params = {
        'sample' :'お腹すいた' ,
        'sentence' :'djangoおいしい',
        'memo' : '次のページ',
        'nextpagesukinabunn' :'index', #ページの遷移先
    }
    return render(request, 'hello/index.html',params)#段落はきちんと分ける
    #http://localhost:8000/hello/testに飛ぶ

def form(request): #def　関数の前につける
    msg = request.POST['msg']
    params = {
        'title' :'hello/Form' ,
        'msg' :'こんにちは' + msg + '様',
    }
    return render(request, 'hello/index.html' ,params)
#create model
def create(request):
    params = {
        'title' : 'Hello',
        'form' : HelloForm(),
    }
    if(request.method == 'POST'):
        name = request.POST['name']
        mail = request.POST['mail']
        gender = 'gender' in request.POST
        age = int(request.POST['age'])
        birth = request.POST['birthday']
        friend = Friend(name=name,mail=mail,gender=gender,age=age,birthday=birth)#入力したものを代入
        friend.save()#friend情報全部保存
        return redirect(to='/hello')#helloに戻る
    return render(request, 'hello/create.html', params)
