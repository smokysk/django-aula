from django.db import models


class ModelBase(models.Model):
    id = models.AutoField(
        null=False,
        primary_key=True
    )
    created_at = models.DateTimeField(
        null=False,
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        null=False,
        auto_now=True
    )
    active = models.BooleanField(
        default=True
    )

    class Meta:
        abstract = True


class State(ModelBase):
    name = models.CharField(
        max_length=64,
        null=False,
        unique=True
    )
    abbreviation = models.CharField(
        max_length=2,
        null=False
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'state'
        managed = True


class City(ModelBase):
    name = models.CharField(
        max_length=64,
        null=False,
    )
    state = models.ForeignKey(
        to=State,
        on_delete=models.DO_NOTHING,
        db_column='id_state',
        related_name='states',
        null=False
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'city'
        managed = True


class Zone(ModelBase):
    name = models.CharField(
        max_length=64,
        null=False,
        unique=True,
        default=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'zone'
        managed = True


class District(ModelBase):
    name = models.CharField(
        max_length=64,
        null=False,
    )
    city = models.ForeignKey(
        to=City,
        db_column='id_city',
        on_delete=models.DO_NOTHING,
        related_name='cities',
        null=False
    )
    zone = models.ForeignKey(
        to=Zone,
        db_column='id_zone',
        on_delete=models.DO_NOTHING,
        related_name='zones',
        null=False
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'district'
        managed = True
