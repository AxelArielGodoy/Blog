from django.urls import reverse_lazy
from BlogApp.forms import CommentForm, FormularioPost, FormularioBusqueda
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from BlogApp.models import Post
from django.views.generic.edit import DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def blog(request):

    posts = Post.objects.all().order_by("-id")
    blog_vacio = posts.count()

    return render(request, "BlogApp/blog.html", {'posts': posts, 'blog_vacio': blog_vacio})


@login_required
def crear_post(request):

    if request.method == "POST":

        formulario_post = FormularioPost(request.POST, request.FILES)

        if formulario_post.is_valid():

            informacion = formulario_post.cleaned_data
            post = Post(
                titulo=informacion['titulo'],
                subtitulo=informacion['subtitulo'],
                contenido=informacion['contenido'],
                imagen=informacion['imagen'],)
            post.autor = request.user
            post.save()

            return redirect('blog')

    else:
        formulario_post = FormularioPost()

    return render(request, 'BlogApp/crear_post.html', {'formulario_post': formulario_post})


def post(request, id):

    post = Post.objects.get(id=id)
    comments = post.comments.filter(active=True)
    new_comment = None
   
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.name = request.user
            new_comment.save()
            return redirect('post', id)
    else:
        comment_form = CommentForm()
    return render(request, "BlogApp/post.html", {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def buscar_post(request):

    consulta = request.GET.get("titulo")

    if consulta:
        listado_post = Post.objects.filter(titulo__icontains=consulta)

    else:
        listado_post = Post.objects.all().order_by("-id")

    formulario_busqueda = FormularioBusqueda()

    return render(request, "BlogApp/buscar_post.html", {"listado_post": listado_post, "formulario_busqueda": formulario_busqueda})


@ login_required
def editar_post(request, id):

    post = Post.objects.get(id=id)
    if request.method == 'POST':

        edit_form = FormularioPost(request.POST, request.FILES)

        form = edit_form

        if edit_form.is_valid():

            form = edit_form.cleaned_data
            post.titulo = form.get('titulo') if form.get(
                'titulo') else post.titulo
            post.subtitulo = form.get('subtitulo') if form.get(
                'subtitulo') else post.subtitulo
            post.contenido = form.get('contenido') if form.get(
                'contenido') else post.contenido
            post.autor = form.get('autor') if form.get('autor') else post.autor
            post.creado = form.get('creado') if form.get(
                'creado') else post.creado
            post.imagen = form.get('imagen') if form.get(
                'imagen') else post.imagen
            post.save()

            return redirect('blog')

        else:
            return render(request, "BlogApp/editar_post.html", {"form": form, "post": post})

    form = FormularioPost(initial={'titulo': post.titulo, 'subtitulo': post.subtitulo,
                                   'contenido': post.contenido, 'autor': post.autor, 'creado': post.creado, 'imagen': post.imagen})

    return render(request, "BlogApp/editar_post.html", {"form": form, "post": post})


@method_decorator(login_required, name='dispatch')
class DeleteView(DeleteView):
    model = Post
    success_url = "/blog"
    template_name ="BlogApp/desea_eliminar.html"
    