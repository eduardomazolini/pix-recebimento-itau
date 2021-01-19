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


class DevolucaoPix(object):
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
        'horario': 'PixsHorario',
        'rtr_id': 'str',
        'valor': 'str',
        'id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'horario': 'horario',
        'rtr_id': 'rtrId',
        'valor': 'valor',
        'id': 'id',
        'status': 'status'
    }

    def __init__(self, horario=None, rtr_id=None, valor=None, id=None, status=None):  # noqa: E501
        """DevolucaoPix - a model defined in Swagger"""  # noqa: E501

        self._horario = None
        self._rtr_id = None
        self._valor = None
        self._id = None
        self._status = None
        self.discriminator = None

        self.horario = horario
        self.rtr_id = rtr_id
        self.valor = valor
        self.id = id
        self.status = status

    @property
    def horario(self):
        """Gets the horario of this DevolucaoPix.  # noqa: E501


        :return: The horario of this DevolucaoPix.  # noqa: E501
        :rtype: PixsHorario
        """
        return self._horario

    @horario.setter
    def horario(self, horario):
        """Sets the horario of this DevolucaoPix.


        :param horario: The horario of this DevolucaoPix.  # noqa: E501
        :type: PixsHorario
        """
        if horario is None:
            raise ValueError("Invalid value for `horario`, must not be `None`")  # noqa: E501

        self._horario = horario

    @property
    def rtr_id(self):
        """Gets the rtr_id of this DevolucaoPix.  # noqa: E501

        ReturnIdentification  # noqa: E501

        :return: The rtr_id of this DevolucaoPix.  # noqa: E501
        :rtype: str
        """
        return self._rtr_id

    @rtr_id.setter
    def rtr_id(self, rtr_id):
        """Sets the rtr_id of this DevolucaoPix.

        ReturnIdentification  # noqa: E501

        :param rtr_id: The rtr_id of this DevolucaoPix.  # noqa: E501
        :type: str
        """
        if rtr_id is None:
            raise ValueError("Invalid value for `rtr_id`, must not be `None`")  # noqa: E501

        self._rtr_id = rtr_id

    @property
    def valor(self):
        """Gets the valor of this DevolucaoPix.  # noqa: E501

        Valor da devolução  # noqa: E501

        :return: The valor of this DevolucaoPix.  # noqa: E501
        :rtype: str
        """
        return self._valor

    @valor.setter
    def valor(self, valor):
        """Sets the valor of this DevolucaoPix.

        Valor da devolução  # noqa: E501

        :param valor: The valor of this DevolucaoPix.  # noqa: E501
        :type: str
        """
        if valor is None:
            raise ValueError("Invalid value for `valor`, must not be `None`")  # noqa: E501

        self._valor = valor

    @property
    def id(self):
        """Gets the id of this DevolucaoPix.  # noqa: E501

        Id da devolução  # noqa: E501

        :return: The id of this DevolucaoPix.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DevolucaoPix.

        Id da devolução  # noqa: E501

        :param id: The id of this DevolucaoPix.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def status(self):
        """Gets the status of this DevolucaoPix.  # noqa: E501

        Status da Devolução. Pode ser: EM_PROCESSAMENTO, DEVOLVIDO ou NAO_REALIZADO  # noqa: E501

        :return: The status of this DevolucaoPix.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DevolucaoPix.

        Status da Devolução. Pode ser: EM_PROCESSAMENTO, DEVOLVIDO ou NAO_REALIZADO  # noqa: E501

        :param status: The status of this DevolucaoPix.  # noqa: E501
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
        if issubclass(DevolucaoPix, dict):
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
        if not isinstance(other, DevolucaoPix):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other