# Create your views here.


from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin
from .models import Services, Comments
from ..Authentication.models import Costumer
from .forms import CommentsForm
from django.core.paginator import Paginator


class EndlessScroll(ListView):
    model = Services
    template_name = 'services/endless_service.html'
    context_object_name = 'resort_services'
    paginate_by = 5
    ordering = ['-create_time']


class PageList(ListView):
    template_name = 'services/service_list.html'
    context_object_name = 'resort_services'
    paginate_by = 5

    def get_queryset(self):
        return Services.objects.order_by('-create_time')

    def listing(request):
        name = Services.objects.all()
        paginator = Paginator(name, 5)  # Show 5 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'list.html', {'page_obj': page_obj})


class Details(FormMixin, DetailView):
    template_name = 'services/service.html'
    form_class = CommentsForm
    model = Comments
    context_object_name = 'service_data'

    def get_queryset(self):
        return Services.objects.all()

    def get_success_url(self):
        return reverse('service:data', kwargs={'slug': self.kwargs['slug']})

    def get_context_data(self, **kwargs):
        context = super(Details, self).get_context_data(**kwargs)
        # context['form'] = CommentsForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            print(form.errors)
            return self.form_invalid(form)

    def form_valid(self, form):
        myform = form.save(commit=False)
        myform.post = self.get_object()
        myform.author = get_object_or_404(Costumer, user_id=self.request.user.id)
        myform.service_id = get_object_or_404(Services, pk=self.object.id)
        myform.save()
        return super(Details, self).form_valid(form)

    def form_invalid(self, form):
        return super(Details, self).form_invalid(form)

    # @register.filter
    # def reply(self, aVal):
    #     result = aVal.filter(is_known=False)
    #     return result