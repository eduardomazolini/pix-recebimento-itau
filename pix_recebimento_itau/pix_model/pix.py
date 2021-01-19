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


class Pix(object):
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
        'horario': 'datetime',
        'devolucoes': 'list[PixsDevolucoes]',
        'pagador': 'PixsPagador',
        'valor': 'str',
        'txid': 'str',
        'info_pagador': 'str',
        'end_to_end_id': 'str'
    }

    attribute_map = {
        'horario': 'horario',
        'devolucoes': 'devolucoes',
        'pagador': 'pagador',
        'valor': 'valor',
        'txid': 'txid',
        'info_pagador': 'infoPagador',
        'end_to_end_id': 'endToEndId'
    }

    def __init__(self, horario=None, devolucoes=None, pagador=None, valor=None, txid=None, info_pagador=None, end_to_end_id=None):  # noqa: E501
        """Pix - a model defined in Swagger"""  # noqa: E501

        self._horario = None
        self._devolucoes = None
        self._pagador = None
        self._valor = None
        self._txid = None
        self._info_pagador = None
        self._end_to_end_id = None
        self.discriminator = None

        self.horario = horario
        if devolucoes is not None:
            self.devolucoes = devolucoes
        if pagador is not None:
            self.pagador = pagador
        self.valor = valor
        if txid is not None:
            self.txid = txid
        if info_pagador is not None:
            self.info_pagador = info_pagador
        self.end_to_end_id = end_to_end_id

    @property
    def horario(self):
        """Gets the horario of this Pix.  # noqa: E501

        Horário do pagamento.  # noqa: E501

        :return: The horario of this Pix.  # noqa: E501
        :rtype: datetime
        """
        return self._horario

    @horario.setter
    def horario(self, horario):
        """Sets the horario of this Pix.

        Horário do pagamento.  # noqa: E501

        :param horario: The horario of this Pix.  # noqa: E501
        :type: datetime
        """
        if horario is None:
            raise ValueError("Invalid value for `horario`, must not be `None`")  # noqa: E501

        self._horario = horario

    @property
    def devolucoes(self):
        """Gets the devolucoes of this Pix.  # noqa: E501

        Devolucoes registradas no documento  # noqa: E501

        :return: The devolucoes of this Pix.  # noqa: E501
        :rtype: list[PixsDevolucoes]
        """
        return self._devolucoes

    @devolucoes.setter
    def devolucoes(self, devolucoes):
        """Sets the devolucoes of this Pix.

        Devolucoes registradas no documento  # noqa: E501

        :param devolucoes: The devolucoes of this Pix.  # noqa: E501
        :type: list[PixsDevolucoes]
        """

        self._devolucoes = devolucoes

    @property
    def pagador(self):
        """Gets the pagador of this Pix.  # noqa: E501


        :return: The pagador of this Pix.  # noqa: E501
        :rtype: PixsPagador
        """
        return self._pagador

    @pagador.setter
    def pagador(self, pagador):
        """Sets the pagador of this Pix.


        :param pagador: The pagador of this Pix.  # noqa: E501
        :type: PixsPagador
        """

        self._pagador = pagador

    @property
    def valor(self):
        """Gets the valor of this Pix.  # noqa: E501

        Valor do pagamento.  # noqa: E501

        :return: The valor of this Pix.  # noqa: E501
        :rtype: str
        """
        return self._valor

    @valor.setter
    def valor(self, valor):
        """Sets the valor of this Pix.

        Valor do pagamento.  # noqa: E501

        :param valor: The valor of this Pix.  # noqa: E501
        :type: str
        """
        if valor is None:
            raise ValueError("Invalid value for `valor`, must not be `None`")  # noqa: E501

        self._valor = valor

    @property
    def txid(self):
        """Gets the txid of this Pix.  # noqa: E501

        ID de identificação do documento entre os bancos e o cliente emissor.O campo txid é obrigatório e determina o identificador da transação.O objetivo desse campo é ser um elemento que possibilite a conciliação de pagamentos. O txid é criado exclusivamente pelo usuário recebedor e está sob sua responsabilidade. Deve ser único por CNPJ do recebedor. Apesar de possuir o tamanho de 35 posições (PAC008), para QR Code Estático o tamanho máximo permitido é de 25 posições (limitação EMV). No caso do QR Code dinâmico o campo deve possuir de 26 posição até 35 posições. Os caracteres permitidos no contexto do Pix para o campo txId são:Letras minúsculas, de ‘a’ a ‘z’, Letras maiúsculas, de ‘A’ a ‘Z’, Dígitos decimais, de ‘0’ a ‘9’  # noqa: E501

        :return: The txid of this Pix.  # noqa: E501
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this Pix.

        ID de identificação do documento entre os bancos e o cliente emissor.O campo txid é obrigatório e determina o identificador da transação.O objetivo desse campo é ser um elemento que possibilite a conciliação de pagamentos. O txid é criado exclusivamente pelo usuário recebedor e está sob sua responsabilidade. Deve ser único por CNPJ do recebedor. Apesar de possuir o tamanho de 35 posições (PAC008), para QR Code Estático o tamanho máximo permitido é de 25 posições (limitação EMV). No caso do QR Code dinâmico o campo deve possuir de 26 posição até 35 posições. Os caracteres permitidos no contexto do Pix para o campo txId são:Letras minúsculas, de ‘a’ a ‘z’, Letras maiúsculas, de ‘A’ a ‘Z’, Dígitos decimais, de ‘0’ a ‘9’  # noqa: E501

        :param txid: The txid of this Pix.  # noqa: E501
        :type: str
        """

        self._txid = txid

    @property
    def info_pagador(self):
        """Gets the info_pagador of this Pix.  # noqa: E501

        Informação livre do pagador.  # noqa: E501

        :return: The info_pagador of this Pix.  # noqa: E501
        :rtype: str
        """
        return self._info_pagador

    @info_pagador.setter
    def info_pagador(self, info_pagador):
        """Sets the info_pagador of this Pix.

        Informação livre do pagador.  # noqa: E501

        :param info_pagador: The info_pagador of this Pix.  # noqa: E501
        :type: str
        """

        self._info_pagador = info_pagador

    @property
    def end_to_end_id(self):
        """Gets the end_to_end_id of this Pix.  # noqa: E501

        Id fim a fim da transação.Esse campo é o 'id do pagamento'. Transita nas mensagens de recebimento dos QR Codes e transferências.  # noqa: E501

        :return: The end_to_end_id of this Pix.  # noqa: E501
        :rtype: str
        """
        return self._end_to_end_id

    @end_to_end_id.setter
    def end_to_end_id(self, end_to_end_id):
        """Sets the end_to_end_id of this Pix.

        Id fim a fim da transação.Esse campo é o 'id do pagamento'. Transita nas mensagens de recebimento dos QR Codes e transferências.  # noqa: E501

        :param end_to_end_id: The end_to_end_id of this Pix.  # noqa: E501
        :type: str
        """
        if end_to_end_id is None:
            raise ValueError("Invalid value for `end_to_end_id`, must not be `None`")  # noqa: E501

        self._end_to_end_id = end_to_end_id

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
        if issubclass(Pix, dict):
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
        if not isinstance(other, Pix):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other