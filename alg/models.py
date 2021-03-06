from django.db import models
from django.contrib.postgres.fields import ArrayField


class Algorithm_description(models.Model):
    """
    Model description of algorithm
    """
    name = models.CharField(max_length=50,
                            verbose_name="Name of algorithm",
                            unique=True)

    description = models.TextField(blank=True,
                                   verbose_name="Description of algorithm")

    big_o_notation = models.CharField(max_length=30,
                                      verbose_name="Bit O notation",
                                      blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Algorithm_execution_result(models.Model):
    """
    Model of resulting algorithms
    """
    name_alg = models.ForeignKey(Alg, on_delete=models.CASCADE)
    timing = models.CharField(max_length=50)
    input_mas = ArrayField(models.IntegerField())
    result_mas = ArrayField(models.IntegerField())

    def __str__(self):
        return '%s sort (%s)' % (self.name_alg, self.timing)