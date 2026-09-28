from django.db import models


class Endereco(models.Model):
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=150)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.logradouro} - {self.bairro}, {self.cidade}/{self.uf}"


class Estado(models.Model):

    UF_CHOICES = [
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    ]

    uf = models.CharField(
        max_length=2,
        unique=True,
        choices=UF_CHOICES
    )

    imagem = models.ImageField(
        upload_to="estados/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.get_uf_display()