from django.contrib import admin

# Register your models here.

from .models import Biblioteca, Autor, Libro, Cliente, DatosCliente
admin.site.register(Biblioteca)
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Cliente)
admin.site.register(DatosCliente)
