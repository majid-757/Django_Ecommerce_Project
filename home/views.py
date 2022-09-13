from django.shortcuts import render
from django.views import View



class HomeView(View):
    def get(self, request):
        return render(request, 'home/home.html')



# def loginView(request):
#     if request.method == 'POST':
#         form = FormLogin(request.POST)
#         form.save()
        
#     else:

#         form = FormLogin()  

#     return render(request, 'home/login.html', {'form': form})


