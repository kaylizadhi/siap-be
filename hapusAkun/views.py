from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import UserAccount 

def delete_akun(request, user_id):
    # Cek apakah pengguna yang mengakses sudah login
    if not request.user.is_authenticated:
        messages.error(request, 'Anda harus login terlebih dahulu.')
        return redirect('login')  

    # Cek apakah user yang mengakses adalah admin sistem
    if request.user.role != 'admin-sistem':
        messages.error(request, 'Hanya admin sistem yang bisa menghapus akun.')
        return redirect('index')  # Harus direct ke halaman yang sesuai, todo laras!

    # Dapatkan user account yang ingin dihapus
    user_account = get_object_or_404(UserAccount, id=user_id)

    # Hapus akun
    user_account.delete()

    # Beri notifikasi bahwa akun berhasil dihapus
    messages.success(request, 'Akun berhasil dihapus!')
    return redirect('index')  # Harus direct ke halaman yang sesuai, todo laras!Redirect ke halaman yang sesuai

def confirm_delete_akun(request, user_id):
    # Cek apakah pengguna yang mengakses sudah login
    if not request.user.is_authenticated:
        messages.error(request, 'Anda harus login terlebih dahulu.')
        return redirect('login')  

    # Cek apakah user yang mengakses adalah admin sistem
    if request.user.role != 'admin-sistem':
        messages.error(request, 'Hanya admin sistem yang bisa menghapus akun.')
        return redirect('index')  # Harus direct ke halaman yang sesuai, todo laras!

    # Dapatkan user account yang ingin dihapus
    user_account = get_object_or_404(UserAccount, id=user_id)

    if request.method == 'POST':
        # Hapus akun jika POST request
        user_account.delete()
        messages.success(request, 'Akun berhasil dihapus!')
        return redirect('index')  # Harus direct ke halaman yang sesuai, todo laras!

    # Render konfirmasi hapus akun
    return render(request, 'delete_confirmation.html', {'user_account': user_account})
