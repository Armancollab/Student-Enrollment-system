from django import forms

class RegistrationForm(forms.Form):
    s_name = forms.CharField(label="Name", max_length=100)
    s_fathername = forms.CharField(label="Father's Name", max_length=200)
    s_mothername = forms.CharField(label="Mother's Name", max_length=200)
    s_addr = forms.CharField(label="Main Address", max_length=200)
    previous_school = forms.CharField(label="Previous School", max_length=200)
    s_phone = forms.CharField(label="Phone Number", max_length=15)
    s_gender = forms.ChoiceField(label="Gender", choices=[("Male", "Male"), ("Female", "Female")])
    s_class = forms.CharField(label="Class", max_length=10)
