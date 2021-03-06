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


class Webhook(object):
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
        'chave': 'str',
        'criacao': 'str',
        'webhook_url': 'str'
    }

    attribute_map = {
        'chave': 'chave',
        'criacao': 'criacao',
        'webhook_url': 'webhookUrl'
    }

    def __init__(self, chave=None, criacao=None, webhook_url=None):  # noqa: E501
        """Webhook - a model defined in Swagger"""  # noqa: E501

        self._chave = None
        self._criacao = None
        self._webhook_url = None
        self.discriminator = None

        if chave is not None:
            self.chave = chave
        if criacao is not None:
            self.criacao = criacao
        self.webhook_url = webhook_url

    @property
    def chave(self):
        """Gets the chave of this Webhook.  # noqa: E501

        Chave de endereçamento do recebedor cadastrada na DICT  # noqa: E501

        :return: The chave of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._chave

    @chave.setter
    def chave(self, chave):
        """Sets the chave of this Webhook.

        Chave de endereçamento do recebedor cadastrada na DICT  # noqa: E501

        :param chave: The chave of this Webhook.  # noqa: E501
        :type: str
        """

        self._chave = chave

    @property
    def criacao(self):
        """Gets the criacao of this Webhook.  # noqa: E501

        Data e hora de criação do webhook em formato de acordo com RFC 3339  # noqa: E501

        :return: The criacao of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._criacao

    @criacao.setter
    def criacao(self, criacao):
        """Sets the criacao of this Webhook.

        Data e hora de criação do webhook em formato de acordo com RFC 3339  # noqa: E501

        :param criacao: The criacao of this Webhook.  # noqa: E501
        :type: str
        """

        self._criacao = criacao

    @property
    def webhook_url(self):
        """Gets the webhook_url of this Webhook.  # noqa: E501

        URL para chamada webhook de aviso de recebimento pix  # noqa: E501

        :return: The webhook_url of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._webhook_url

    @webhook_url.setter
    def webhook_url(self, webhook_url):
        """Sets the webhook_url of this Webhook.

        URL para chamada webhook de aviso de recebimento pix  # noqa: E501

        :param webhook_url: The webhook_url of this Webhook.  # noqa: E501
        :type: str
        """
        if webhook_url is None:
            raise ValueError("Invalid value for `webhook_url`, must not be `None`")  # noqa: E501

        self._webhook_url = webhook_url

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
        if issubclass(Webhook, dict):
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
        if not isinstance(other, Webhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
