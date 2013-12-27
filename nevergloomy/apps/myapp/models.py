from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Event(models.Model):
	link = models.CharField(max_length=255, blank=True, default='')
	title = models.CharField(max_length=50, blank=True, default='')
	showtime = models.CharField(max_length=50, blank=True, default='')
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey('auth.User', related_name='events')

	class Meta:
		ordering = ('created',)