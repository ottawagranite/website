from django import forms
from membership.models import Member

class MemberForm(forms.ModelForm):
    """Form for a member's information."""
    pass

    class Meta:
        model = Member
        fields = ['username', 'first_name', 'last_name', 'email', 'gender']
