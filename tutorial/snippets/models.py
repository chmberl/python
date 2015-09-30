from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


# Create your models here.
class Snippet(models.Model):
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    language = models.CharField(choices=LANGUAGE_CHOICES, default='python',
                                max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default="friendly",
                             max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets')
    highlightd = models.TextField()

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)


# from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin
# import datetime
# class ProfileBase(type):
#     def __new__(cls, name, bases, attrs):
#         module = attrs.pop('__module__')
#         parents = [b for b in bases if isinstance(b, ProfileBase)]
#         if parents:
#             fields = []
#             for obj_name, obj in attrs.items():
#                 if isinstance(obj, models.Field): fields.append(obj_name)
#                 User.add_to_class(obj_name, obj)
#             UserAdmin.fieldsets = list(UserAdmin.fieldsets)
#             UserAdmin.fieldsets.append((name, {'fields': fields}))
#         return super(ProfileBase, cls).__new__(cls, name, bases, attrs)

# class Profile(object):
#     __metaclass__ = ProfileBase

# class MyProfile(Profile):
#     nickname = models.CharField(max_length = 255)
#     birthday = models.DateTimeField(null = True, blank = True)
#     city = models.CharField(max_length = 30, blank = True)
#     university = models.CharField(max_length = 255, blank = True)

#     def is_today_birthday(self):
#         return self.birthday.date() == datetime.date.today()
