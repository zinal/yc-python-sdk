# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/ydb/v1/location.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/ydb/v1/location.proto',
  package='yandex.cloud.ydb.v1',
  syntax='proto3',
  serialized_options=b'\n\027yandex.cloud.api.ydb.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/ydb/v1;ydb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"yandex/cloud/ydb/v1/location.proto\x12\x13yandex.cloud.ydb.v1\"+\n\x08Location\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\tBV\n\x17yandex.cloud.api.ydb.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/ydb/v1;ydbb\x06proto3'
)




_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='yandex.cloud.ydb.v1.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.ydb.v1.Location.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.ydb.v1.Location.description', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=102,
)

DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'yandex.cloud.ydb.v1.location_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ydb.v1.Location)
  })
_sym_db.RegisterMessage(Location)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
