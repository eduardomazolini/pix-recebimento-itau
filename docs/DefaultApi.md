# pix_recebimento_itau.DefaultApi

All URIs are relative to *<https://sandbox.mbi.cloud.ihf/sandbox/pix_recebimentos/v1>*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_webhookchave**](DefaultApi.md#d_elete_webhookchave) | **DELETE** /webhook/{chave} |
[**g_et_cob**](DefaultApi.md#g_et_cob) | **GET** /cob |
[**g_et_cobtxid**](DefaultApi.md#g_et_cobtxid) | **GET** /cob/{txid} |
[**g_et_cobtxidqrcode**](DefaultApi.md#g_et_cobtxidqrcode) | **GET** /cob/{txid}/qrcode |
[**g_et_pix**](DefaultApi.md#g_et_pix) | **GET** /pix |
[**g_et_pixe2eid**](DefaultApi.md#g_et_pixe2eid) | **GET** /pix/{e2eid} |
[**g_et_pixe2eiddevolucaoid**](DefaultApi.md#g_et_pixe2eiddevolucaoid) | **GET** /pix/{e2eid}/devolucao/{id} |
[**g_et_webhook**](DefaultApi.md#g_et_webhook) | **GET** /webhook |
[**g_et_webhookchave**](DefaultApi.md#g_et_webhookchave) | **GET** /webhook/{chave} |
[**p_atch_cobtxid**](DefaultApi.md#p_atch_cobtxid) | **PATCH** /cob/{txid} |
[**p_ut_cobtxid**](DefaultApi.md#p_ut_cobtxid) | **PUT** /cob/{txid} |
[**p_ut_pixe2eiddevolucaoid**](DefaultApi.md#p_ut_pixe2eiddevolucaoid) | **PUT** /pix/{e2eid}/devolucao/{id} |
[**p_ut_webhookchave**](DefaultApi.md#p_ut_webhookchave) | **PUT** /webhook/{chave} |

# **d_elete_webhookchave**

> d_elete_webhookchave(chave, x_correlation_id=x_correlation_id)

Operação responsável por deletar webhook para aviso de recebimentos pix por chave

### Example

```python
from __future__ import print_function
import time
import pix_recebimento_itau
from pix_recebimento_itau.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuthAccessCode
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: OAuthImplicit
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = pix_recebimento_itau.DefaultApi(pix_recebimento_itau.ApiClient(configuration))
chave = 'chave_example' # str | Chave de endereçamento do recebedor
x_correlation_id = 'x_correlation_id_example' # str | Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail (optional)

try:
    api_instance.d_elete_webhookchave(chave, x_correlation_id=x_correlation_id)
except ApiException as e:
    print("Exception when calling DefaultApi->d_elete_webhookchave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chave** | **str**| Chave de endereçamento do recebedor |
 **x_correlation_id** | **str**| Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail | [optional]

### Return type

void (empty response body)

### Authorization

[OAuthAccessCode](../README.md#OAuthAccessCode), [OAuthImplicit](../README.md#OAuthImplicit)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_cob**

> Cobrancas g_et_cob(inicio, fim, cpf=cpf, cnpj=cnpj, status=status, paginacao_pagina_atual=paginacao_pagina_atual, paginacao_itens_por_pagina=paginacao_itens_por_pagina, x_correlation_id=x_correlation_id)

Operação responsável por recuperar os dados de documentos de acordo com os filtros enviados

### Example

```python
from __future__ import print_function
import time
import pix_recebimento_itau
from pix_recebimento_itau.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuthAccessCode
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: OAuthImplicit
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = pix_recebimento_itau.DefaultApi(pix_recebimento_itau.ApiClient(configuration))
inicio = 'inicio_example' # str | Data início da criação da cobrança, no formato '2020-06-01T09:00'
fim = 'fim_example' # str | Data fim da criação da Cobrança, no formato '2020-06-01T09:00'
cpf = 'cpf_example' # str | CPF do pagador cadastrado na cobrança. (optional)
cnpj = 'cnpj_example' # str | CNPJ do pagador cadastrado na cobrança. (optional)
status = 'status_example' # str | Filtro pelo status da cobrança. Pode ser ATIVA, CONCLUIDA, REMOVIDA_PELO_PSP OU REMOVIDA_PELO_USUARIO_RECEBEDOR (optional)
paginacao_pagina_atual = 'paginacao_pagina_atual_example' # str | Numero da Página que deseja realizar o acesso, valor considerado por default 0. (optional)
paginacao_itens_por_pagina = 'paginacao_itens_por_pagina_example' # str | Quantidade de ocorrência retornadas por pagina, valor por default 100. (optional)
x_correlation_id = 'x_correlation_id_example' # str | Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail (optional)

try:
    api_response = api_instance.g_et_cob(inicio, fim, cpf=cpf, cnpj=cnpj, status=status, paginacao_pagina_atual=paginacao_pagina_atual, paginacao_itens_por_pagina=paginacao_itens_por_pagina, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->g_et_cob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inicio** | **str**| Data início da criação da cobrança, no formato &#39;2020-06-01T09:00&#39; |
 **fim** | **str**| Data fim da criação da Cobrança, no formato &#39;2020-06-01T09:00&#39; |
 **cpf** | **str**| CPF do pagador cadastrado na cobrança. | [optional]
 **cnpj** | **str**| CNPJ do pagador cadastrado na cobrança. | [optional]
 **status** | **str**| Filtro pelo status da cobrança. Pode ser ATIVA, CONCLUIDA, REMOVIDA_PELO_PSP OU REMOVIDA_PELO_USUARIO_RECEBEDOR | [optional]
 **paginacao_pagina_atual** | **str**| Numero da Página que deseja realizar o acesso, valor considerado por default 0. | [optional]
 **paginacao_itens_por_pagina** | **str**| Quantidade de ocorrência retornadas por pagina, valor por default 100. | [optional]
 **x_correlation_id** | **str**| Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail | [optional]

### Return type

[**Cobrancas**](Cobrancas.md)

### Authorization

[OAuthAccessCode](../README.md#OAuthAccessCode), [OAuthImplicit](../README.md#OAuthImplicit)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_cobtxid**

> Cobranca g_et_cobtxid(txid, revisao=revisao, x_correlation_id=x_correlation_id)

Operação responsável por recuperar os dados do documento pelo id transacional

### Example

```python
from __future__ import print_function
import time
import pix_recebimento_itau
from pix_recebimento_itau.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuthAccessCode
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: OAuthImplicit
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = pix_recebimento_itau.DefaultApi(pix_recebimento_itau.ApiClient(configuration))
txid = 'txid_example' # str | Txid a ser consultado.
revisao = 'revisao_example' # str | Id de transaçao do documento, utilizado para a sua identificação no banco central (optional)
x_correlation_id = 'x_correlation_id_example' # str | Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail (optional)

try:
    api_response = api_instance.g_et_cobtxid(txid, revisao=revisao, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->g_et_cobtxid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Txid a ser consultado. |
 **revisao** | **str**| Id de transaçao do documento, utilizado para a sua identificação no banco central | [optional]
 **x_correlation_id** | **str**| Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail | [optional]

### Return type

[**Cobranca**](Cobranca.md)

### Authorization

[OAuthAccessCode](../README.md#OAuthAccessCode), [OAuthImplicit](../README.md#OAuthImplicit)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_cobtxidqrcode**

> Qrcode g_et_cobtxidqrcode(txid, x_correlation_id=x_correlation_id)

Operação responsável por recuperar os dados do documento

### Example

```python
from __future__ import print_function
import time
import pix_recebimento_itau
from pix_recebimento_itau.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuthAccessCode
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: OAuthImplicit
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = pix_recebimento_itau.DefaultApi(pix_recebimento_itau.ApiClient(configuration))
txid = 'txid_example' # str | Txid a ser consultado.
x_correlation_id = 'x_correlation_id_example' # str | Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail (optional)

try:
    api_response = api_instance.g_et_cobtxidqrcode(txid, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->g_et_cobtxidqrcode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Txid a ser consultado. |
 **x_correlation_id** | **str**| Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail | [optional]

### Return type

[**Qrcode**](Qrcode.md)

### Authorization

[OAuthAccessCode](../README.md#OAuthAccessCode), [OAuthImplicit](../README.md#OAuthImplicit)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_pix**

> Pixs g_et_pix(inicio, fim, txid=txid, cpf=cpf, cnpj=cnpj, paginacao_pagina_atual=paginacao_pagina_atual, paginacao_itens_por_pagina=paginacao_itens_por_pagina, x_correlation_id=x_correlation_id)

Operação responsável por recuperar os dados de documentos de acordo com os filtros enviados

### Example

```python
from __future__ import print_function
import time
import pix_recebimento_itau
from pix_recebimento_itau.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuthAccessCode
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: OAuthImplicit
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = pix_recebimento_itau.DefaultApi(pix_recebimento_itau.ApiClient(configuration))
inicio = 'inicio_example' # str | Data início da criação da cobrança, no formato '2020-06-01T09:00'
fim = 'fim_example' # str | Data fim da criação da Cobrança, no formato '2020-06-01T09:00'
txid = 'txid_example' # str | ID de identificação do documento entre os bancos e o cliente emissor. O campo txid é obrigatório e determina o identificador da transação.O objetivo desse campo é ser um elemento que possibilite a conciliação de pagamentos. O txid é criado exclusivamente pelo usuário recebedor e está sob sua responsabilidade. Deve ser único por CNPJ do recebedor. Apesar de possuir o tamanho de 35 posições (PAC008), para QR Code Estático o tamanho máximo permitido é de 25 posições (limitação EMV). No caso do QR Code dinâmico o campo deve possuir de 26 posição até 35 posições. Os caracteres permitidos no contexto do Pix para o campo txId são:Letras minúsculas, de ‘a’ a ‘z’, Letras maiúsculas, de ‘A’ a ‘Z’, Dígitos decimais, de ‘0’ a ‘9’ (optional)
cpf = 'cpf_example' # str | CPF do pagador cadastrado na cobrança (optional)
cnpj = 'cnpj_example' # str | CNPJ do pagador cadastrado na cobrança. (optional)
paginacao_pagina_atual = 'paginacao_pagina_atual_example' # str | Numero da Página que deseja realizar o acesso, valor considerado por default 0. (optional)
paginacao_itens_por_pagina = 'paginacao_itens_por_pagina_example' # str | Quantidade de ocorrência retornadas por pagina, valor por default 100. (optional)
x_correlation_id = 'x_correlation_id_example' # str | Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail (optional)

try:
    api_response = api_instance.g_et_pix(inicio, fim, txid=txid, cpf=cpf, cnpj=cnpj, paginacao_pagina_atual=paginacao_pagina_atual, paginacao_itens_por_pagina=paginacao_itens_por_pagina, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->g_et_pix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inicio** | **str**| Data início da criação da cobrança, no formato &#39;2020-06-01T09:00&#39; |
 **fim** | **str**| Data fim da criação da Cobrança, no formato &#39;2020-06-01T09:00&#39; |
 **txid** | **str**| ID de identificação do documento entre os bancos e o cliente emissor. O campo txid é obrigatório e determina o identificador da transação.O objetivo desse campo é ser um elemento que possibilite a conciliação de pagamentos. O txid é criado exclusivamente pelo usuário recebedor e está sob sua responsabilidade. Deve ser único por CNPJ do recebedor. Apesar de possuir o tamanho de 35 posições (PAC008), para QR Code Estático o tamanho máximo permitido é de 25 posições (limitação EMV). No caso do QR Code dinâmico o campo deve possuir de 26 posição até 35 posições. Os caracteres permitidos no contexto do Pix para o campo txId são:Letras minúsculas, de ‘a’ a ‘z’, Letras maiúsculas, de ‘A’ a ‘Z’, Dígitos decimais, de ‘0’ a ‘9’ | [optional]
 **cpf** | **str**| CPF do pagador cadastrado na cobrança | [optional]
 **cnpj** | **str**| CNPJ do pagador cadastrado na cobrança. | [optional]
 **paginacao_pagina_atual** | **str**| Numero da Página que deseja realizar o acesso, valor considerado por default 0. | [optional]
 **paginacao_itens_por_pagina** | **str**| Quantidade de ocorrência retornadas por pagina, valor por default 100. | [optional]
 **x_correlation_id** | **str**| Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail | [optional]

### Return type

[**Pixs**](Pixs.md)

### Authorization

[OAuthAccessCode](../README.md#OAuthAccessCode), [OAuthImplicit](../README.md#OAuthImplicit)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_pixe2eid**

> Pix g_et_pixe2eid(e2eid, x_correlation_id=x_correlation_id)

Operação responsável por recuperar os dados do documento pelo id transacional

### Example

```python
from __future__ import print_function
import time
import pix_recebimento_itau
from pix_recebimento_itau.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuthAccessCode
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: OAuthImplicit
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = pix_recebimento_itau.DefaultApi(pix_recebimento_itau.ApiClient(configuration))
e2eid = 'e2eid_example' # str | Id fim a fim da transação.
x_correlation_id = 'x_correlation_id_example' # str | Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail (optional)

try:
    api_response = api_instance.g_et_pixe2eid(e2eid, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->g_et_pixe2eid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **e2eid** | **str**| Id fim a fim da transação. |
 **x_correlation_id** | **str**| Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail | [optional]

### Return type

[**Pix**](Pix.md)

### Authorization

[OAuthAccessCode](../README.md#OAuthAccessCode), [OAuthImplicit](../README.md#OAuthImplicit)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_pixe2eiddevolucaoid**

> DevolucaoPix g_et_pixe2eiddevolucaoid(e2eid, id, x_correlation_id=x_correlation_id)

Operação responsavel por resgatar um pagamento específico para o PIX.

### Example

```python
from __future__ import print_function
import time
import pix_recebimento_itau
from pix_recebimento_itau.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuthAccessCode
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: OAuthImplicit
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = pix_recebimento_itau.DefaultApi(pix_recebimento_itau.ApiClient(configuration))
e2eid = 'e2eid_example' # str | Id fim a fim da transação.
id = 'id_example' # str | id da devolução
x_correlation_id = 'x_correlation_id_example' # str | Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail (optional)

try:
    api_response = api_instance.g_et_pixe2eiddevolucaoid(e2eid, id, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->g_et_pixe2eiddevolucaoid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **e2eid** | **str**| Id fim a fim da transação. |
 **id** | **str**| id da devolução |
 **x_correlation_id** | **str**| Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail | [optional]

### Return type

[**DevolucaoPix**](DevolucaoPix.md)

### Authorization

[OAuthAccessCode](../README.md#OAuthAccessCode), [OAuthImplicit](../README.md#OAuthImplicit)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_webhook**

> Webhooks g_et_webhook(inicio, fim, paginacao_pagina_atual=paginacao_pagina_atual, paginacao_itens_por_pagina=paginacao_itens_por_pagina, x_correlation_id=x_correlation_id, status_code=status_code)

Operação responsável por resgatar webhooks de aviso de recebimentos pix para um parceiro

### Example

```python
from __future__ import print_function
import time
import pix_recebimento_itau
from pix_recebimento_itau.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuthAccessCode
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: OAuthImplicit
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = pix_recebimento_itau.DefaultApi(pix_recebimento_itau.ApiClient(configuration))
inicio = 'inicio_example' # str | Data de inicio da pesquisa de webhooks, no formato de acordo com RFC3339
fim = 'fim_example' # str | Data fim da pesquisa de webhooks, no formato de acordo com RFC3339
paginacao_pagina_atual = 'paginacao_pagina_atual_example' # str | Numero da Página que deseja realizar o acesso, valor considerado por default 0 (optional)
paginacao_itens_por_pagina = 'paginacao_itens_por_pagina_example' # str | Quantidade de ocorrência retornadas por pagina, valor por default 100 (optional)
x_correlation_id = 'x_correlation_id_example' # str | Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail (optional)
status_code = 'status_code_example' # str | Define Status Code Sandbox (optional)

try:
    api_response = api_instance.g_et_webhook(inicio, fim, paginacao_pagina_atual=paginacao_pagina_atual, paginacao_itens_por_pagina=paginacao_itens_por_pagina, x_correlation_id=x_correlation_id, status_code=status_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->g_et_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inicio** | **str**| Data de inicio da pesquisa de webhooks, no formato de acordo com RFC3339 |
 **fim** | **str**| Data fim da pesquisa de webhooks, no formato de acordo com RFC3339 |
 **paginacao_pagina_atual** | **str**| Numero da Página que deseja realizar o acesso, valor considerado por default 0 | [optional]
 **paginacao_itens_por_pagina** | **str**| Quantidade de ocorrência retornadas por pagina, valor por default 100 | [optional]
 **x_correlation_id** | **str**| Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail | [optional]
 **status_code** | **str**| Define Status Code Sandbox | [optional]

### Return type

[**Webhooks**](Webhooks.md)

### Authorization

[OAuthAccessCode](../README.md#OAuthAccessCode), [OAuthImplicit](../README.md#OAuthImplicit)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_webhookchave**

> Webhook g_et_webhookchave(chave, x_correlation_id=x_correlation_id)

Operação responsável por resgatar webhook de aviso de recebimentos pix por chave

### Example

```python
from __future__ import print_function
import time
import pix_recebimento_itau
from pix_recebimento_itau.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuthAccessCode
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: OAuthImplicit
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = pix_recebimento_itau.DefaultApi(pix_recebimento_itau.ApiClient(configuration))
chave = 'chave_example' # str | Chave de endereçamento do recebedor
x_correlation_id = 'x_correlation_id_example' # str | Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail (optional)

try:
    api_response = api_instance.g_et_webhookchave(chave, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->g_et_webhookchave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chave** | **str**| Chave de endereçamento do recebedor |
 **x_correlation_id** | **str**| Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail | [optional]

### Return type

[**Webhook**](Webhook.md)

### Authorization

[OAuthAccessCode](../README.md#OAuthAccessCode), [OAuthImplicit](../README.md#OAuthImplicit)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_atch_cobtxid**

> CobrancaPatchResponse p_atch_cobtxid(txid, body=body, x_correlation_id=x_correlation_id)

Operação responsável por revisar uma cobranca

### Example

```python
from __future__ import print_function
import time
import pix_recebimento_itau
from pix_recebimento_itau.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuthAccessCode
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: OAuthImplicit
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = pix_recebimento_itau.DefaultApi(pix_recebimento_itau.ApiClient(configuration))
txid = 'txid_example' # str | Txid a ser consultado.
body = pix_recebimento_itau.CobrancaPatchRequest() # CobrancaPatchRequest | Objeto cobranca a ser revisado (optional)
x_correlation_id = 'x_correlation_id_example' # str | Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail (optional)

try:
    api_response = api_instance.p_atch_cobtxid(txid, body=body, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->p_atch_cobtxid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Txid a ser consultado. |
 **body** | [**CobrancaPatchRequest**](CobrancaPatchRequest.md)| Objeto cobranca a ser revisado | [optional]
 **x_correlation_id** | **str**| Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail | [optional]

### Return type

[**CobrancaPatchResponse**](CobrancaPatchResponse.md)

### Authorization

[OAuthAccessCode](../README.md#OAuthAccessCode), [OAuthImplicit](../README.md#OAuthImplicit)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_cobtxid**

> CobrancaPutResponse p_ut_cobtxid(txid, body=body, x_correlation_id=x_correlation_id)

Operação responsável por incluir uma nova cobranca

### Example

```python
from __future__ import print_function
import time
import pix_recebimento_itau
from pix_recebimento_itau.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuthAccessCode
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: OAuthImplicit
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = pix_recebimento_itau.DefaultApi(pix_recebimento_itau.ApiClient(configuration))
txid = 'txid_example' # str | Txid a ser consultado.
body = pix_recebimento_itau.CobrancaPutRequest() # CobrancaPutRequest | Objeto cobranca a ser criado (optional)
x_correlation_id = 'x_correlation_id_example' # str | Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail (optional)

try:
    api_response = api_instance.p_ut_cobtxid(txid, body=body, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->p_ut_cobtxid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Txid a ser consultado. |
 **body** | [**CobrancaPutRequest**](CobrancaPutRequest.md)| Objeto cobranca a ser criado | [optional]
 **x_correlation_id** | **str**| Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail | [optional]

### Return type

[**CobrancaPutResponse**](CobrancaPutResponse.md)

### Authorization

[OAuthAccessCode](../README.md#OAuthAccessCode), [OAuthImplicit](../README.md#OAuthImplicit)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_pixe2eiddevolucaoid**

> DevolucaoPutResponse p_ut_pixe2eiddevolucaoid(e2eid, id, body=body, x_correlation_id=x_correlation_id)

Operação responsável por solicitar um nova devolução, por meio do e2eid e do ID da devolução

### Example

```python
from __future__ import print_function
import time
import pix_recebimento_itau
from pix_recebimento_itau.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuthAccessCode
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: OAuthImplicit
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = pix_recebimento_itau.DefaultApi(pix_recebimento_itau.ApiClient(configuration))
e2eid = 'e2eid_example' # str | Id fim a fim da transação.
id = 'id_example' # str | id da devolução
body = pix_recebimento_itau.DevolucaoPutRequest() # DevolucaoPutRequest | Objeto de devolução cobranca a ser solicitado (optional)
x_correlation_id = 'x_correlation_id_example' # str | Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail (optional)

try:
    api_response = api_instance.p_ut_pixe2eiddevolucaoid(e2eid, id, body=body, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->p_ut_pixe2eiddevolucaoid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **e2eid** | **str**| Id fim a fim da transação. |
 **id** | **str**| id da devolução |
 **body** | [**DevolucaoPutRequest**](DevolucaoPutRequest.md)| Objeto de devolução cobranca a ser solicitado | [optional]
 **x_correlation_id** | **str**| Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail | [optional]

### Return type

[**DevolucaoPutResponse**](DevolucaoPutResponse.md)

### Authorization

[OAuthAccessCode](../README.md#OAuthAccessCode), [OAuthImplicit](../README.md#OAuthImplicit)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ut_webhookchave**

> p_ut_webhookchave(chave, body=body, x_correlation_id=x_correlation_id)

Operação responsável por cadastrar webhook para aviso de recebimentos pix por chave

### Example

```python
from __future__ import print_function
import time
import pix_recebimento_itau
from pix_recebimento_itau.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuthAccessCode
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: OAuthImplicit
configuration = pix_recebimento_itau.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = pix_recebimento_itau.DefaultApi(pix_recebimento_itau.ApiClient(configuration))
chave = 'chave_example' # str | Chave de endereçamento do recebedor
body = pix_recebimento_itau.Webhook() # Webhook | Objeto de webhook a ser solicitado (optional)
x_correlation_id = 'x_correlation_id_example' # str | Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail (optional)

try:
    api_instance.p_ut_webhookchave(chave, body=body, x_correlation_id=x_correlation_id)
except ApiException as e:
    print("Exception when calling DefaultApi->p_ut_webhookchave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chave** | **str**| Chave de endereçamento do recebedor |
 **body** | [**Webhook**](Webhook.md)| Objeto de webhook a ser solicitado | [optional]
 **x_correlation_id** | **str**| Identificador de correlação que serve como um agrupar dentro da estrutura de audit trail | [optional]

### Return type

void (empty response body)

### Authorization

[OAuthAccessCode](../README.md#OAuthAccessCode), [OAuthImplicit](../README.md#OAuthImplicit)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
