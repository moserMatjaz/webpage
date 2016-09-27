from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import SignUpForm
from .forms import ContactForm
from django.conf import settings

from .models import SignUp

# Create your views here.
def home(request):
	"""
	locals() creates a dictinary of variables in scope. Render puts it all
	together.

	locals = {"username": "Matjaz"}
	"""
	return render(request, "home.html", locals())


def signUpForm(request):
	"""
	Context alows us to vbring some form of 'context' to our website. This context
	can be avariable, form, .....

	form.cleaned_data is a dictionary !!!
	"""
	form = SignUpForm(request.POST or None)

	context = {"form": form,
			   "title": "Contact Form",
			   "description": "Plsease fill in the contact from with your information..."}


	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/thankYou')
	return render(request, "signUpForm.html", context)

def thankYouNewsletter(request):
	return render(request, "thankYou.html", {})

def contact(request):
	"""
	Can also be send as htmlMessage to amke it prettier:
	https://docs.djangoproject.com/en/1.10/topics/email/
	"""


	form = ContactForm(request.POST or None)

	if form.is_valid():
		email = form.cleaned_data.get("email")
		name = form.cleaned_data.get("name")
		lastName = form.cleaned_data.get("lastName")
		message = form.cleaned_data.get("message")


		subject = "Site contact message."
		fromEmail = settings.EMAIL_HOST_USER
		contactMessage = "From: {0}\nMessage: {1}\n".format(email, message)

		# we are sending the email to ourselves (from = to)
		send_mail(subject, contactMessage, fromEmail, [fromEmail], fail_silently=False)


	return render(request, "contact.html", {"form": form})

def about(request):
	"""
	Query set:
		- all objects: model.objects.all()
		- filter: model.objects.all().order_by("-timestamp").filter(lastName__icontains="bla bla bla")
		- order by: model.objects.all().order_by("-timestamp")
		- distinct:
		- count: model.objects.all().order_by("-timestamp").count()

	-----> https://docs.djangoproject.com/el/1.10/ref/models/querysets/

	"""
	if request.user.is_authenticated and request.user.is_staff:
		context = {"dataSet": SignUp.objects.all().order_by("-timestamp")}
		return render(request, "about.html", context)

	return render(request, "about.html", {})

def recipesVisualisation(request):

	return render(request, "msiasu.html", {})





