from django.shortcuts import render

# Create your views here.

def home_screen_view(request):
	
	context = {}
	# context['some_string'] = "This is some string that I'm passing to view."
	# context['some_number'] = 123456

	# context = {
	#	'some_string' : "This is some string that I'm passing to view.",
	#	'some_number' : 123456,
	# }

	list_of_values = []
	list_of_values.append("first entry")
	list_of_values.append("second entry")
	list_of_values.append("third entry")
	list_of_values.append("fourth entry")
	context['list_of_values'] = list_of_values

	return render(request, "personal/home.html", context)

