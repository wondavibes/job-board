from django.contrib.auth.decorators import user_passes_test


def employer_required(view_func):
    """Decorator: allow only employers."""
    decorated_view_func = user_passes_test(
        lambda u: u.is_authenticated and u.role == "employer"
    )(view_func)
    return decorated_view_func


def candidate_required(view_func):
    """Decorator: allow only candidates."""
    decorated_view_func = user_passes_test(
        lambda u: u.is_authenticated and u.role == "candidate"
    )(view_func)
    return decorated_view_func
