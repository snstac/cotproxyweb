from django.db import models
import uuid


class COTObject(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    uid = models.CharField(max_length=128, primary_key=True, default=uuid.uuid4)
    n_number = models.CharField(max_length=16, blank=True)

    class Meta:
        ordering = ['uid']
        verbose_name = 'COT Object'
        verbose_name_plural = 'COT Objects'

    def __str__(self):
        _str = self.uid
        if self.n_number:
            _str = f"{self.uid} ({self.n_number})"
        return _str


class IconSet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    defaultGroup = models.CharField(max_length=128, blank=True)
    skipResize = models.BooleanField(default=False)
    version = models.CharField(max_length=16, blank=True)
    name = models.CharField(max_length=128, blank=True)
    class Meta:
        ordering = ['name', 'defaultGroup', 'uuid']
        verbose_name = 'Icon Set'
        verbose_name_plural = 'Icon Sets'

    def __str__(self):
        return self.defaultGroup or self.name


class Icon(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    iconset = models.ForeignKey(
        IconSet,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    name = models.CharField(primary_key=True, max_length=128)
    type2525b = models.CharField(max_length=32, blank=True)

    class Meta:
        ordering = ['name', 'type2525b']
        verbose_name = 'Icon'
        verbose_name_plural = 'Icons'
    
    def __str__(self):
        return self.name


class CPTransform(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    cot_uid = models.ForeignKey(
        COTObject,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    icon = models.ForeignKey(
        Icon,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    callsign = models.CharField(max_length=32, blank=True)
    cot_type = models.CharField(max_length=32, blank=True)
    active = models.BooleanField(default=False)

    domain = models.CharField(max_length=32, blank=True)
    agency = models.CharField(max_length=64, blank=True)
    reg = models.CharField(max_length=32, blank=True)
    model = models.CharField(max_length=32, blank=True)
    hex = models.CharField(max_length=32, blank=True)
    remarks = models.CharField(max_length=256, blank=True)

    class Meta:
        ordering = ['callsign', 'cot_uid']
        verbose_name = 'Transform'
        verbose_name_plural = 'Transforms'

    def __str__(self):
        return f"{self.callsign} ({self.cot_uid})"

