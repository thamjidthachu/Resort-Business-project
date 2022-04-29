# Create your views here.
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin, CreateView
from .models import Services, Comments
from ..Authentication.models import Costumer
from .forms import CommentsForm
from django.core.paginator import Paginator
import datetime


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


# Service_Individual
class Details(FormMixin, DetailView):
    template_name = 'services/service.html'
    form_class = CommentsForm
    model = Comments
    context_object_name = 'service_data'

    def get_queryset(self):
        return Services.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Details, self).get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse('service:datas', kwargs={'slug': self.kwargs['slug']})

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
        print(myform.post)
        myform.author = get_object_or_404(Costumer, user_id=self.request.user.id)
        print(myform.author)
        myform.service_id = get_object_or_404(Services, pk=self.object.id)
        print(myform.service_id)
        myform.content_type = ContentType.objects.get(app_label='Services', model='services')
        print(myform.content_type)
        myform.content_object = get_object_or_404(Services, pk=self.object.id)
        print(myform.content_object)
        myform.save()
        return super(Details, self).form_valid(form)

    def form_invalid(self, form):
        return super(Details, self).form_invalid(form)


def replyPost(request):
    content_obj = ContentType.objects.get(app_label='Services', model='comments')
    print(content_obj)
    obj_id = request.POST['reply_id']
    print(obj_id)
    reply = request.POST['reply']
    print(reply)
    auth = get_object_or_404(Costumer, user_id=request.POST['authuser'])
    print(auth)
    serve_id = get_object_or_404(Services, id=request.POST['service_id'])
    print(serve_id)
    timestamp = datetime.datetime.now()
    newreply, created = Comments.objects.get_or_create(
        content_type=content_obj,
        object_id=obj_id,
        message=reply,
        author=auth,
        service_id=serve_id,
        comment_time=timestamp
    )
    test = get_object_or_404(Services, id=request.POST['service_id'])
    slugify = test.slug
    print(slugify)

    if not created:
        newreply.save()
    return redirect(reverse('service:datas', args=[slugify]))


