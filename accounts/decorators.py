from django.contrib.auth.decorators import user_passes_test

def admin_required(view_func):
    return user_passes_test(lambda u: u.role == 'Admin', login_url='http://localhost:3000/login')(view_func)

def administrator_required(view_func):
    return user_passes_test(lambda u: u.role == 'Administrator', login_url='http://localhost:3000/login')(view_func)

def eksekutif_required(view_func):
    return user_passes_test(lambda u: u.role == 'Eksekutif', login_url='http://localhost:3000/login')(view_func)

def pengendali_mutu_required(view_func):
    return user_passes_test(lambda u: u.role == 'Pengendali Mutu', login_url='http://localhost:3000/login')(view_func)

def logistik_required(view_func):
    return user_passes_test(lambda u: u.role == 'Logistik', login_url='http://localhost:3000/login')(view_func)
