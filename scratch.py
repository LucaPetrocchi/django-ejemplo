nuevo_elemento = Modelo.objects.create(
    attr_1='LOL',
    attr_2=float(1200),
    attr_3='rer'
)

modelo = Modelo.objects.all()

modeloPrimero = Modelo.objects.first()

modeloUltimo = Modelo.objects.last()

cantidad_elementos = len(modelo)
# OR
cantidad_elementos = Modelo.objects.count()

filtro_attr_1 = Modelo.objects.filter(
    attr_1='valor cualquiera'
)
# retorna un QuerySet -- si no encuentra nada, está vacío
# para sacar 1 solo objeto...
filtro_attr_1 = Modelo.objects.filter(
    attr_1='valor cualquiera'
).first()

excluir = Modelo.objects.exclude(name="SOSOIDE")

# lookups (para .filter(), .exclude(), etc, se pueden combinar)
# attr__contains
# attr__exact
# attr__iexact (no distingue mayus/minus)
# attr__gt=float(100) (greater than)
# attr__lt=float(100) (lower than)
# attr__in=['value', 'value'] (para una lista)
# attr__startswith='value'
# attr__endswith='value'
# attr__range=(float(100), float(200))
# attr__isnull