from rest_framework import serializers
from .models import Produto

class ProdutoSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['nome', 'preco']
        read_only_fields = ['id', 'criado_em']

        # Valida campo individual
        def validate_preco(self, value):
            if value <= 0:
                raise serializers.ValidationError(
                'Preço deve ser positivo.')
            return value
            # Valida múltiplos campos juntos
        def validate(self, data):
            if data['estoque'] == 0 and data['ativo']:
                raise serializers.ValidationError(
                'Produto ativo precisade estoque.')
            return data