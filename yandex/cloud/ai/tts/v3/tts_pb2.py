# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/ai/tts/v3/tts.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/ai/tts/v3/tts.proto',
  package='speechkit.tts.v3',
  syntax='proto3',
  serialized_options=b'\n\032yandex.cloud.api.ai.tts.v3Z>github.com/yandex-cloud/go-genproto/yandex/cloud/ai/tts/v3;tts',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n yandex/cloud/ai/tts/v3/tts.proto\x12\x10speechkit.tts.v3\"j\n\x0c\x41udioContent\x12\x11\n\x07\x63ontent\x18\x01 \x01(\x0cH\x00\x12\x38\n\naudio_spec\x18\x02 \x01(\x0b\x32$.speechkit.tts.v3.AudioFormatOptionsB\r\n\x0b\x41udioSource\"\x91\x01\n\x12\x41udioFormatOptions\x12/\n\traw_audio\x18\x01 \x01(\x0b\x32\x1a.speechkit.tts.v3.RawAudioH\x00\x12;\n\x0f\x63ontainer_audio\x18\x02 \x01(\x0b\x32 .speechkit.tts.v3.ContainerAudioH\x00\x42\r\n\x0b\x41udioFormat\"\xaa\x01\n\x08RawAudio\x12@\n\x0e\x61udio_encoding\x18\x01 \x01(\x0e\x32(.speechkit.tts.v3.RawAudio.AudioEncoding\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\x03\"A\n\rAudioEncoding\x12\x1e\n\x1a\x41UDIO_ENCODING_UNSPECIFIED\x10\x00\x12\x10\n\x0cLINEAR16_PCM\x10\x01\"\xb6\x01\n\x0e\x43ontainerAudio\x12Q\n\x14\x63ontainer_audio_type\x18\x01 \x01(\x0e\x32\x33.speechkit.tts.v3.ContainerAudio.ContainerAudioType\"Q\n\x12\x43ontainerAudioType\x12$\n CONTAINER_AUDIO_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03WAV\x10\x01\x12\x0c\n\x08OGG_OPUS\x10\x02\"=\n\x0cTextVariable\x12\x15\n\rvariable_name\x18\x01 \x01(\t\x12\x16\n\x0evariable_value\x18\x02 \x01(\t\"]\n\rAudioVariable\x12\x15\n\rvariable_name\x18\x01 \x01(\t\x12\x19\n\x11variable_start_ms\x18\x02 \x01(\x03\x12\x1a\n\x12variable_length_ms\x18\x03 \x01(\x03\"O\n\x1aUtteranceSynthesisResponse\x12\x31\n\x0b\x61udio_chunk\x18\x01 \x01(\x0b\x32\x1c.speechkit.tts.v3.AudioChunk\"\xa9\x01\n\rAudioTemplate\x12-\n\x05\x61udio\x18\x01 \x01(\x0b\x32\x1e.speechkit.tts.v3.AudioContent\x12\x35\n\rtext_template\x18\x02 \x01(\x0b\x32\x1e.speechkit.tts.v3.TextTemplate\x12\x32\n\tvariables\x18\x03 \x03(\x0b\x32\x1f.speechkit.tts.v3.AudioVariable\"\x1a\n\nAudioChunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"X\n\x0cTextTemplate\x12\x15\n\rtext_template\x18\x01 \x01(\t\x12\x31\n\tvariables\x18\x02 \x03(\x0b\x32\x1e.speechkit.tts.v3.TextVariable\"~\n\x05Hints\x12\x0f\n\x05voice\x18\x01 \x01(\tH\x00\x12\x39\n\x0e\x61udio_template\x18\x02 \x01(\x0b\x32\x1f.speechkit.tts.v3.AudioTemplateH\x00\x12\x0f\n\x05speed\x18\x03 \x01(\x01H\x00\x12\x10\n\x06volume\x18\x04 \x01(\x01H\x00\x42\x06\n\x04Hint\"\xe9\x01\n\x19UtteranceSynthesisRequest\x12\r\n\x05model\x18\x01 \x01(\t\x12\x0e\n\x04text\x18\x02 \x01(\tH\x00\x12\x37\n\rtext_template\x18\x03 \x01(\x0b\x32\x1e.speechkit.tts.v3.TextTemplateH\x00\x12&\n\x05hints\x18\x04 \x03(\x0b\x32\x17.speechkit.tts.v3.Hints\x12?\n\x11output_audio_spec\x18\x05 \x01(\x0b\x32$.speechkit.tts.v3.AudioFormatOptionsB\x0b\n\tUtteranceB\\\n\x1ayandex.cloud.api.ai.tts.v3Z>github.com/yandex-cloud/go-genproto/yandex/cloud/ai/tts/v3;ttsb\x06proto3'
)



_RAWAUDIO_AUDIOENCODING = _descriptor.EnumDescriptor(
  name='AudioEncoding',
  full_name='speechkit.tts.v3.RawAudio.AudioEncoding',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUDIO_ENCODING_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LINEAR16_PCM', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=416,
  serialized_end=481,
)
_sym_db.RegisterEnumDescriptor(_RAWAUDIO_AUDIOENCODING)

_CONTAINERAUDIO_CONTAINERAUDIOTYPE = _descriptor.EnumDescriptor(
  name='ContainerAudioType',
  full_name='speechkit.tts.v3.ContainerAudio.ContainerAudioType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONTAINER_AUDIO_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WAV', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OGG_OPUS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=585,
  serialized_end=666,
)
_sym_db.RegisterEnumDescriptor(_CONTAINERAUDIO_CONTAINERAUDIOTYPE)


_AUDIOCONTENT = _descriptor.Descriptor(
  name='AudioContent',
  full_name='speechkit.tts.v3.AudioContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='speechkit.tts.v3.AudioContent.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audio_spec', full_name='speechkit.tts.v3.AudioContent.audio_spec', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='AudioSource', full_name='speechkit.tts.v3.AudioContent.AudioSource',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=54,
  serialized_end=160,
)


_AUDIOFORMATOPTIONS = _descriptor.Descriptor(
  name='AudioFormatOptions',
  full_name='speechkit.tts.v3.AudioFormatOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw_audio', full_name='speechkit.tts.v3.AudioFormatOptions.raw_audio', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='container_audio', full_name='speechkit.tts.v3.AudioFormatOptions.container_audio', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='AudioFormat', full_name='speechkit.tts.v3.AudioFormatOptions.AudioFormat',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=163,
  serialized_end=308,
)


_RAWAUDIO = _descriptor.Descriptor(
  name='RawAudio',
  full_name='speechkit.tts.v3.RawAudio',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio_encoding', full_name='speechkit.tts.v3.RawAudio.audio_encoding', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sample_rate_hertz', full_name='speechkit.tts.v3.RawAudio.sample_rate_hertz', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RAWAUDIO_AUDIOENCODING,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=311,
  serialized_end=481,
)


_CONTAINERAUDIO = _descriptor.Descriptor(
  name='ContainerAudio',
  full_name='speechkit.tts.v3.ContainerAudio',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_audio_type', full_name='speechkit.tts.v3.ContainerAudio.container_audio_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONTAINERAUDIO_CONTAINERAUDIOTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=484,
  serialized_end=666,
)


_TEXTVARIABLE = _descriptor.Descriptor(
  name='TextVariable',
  full_name='speechkit.tts.v3.TextVariable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='variable_name', full_name='speechkit.tts.v3.TextVariable.variable_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='variable_value', full_name='speechkit.tts.v3.TextVariable.variable_value', index=1,
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
  serialized_start=668,
  serialized_end=729,
)


_AUDIOVARIABLE = _descriptor.Descriptor(
  name='AudioVariable',
  full_name='speechkit.tts.v3.AudioVariable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='variable_name', full_name='speechkit.tts.v3.AudioVariable.variable_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='variable_start_ms', full_name='speechkit.tts.v3.AudioVariable.variable_start_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='variable_length_ms', full_name='speechkit.tts.v3.AudioVariable.variable_length_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=731,
  serialized_end=824,
)


_UTTERANCESYNTHESISRESPONSE = _descriptor.Descriptor(
  name='UtteranceSynthesisResponse',
  full_name='speechkit.tts.v3.UtteranceSynthesisResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio_chunk', full_name='speechkit.tts.v3.UtteranceSynthesisResponse.audio_chunk', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=826,
  serialized_end=905,
)


_AUDIOTEMPLATE = _descriptor.Descriptor(
  name='AudioTemplate',
  full_name='speechkit.tts.v3.AudioTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio', full_name='speechkit.tts.v3.AudioTemplate.audio', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text_template', full_name='speechkit.tts.v3.AudioTemplate.text_template', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='variables', full_name='speechkit.tts.v3.AudioTemplate.variables', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=908,
  serialized_end=1077,
)


_AUDIOCHUNK = _descriptor.Descriptor(
  name='AudioChunk',
  full_name='speechkit.tts.v3.AudioChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='speechkit.tts.v3.AudioChunk.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=1079,
  serialized_end=1105,
)


_TEXTTEMPLATE = _descriptor.Descriptor(
  name='TextTemplate',
  full_name='speechkit.tts.v3.TextTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text_template', full_name='speechkit.tts.v3.TextTemplate.text_template', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='variables', full_name='speechkit.tts.v3.TextTemplate.variables', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1107,
  serialized_end=1195,
)


_HINTS = _descriptor.Descriptor(
  name='Hints',
  full_name='speechkit.tts.v3.Hints',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='voice', full_name='speechkit.tts.v3.Hints.voice', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audio_template', full_name='speechkit.tts.v3.Hints.audio_template', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speed', full_name='speechkit.tts.v3.Hints.speed', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='volume', full_name='speechkit.tts.v3.Hints.volume', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
    _descriptor.OneofDescriptor(
      name='Hint', full_name='speechkit.tts.v3.Hints.Hint',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1197,
  serialized_end=1323,
)


_UTTERANCESYNTHESISREQUEST = _descriptor.Descriptor(
  name='UtteranceSynthesisRequest',
  full_name='speechkit.tts.v3.UtteranceSynthesisRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='speechkit.tts.v3.UtteranceSynthesisRequest.model', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='speechkit.tts.v3.UtteranceSynthesisRequest.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text_template', full_name='speechkit.tts.v3.UtteranceSynthesisRequest.text_template', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hints', full_name='speechkit.tts.v3.UtteranceSynthesisRequest.hints', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_audio_spec', full_name='speechkit.tts.v3.UtteranceSynthesisRequest.output_audio_spec', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='Utterance', full_name='speechkit.tts.v3.UtteranceSynthesisRequest.Utterance',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1326,
  serialized_end=1559,
)

_AUDIOCONTENT.fields_by_name['audio_spec'].message_type = _AUDIOFORMATOPTIONS
_AUDIOCONTENT.oneofs_by_name['AudioSource'].fields.append(
  _AUDIOCONTENT.fields_by_name['content'])
_AUDIOCONTENT.fields_by_name['content'].containing_oneof = _AUDIOCONTENT.oneofs_by_name['AudioSource']
_AUDIOFORMATOPTIONS.fields_by_name['raw_audio'].message_type = _RAWAUDIO
_AUDIOFORMATOPTIONS.fields_by_name['container_audio'].message_type = _CONTAINERAUDIO
_AUDIOFORMATOPTIONS.oneofs_by_name['AudioFormat'].fields.append(
  _AUDIOFORMATOPTIONS.fields_by_name['raw_audio'])
_AUDIOFORMATOPTIONS.fields_by_name['raw_audio'].containing_oneof = _AUDIOFORMATOPTIONS.oneofs_by_name['AudioFormat']
_AUDIOFORMATOPTIONS.oneofs_by_name['AudioFormat'].fields.append(
  _AUDIOFORMATOPTIONS.fields_by_name['container_audio'])
_AUDIOFORMATOPTIONS.fields_by_name['container_audio'].containing_oneof = _AUDIOFORMATOPTIONS.oneofs_by_name['AudioFormat']
_RAWAUDIO.fields_by_name['audio_encoding'].enum_type = _RAWAUDIO_AUDIOENCODING
_RAWAUDIO_AUDIOENCODING.containing_type = _RAWAUDIO
_CONTAINERAUDIO.fields_by_name['container_audio_type'].enum_type = _CONTAINERAUDIO_CONTAINERAUDIOTYPE
_CONTAINERAUDIO_CONTAINERAUDIOTYPE.containing_type = _CONTAINERAUDIO
_UTTERANCESYNTHESISRESPONSE.fields_by_name['audio_chunk'].message_type = _AUDIOCHUNK
_AUDIOTEMPLATE.fields_by_name['audio'].message_type = _AUDIOCONTENT
_AUDIOTEMPLATE.fields_by_name['text_template'].message_type = _TEXTTEMPLATE
_AUDIOTEMPLATE.fields_by_name['variables'].message_type = _AUDIOVARIABLE
_TEXTTEMPLATE.fields_by_name['variables'].message_type = _TEXTVARIABLE
_HINTS.fields_by_name['audio_template'].message_type = _AUDIOTEMPLATE
_HINTS.oneofs_by_name['Hint'].fields.append(
  _HINTS.fields_by_name['voice'])
_HINTS.fields_by_name['voice'].containing_oneof = _HINTS.oneofs_by_name['Hint']
_HINTS.oneofs_by_name['Hint'].fields.append(
  _HINTS.fields_by_name['audio_template'])
_HINTS.fields_by_name['audio_template'].containing_oneof = _HINTS.oneofs_by_name['Hint']
_HINTS.oneofs_by_name['Hint'].fields.append(
  _HINTS.fields_by_name['speed'])
_HINTS.fields_by_name['speed'].containing_oneof = _HINTS.oneofs_by_name['Hint']
_HINTS.oneofs_by_name['Hint'].fields.append(
  _HINTS.fields_by_name['volume'])
_HINTS.fields_by_name['volume'].containing_oneof = _HINTS.oneofs_by_name['Hint']
_UTTERANCESYNTHESISREQUEST.fields_by_name['text_template'].message_type = _TEXTTEMPLATE
_UTTERANCESYNTHESISREQUEST.fields_by_name['hints'].message_type = _HINTS
_UTTERANCESYNTHESISREQUEST.fields_by_name['output_audio_spec'].message_type = _AUDIOFORMATOPTIONS
_UTTERANCESYNTHESISREQUEST.oneofs_by_name['Utterance'].fields.append(
  _UTTERANCESYNTHESISREQUEST.fields_by_name['text'])
_UTTERANCESYNTHESISREQUEST.fields_by_name['text'].containing_oneof = _UTTERANCESYNTHESISREQUEST.oneofs_by_name['Utterance']
_UTTERANCESYNTHESISREQUEST.oneofs_by_name['Utterance'].fields.append(
  _UTTERANCESYNTHESISREQUEST.fields_by_name['text_template'])
_UTTERANCESYNTHESISREQUEST.fields_by_name['text_template'].containing_oneof = _UTTERANCESYNTHESISREQUEST.oneofs_by_name['Utterance']
DESCRIPTOR.message_types_by_name['AudioContent'] = _AUDIOCONTENT
DESCRIPTOR.message_types_by_name['AudioFormatOptions'] = _AUDIOFORMATOPTIONS
DESCRIPTOR.message_types_by_name['RawAudio'] = _RAWAUDIO
DESCRIPTOR.message_types_by_name['ContainerAudio'] = _CONTAINERAUDIO
DESCRIPTOR.message_types_by_name['TextVariable'] = _TEXTVARIABLE
DESCRIPTOR.message_types_by_name['AudioVariable'] = _AUDIOVARIABLE
DESCRIPTOR.message_types_by_name['UtteranceSynthesisResponse'] = _UTTERANCESYNTHESISRESPONSE
DESCRIPTOR.message_types_by_name['AudioTemplate'] = _AUDIOTEMPLATE
DESCRIPTOR.message_types_by_name['AudioChunk'] = _AUDIOCHUNK
DESCRIPTOR.message_types_by_name['TextTemplate'] = _TEXTTEMPLATE
DESCRIPTOR.message_types_by_name['Hints'] = _HINTS
DESCRIPTOR.message_types_by_name['UtteranceSynthesisRequest'] = _UTTERANCESYNTHESISREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AudioContent = _reflection.GeneratedProtocolMessageType('AudioContent', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOCONTENT,
  '__module__' : 'yandex.cloud.ai.tts.v3.tts_pb2'
  # @@protoc_insertion_point(class_scope:speechkit.tts.v3.AudioContent)
  })
_sym_db.RegisterMessage(AudioContent)

AudioFormatOptions = _reflection.GeneratedProtocolMessageType('AudioFormatOptions', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOFORMATOPTIONS,
  '__module__' : 'yandex.cloud.ai.tts.v3.tts_pb2'
  # @@protoc_insertion_point(class_scope:speechkit.tts.v3.AudioFormatOptions)
  })
