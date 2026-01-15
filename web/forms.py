from django import forms
from django.utils.text import slugify
from uuid import uuid4
from datetime import datetime


from uuid import uuid4
from django.utils.text import slugify
from datetime import datetime

class PostCreationForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(min_length=5)
    is_published = forms.BooleanField(required=False, initial=True)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")

        if title:
            unique_id = uuid4().hex[:8]  # qisqa unique
            base_slug = slugify(title)

            cleaned_data["id"] = str(uuid4())
            cleaned_data["slug"] = f"{base_slug}-{unique_id}"

            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            cleaned_data["created_at"] = now
            cleaned_data["updated_at"] = now

        return cleaned_data

class PostUpdateForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(min_length=5)
    is_published = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        return cleaned_data
