from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
	return render(request,'home.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	return HttpResponse('<h1> contact us </h1><br> This is contact page ')	

def count(request):
	data = request.GET['textarea']
	word_list = data.split()
	print(word_list)
	len_list=len(word_list)
	dictn = {}
	for word in word_list:
		if word in dictn:
			dictn[word] +=1
		else:
			dictn[word] = 1
	sorted_list = sorted(dictn.items(),key = operator.itemgetter(1))
	return render(request,'count.html',{'valuetext': data,'words': len_list, 'worddict': sorted_list})	