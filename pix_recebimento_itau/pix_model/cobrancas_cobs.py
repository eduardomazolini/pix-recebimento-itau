# coding: utf-8

"""
    pix_recebimentos

    APis Pix Recebimentos para Clientes (regulatórias).   # noqa: E501

    OpenAPI spec version: 1.40.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CobrancasCobs(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'devedor': 'CobrancasDevedor',
        'valor': 'CobrancasValor',
        'chave': 'str',
        'calendario': 'CobrancasCalendario',
        'txid': 'str',
        'info_adicionais': 'list[CobrancasInfoAdicionais]',
        'location': 'str',
        'revisao': 'float',
        'solicitacao_pagador': 'str',
        'pix': 'list[PixsPix]',
        'status': 'str'
    }

    attribute_map = {
        'devedor': 'devedor',
        'valor': 'valor',
        'chave': 'chave',
        'calendario': 'calendario',
        'txid': 'txid',
        'info_adicionais': 'infoAdicionais',
        'location': 'location',
        'revisao': 'revisao',
        'solicitacao_pagador': 'solicitacaoPagador',
        'pix': 'pix',
        'status': 'status'
    }

    def __init__(self, devedor=None, valor=None, chave=None, calendario=None, txid=None, info_adicionais=None, location=None, revisao=None, solicitacao_pagador=None, pix=None, status=None):  # noqa: E501
        """CobrancasCobs - a model defined in Swagger"""  # noqa: E501

        self._devedor = None
        self._valor = None
        self._chave = None
        self._calendario = None
        self._txid = None
        self._info_adicionais = None
        self._location = None
        self._revisao = None
        self._solicitacao_pagador = None
        self._pix = None
        self._status = None
        self.discriminator = None

        if devedor is not None:
            self.devedor = devedor
        self.valor = valor
        self.chave = chave
        self.calendario = calendario
        self.txid = txid
        if info_adicionais is not None:
            self.info_adicionais = info_adicionais
        self.location = location
        self.revisao = revisao
        if solicitacao_pagador is not None:
            self.solicitacao_pagador = solicitacao_pagador
        if pix is not None:
            self.pix = pix
        self.status = status

    @property
    def devedor(self):
        """Gets the devedor of this CobrancasCobs.  # noqa: E501


        :return: The devedor of this CobrancasCobs.  # noqa: E501
        :rtype: CobrancasDevedor
        """
        return self._devedor

    @devedor.setter
    def devedor(self, devedor):
        """Sets the devedor of this CobrancasCobs.


        :param devedor: The devedor of this CobrancasCobs.  # noqa: E501
        :type: CobrancasDevedor
        """

        self._devedor = devedor

    @property
    def valor(self):
        """Gets the valor of this CobrancasCobs.  # noqa: E501


        :return: The valor of this CobrancasCobs.  # noqa: E501
        :rtype: CobrancasValor
        """
        return self._valor

    @valor.setter
    def valor(self, valor):
        """Sets the valor of this CobrancasCobs.


        :param valor: The valor of this CobrancasCobs.  # noqa: E501
        :type: CobrancasValor
        """
        if valor is None:
            raise ValueError("Invalid value for `valor`, must not be `None`")  # noqa: E501

        self._valor = valor

    @property
    def chave(self):
        """Gets the chave of this CobrancasCobs.  # noqa: E501

        Chave Pix do Sistema DICT - BACEN  # noqa: E501

        :return: The chave of this CobrancasCobs.  # noqa: E501
        :rtype: str
        """
        return self._chave

    @chave.setter
    def chave(self, chave):
        """Sets the chave of this CobrancasCobs.

        Chave Pix do Sistema DICT - BACEN  # noqa: E501

        :param chave: The chave of this CobrancasCobs.  # noqa: E501
        :type: str
        """
        if chave is None:
            raise ValueError("Invalid value for `chave`, must not be `None`")  # noqa: E501

        self._chave = chave

    @property
    def calendario(self):
        """Gets the calendario of this CobrancasCobs.  # noqa: E501


        :return: The calendario of this CobrancasCobs.  # noqa: E501
        :rtype: CobrancasCalendario
        """
        return self._calendario

    @calendario.setter
    def calendario(self, calendario):
        """Sets the calendario of this CobrancasCobs.


        :param calendario: The calendario of this CobrancasCobs.  # noqa: E501
        :type: CobrancasCalendario
        """
        if calendario is None:
            raise ValueError("Invalid value for `calendario`, must not be `None`")  # noqa: E501

        self._calendario = calendario

    @property
    def txid(self):
        """Gets the txid of this CobrancasCobs.  # noqa: E501

        ID de identificação do documento entre os bancos e o cliente emissor.O campo txid é obrigatório e determina o identificador da transação.O objetivo desse campo é ser um elemento que possibilite a conciliação de pagamentos. O txid é criado exclusivamente pelo usuário recebedor e está sob sua responsabilidade. Deve ser único por CNPJ do recebedor. Apesar de possuir o tamanho de 35 posições (PAC008), para QR Code Estático o tamanho máximo permitido é de 25 posições (limitação EMV). No caso do QR Code dinâmico o campo deve possuir de 26 posição até 35 posições. Os caracteres permitidos no contexto do Pix para o campo txId são:Letras minúsculas, de ‘a’ a ‘z’, Letras maiúsculas, de ‘A’ a ‘Z’, Dígitos decimais, de ‘0’ a ‘9’  # noqa: E501

        :return: The txid of this CobrancasCobs.  # noqa: E501
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this CobrancasCobs.

        ID de identificação do documento entre os bancos e o cliente emissor.O campo txid é obrigatório e determina o identificador da transação.O objetivo desse campo é ser um elemento que possibilite a conciliação de pagamentos. O txid é criado exclusivamente pelo usuário recebedor e está sob sua responsabilidade. Deve ser único por CNPJ do recebedor. Apesar de possuir o tamanho de 35 posições (PAC008), para QR Code Estático o tamanho máximo permitido é de 25 posições (limitação EMV). No caso do QR Code dinâmico o campo deve possuir de 26 posição até 35 posições. Os caracteres permitidos no contexto do Pix para o campo txId são:Letras minúsculas, de ‘a’ a ‘z’, Letras maiúsculas, de ‘A’ a ‘Z’, Dígitos decimais, de ‘0’ a ‘9’  # noqa: E501

        :param txid: The txid of this CobrancasCobs.  # noqa: E501
        :type: str
        """
        if txid is None:
            raise ValueError("Invalid value for `txid`, must not be `None`")  # noqa: E501

        self._txid = txid

    @property
    def info_adicionais(self):
        """Gets the info_adicionais of this CobrancasCobs.  # noqa: E501

        Cada respectiva informação adicional contida na lista (nome e valor) deve ser apresentada ao pagador  # noqa: E501

        :return: The info_adicionais of this CobrancasCobs.  # noqa: E501
        :rtype: list[CobrancasInfoAdicionais]
        """
        return self._info_adicionais

    @info_adicionais.setter
    def info_adicionais(self, info_adicionais):
        """Sets the info_adicionais of this CobrancasCobs.

        Cada respectiva informação adicional contida na lista (nome e valor) deve ser apresentada ao pagador  # noqa: E501

        :param info_adicionais: The info_adicionais of this CobrancasCobs.  # noqa: E501
        :type: list[CobrancasInfoAdicionais]
        """

        self._info_adicionais = info_adicionais

    @property
    def location(self):
        """Gets the location of this CobrancasCobs.  # noqa: E501

        URL com a Localização do Payload informado na criação da cobrança  # noqa: E501

        :return: The location of this CobrancasCobs.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this CobrancasCobs.

        URL com a Localização do Payload informado na criação da cobrança  # noqa: E501

        :param location: The location of this CobrancasCobs.  # noqa: E501
        :type: str
        """
        if location is None:
            print("Invalid value for `location`, must not be `None`")  # noqa: E501
            #raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def revisao(self):
        """Gets the revisao of this CobrancasCobs.  # noqa: E501

        Quantidade de revisões da cobrança  # noqa: E501

        :return: The revisao of this CobrancasCobs.  # noqa: E501
        :rtype: float
        """
        return self._revisao

    @revisao.setter
    def revisao(self, revisao):
        """Sets the revisao of this CobrancasCobs.

        Quantidade de revisões da cobrança  # noqa: E501

        :param revisao: The revisao of this CobrancasCobs.  # noqa: E501
        :type: float
        """
        if revisao is None:
            raise ValueError("Invalid value for `revisao`, must not be `None`")  # noqa: E501

        self._revisao = revisao

    @property
    def solicitacao_pagador(self):
        """Gets the solicitacao_pagador of this CobrancasCobs.  # noqa: E501

        O campo solicitacaoPagador, determina um texto a ser apresentado ao pagador para que ele possa digitar uma informação correlata, em formato livre, a ser enviada ao recebedor  # noqa: E501

        :return: The solicitacao_pagador of this CobrancasCobs.  # noqa: E501
        :rtype: str
        """
        return self._solicitacao_pagador

    @solicitacao_pagador.setter
    def solicitacao_pagador(self, solicitacao_pagador):
        """Sets the solicitacao_pagador of this CobrancasCobs.

        O campo solicitacaoPagador, determina um texto a ser apresentado ao pagador para que ele possa digitar uma informação correlata, em formato livre, a ser enviada ao recebedor  # noqa: E501

        :param solicitacao_pagador: The solicitacao_pagador of this CobrancasCobs.  # noqa: E501
        :type: str
        """

        self._solicitacao_pagador = solicitacao_pagador

    @property
    def pix(self):
        """Gets the pix of this CobrancasCobs.  # noqa: E501

        Lista de Pix recebidos  # noqa: E501

        :return: The pix of this CobrancasCobs.  # noqa: E501
        :rtype: list[PixsPix]
        """
        return self._pix

    @pix.setter
    def pix(self, pix):
        """Sets the pix of this CobrancasCobs.

        Lista de Pix recebidos  # noqa: E501

        :param pix: The pix of this CobrancasCobs.  # noqa: E501
        :type: list[PixsPix]
        """

        self._pix = pix

    @property
    def status(self):
        """Gets the status of this CobrancasCobs.  # noqa: E501

        Status da Cobrança. Pode ser: ATIVA, CONCLUIDA, REMOVIDA_PELO_USUARIO_RECEBEDOR, REMOVIDA_PELO_PSP  # noqa: E501

        :return: The status of this CobrancasCobs.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CobrancasCobs.

        Status da Cobrança. Pode ser: ATIVA, CONCLUIDA, REMOVIDA_PELO_USUARIO_RECEBEDOR, REMOVIDA_PELO_PSP  # noqa: E501

        :param status: The status of this CobrancasCobs.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CobrancasCobs, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CobrancasCobs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
