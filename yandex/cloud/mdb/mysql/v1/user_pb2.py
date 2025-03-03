# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/mysql/v1/user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/mysql/v1/user.proto',
  package='yandex.cloud.mdb.mysql.v1',
  syntax='proto3',
  serialized_options=b'\n\035yandex.cloud.api.mdb.mysql.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1;mysql',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$yandex/cloud/mdb/mysql/v1/user.proto\x12\x19yandex.cloud.mdb.mysql.v1\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"\xbb\x02\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12:\n\x0bpermissions\x18\x03 \x03(\x0b\x32%.yandex.cloud.mdb.mysql.v1.Permission\x12G\n\x12global_permissions\x18\x04 \x03(\x0e\x32+.yandex.cloud.mdb.mysql.v1.GlobalPermission\x12\x46\n\x11\x63onnection_limits\x18\x05 \x01(\x0b\x32+.yandex.cloud.mdb.mysql.v1.ConnectionLimits\x12\x44\n\x15\x61uthentication_plugin\x18\x06 \x01(\x0e\x32%.yandex.cloud.mdb.mysql.v1.AuthPlugin\"\xaf\x03\n\nPermission\x12\x15\n\rdatabase_name\x18\x01 \x01(\t\x12G\n\x05roles\x18\x02 \x03(\x0e\x32/.yandex.cloud.mdb.mysql.v1.Permission.PrivilegeB\x07\x82\xc8\x31\x03>=1\"\xc0\x02\n\tPrivilege\x12\x19\n\x15PRIVILEGE_UNSPECIFIED\x10\x00\x12\x12\n\x0e\x41LL_PRIVILEGES\x10\x01\x12\t\n\x05\x41LTER\x10\x02\x12\x11\n\rALTER_ROUTINE\x10\x03\x12\n\n\x06\x43REATE\x10\x04\x12\x12\n\x0e\x43REATE_ROUTINE\x10\x05\x12\x1b\n\x17\x43REATE_TEMPORARY_TABLES\x10\x06\x12\x0f\n\x0b\x43REATE_VIEW\x10\x07\x12\n\n\x06\x44\x45LETE\x10\x08\x12\x08\n\x04\x44ROP\x10\t\x12\t\n\x05\x45VENT\x10\n\x12\x0b\n\x07\x45XECUTE\x10\x0b\x12\t\n\x05INDEX\x10\x0c\x12\n\n\x06INSERT\x10\r\x12\x0f\n\x0bLOCK_TABLES\x10\x0e\x12\n\n\x06SELECT\x10\x0f\x12\r\n\tSHOW_VIEW\x10\x10\x12\x0b\n\x07TRIGGER\x10\x11\x12\n\n\x06UPDATE\x10\x12\x12\x0e\n\nREFERENCES\x10\x13\"\xa8\x02\n\x10\x43onnectionLimits\x12\x44\n\x16max_questions_per_hour\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x42\n\x14max_updates_per_hour\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x46\n\x18max_connections_per_hour\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x42\n\x14max_user_connections\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\"\xeb\x02\n\x08UserSpec\x12+\n\x04name\x18\x01 \x01(\tB\x1d\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=32\xf2\xc7\x31\r[a-zA-Z0-9_]*\x12\x1f\n\x08password\x18\x02 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05\x38-128\x12:\n\x0bpermissions\x18\x03 \x03(\x0b\x32%.yandex.cloud.mdb.mysql.v1.Permission\x12G\n\x12global_permissions\x18\x04 \x03(\x0e\x32+.yandex.cloud.mdb.mysql.v1.GlobalPermission\x12\x46\n\x11\x63onnection_limits\x18\x05 \x01(\x0b\x32+.yandex.cloud.mdb.mysql.v1.ConnectionLimits\x12\x44\n\x15\x61uthentication_plugin\x18\x06 \x01(\x0e\x32%.yandex.cloud.mdb.mysql.v1.AuthPlugin*\x9e\x01\n\x10GlobalPermission\x12!\n\x1dGLOBAL_PERMISSION_UNSPECIFIED\x10\x00\x12\x16\n\x12REPLICATION_CLIENT\x10\x01\x12\x15\n\x11REPLICATION_SLAVE\x10\x02\x12\x0b\n\x07PROCESS\x10\x03\x12\x19\n\x15\x46LUSH_OPTIMIZER_COSTS\x10\x04\x12\x10\n\x0cSHOW_ROUTINE\x10\x05*t\n\nAuthPlugin\x12\x1b\n\x17\x41UTH_PLUGIN_UNSPECIFIED\x10\x00\x12\x19\n\x15MYSQL_NATIVE_PASSWORD\x10\x01\x12\x19\n\x15\x43\x41\x43HING_SHA2_PASSWORD\x10\x02\x12\x13\n\x0fSHA256_PASSWORD\x10\x03\x42\x64\n\x1dyandex.cloud.api.mdb.mysql.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1;mysqlb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])

