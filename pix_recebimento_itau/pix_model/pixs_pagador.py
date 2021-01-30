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


class PixsPagador(object):
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
        'cpf': 'str',
        'nome': 'str',
        'cnpj': 'str'
    }

    attribute_map = {
        'cpf': 'cpf',
        'nome': 'nome',
        'cnpj': 'cnpj'
    }

    def __init__(self, cpf=None, nome=None, cnpj=None):  # noqa: E501
        """PixsPagador - a model defined in Swagger"""  # noqa: E501

        self._nome = None
        self._cpf = None
        self._cnpj = None
        self.discriminator = None

        self.nome = nome
        if cpf:
            self.cpf = cpf
        else:
            self.cnpj = cnpj

    @property
    def cpf(self):
        """Gets the cpf of this PixsPagador.  # noqa: E501

        Número do Documento Cadastro de Pessoa Física. (Apenas CPF, não enviar CNPJ)  # noqa: E501

        :return: The cpf of this PixsPagador.  # noqa: E501
        :rtype: str
        """
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        """Sets the cpf of this PixsPagador.

        Número do Documento Cadastro de Pessoa Física. (Apenas CPF, não enviar CNPJ)  # noqa: E501

        :param cpf: The cpf of this PixsPagador.  # noqa: E501
        :type: str
        """
        if cpf is None:
            raise ValueError("Invalid value for `cpf`, must not be `None`")  # noqa: E501

        self._cpf = cpf

    @property
    def nome(self):
        """Gets the nome of this PixsPagador.  # noqa: E501

        Nome do pagador da Cobrança. Necessário preencher o campo CNPJ ou o campo CPF.   # noqa: E501

        :return: The nome of this PixsPagador.  # noqa: E501
        :rtype: str
        """
        return self._nome

    @nome.setter
    def nome(self, nome):
        """Sets the nome of this PixsPagador.

        Nome do pagador da Cobrança. Necessário preencher o campo CNPJ ou o campo CPF.   # noqa: E501

        :param nome: The nome of this PixsPagador.  # noqa: E501
        :type: str
        """
        if nome is None:
            raise ValueError("Invalid value for `nome`, must not be `None`")  # noqa: E501

        self._nome = nome

    @property
    def cnpj(self):
        """Gets the cnpj of this PixsPagador.  # noqa: E501

        Número do Cadastro Nacional da Pessoa Jurídica. (Apenas CNPJ, não enviar CPF)  # noqa: E501

        :return: The cnpj of this PixsPagador.  # noqa: E501
        :rtype: str
        """
        return self._cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        """Sets the cnpj of this PixsPagador.

        Número do Cadastro Nacional da Pessoa Jurídica. (Apenas CNPJ, não enviar CPF)  # noqa: E501

        :param cnpj: The cnpj of this PixsPagador.  # noqa: E501
        :type: str
        """
        if cnpj is None:
            raise ValueError("Invalid value for `cnpj`, must not be `None`")  # noqa: E501

        self._cnpj = cnpj

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
        if issubclass(PixsPagador, dict):
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
        if not isinstance(other, PixsPagador):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
