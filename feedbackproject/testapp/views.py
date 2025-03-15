from django.shortcuts import render
from testapp.forms import FeedBackForm

def feedback_view(request):
    form = FeedBackForm()
    submitted = False
    sname = ''
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            print('Form validation success and printing feedback information')
            print('*'*55)
            print('Name:',form.cleaned_data['name'])
            print('Rollno:',form.cleaned_data['rollno'])
            print('Mail ID:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['feedback'])
            submitted = True
            sname = form.cleaned_data['name']
        else:
            print('some field validations failed ')
    return render(request,'testapp/feed.html ',{'form':form,'submitted':submitted,'sname':sname})

