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


class Cobrancas(object):
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
        'cobs': 'list[CobrancasCobs]',
        'parametros': 'CobrancasParametros'
    }

    attribute_map = {
        'cobs': 'cobs',
        'parametros': 'parametros'
    }

    def __init__(self, cobs=None, parametros=None):  # noqa: E501
        """Cobrancas - a model defined in Swagger"""  # noqa: E501

        self._cobs = None
        self._parametros = None
        self.discriminator = None

        self.cobs = cobs
        self.parametros = parametros

    @property
    def cobs(self):
        """Gets the cobs of this Cobrancas.  # noqa: E501

        Estrutura com informações referentes a cobranca do documento  # noqa: E501

        :return: The cobs of this Cobrancas.  # noqa: E501
        :rtype: list[CobrancasCobs]
        """
        return self._cobs

    @cobs.setter
    def cobs(self, cobs):
        """Sets the cobs of this Cobrancas.

        Estrutura com informações referentes a cobranca do documento  # noqa: E501

        :param cobs: The cobs of this Cobrancas.  # noqa: E501
        :type: list[CobrancasCobs]
        """
        if cobs is None:
            raise ValueError("Invalid value for `cobs`, must not be `None`")  # noqa: E501

        self._cobs = cobs

    @property
    def parametros(self):
        """Gets the parametros of this Cobrancas.  # noqa: E501


        :return: The parametros of this Cobrancas.  # noqa: E501
        :rtype: CobrancasParametros
        """
        return self._parametros

    @parametros.setter
    def parametros(self, parametros):
        """Sets the parametros of this Cobrancas.


        :param parametros: The parametros of this Cobrancas.  # noqa: E501
        :type: CobrancasParametros
        """
        if parametros is None:
            raise ValueError("Invalid value for `parametros`, must not be `None`")  # noqa: E501

        self._parametros = parametros

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
        if issubclass(Cobrancas, dict):
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
        if not isinstance(other, Cobrancas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
