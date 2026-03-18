from django.db import models
from produtos.models import Produto
from clientes.models import Cliente
from django.core.validators import MinValueValidator

# Create your models here.
class Venda(models.Model):
    # Relacionamentos (Chaves Estrangeiras)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    # Campos da Tabela Venda
    preco = models.DecimalField(verbose_name="Preço Unitário",
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0.00)]
    )
    data_venda = models.DateField(verbose_name="Data da Venda")
    quantidade = models.PositiveIntegerField()

    # REGRA DE NEGÓCIO: BAIXA NO ESTOQUE (CRIAR E EDITAR)
    def save(self, *args, **kwargs):
        if self.pk is not None:
            venda_antiga = Venda.objects.get(pk=self.pk)
            
            # Se o produto for o mesmo, calcula a diferença
            if venda_antiga.produto == self.produto:
                # Exemplo: Vendeu 10, editou para 12. Diferença = 2. Tira mais 2 do estoque.
                diferenca = self.quantidade - venda_antiga.quantidade
                self.produto.quantidade -= diferenca
                
            # Se trocou o produto na edição
            else:
                # Devolve o estoque para o produto errado
                produto_antigo = venda_antiga.produto
                produto_antigo.quantidade += venda_antiga.quantidade
                produto_antigo.save()
                
                # Tira o estoque do produto certo
                self.produto.quantidade -= self.quantidade
                
        # Se for uma venda nova
        else:
            self.produto.quantidade -= self.quantidade

        super().save(*args, **kwargs)
        self.produto.save()

    # REGRA DE NEGÓCIO: ESTORNO DE VENDA (EXCLUIR)
    def delete(self, *args, **kwargs):
        # Devolve o produto para a prateleira
        self.produto.quantidade += self.quantidade
        self.produto.save()
        
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Venda #{self.id} - {self.produto.nome} para {self.cliente.nome}"