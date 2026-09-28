import csv
from pathlib import Path

from django.core.management.base import BaseCommand

from ceps.models import Endereco


class Command(BaseCommand):
    help = "Importa os CEPs do arquivo CSV para o banco de dados."

    def handle(self, *args, **kwargs):
        arquivo_csv = Path("dados/cep-20190602.csv")
        tamanho_lote = 5000

        if not arquivo_csv.exists():
            self.stdout.write(
                self.style.ERROR(
                    f"Arquivo não encontrado: {arquivo_csv}"
                )
            )
            return

        lote = []
        total_importado = 0

        with open(
            arquivo_csv,
            mode="r",
            encoding="utf-8-sig",
            newline=""
        ) as arquivo:

            leitor = csv.reader(arquivo)

            for linha in leitor:
                if len(linha) < 5:
                    continue

                uf = linha[0].strip()
                cidade = linha[1].strip()
                bairro = linha[2].strip()
                cep = linha[3].strip()
                logradouro = linha[4].strip()

                endereco = Endereco(
                    uf=uf,
                    cidade=cidade,
                    bairro=bairro,
                    cep=cep,
                    logradouro=logradouro,
                )

                lote.append(endereco)

                if len(lote) >= tamanho_lote:
                    Endereco.objects.bulk_create(lote)
                    total_importado += len(lote)
                    lote = []

                    self.stdout.write(
                        f"{total_importado} registros importados..."
                    )

        if lote:
            Endereco.objects.bulk_create(lote)
            total_importado += len(lote)

        self.stdout.write(
            self.style.SUCCESS(
                f"Importação concluída: {total_importado} registros."
            )
        )