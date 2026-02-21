from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_view(request):
    """
    GET  /contact/ → Show empty contact form.
    POST /contact/ → Save ContactMessage → Show success message → Redirect.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thanks for reaching out! We'll get back to you within 24 hours. 💌"
            )
            return redirect('contact')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
