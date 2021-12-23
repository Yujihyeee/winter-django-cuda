from django.db import models

# Create your models here.
class AnalysisVisitor(models.Model):

    #AnalysisVisitor
    month = models.DateField(primary_key=True)
    local = models.IntegerField(null=True)
    foreigner = models.IntegerField(null=True)

    class Mete:
        db_table = "expected_visitor"

    def __str__(self):
        return f'{self.month}'


class VisitorNumber(models.Model):

    # VisitorNumber
    month = models.DateField(primary_key=True)
    local = models.IntegerField()
    foreigner = models.IntegerField()

    class Mete:
        db_table = "visitor_number"

    def __str__(self):
        return f'{self.month}'
