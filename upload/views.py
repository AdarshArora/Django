from django.http import response
from django.shortcuts import render,HttpResponse, redirect
from . models import FileUpload, Post
import os, json
# import requests
from django.db.models import Q
# Create your views here.

def index(request):
    if request.method == 'POST':
        # name = request.POST.get['filename']
        myfile = request.FILES.getlist('files')
        for f in myfile:
            FileUpload(myfiles = f).save()

        return HttpResponse('Your file was uploaded')
    return render(request,'index.html')



def login(request):
    return render(request,'login_page.html')


#Search to JSON
def search(request):
  
    search_post = request.GET.get('query')

    dictionary ={  
        "Search": search_post
    }  
       
    # Serializing json   
    json_object = json.dumps(dictionary, indent = 4)  
    print(json_object)

    # print(search_post)

    # if search_post:
    #     posts = Post.objects.filter(Q(title__icontains=search_post) & Q(content__icontains=search_post))
    # else:
    #     posts = Post.objects.all().order_by('-date_created')

    # return render(request,'search.html',{'posts':posts})
 

def list(request):

    return render(request,'list.html',{'files': os.listdir('media/')})


def output(request):

    data = {
    "Files": [
        {
        "File": "document1.pdf",
        "Original_name": "1",
        "File_id": "1",
        "File_type": "pdf",
        "Modified_date": "yy-mm-dd",
        
        },
        {
        "File": "document2.pdf",
        "Original_name": "1",
        "File_id": "2",
        "File_type": "pdf",
        "Modified_date": "yy-mm-dd",
        
        },
        {
        "File": "document3.mp3",
        "Original_name": "1",
        "File_id": "3",
        "File_type": "mp3",
        "Modified_date": "yy-mm-dd",
        
        },
        ]
    }


        
    data_obj= json.dumps(data)
    with open("practice.json", "w") as outfile:
        outfile.write(data_obj)
        print(outfile)


    with open('practice.json', 'r') as openfile:
    
        # Reading from json file
        json_object = json.load(openfile)
        print(type(json_object))

        
