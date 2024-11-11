
# from django.shortcuts import render, redirect
# from .models import DaftarAkun
# from .forms import FormBuatAkun #account form nya disamain sama di buatAkun 

# # Liat list akun
# def list_accounts(request):
#     accounts = Account.objects.all()
#     return render(request, 'daftarAkun/list_accounts.html', {'accounts': accounts})

# # View untuk buat akun baru, harus diganti untuk liat details akun
# def create_account(request):
#     if request.method == 'POST':
#         form = AccountForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('list-accounts')
#     else:
#         form = AccountForm()
#     return render(request, 'accounts/create_account.html', {'form': form})
