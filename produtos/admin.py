from django.contrib import admin

from .models import Processadore
from .models import Memoria_ram
from .models import Disco_rigido
from .models import Placa_de_video
from .models import Gabinete
from .models import Placa_mae
from .models import Fone

admin.site.register(Processadore)
admin.site.register(Memoria_ram)
admin.site.register(Disco_rigido)
admin.site.register(Placa_de_video)
admin.site.register(Gabinete)
admin.site.register(Placa_mae)
admin.site.register(Fone)