_sym_db.RegisterMessage(AudioFormatOptions)

RawAudio = _reflection.GeneratedProtocolMessageType('RawAudio', (_message.Message,), {
  'DESCRIPTOR' : _RAWAUDIO,
  '__module__' : 'yandex.cloud.ai.tts.v3.tts_pb2'
  # @@protoc_insertion_point(class_scope:speechkit.tts.v3.RawAudio)
  })
_sym_db.RegisterMessage(RawAudio)

ContainerAudio = _reflection.GeneratedProtocolMessageType('ContainerAudio', (_message.Message,), {
  'DESCRIPTOR' : _CONTAINERAUDIO,
  '__module__' : 'yandex.cloud.ai.tts.v3.tts_pb2'
  # @@protoc_insertion_point(class_scope:speechkit.tts.v3.ContainerAudio)
  })
_sym_db.RegisterMessage(ContainerAudio)

TextVariable = _reflection.GeneratedProtocolMessageType('TextVariable', (_message.Message,), {
  'DESCRIPTOR' : _TEXTVARIABLE,
  '__module__' : 'yandex.cloud.ai.tts.v3.tts_pb2'
  # @@protoc_insertion_point(class_scope:speechkit.tts.v3.TextVariable)
  })
_sym_db.RegisterMessage(TextVariable)

