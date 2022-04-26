# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/vpc/v1/gateway.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/vpc/v1/gateway.proto',
  package='yandex.cloud.vpc.v1',
  syntax='proto3',
  serialized_options=b'\n\027yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!yandex/cloud/vpc/v1/gateway.proto\x12\x13yandex.cloud.vpc.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xba\x02\n\x07Gateway\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x38\n\x06labels\x18\x06 \x03(\x0b\x32(.yandex.cloud.vpc.v1.Gateway.LabelsEntry\x12I\n\x15shared_egress_gateway\x18\x07 \x01(\x0b\x32(.yandex.cloud.vpc.v1.SharedEgressGatewayH\x00\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\t\n\x07gateway\"\x15\n\x13SharedEgressGatewayBV\n\x17yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpcb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_GATEWAY_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.vpc.v1.Gateway.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.vpc.v1.Gateway.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.vpc.v1.Gateway.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=350,
  serialized_end=395,
)

_GATEWAY = _descriptor.Descriptor(
  name='Gateway',
  full_name='yandex.cloud.vpc.v1.Gateway',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.vpc.v1.Gateway.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.vpc.v1.Gateway.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.vpc.v1.Gateway.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.vpc.v1.Gateway.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.vpc.v1.Gateway.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.vpc.v1.Gateway.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shared_egress_gateway', full_name='yandex.cloud.vpc.v1.Gateway.shared_egress_gateway', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GATEWAY_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='gateway', full_name='yandex.cloud.vpc.v1.Gateway.gateway',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=92,
  serialized_end=406,
)


_SHAREDEGRESSGATEWAY = _descriptor.Descriptor(
  name='SharedEgressGateway',
  full_name='yandex.cloud.vpc.v1.SharedEgressGateway',
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
  serialized_start=408,
  serialized_end=429,
)

_GATEWAY_LABELSENTRY.containing_type = _GATEWAY
_GATEWAY.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GATEWAY.fields_by_name['labels'].message_type = _GATEWAY_LABELSENTRY
_GATEWAY.fields_by_name['shared_egress_gateway'].message_type = _SHAREDEGRESSGATEWAY
_GATEWAY.oneofs_by_name['gateway'].fields.append(
  _GATEWAY.fields_by_name['shared_egress_gateway'])
_GATEWAY.fields_by_name['shared_egress_gateway'].containing_oneof = _GATEWAY.oneofs_by_name['gateway']
DESCRIPTOR.message_types_by_name['Gateway'] = _GATEWAY
DESCRIPTOR.message_types_by_name['SharedEgressGateway'] = _SHAREDEGRESSGATEWAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Gateway = _reflection.GeneratedProtocolMessageType('Gateway', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _GATEWAY_LABELSENTRY,
    '__module__' : 'yandex.cloud.vpc.v1.gateway_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.Gateway.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _GATEWAY,
  '__module__' : 'yandex.cloud.vpc.v1.gateway_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.Gateway)
  })
_sym_db.RegisterMessage(Gateway)
_sym_db.RegisterMessage(Gateway.LabelsEntry)

SharedEgressGateway = _reflection.GeneratedProtocolMessageType('SharedEgressGateway', (_message.Message,), {
  'DESCRIPTOR' : _SHAREDEGRESSGATEWAY,
  '__module__' : 'yandex.cloud.vpc.v1.gateway_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.SharedEgressGateway)
  })
_sym_db.RegisterMessage(SharedEgressGateway)


DESCRIPTOR._options = None
_GATEWAY_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)