_GLOBALPERMISSION = _descriptor.EnumDescriptor(
  name='GlobalPermission',
  full_name='yandex.cloud.mdb.mysql.v1.GlobalPermission',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GLOBAL_PERMISSION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REPLICATION_CLIENT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REPLICATION_SLAVE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROCESS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FLUSH_OPTIMIZER_COSTS', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHOW_ROUTINE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1548,
  serialized_end=1706,
)
_sym_db.RegisterEnumDescriptor(_GLOBALPERMISSION)

GlobalPermission = enum_type_wrapper.EnumTypeWrapper(_GLOBALPERMISSION)
_AUTHPLUGIN = _descriptor.EnumDescriptor(
  name='AuthPlugin',
  full_name='yandex.cloud.mdb.mysql.v1.AuthPlugin',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUTH_PLUGIN_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MYSQL_NATIVE_PASSWORD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CACHING_SHA2_PASSWORD', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHA256_PASSWORD', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1708,
  serialized_end=1824,
)
_sym_db.RegisterEnumDescriptor(_AUTHPLUGIN)

AuthPlugin = enum_type_wrapper.EnumTypeWrapper(_AUTHPLUGIN)
GLOBAL_PERMISSION_UNSPECIFIED = 0
REPLICATION_CLIENT = 1
REPLICATION_SLAVE = 2
PROCESS = 3
FLUSH_OPTIMIZER_COSTS = 4
SHOW_ROUTINE = 5
AUTH_PLUGIN_UNSPECIFIED = 0
MYSQL_NATIVE_PASSWORD = 1
CACHING_SHA2_PASSWORD = 2
SHA256_PASSWORD = 3


_PERMISSION_PRIVILEGE = _descriptor.EnumDescriptor(
  name='Privilege',
  full_name='yandex.cloud.mdb.mysql.v1.Permission.Privilege',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PRIVILEGE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALL_PRIVILEGES', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALTER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALTER_ROUTINE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATE_ROUTINE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATE_TEMPORARY_TABLES', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATE_VIEW', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DROP', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EVENT', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXECUTE', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INDEX', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INSERT', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOCK_TABLES', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SELECT', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHOW_VIEW', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRIGGER', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REFERENCES', index=19, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=560,
  serialized_end=880,
)
_sym_db.RegisterEnumDescriptor(_PERMISSION_PRIVILEGE)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='yandex.cloud.mdb.mysql.v1.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.mysql.v1.User.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mysql.v1.User.cluster_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='yandex.cloud.mdb.mysql.v1.User.permissions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='global_permissions', full_name='yandex.cloud.mdb.mysql.v1.User.global_permissions', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connection_limits', full_name='yandex.cloud.mdb.mysql.v1.User.connection_limits', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authentication_plugin', full_name='yandex.cloud.mdb.mysql.v1.User.authentication_plugin', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=131,
  serialized_end=446,
)


_PERMISSION = _descriptor.Descriptor(
  name='Permission',
  full_name='yandex.cloud.mdb.mysql.v1.Permission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='database_name', full_name='yandex.cloud.mdb.mysql.v1.Permission.database_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roles', full_name='yandex.cloud.mdb.mysql.v1.Permission.roles', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\3101\003>=1', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PERMISSION_PRIVILEGE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=449,
  serialized_end=880,
)


