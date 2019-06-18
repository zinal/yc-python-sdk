# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/ai/vision/v1/vision_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.ai.vision.v1 import text_detection_pb2 as yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_text__detection__pb2
from yandex.cloud.ai.vision.v1 import classification_pb2 as yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_classification__pb2
from yandex.cloud.ai.vision.v1 import face_detection_pb2 as yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_face__detection__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/ai/vision/v1/vision_service.proto',
  package='yandex.cloud.ai.vision.v1',
  syntax='proto3',
  serialized_options=_b('ZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/vision/v1;vision'),
  serialized_pb=_b('\n.yandex/cloud/ai/vision/v1/vision_service.proto\x12\x19yandex.cloud.ai.vision.v1\x1a.yandex/cloud/ai/vision/v1/text_detection.proto\x1a.yandex/cloud/ai/vision/v1/classification.proto\x1a.yandex/cloud/ai/vision/v1/face_detection.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/rpc/status.proto\"z\n\x13\x42\x61tchAnalyzeRequest\x12\x46\n\ranalyze_specs\x18\x01 \x03(\x0b\x32&.yandex.cloud.ai.vision.v1.AnalyzeSpecB\x07\x82\xc8\x31\x03\x31-8\x12\x1b\n\tfolder_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\"~\n\x0b\x41nalyzeSpec\x12 \n\x07\x63ontent\x18\x01 \x01(\x0c\x42\r\x8a\xc8\x31\t<=1048576H\x00\x12=\n\x08\x66\x65\x61tures\x18\x03 \x03(\x0b\x32\".yandex.cloud.ai.vision.v1.FeatureB\x07\x82\xc8\x31\x03\x31-8B\x0e\n\x06source\x12\x04\xc0\xc1\x31\x01\"\xd5\x02\n\x07\x46\x65\x61ture\x12\x35\n\x04type\x18\x01 \x01(\x0e\x32\'.yandex.cloud.ai.vision.v1.Feature.Type\x12W\n\x15\x63lassification_config\x18\x02 \x01(\x0b\x32\x36.yandex.cloud.ai.vision.v1.FeatureClassificationConfigH\x00\x12V\n\x15text_detection_config\x18\x03 \x01(\x0b\x32\x35.yandex.cloud.ai.vision.v1.FeatureTextDetectionConfigH\x00\"X\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0eTEXT_DETECTION\x10\x01\x12\x12\n\x0e\x43LASSIFICATION\x10\x02\x12\x12\n\x0e\x46\x41\x43\x45_DETECTION\x10\x03\x42\x08\n\x06\x63onfig\"7\n\x1b\x46\x65\x61tureClassificationConfig\x12\x18\n\x05model\x18\x01 \x01(\tB\t\x8a\xc8\x31\x05<=256\"]\n\x1a\x46\x65\x61tureTextDetectionConfig\x12&\n\x0elanguage_codes\x18\x01 \x03(\tB\x0e\x82\xc8\x31\x03\x31-8\x8a\xc8\x31\x03<=3\x12\x17\n\x05model\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\"Q\n\x14\x42\x61tchAnalyzeResponse\x12\x39\n\x07results\x18\x01 \x03(\x0b\x32(.yandex.cloud.ai.vision.v1.AnalyzeResult\"m\n\rAnalyzeResult\x12\x39\n\x07results\x18\x02 \x03(\x0b\x32(.yandex.cloud.ai.vision.v1.FeatureResult\x12!\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\"\x8d\x02\n\rFeatureResult\x12\x43\n\x0etext_detection\x18\x02 \x01(\x0b\x32).yandex.cloud.ai.vision.v1.TextAnnotationH\x00\x12\x44\n\x0e\x63lassification\x18\x03 \x01(\x0b\x32*.yandex.cloud.ai.vision.v1.ClassAnnotationH\x00\x12\x43\n\x0e\x66\x61\x63\x65_detection\x18\x04 \x01(\x0b\x32).yandex.cloud.ai.vision.v1.FaceAnnotationH\x00\x12!\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x12.google.rpc.StatusB\t\n\x07\x66\x65\x61ture2\xa5\x01\n\rVisionService\x12\x93\x01\n\x0c\x42\x61tchAnalyze\x12..yandex.cloud.ai.vision.v1.BatchAnalyzeRequest\x1a/.yandex.cloud.ai.vision.v1.BatchAnalyzeResponse\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/vision/v1/batchAnalyze:\x01*BFZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/ai/vision/v1;visionb\x06proto3')
  ,
  dependencies=[yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_text__detection__pb2.DESCRIPTOR,yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_classification__pb2.DESCRIPTOR,yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_face__detection__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])



