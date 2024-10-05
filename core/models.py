from django.db import models

class Code(models.Model):
    text = models.TextField(default="",blank=True)
    result = models.TextField(default="",blank=True)
    is_done = models.BooleanField(default=False)

    def run_code(self):
        self.result = ""
        def dprint(*args,sep=" ", end="\n"):
            args = list(
            map(str,args))
            self.result+= sep.join(args)+end
        try:
            exec(self.text)
        except Exception as e:
        self.is_done = True
        self.save()
# Create your models here.
