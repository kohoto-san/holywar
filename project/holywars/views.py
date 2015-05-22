from django.shortcuts import render, render_to_response

from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect, HttpResponse

from django.template import RequestContext

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage

from django.views.generic import ListView, CreateView, DetailView
from holywars.models import Holywar, HolywarLike, HolywarArgument, Thread, ThreadComments, ThreadCommentsLike, ThreadLike, Invite, InviteForm

import random

from allauth.account.views import SignupView

from django.shortcuts import get_object_or_404

def loginNone(request):
    return render_to_response('account/a_login_none.html', RequestContext(request))


class HolywarList(ListView):
    model = Holywar
    template_name = 'holywars/index.html'

    def get_queryset(self):
        qs = super(HolywarList, self).get_queryset()
        return qs.order_by('-id')[:10]

    def dispatch(self, request, *args, **kwargs):

        if not self.request.user.is_authenticated():
            return HttpResponseRedirect('/ln')
        else:
            return super(HolywarList, self).dispatch(request, *args, **kwargs)


def holywarUpdate(request):

    if request.user.is_authenticated():

        hw = Holywar.objects.all()
        hw = hw.order_by('-id')

        paginator = Paginator(hw, 10)

        page = request.GET.get('page')

        try:
            hw = paginator.page(page)
        except PageNotAnInteger:
            page = 1
            hw = paginator.page(1)
        except (EmptyPage, InvalidPage):
            hw = paginator.page(paginator.num_pages)

        return render_to_response('holywars/index.html', {"object_list": hw})

    else:
        return HttpResponseRedirect('/ln')


class HolywarCreate(CreateView):
    model = Holywar
    template_name = 'holywars/new_holywar.html'

    fields = ['holywar_object_1', 'holywar_object_2', 'holywar_description_1', 'holywar_description_2']

    def form_valid(self, form):

        #instance = form.save(commit = False)

        # instance.background = bg
        # instance.save()

        if self.request.user.is_authenticated():

            form.instance.user = self.request.user

            form.save()
            return super(HolywarCreate, self).form_valid(form)

        else:
            return HttpResponseRedirect('/ln')

    def get_success_url(self):
        return reverse('holywar_detail', args=(self.object.id,))

    def dispatch(self, request, *args, **kwargs):

        if not self.request.user.is_authenticated():
            return HttpResponseRedirect('/ln')
        else:
            return super(HolywarCreate, self).dispatch(request, *args, **kwargs)


def like_holywar(request):

    if request.user.is_authenticated() and request.method == 'GET':
        #id_comment = request.self.kwargs['pk']
        id_holywar = request.GET['pk']

        holywar = Holywar.objects.filter(id=id_holywar).first()

        obj, created = HolywarLike.objects.get_or_create(holywar = holywar, user = request.user)

        if created == True:
            holywar.holywar_likes += 1
            holywar.save()
            return HttpResponse('liked')
        else:
            return HttpResponse('no_liked')


class HolywarDetail(DetailView):
    model = Holywar
    template_name = 'holywars/holywar.html'

    def get_context_data(self, **kwargs):
        context = super(HolywarDetail, self).get_context_data(**kwargs)

        holywar_data = Holywar.objects.filter(id=self.kwargs['pk']).first()

        arguments_for_1 = Thread.objects.filter(holywar = holywar_data, argument_for = 1)
        arguments_for_1 = arguments_for_1.all().order_by('-thread_likes')[:5]

        arguments_for_2 = Thread.objects.filter(holywar = holywar_data, argument_for = 2)
        arguments_for_2 = arguments_for_2.all().order_by('-thread_likes')[:5]

        threads_data = Thread.objects.filter(holywar=holywar_data)
        threads_data = threads_data.order_by('-id')

        paginator = Paginator(threads_data, 10)

        page = self.request.GET.get('page')

        try:
            threads = paginator.page(page)
        except PageNotAnInteger:
            page = 1
            threads = paginator.page(1)
        except (EmptyPage, InvalidPage):
            threads = paginator.page(paginator.num_pages)

        context["threads"] = threads

        p = HolywarLike.objects.filter(holywar=holywar_data, user=self.request.user)
        if p:
            i_like = 1
        else:
            i_like = 0

        context["i_like"] = i_like

        context["holywar"] = holywar_data

        context["arguments_for_1"] = arguments_for_1
        context["arguments_for_2"] = arguments_for_2

        # context["comments_list"] = self.model.objects.filter(thread = holywar_data)
        # context["thread"] = get_object_or_404(Thread, pk=pk)

        return context

    def dispatch(self, request, *args, **kwargs):

        if not self.request.user.is_authenticated():
            return HttpResponseRedirect('/ln')
        else:
            return super(HolywarDetail, self).dispatch(request, *args, **kwargs)