_FEATURE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='yandex.cloud.ai.vision.v1.Feature.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT_DETECTION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLASSIFICATION', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FACE_DETECTION', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=803,
  serialized_end=891,
)
_sym_db.RegisterEnumDescriptor(_FEATURE_TYPE)


_BATCHANALYZEREQUEST = _descriptor.Descriptor(
  name='BatchAnalyzeRequest',
  full_name='yandex.cloud.ai.vision.v1.BatchAnalyzeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='analyze_specs', full_name='yandex.cloud.ai.vision.v1.BatchAnalyzeRequest.analyze_specs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\202\3101\0031-8'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.ai.vision.v1.BatchAnalyzeRequest.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\004<=50'), file=DESCRIPTOR),
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
  serialized_start=307,
  serialized_end=429,
)


_ANALYZESPEC = _descriptor.Descriptor(
  name='AnalyzeSpec',
  full_name='yandex.cloud.ai.vision.v1.AnalyzeSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='yandex.cloud.ai.vision.v1.AnalyzeSpec.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\t<=1048576'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='features', full_name='yandex.cloud.ai.vision.v1.AnalyzeSpec.features', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\202\3101\0031-8'), file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='source', full_name='yandex.cloud.ai.vision.v1.AnalyzeSpec.source',
      index=0, containing_type=None, fields=[], serialized_options=_b('\300\3011\001')),
  ],
  serialized_start=431,
  serialized_end=557,
)


_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='yandex.cloud.ai.vision.v1.Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='yandex.cloud.ai.vision.v1.Feature.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classification_config', full_name='yandex.cloud.ai.vision.v1.Feature.classification_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_detection_config', full_name='yandex.cloud.ai.vision.v1.Feature.text_detection_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FEATURE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='config', full_name='yandex.cloud.ai.vision.v1.Feature.config',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=560,
  serialized_end=901,
)


_FEATURECLASSIFICATIONCONFIG = _descriptor.Descriptor(
  name='FeatureClassificationConfig',
  full_name='yandex.cloud.ai.vision.v1.FeatureClassificationConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='yandex.cloud.ai.vision.v1.FeatureClassificationConfig.model', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\005<=256'), file=DESCRIPTOR),
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
  serialized_start=903,
  serialized_end=958,
)


_FEATURETEXTDETECTIONCONFIG = _descriptor.Descriptor(
  name='FeatureTextDetectionConfig',
  full_name='yandex.cloud.ai.vision.v1.FeatureTextDetectionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='language_codes', full_name='yandex.cloud.ai.vision.v1.FeatureTextDetectionConfig.language_codes', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\202\3101\0031-8\212\3101\003<=3'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='yandex.cloud.ai.vision.v1.FeatureTextDetectionConfig.model', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\004<=50'), file=DESCRIPTOR),
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
  serialized_start=960,
  serialized_end=1053,
)


_BATCHANALYZERESPONSE = _descriptor.Descriptor(
  name='BatchAnalyzeResponse',
  full_name='yandex.cloud.ai.vision.v1.BatchAnalyzeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='yandex.cloud.ai.vision.v1.BatchAnalyzeResponse.results', index=0,
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
  serialized_start=1055,
  serialized_end=1136,
)


_ANALYZERESULT = _descriptor.Descriptor(
  name='AnalyzeResult',
  full_name='yandex.cloud.ai.vision.v1.AnalyzeResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='yandex.cloud.ai.vision.v1.AnalyzeResult.results', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='yandex.cloud.ai.vision.v1.AnalyzeResult.error', index=1,
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
  serialized_start=1138,
  serialized_end=1247,
)


