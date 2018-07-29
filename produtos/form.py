from django.forms import ModelForm
from .models import Processadore
from .models import Memoria_ram
from .models import Disco_rigido
from .models import Placa_de_video
from .models import Gabinete
from .models import Placa_mae
from .models import Fone

class ProcessadoreForm(ModelForm):
    class Meta:
        model = Processadore
        fields = ['nome','valor','estoque']

class Memoria_ramForm(ModelForm):
    class Meta:
        model = Memoria_ram
        fields = ['nome','valor','estoque']

class Disco_rigidoForm(ModelForm):
    class Meta:
        model = Disco_rigido
        fields = ['nome','valor','estoque']

class Placa_de_videoForm(ModelForm):
    class Meta:
        model = Placa_de_video
        fields = ['nome','valor','estoque']

class GabineteForm(ModelForm):
    class Meta:
        model = Gabinete
        fields = ['nome','valor','estoque']

class Placa_maeForm(ModelForm):
    class Meta:
        model = Placa_mae
        fields = ['nome','valor','estoque']

class FoneForm(ModelForm):
    class Meta:
        model = Fone
        fields = ['nome','valor','estoque']