AudioVariable = _reflection.GeneratedProtocolMessageType('AudioVariable', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOVARIABLE,
  '__module__' : 'yandex.cloud.ai.tts.v3.tts_pb2'
  # @@protoc_insertion_point(class_scope:speechkit.tts.v3.AudioVariable)
  })
_sym_db.RegisterMessage(AudioVariable)

UtteranceSynthesisResponse = _reflection.GeneratedProtocolMessageType('UtteranceSynthesisResponse', (_message.Message,), {
  'DESCRIPTOR' : _UTTERANCESYNTHESISRESPONSE,
  '__module__' : 'yandex.cloud.ai.tts.v3.tts_pb2'
  # @@protoc_insertion_point(class_scope:speechkit.tts.v3.UtteranceSynthesisResponse)
  })
_sym_db.RegisterMessage(UtteranceSynthesisResponse)

AudioTemplate = _reflection.GeneratedProtocolMessageType('AudioTemplate', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOTEMPLATE,
  '__module__' : 'yandex.cloud.ai.tts.v3.tts_pb2'
  # @@protoc_insertion_point(class_scope:speechkit.tts.v3.AudioTemplate)
  })
_sym_db.RegisterMessage(AudioTemplate)

AudioChunk = _reflection.GeneratedProtocolMessageType('AudioChunk', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOCHUNK,
  '__module__' : 'yandex.cloud.ai.tts.v3.tts_pb2'
  # @@protoc_insertion_point(class_scope:speechkit.tts.v3.AudioChunk)
  })