_FEATURERESULT = _descriptor.Descriptor(
  name='FeatureResult',
  full_name='yandex.cloud.ai.vision.v1.FeatureResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text_detection', full_name='yandex.cloud.ai.vision.v1.FeatureResult.text_detection', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classification', full_name='yandex.cloud.ai.vision.v1.FeatureResult.classification', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='face_detection', full_name='yandex.cloud.ai.vision.v1.FeatureResult.face_detection', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='yandex.cloud.ai.vision.v1.FeatureResult.error', index=3,
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
    _descriptor.OneofDescriptor(
      name='feature', full_name='yandex.cloud.ai.vision.v1.FeatureResult.feature',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1250,
  serialized_end=1519,
)

_BATCHANALYZEREQUEST.fields_by_name['analyze_specs'].message_type = _ANALYZESPEC
_ANALYZESPEC.fields_by_name['features'].message_type = _FEATURE
_ANALYZESPEC.oneofs_by_name['source'].fields.append(
  _ANALYZESPEC.fields_by_name['content'])
_ANALYZESPEC.fields_by_name['content'].containing_oneof = _ANALYZESPEC.oneofs_by_name['source']
_FEATURE.fields_by_name['type'].enum_type = _FEATURE_TYPE
_FEATURE.fields_by_name['classification_config'].message_type = _FEATURECLASSIFICATIONCONFIG
_FEATURE.fields_by_name['text_detection_config'].message_type = _FEATURETEXTDETECTIONCONFIG
_FEATURE_TYPE.containing_type = _FEATURE
_FEATURE.oneofs_by_name['config'].fields.append(
  _FEATURE.fields_by_name['classification_config'])
_FEATURE.fields_by_name['classification_config'].containing_oneof = _FEATURE.oneofs_by_name['config']
_FEATURE.oneofs_by_name['config'].fields.append(
  _FEATURE.fields_by_name['text_detection_config'])
_FEATURE.fields_by_name['text_detection_config'].containing_oneof = _FEATURE.oneofs_by_name['config']
_BATCHANALYZERESPONSE.fields_by_name['results'].message_type = _ANALYZERESULT
_ANALYZERESULT.fields_by_name['results'].message_type = _FEATURERESULT
_ANALYZERESULT.fields_by_name['error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_FEATURERESULT.fields_by_name['text_detection'].message_type = yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_text__detection__pb2._TEXTANNOTATION
_FEATURERESULT.fields_by_name['classification'].message_type = yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_classification__pb2._CLASSANNOTATION
_FEATURERESULT.fields_by_name['face_detection'].message_type = yandex_dot_cloud_dot_ai_dot_vision_dot_v1_dot_face__detection__pb2._FACEANNOTATION
_FEATURERESULT.fields_by_name['error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_FEATURERESULT.oneofs_by_name['feature'].fields.append(
  _FEATURERESULT.fields_by_name['text_detection'])
_FEATURERESULT.fields_by_name['text_detection'].containing_oneof = _FEATURERESULT.oneofs_by_name['feature']
_FEATURERESULT.oneofs_by_name['feature'].fields.append(
  _FEATURERESULT.fields_by_name['classification'])
_FEATURERESULT.fields_by_name['classification'].containing_oneof = _FEATURERESULT.oneofs_by_name['feature']
_FEATURERESULT.oneofs_by_name['feature'].fields.append(
  _FEATURERESULT.fields_by_name['face_detection'])
_FEATURERESULT.fields_by_name['face_detection'].containing_oneof = _FEATURERESULT.oneofs_by_name['feature']
DESCRIPTOR.message_types_by_name['BatchAnalyzeRequest'] = _BATCHANALYZEREQUEST
DESCRIPTOR.message_types_by_name['AnalyzeSpec'] = _ANALYZESPEC
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE
DESCRIPTOR.message_types_by_name['FeatureClassificationConfig'] = _FEATURECLASSIFICATIONCONFIG
DESCRIPTOR.message_types_by_name['FeatureTextDetectionConfig'] = _FEATURETEXTDETECTIONCONFIG
DESCRIPTOR.message_types_by_name['BatchAnalyzeResponse'] = _BATCHANALYZERESPONSE
DESCRIPTOR.message_types_by_name['AnalyzeResult'] = _ANALYZERESULT
DESCRIPTOR.message_types_by_name['FeatureResult'] = _FEATURERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BatchAnalyzeRequest = _reflection.GeneratedProtocolMessageType('BatchAnalyzeRequest', (_message.Message,), dict(
  DESCRIPTOR = _BATCHANALYZEREQUEST,
  __module__ = 'yandex.cloud.ai.vision.v1.vision_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ai.vision.v1.BatchAnalyzeRequest)
  ))
_sym_db.RegisterMessage(BatchAnalyzeRequest)

AnalyzeSpec = _reflection.GeneratedProtocolMessageType('AnalyzeSpec', (_message.Message,), dict(
  DESCRIPTOR = _ANALYZESPEC,
  __module__ = 'yandex.cloud.ai.vision.v1.vision_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ai.vision.v1.AnalyzeSpec)
  ))
_sym_db.RegisterMessage(AnalyzeSpec)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), dict(
  DESCRIPTOR = _FEATURE,
  __module__ = 'yandex.cloud.ai.vision.v1.vision_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ai.vision.v1.Feature)
  ))
