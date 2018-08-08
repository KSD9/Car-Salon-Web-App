from django.contrib.auth.decorators import login_required , user_passes_test

def logged_user(view_func=None, login_url='/login'):

    actual_decorator = user_passes_test(
        lambda u: u.is_active,
        login_url=login_url,
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator

def superuser_required(view_func=None, login_url='/index'):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url=login_url,
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator

def RentManager_required(view_func=None, login_url='/index'):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.role == 'RentManager' or u.role == 'Administrator' or  u.is_superuser ,
        login_url=login_url,
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator 

def SalesManager_required(view_func=None, login_url='/index'):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.role == 'SalesManager' or u.role == 'Administrator' or  u.is_superuser ,
        login_url=login_url,
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator   



