"""
verifica_qualis.py — Helper pra consultar Qualis CAPES.

⚠️ A CAPES não disponibiliza API pública pra consulta automática do Qualis.
Esse script funciona como **guia interativo**: orienta o usuário no Sucupira.

Uso:
    python verifica_qualis.py --issn 1413-2478
    python verifica_qualis.py --titulo "Revista Brasileira de Educação"
"""

import argparse
import sys


SUCUPIRA_QUALIS_URL = (
    "https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/"
    "veiculoPublicacaoQualis/listaConsultaGeralPeriodicos.jsf"
)


def main():
    parser = argparse.ArgumentParser(
        description='Guia para consulta de Qualis CAPES no Sucupira.',
    )
    parser.add_argument('--issn', help='ISSN da revista (formato XXXX-XXXX)')
    parser.add_argument('--titulo', help='Título da revista (pode ser parcial)')
    parser.add_argument('--area', help='Área de avaliação CAPES (opcional)')

    args = parser.parse_args()

    if not (args.issn or args.titulo):
        parser.error('Informe --issn ou --titulo')

    print('=' * 70)
    print('🔍 Consulta Qualis CAPES')
    print('=' * 70)
    print()
    print('Não há API pública oficial pro Qualis. Consulta manual:')
    print()
    print(f'1. Acesse: {SUCUPIRA_QUALIS_URL}')
    print('2. No "Evento de Classificação", selecione: 2017-2020 (atual)')

    if args.area:
        print(f'3. No campo "Área de Avaliação", selecione: {args.area}')
    else:
        print('3. No campo "Área de Avaliação", selecione a área CAPES do trabalho')
        print('   (ex: Ciência da Computação, Educação, Saúde Coletiva, etc)')

    if args.issn:
        print(f'4. No campo "ISSN", digite: {args.issn}')
    elif args.titulo:
        print(f'4. No campo "Título", digite: {args.titulo}')

    print('5. Clique "Consultar"')
    print('6. O resultado mostra o estrato (A1, A2, A3, A4, B1, B2, B3, B4, C)')
    print()
    print('=' * 70)
    print('📊 Significado dos estratos')
    print('=' * 70)
    print()
    print('A1 ━━━ Excelência internacional (top 12.5% percentil)')
    print('A2 ━━━ Excelência (12.5%-25%)')
    print('A3 ━━━ Muito boa (25%-37.5%)')
    print('A4 ━━━ Boa (37.5%-50%)')
    print('B1 ━━━ Acima da média (50%-62.5%)')
    print('B2 ━━━ Média (62.5%-75%)')
    print('B3 ━━━ Abaixo da média (75%-87.5%)')
    print('B4 ━━━ Baixa (87.5%-100%)')
    print('C  ━━━ Sem mérito acadêmico (não recomendado)')
    print()
    print('💡 Dica: Mire em A1-B1 para currículo Lattes forte.')
    print('         Estrato C indica revista sem rigor; evite.')
    print()


if __name__ == '__main__':
    main()
