from django.views.generic import FormView, TemplateView
from .forms import OSAGOForm, KASKOForm, PropertyForm, TravelForm
from .services import CALCULATORS


class CalculatorsIndexView(TemplateView):
    template_name = 'calculators/index.html'


class _CalcMixin:
    calc_key = None
    template_name = None
    form_class = None

    def form_valid(self, form):
        result = CALCULATORS[self.calc_key].calculate(form.cleaned_data)
        return self.render_to_response(self.get_context_data(form=form, result=result))


class OSAGOCalculatorView(_CalcMixin, FormView):
    template_name = 'calculators/osago.html'
    form_class = OSAGOForm
    calc_key = 'osago'


class KASKOCalculatorView(_CalcMixin, FormView):
    template_name = 'calculators/kasko.html'
    form_class = KASKOForm
    calc_key = 'kasko'


class PropertyCalculatorView(_CalcMixin, FormView):
    template_name = 'calculators/property.html'
    form_class = PropertyForm
    calc_key = 'property'


class TravelCalculatorView(_CalcMixin, FormView):
    template_name = 'calculators/travel.html'
    form_class = TravelForm
    calc_key = 'travel'
