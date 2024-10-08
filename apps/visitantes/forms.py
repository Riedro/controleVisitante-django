from django import forms
from .models import Visitante
from typing_extensions import Required # type: ignore


class  VisitanteForm(forms.ModelForm):

    class Meta:

        model = Visitante
        fields =  [
            'nome_completo', 'cpf', 'telefone', 'data_nascimento', 'numero_casa', 'placa_veiculo'
            ]
        error_messages = {

            'nome_completo':{'requirid': 'O nome completo do visitante é obrigatorio para o registro'
            },
            'cpf':{
                'requirid' : 'O cpf do visitante é obrigatorio para o registro'
            },
            'data_nascimento':{
                'requirid' : 'Por favor, informe um formato valido para a data de nascimento (DD/MM/AAAA)'
            },
            'numero_casa':{
                'requirid': 'Por favor, informe o número da casa a ser visitada'
                },
            'telefone' : {
                'requirid': 'Por favor, informe o número de telefone'

            }
        }

        

class AutorizaVisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = ['morador_responsavel']

        error_messages = {
            'morador_responsavel':{
                    'requirid': 'Por favor, informe do nome do morador responsavel por autorizar a entrada do visitante' 
            }
        }
