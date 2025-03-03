# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iot/broker/v1/broker_data_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/iot/broker/v1/broker_data_service.proto',
  package='yandex.cloud.iot.broker.v1',
  syntax='proto3',
  serialized_options=b'\n\036yandex.cloud.api.iot.broker.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/iot/broker/v1;broker',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n4yandex/cloud/iot/broker/v1/broker_data_service.proto\x12\x1ayandex.cloud.iot.broker.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1dyandex/cloud/validation.proto\"v\n\x18PublishBrokerDataRequest\x12\x1f\n\tbroker_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\x05topic\x18\x02 \x01(\tB\x0e\xe8\xc7\x31\x01\x8a\xc8\x31\x06<=1024\x12\x1a\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x42\x0c\x8a\xc8\x31\x08<=262144\"\x1b\n\x19PublishBrokerDataResponse2\xc3\x01\n\x11\x42rokerDataService\x12\xad\x01\n\x07Publish\x12\x34.yandex.cloud.iot.broker.v1.PublishBrokerDataRequest\x1a\x35.yandex.cloud.iot.broker.v1.PublishBrokerDataResponse\"5\x82\xd3\xe4\x93\x02/\"*/iot-broker/v1/brokers/{broker_id}/publish:\x01*Bg\n\x1eyandex.cloud.api.iot.broker.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/iot/broker/v1;brokerb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_PUBLISHBROKERDATAREQUEST = _descriptor.Descriptor(
  name='PublishBrokerDataRequest',
  full_name='yandex.cloud.iot.broker.v1.PublishBrokerDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='broker_id', full_name='yandex.cloud.iot.broker.v1.PublishBrokerDataRequest.broker_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topic', full_name='yandex.cloud.iot.broker.v1.PublishBrokerDataRequest.topic', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\006<=1024', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='yandex.cloud.iot.broker.v1.PublishBrokerDataRequest.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\010<=262144', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=263,
)


_PUBLISHBROKERDATARESPONSE = _descriptor.Descriptor(
  name='PublishBrokerDataResponse',
  full_name='yandex.cloud.iot.broker.v1.PublishBrokerDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=265,
  serialized_end=292,
)

DESCRIPTOR.message_types_by_name['PublishBrokerDataRequest'] = _PUBLISHBROKERDATAREQUEST
DESCRIPTOR.message_types_by_name['PublishBrokerDataResponse'] = _PUBLISHBROKERDATARESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PublishBrokerDataRequest = _reflection.GeneratedProtocolMessageType('PublishBrokerDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHBROKERDATAREQUEST,
  '__module__' : 'yandex.cloud.iot.broker.v1.broker_data_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.broker.v1.PublishBrokerDataRequest)
  })
_sym_db.RegisterMessage(PublishBrokerDataRequest)

PublishBrokerDataResponse = _reflection.GeneratedProtocolMessageType('PublishBrokerDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHBROKERDATARESPONSE,
  '__module__' : 'yandex.cloud.iot.broker.v1.broker_data_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.broker.v1.PublishBrokerDataResponse)
  })
_sym_db.RegisterMessage(PublishBrokerDataResponse)


DESCRIPTOR._options = None
_PUBLISHBROKERDATAREQUEST.fields_by_name['broker_id']._options = None
_PUBLISHBROKERDATAREQUEST.fields_by_name['topic']._options = None
_PUBLISHBROKERDATAREQUEST.fields_by_name['data']._options = None

_BROKERDATASERVICE = _descriptor.ServiceDescriptor(
  name='BrokerDataService',
  full_name='yandex.cloud.iot.broker.v1.BrokerDataService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=295,
  serialized_end=490,
  methods=[
  _descriptor.MethodDescriptor(
    name='Publish',
    full_name='yandex.cloud.iot.broker.v1.BrokerDataService.Publish',
    index=0,
    containing_service=None,
    input_type=_PUBLISHBROKERDATAREQUEST,
    output_type=_PUBLISHBROKERDATARESPONSE,
    serialized_options=b'\202\323\344\223\002/\"*/iot-broker/v1/brokers/{broker_id}/publish:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BROKERDATASERVICE)

DESCRIPTOR.services_by_name['BrokerDataService'] = _BROKERDATASERVICE

# @@protoc_insertion_point(module_scope)
