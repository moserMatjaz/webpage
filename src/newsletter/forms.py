from django import forms
from .models import SignUp


class ContactForm(forms.Form):

	name = forms.CharField(required=True)
	lastName = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	message = forms.CharField(required=True, widget=forms.Textarea)

	def toCapitalFirst(self, wordString):
		"""
		Capitalizes the first letter and return the whole word.
		"""
		firstLetter = wordString[0].upper()
		otherLetters = wordString[1:]
		return firstLetter + otherLetters

	def clean_name(self):
		name = self.cleaned_data.get("name")
		return self.toCapitalFirst(name)

	def clean_lastName(self):
		lastName = self.cleaned_data.get("lastName")
		return self.toCapitalFirst(lastName) 

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ["name", "lastName", "email"]

	"""
	The clean_xxx methods are built in and we can overwrite them with our own.
	Name of the method thas to be the same.
	"""

	def clean_name(self):
		name = self.cleaned_data.get("name")
		return self.toCapitalFirst(name)

	def clean_lastName(self):
		lastName = self.cleaned_data.get("lastName")
		return self.toCapitalFirst(lastName)

	def clean_email(self):

		fullEmail = self.cleaned_data.get("email")
		user = fullEmail.split("@")[0]
		extension = fullEmail.split("@")[1]
		domain = extension.split(".")[1] 

		if domain == "edu":
			return fullEmail
		else:
			raise forms.ValidationError("Invalid domain. Should be '.EDU'.")

	def toCapitalFirst(self, wordString):
		"""
		Capitalizes the first letter and returns the whole word.
		"""
		firstLetter = wordString[0].upper()
		otherLetters = wordString[1:]
		return firstLetter + otherLetters


