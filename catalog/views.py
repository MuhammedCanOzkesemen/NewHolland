from django.shortcuts import render, get_object_or_404
from .models import TractorSeries, TractorModel

def home(request):
    return render(request, "site/home.html")

def series_list(request):
    series = TractorSeries.objects.filter(is_active=True).order_by("sort_order")
    return render(request, "site/series_list.html", {"series": series})

def series_detail(request, slug):
    series = get_object_or_404(TractorSeries, slug=slug, is_active=True)
    models = series.models.filter(is_active=True).order_by("sort_order", "name")
    return render(request, "site/series_detail.html", {
        "series": series,
        "models": models,
    })

def model_detail(request, slug):
    model = get_object_or_404(TractorModel, slug=slug, is_active=True)
    spec_groups = model.spec_groups.all()
    return render(request, "site/model_detail.html", {
        "model": model,
        "spec_groups": spec_groups,
    })

def contact(request):
    return render(request, "site/iletisim.html")