_sym_db.RegisterMessage(AudioChunk)

TextTemplate = _reflection.GeneratedProtocolMessageType('TextTemplate', (_message.Message,), {
  'DESCRIPTOR' : _TEXTTEMPLATE,
  '__module__' : 'yandex.cloud.ai.tts.v3.tts_pb2'
  # @@protoc_insertion_point(class_scope:speechkit.tts.v3.TextTemplate)
  })
_sym_db.RegisterMessage(TextTemplate)

Hints = _reflection.GeneratedProtocolMessageType('Hints', (_message.Message,), {
  'DESCRIPTOR' : _HINTS,
  '__module__' : 'yandex.cloud.ai.tts.v3.tts_pb2'
  # @@protoc_insertion_point(class_scope:speechkit.tts.v3.Hints)
  })
_sym_db.RegisterMessage(Hints)

UtteranceSynthesisRequest = _reflection.GeneratedProtocolMessageType('UtteranceSynthesisRequest', (_message.Message,), {
  'DESCRIPTOR' : _UTTERANCESYNTHESISREQUEST,
  '__module__' : 'yandex.cloud.ai.tts.v3.tts_pb2'
  # @@protoc_insertion_point(class_scope:speechkit.tts.v3.UtteranceSynthesisRequest)
  })
_sym_db.RegisterMessage(UtteranceSynthesisRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