_sym_db.RegisterMessage(Feature)

FeatureClassificationConfig = _reflection.GeneratedProtocolMessageType('FeatureClassificationConfig', (_message.Message,), dict(
  DESCRIPTOR = _FEATURECLASSIFICATIONCONFIG,
  __module__ = 'yandex.cloud.ai.vision.v1.vision_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ai.vision.v1.FeatureClassificationConfig)
  ))
_sym_db.RegisterMessage(FeatureClassificationConfig)

FeatureTextDetectionConfig = _reflection.GeneratedProtocolMessageType('FeatureTextDetectionConfig', (_message.Message,), dict(
  DESCRIPTOR = _FEATURETEXTDETECTIONCONFIG,
  __module__ = 'yandex.cloud.ai.vision.v1.vision_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ai.vision.v1.FeatureTextDetectionConfig)
  ))
_sym_db.RegisterMessage(FeatureTextDetectionConfig)

BatchAnalyzeResponse = _reflection.GeneratedProtocolMessageType('BatchAnalyzeResponse', (_message.Message,), dict(
  DESCRIPTOR = _BATCHANALYZERESPONSE,
  __module__ = 'yandex.cloud.ai.vision.v1.vision_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ai.vision.v1.BatchAnalyzeResponse)
  ))
_sym_db.RegisterMessage(BatchAnalyzeResponse)

AnalyzeResult = _reflection.GeneratedProtocolMessageType('AnalyzeResult', (_message.Message,), dict(
  DESCRIPTOR = _ANALYZERESULT,
  __module__ = 'yandex.cloud.ai.vision.v1.vision_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ai.vision.v1.AnalyzeResult)
  ))
_sym_db.RegisterMessage(AnalyzeResult)

FeatureResult = _reflection.GeneratedProtocolMessageType('FeatureResult', (_message.Message,), dict(
  DESCRIPTOR = _FEATURERESULT,
  __module__ = 'yandex.cloud.ai.vision.v1.vision_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.ai.vision.v1.FeatureResult)
  ))
_sym_db.RegisterMessage(FeatureResult)


DESCRIPTOR._options = None
_BATCHANALYZEREQUEST.fields_by_name['analyze_specs']._options = None
_BATCHANALYZEREQUEST.fields_by_name['folder_id']._options = None
_ANALYZESPEC.oneofs_by_name['source']._options = None
_ANALYZESPEC.fields_by_name['content']._options = None
_ANALYZESPEC.fields_by_name['features']._options = None
_FEATURECLASSIFICATIONCONFIG.fields_by_name['model']._options = None
_FEATURETEXTDETECTIONCONFIG.fields_by_name['language_codes']._options = None
_FEATURETEXTDETECTIONCONFIG.fields_by_name['model']._options = None

_VISIONSERVICE = _descriptor.ServiceDescriptor(
  name='VisionService',
  full_name='yandex.cloud.ai.vision.v1.VisionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1522,
  serialized_end=1687,
  methods=[
  _descriptor.MethodDescriptor(
    name='BatchAnalyze',
    full_name='yandex.cloud.ai.vision.v1.VisionService.BatchAnalyze',
    index=0,
    containing_service=None,
    input_type=_BATCHANALYZEREQUEST,
    output_type=_BATCHANALYZERESPONSE,
    serialized_options=_b('\202\323\344\223\002\034\"\027/vision/v1/batchAnalyze:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_VISIONSERVICE)

DESCRIPTOR.services_by_name['VisionService'] = _VISIONSERVICE

# @@protoc_insertion_point(module_scope)
