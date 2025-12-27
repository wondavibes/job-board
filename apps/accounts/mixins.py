from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class EmployerRequiredMixin(UserPassesTestMixin, LoginRequiredMixin):
    """Allow access only to users with role='employer'."""

    def test_func(self):
        return (
            self.request.user.is_authenticated and self.request.user.role == "employer"
        )


class CandidateRequiredMixin(UserPassesTestMixin):
    """Allow access only to users with role='candidate'."""

    def test_func(self):
        return (
            self.request.user.is_authenticated and self.request.user.role == "candidate"
        )
