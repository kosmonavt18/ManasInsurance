from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView
from .forms import ApplicationForm
from .models import Application


class ApplicationCreateView(LoginRequiredMixin, CreateView):
    """Страница 'Отправить заявку'. Требует авторизации."""
    model = Application
    form_class = ApplicationForm
    template_name = 'applications/create.html'
    success_url = reverse_lazy('applications:thanks')
    login_url = reverse_lazy('accounts:register')
    redirect_field_name = 'next'

    def handle_no_permission(self):
        messages.warning(self.request,
                         'Чтобы отправить заявку, пожалуйста, зарегистрируйтесь или войдите.')
        return redirect(f"{reverse('accounts:register')}?next={self.request.get_full_path()}")

    def dispatch(self, request, *args, **kwargs):
        # Админ/сотрудник не может отправлять заявки от своего имени
        if request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser):
            messages.error(request,
                           'Администраторы и сотрудники не могут отправлять заявки. '
                           'Заявки отправляют только клиенты.')
            return redirect('core:home')
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        u = self.request.user
        if u.is_authenticated:
            initial.update({
                'full_name': u.get_full_name() or u.username,
                'phone': getattr(u, 'phone', '') or '',
                'email': u.email or '',
            })
        t = self.request.GET.get('type')
        if t in dict(Application.INSURANCE_TYPE_CHOICES):
            initial['insurance_type'] = t
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Заявка успешно отправлена. Мы свяжемся с вами.')
        return super().form_valid(form)


class ThanksView(TemplateView):
    template_name = 'applications/thanks.html'
