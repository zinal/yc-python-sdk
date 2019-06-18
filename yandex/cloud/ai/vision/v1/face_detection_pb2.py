# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/ai/vision/v1/face_detection.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.ai.vision.v1 import primitives_pb2 as yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_primitives__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/ai/vision/v1/face_detection.proto',
  package='yandex.cloud.ai.vision.v1',
  syntax='proto3',
  serialized_options=_b('ZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/vision/v1;vision'),
  serialized_pb=_b('\n.yandex/cloud/ai/vision/v1/face_detection.proto\x12\x19yandex.cloud.ai.vision.v1\x1a*yandex/cloud/ai/vision/v1/primitives.proto\"@\n\x0e\x46\x61\x63\x65\x41nnotation\x12.\n\x05\x66\x61\x63\x65s\x18\x01 \x03(\x0b\x32\x1f.yandex.cloud.ai.vision.v1.Face\"@\n\x04\x46\x61\x63\x65\x12\x38\n\x0c\x62ounding_box\x18\x01 \x01(\x0b\x32\".yandex.cloud.ai.vision.v1.PolygonBFZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/vision/v1;visionb\x06proto3')
  ,
  dependencies=[yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_primitives__pb2.DESCRIPTOR,])




_FACEANNOTATION = _descriptor.Descriptor(
  name='FaceAnnotation',
  full_name='yandex.cloud.ai.vision.v1.FaceAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='faces', full_name='yandex.cloud.ai.vision.v1.FaceAnnotation.faces', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=121,
  serialized_end=185,
)


_FACE = _descriptor.Descriptor(
  name='Face',
  full_name='yandex.cloud.ai.vision.v1.Face',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bounding_box', full_name='yandex.cloud.ai.vision.v1.Face.bounding_box', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=187,
  serialized_end=251,
)

_FACEANNOTATION.fields_by_name['faces'].message_type = _FACE
_FACE.fields_by_name['bounding_box'].message_type = yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_primitives__pb2._POLYGON
DESCRIPTOR.message_types_by_name['FaceAnnotation'] = _FACEANNOTATION
DESCRIPTOR.message_types_by_name['Face'] = _FACE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FaceAnnotation = _reflection.GeneratedProtocolMessageType('FaceAnnotation', (_message.Message,), dict(
  DESCRIPTOR = _FACEANNOTATION,
  __module__ = 'yandex.cloud.ai.vision.v1.face_detection_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ai.vision.v1.FaceAnnotation)
  ))
_sym_db.RegisterMessage(FaceAnnotation)

Face = _reflection.GeneratedProtocolMessageType('Face', (_message.Message,), dict(
  DESCRIPTOR = _FACE,
  __module__ = 'yandex.cloud.ai.vision.v1.face_detection_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ai.vision.v1.Face)
  ))
_sym_db.RegisterMessage(Face)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
