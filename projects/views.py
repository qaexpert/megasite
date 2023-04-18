import os
import random

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProjectForm, ReviewForm
from .models import Project, Tag
from .utils import paginateProjects, searchProjects

def projects(request):
    projects, search_query = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 6)
    image_urls = ['/static/flowers_images/' + filename for filename in os.listdir('static/flowers_images/')]
    projects_with_images = zip(projects, image_urls)
    context = {
        'projects_with_images': projects_with_images,
        'search_query': search_query,
        'custom_range': custom_range,
    }
    return render(request, 'projects/projects.html', context)

#def projects(request):
#    projects, search_query = searchProjects( request )
#    custom_range, projects = paginateProjects( request, projects, 6 )
#    image_url = '/static/flowers_images/' + random.choice( os.listdir( 'static/flowers_images' ) )
 #   context = {'projects': projects,
 #              'search_query': search_query, 'custom_range': custom_range, 'image_url': image_url}
 #   return render( request, 'projects/projects.html', context )

#def projects(request):
#    projects, search_query = searchProjects(request)
#    custom_range, projects = paginateProjects(request, projects, 6)

    # выбрать случайный файл из папки static/flowers_images/
#    images_dir = 'static/flowers_images/'
#    image_file = random.choice(os.listdir(images_dir))
#    image_url = f'/{images_dir}/{image_file}'

  #  context = {'projects': projects,
  #             'search_query': search_query,
  #             'custom_range': custom_range,
  #             'image_url': image_url}
  #  return render(request, 'projects/projects.html', context)

def project(request, project_slug):
    project = Project.objects.get( slug=project_slug )
    tags = project.tags.all()
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm( request.POST )
        review = form.save( commit=False )
        review.project = project
        review.owner = request.user.profile
        review.save()
        var = project.getVoteCount
        messages.success( request, 'Ваш отзыв был добавлен!' )
        return redirect( 'project', project_slug=project.slug )
    return render( request, 'projects/single-project.html', {'project': project, 'form': form} )


@login_required( login_url="login" )
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        newtags = request.POST.get( 'newtags' ).replace( ',', " " ).split()
        form = ProjectForm( request.POST, request.FILES )
        if form.is_valid():
            project = form.save( commit=False )
            project.owner = profile
            project.save()

            for tag in newtags:
                tag, created = Tag.objects.get_or_create( name=tag )
                project.tags.add( tag )
            return redirect( 'account' )

    context = {'form': form}
    return render( request, "projects/project_form.html", context )


@login_required( login_url="login" )
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get( id=pk )
    form = ProjectForm( instance=project )

    if request.method == 'POST':
        newtags = request.POST.get( 'newtags' ).replace( ',', " " ).split()

        form = ProjectForm( request.POST, request.FILES, instance=project )
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create( name=tag )
                project.tags.add( tag )

            return redirect( 'account' )

    context = {'form': form, 'project': project}
    return render( request, "projects/project_form.html", context )


@login_required( login_url="login" )
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get( id=pk )
    if request.method == 'POST':
        project.delete()
        return redirect( 'projects' )
    context = {'object': project}
    return render( request, 'delete_template.html', context )


def projects_by_tag(request, tag_slug):
    tag = get_object_or_404( Tag, slug=tag_slug )
    projects = Project.objects.filter( tags__in=[tag] )
    context = {
        "projects": projects
    }

    return render( request, "projects/projects.html", context )
