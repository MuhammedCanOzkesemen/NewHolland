from django.db import models

class TractorSeries(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=120)
    short_summary = models.CharField(max_length=220, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name


class TractorModel(models.Model):
    series = models.ForeignKey(TractorSeries, on_delete=models.PROTECT, related_name="models")
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=160)
    short_summary = models.CharField(max_length=220, blank=True)
    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    hero_image = models.ImageField(upload_to="tractors/hero/", blank=True, null=True)
    brochure_pdf = models.FileField(upload_to="tractors/brochures/", blank=True, null=True)

    class Meta:
        ordering = ["series__sort_order", "sort_order", "name"]

    def __str__(self):
        return self.name


class SpecGroup(models.Model):
    model = models.ForeignKey(TractorModel, on_delete=models.CASCADE, related_name="spec_groups")
    title = models.CharField(max_length=120)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return f"{self.model.name} - {self.title}"


class SpecItem(models.Model):
    group = models.ForeignKey(SpecGroup, on_delete=models.CASCADE, related_name="items")
    label = models.CharField(max_length=140)
    value = models.CharField(max_length=240)
    unit = models.CharField(max_length=40, blank=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        unit = f" {self.unit}" if self.unit else ""
        return f"{self.label}: {self.value}{unit}"
