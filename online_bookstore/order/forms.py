from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Wichita', 'Wichita'),
		('Overland Park', 'Overland Park'),
		('Kansas City', 'Kansas City'),
		('Olathe', 'Olathe'),
		('Topeka', 'Topeka'),
	)

	DISCRICT_CHOICES = (
		('Allen', 'Allen'),
		('Anderson', 'Anderson'),
		('Atchison', 'Atchison'),
		('Barber', 'Barber'),
		('Chase', 'Chase'),
	)

	PAYMENT_METHOD_CHOICES = (
		('Paypal', 'Paypal'),
		('Credit Card', 'Credit Card')
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district = forms.ChoiceField(choices=DISCRICT_CHOICES)
	# payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code']
