from django.db import models
from produtos.models import Produto
from fornecedores.models import Fornecedor
from django.core.validators import MinValueValidator

# Create your models here.

class Compra(models.Model):
    # Relacionamentos (Chaves Estrangeiras)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    
    # Campos da Tabela Compra
    preco = models.DecimalField(verbose_name="Preço Unitário",
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0.00)]
    )
    data_compra = models.DateField(verbose_name="Data da Compra")
    quantidade = models.PositiveIntegerField()

    # REGRA DE NEGÓCIO: CRIAR E EDITAR
    def save(self, *args, **kwargs):
        # Verifica se é uma edição (o ID já existe)
        if self.pk is not None:
            # Vai no banco de dados e busca a compra original ANTES de salvar a nova
            compra_antiga = Compra.objects.get(pk=self.pk)
            
            # Cenário 1: O produto continua o mesmo, só a quantidade mudou
            if compra_antiga.produto == self.produto:
                # Calcula a diferença (Ex: era 10, virou 15 -> diferença = +5)
                diferenca = self.quantidade - compra_antiga.quantidade
                self.produto.quantidade += diferenca
                
            # Cenário 2: O usuário trocou o produto na hora da edição
            else:
                # Devolve o estoque para o produto que estava antes
                produto_antigo = compra_antiga.produto
                produto_antigo.quantidade -= compra_antiga.quantidade
                produto_antigo.save()
                
                # Adiciona o estoque inteiro no produto novo
                self.produto.quantidade += self.quantidade
                
        # Se for uma compra totalmente nova
        else:
            self.produto.quantidade += self.quantidade

        # Salva a compra
        super().save(*args, **kwargs)
        # Salva as alterações no produto atual
        self.produto.save()

    # REGRA DE NEGÓCIO: EXCLUIR (ESTORNO)
    def delete(self, *args, **kwargs):
        # Antes de apagar a compra, retira a quantidade do estoque do produto
        self.produto.quantidade -= self.quantidade
        self.produto.save()
        
        # Apaga a compra do banco
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Compra #{self.id} - {self.produto.nome}"