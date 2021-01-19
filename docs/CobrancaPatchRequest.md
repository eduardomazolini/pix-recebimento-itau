# CobrancaPatchRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devedor** | [**CobrancasDevedor**](CobrancasDevedor.md) |  | [optional]
**valor** | [**CobrancasValor**](CobrancasValor.md) |  | [optional]
**calendario** | [**CobrancaPutRequestCalendario**](CobrancaPutRequestCalendario.md) |  | [optional]
**info_adicionais** | [**list[CobrancasInfoAdicionais]**](CobrancasInfoAdicionais.md) | Cada respectiva informação adicional contida na lista (nome e valor) deve ser apresentada ao pagador | [optional]
**solicitacao_pagador** | **str** | O campo solicitacaoPagador, determina um texto a ser apresentado ao pagador para que ele possa digitar uma informação correlata, em formato livre, a ser enviada ao recebedor | [optional]
**status** | **str** | Status da Cobrança | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