class ThreadCreate(CreateView):
    model = Thread
    template_name = 'holywars/new_thread.html'
    fields = ['name', 'description', 'argument_for']

    def form_valid(self, form):

        holywar = Holywar.objects.filter(id = self.kwargs['holywar']).first()

        if self.request.user.is_authenticated():

            holywar.threads += 1
            holywar.save()

            form.instance.user = self.request.user

            form.instance.holywar = holywar
            form.save()
            return super(ThreadCreate, self).form_valid(form)

        else:
           return HttpResponseRedirect('/h')

    def get_context_data(self, **kwargs):

        context = super(ThreadCreate, self).get_context_data(**kwargs)

        holywar_data = get_object_or_404(Holywar, pk=self.kwargs['holywar'])

        context["holywar"] = holywar_data

        return context

    def get_success_url(self):
        return reverse('thread_detail',kwargs={'holywar': self.object.holywar.id, 'pk': self.object.id})

    def dispatch(self, request, *args, **kwargs):

        if not self.request.user.is_authenticated():
            return HttpResponseRedirect('/ln')
        else:
            return super(ThreadCreate, self).dispatch(request, *args, **kwargs)


class ThreadDetail(CreateView):
    model = ThreadComments
    fields = ['text']
    template_name = 'holywars/thread.html'

    def get_success_url(self):
        return reverse('thread_detail', args=(self.object.thread.id,))

    def form_valid(self, form):
        thread = Thread.objects.filter(id=self.kwargs['pk']).first()

        if self.request.user.is_authenticated():

            ava_number = random.randint(0, 14)

            thread.comments += 1
            thread.save()

            instance = form.save(commit=False)

            instance.avatar = ava_number

            instance.user = self.request.user

            instance.thread = thread
            instance.save()

            return HttpResponseRedirect(reverse('thread_detail',
                kwargs={'holywar': thread.holywar.id, 'pk': thread.id}))

        else:
            return HttpResponseRedirect('/h')

    def get_context_data(self, **kwargs):

        context = super(ThreadDetail, self).get_context_data(**kwargs)

        thread_data = get_object_or_404(Thread, pk=self.kwargs['pk'], holywar=self.kwargs['holywar'])

        comments = ThreadComments.objects.filter(thread=thread_data)

        p = ThreadLike.objects.filter(thread=thread_data, user=self.request.user)
        if p:
            i_like_thread = 1
        else:
            i_like_thread = 0

        context["i_like_thread"] = i_like_thread

        c = ThreadCommentsLike.objects.filter(comment=comments).values_list('comment__id', flat=True)

        context["comments_like"] = c

        argument = None

        if thread_data.argument_for == '1':
            argument = thread_data.holywar.holywar_object_1

        if thread_data.argument_for == '2':
            argument = thread_data.holywar.holywar_object_2


        context["argument"] = argument

        context["comments"] = comments
        context["object"] = thread_data

        return context

    def dispatch(self, request, *args, **kwargs):

        if not self.request.user.is_authenticated():
            return HttpResponseRedirect('/ln')
        else:
            return super(ThreadDetail, self).dispatch(request, *args, **kwargs)


def like_comment(request):

    if request.user.is_authenticated() and request.method == 'GET':
        #id_comment = request.self.kwargs['pk']
        id_comment = request.GET['pk']

        comment = ThreadComments.objects.filter(id=id_comment).first()

        obj, created = ThreadCommentsLike.objects.get_or_create(comment = comment, user = request.user)

        if created == True:
            comment.comment_likes += 1
            comment.save()
            return HttpResponse('liked')
        else:
            return HttpResponse('no_liked')

        # comment.likes += 1
        # comment.save()


def like_thread(request):

    if request.user.is_authenticated() and request.method == 'GET':

        id_thread = request.GET['pk']

        thread = Thread.objects.filter(id = id_thread).first()

        obj, created = ThreadLike.objects.get_or_create(thread = thread, user = request.user)

        if created == True:
            thread.thread_likes += 1
            thread.save()
            return HttpResponse('liked')
        else:
            return HttpResponse('no_liked')


def my_profile(request):

    if request.user.is_authenticated():

        holywars = Holywar.objects.filter(user=request.user).order_by('-id')
        threads = Thread.objects.filter(user=request.user).order_by('-id')
        comments = ThreadComments.objects.filter(user=request.user).order_by('-id')

        context = {'holywars':  holywars, 'threads': threads, 'comments': comments}

        return render(request, 'holywars/my_profile.html', context)
    else:
        return HttpResponseRedirect('/ln')


def homepage(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/h')

    else:
        return render_to_response("holywars/homepage.html", RequestContext(request))


class HomepageView(SignupView):

    def get_context_data(self, **kwargs):

        context = super(HomepageView,
                        self).get_context_data(**kwargs)

        #context['login_form'] = LoginForm() # add form to context

        return context
