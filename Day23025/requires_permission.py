
def requires_permission(required_roles):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.role in required_roles:
                return func(user, *args, **kwargs)
            else:
                print("Lỗi: Bạn không có quyền truy cập.")
        return wrapper
    return decorator