_CONNECTIONLIMITS = _descriptor.Descriptor(
  name='ConnectionLimits',
  full_name='yandex.cloud.mdb.mysql.v1.ConnectionLimits',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_questions_per_hour', full_name='yandex.cloud.mdb.mysql.v1.ConnectionLimits.max_questions_per_hour', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\003>=0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_updates_per_hour', full_name='yandex.cloud.mdb.mysql.v1.ConnectionLimits.max_updates_per_hour', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\003>=0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_connections_per_hour', full_name='yandex.cloud.mdb.mysql.v1.ConnectionLimits.max_connections_per_hour', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\003>=0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_user_connections', full_name='yandex.cloud.mdb.mysql.v1.ConnectionLimits.max_user_connections', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\003>=0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=883,
  serialized_end=1179,
)


_USERSPEC = _descriptor.Descriptor(
  name='UserSpec',
  full_name='yandex.cloud.mdb.mysql.v1.UserSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.mysql.v1.UserSpec.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=32\362\3071\r[a-zA-Z0-9_]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='yandex.cloud.mdb.mysql.v1.UserSpec.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\0058-128', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='yandex.cloud.mdb.mysql.v1.UserSpec.permissions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='global_permissions', full_name='yandex.cloud.mdb.mysql.v1.UserSpec.global_permissions', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connection_limits', full_name='yandex.cloud.mdb.mysql.v1.UserSpec.connection_limits', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authentication_plugin', full_name='yandex.cloud.mdb.mysql.v1.UserSpec.authentication_plugin', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1182,
  serialized_end=1545,
)

_USER.fields_by_name['permissions'].message_type = _PERMISSION
_USER.fields_by_name['global_permissions'].enum_type = _GLOBALPERMISSION
_USER.fields_by_name['connection_limits'].message_type = _CONNECTIONLIMITS
_USER.fields_by_name['authentication_plugin'].enum_type = _AUTHPLUGIN
_PERMISSION.fields_by_name['roles'].enum_type = _PERMISSION_PRIVILEGE
_PERMISSION_PRIVILEGE.containing_type = _PERMISSION
_CONNECTIONLIMITS.fields_by_name['max_questions_per_hour'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_CONNECTIONLIMITS.fields_by_name['max_updates_per_hour'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_CONNECTIONLIMITS.fields_by_name['max_connections_per_hour'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_CONNECTIONLIMITS.fields_by_name['max_user_connections'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_USERSPEC.fields_by_name['permissions'].message_type = _PERMISSION
_USERSPEC.fields_by_name['global_permissions'].enum_type = _GLOBALPERMISSION
_USERSPEC.fields_by_name['connection_limits'].message_type = _CONNECTIONLIMITS
_USERSPEC.fields_by_name['authentication_plugin'].enum_type = _AUTHPLUGIN
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Permission'] = _PERMISSION
DESCRIPTOR.message_types_by_name['ConnectionLimits'] = _CONNECTIONLIMITS
DESCRIPTOR.message_types_by_name['UserSpec'] = _USERSPEC
DESCRIPTOR.enum_types_by_name['GlobalPermission'] = _GLOBALPERMISSION
DESCRIPTOR.enum_types_by_name['AuthPlugin'] = _AUTHPLUGIN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.User)
  })
_sym_db.RegisterMessage(User)

Permission = _reflection.GeneratedProtocolMessageType('Permission', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSION,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.Permission)
  })
_sym_db.RegisterMessage(Permission)

ConnectionLimits = _reflection.GeneratedProtocolMessageType('ConnectionLimits', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONLIMITS,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.ConnectionLimits)
  })
_sym_db.RegisterMessage(ConnectionLimits)

UserSpec = _reflection.GeneratedProtocolMessageType('UserSpec', (_message.Message,), {
  'DESCRIPTOR' : _USERSPEC,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.UserSpec)
  })
_sym_db.RegisterMessage(UserSpec)


DESCRIPTOR._options = None
_PERMISSION.fields_by_name['roles']._options = None
_CONNECTIONLIMITS.fields_by_name['max_questions_per_hour']._options = None
_CONNECTIONLIMITS.fields_by_name['max_updates_per_hour']._options = None
_CONNECTIONLIMITS.fields_by_name['max_connections_per_hour']._options = None
_CONNECTIONLIMITS.fields_by_name['max_user_connections']._options = None
_USERSPEC.fields_by_name['name']._options = None
_USERSPEC.fields_by_name['password']._options = None
# @@protoc_insertion_point(module_scope)
