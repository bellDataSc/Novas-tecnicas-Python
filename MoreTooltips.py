# seleciona um ponto para o qual fornecer detalhes sob demanda

label = alt.selection_single(
    encodings=['x'], # limita a seleção ao valor do eixo x
    on='mouseover',  # seleciona nos eventos do mouseover
    nearest=True,    # seleciona o ponto de dados mais próximo do cursor
    empty='none'    # seleção vazia não inclui pontos de dados
)


# definir nosso gráfico de linha de base dos preços das ações

base = alt.Chart().mark_line().encode(
    alt.X('date:T'),
    alt.Y('price:Q', scale=alt.Scale(type='log')),
    alt.Color('symbol:N')
)

alt.layer(
    base, # gráfico de linhas de base
    
    # adiciona uma marca de regra para servir de guia
    alt.Chart().mark_rule(color='#aaa').encode(
        x='date:T'
    ).transform_filter(label),
    
    # adiciona marcas de círculo para pontos de tempo selecionados, oculta pontos não selecionados
    base.mark_circle().encode(
        opacity=alt.condition(label, alt.value(1), alt.value(0))
    ).add_selection(label),

    # adicione texto com traços brancos para fornecer um plano de fundo legível para rótulos
    base.mark_text(align='left', dx=5, dy=-5, stroke='white', strokeWidth=2).encode(
        text='price:Q'
    ).transform_filter(label),

    # adicione rótulos de texto para preços de ações
    base.mark_text(align='left', dx=5, dy=-5).encode(
        text='price:Q'
    ).transform_filter(label),
    
    data=stocks
).properties(
    width=500,
    height=400
)
