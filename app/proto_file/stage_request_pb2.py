# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stage_request.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import stage_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stage_request.proto',
  package='',
  serialized_pb='\n\x13stage_request.proto\x1a\x0bstage.proto\"$\n\x10StageInfoRequest\x12\x10\n\x08stage_id\x18\x01 \x02(\x05\"(\n\x12\x43hapterInfoRequest\x12\x12\n\nchapter_id\x18\x01 \x02(\x05\"l\n\x11StageStartRequest\x12\x10\n\x08stage_id\x18\x01 \x02(\x05\x12\x12\n\nstage_type\x18\x02 \x02(\x05\x12\x0e\n\x06lineup\x18\x03 \x03(\x05\x12\x14\n\x0cunparalleled\x18\x04 \x01(\x05\x12\x0b\n\x03\x66id\x18\x05 \x01(\x05\"y\n\x16StageSettlementRequest\x12\x10\n\x08stage_id\x18\x01 \x02(\x05\x12\x12\n\nstage_type\x18\x02 \x02(\x05\x12\x18\n\x05steps\x18\x03 \x03(\x0b\x32\t.StepInfo\x12\x0e\n\x06result\x18\x04 \x02(\x08\x12\x0f\n\x07is_skip\x18\x05 \x01(\x08\"H\n\x11StageSweepRequest\x12\x10\n\x08stage_id\x18\x01 \x02(\x05\x12\r\n\x05times\x18\x02 \x02(\x05\x12\x12\n\nsweep_type\x18\x03 \x02(\x05\"%\n\x11ResetStageRequest\x12\x10\n\x08stage_id\x18\x01 \x02(\x05\":\n\x10StarAwardRequest\x12\x12\n\nchapter_id\x18\x01 \x02(\x05\x12\x12\n\naward_type\x18\x02 \x02(\x05\".\n\x18UpdataPlotChapterRequest\x12\x12\n\nchapter_id\x18\x01 \x02(\x05\")\n\x15OpenStageChestRequest\x12\x10\n\x08stage_id\x18\x01 \x02(\x05')




_STAGEINFOREQUEST = _descriptor.Descriptor(
  name='StageInfoRequest',
  full_name='StageInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage_id', full_name='StageInfoRequest.stage_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=36,
  serialized_end=72,
)


_CHAPTERINFOREQUEST = _descriptor.Descriptor(
  name='ChapterInfoRequest',
  full_name='ChapterInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chapter_id', full_name='ChapterInfoRequest.chapter_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=74,
  serialized_end=114,
)


_STAGESTARTREQUEST = _descriptor.Descriptor(
  name='StageStartRequest',
  full_name='StageStartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage_id', full_name='StageStartRequest.stage_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stage_type', full_name='StageStartRequest.stage_type', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lineup', full_name='StageStartRequest.lineup', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unparalleled', full_name='StageStartRequest.unparalleled', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fid', full_name='StageStartRequest.fid', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=116,
  serialized_end=224,
)


_STAGESETTLEMENTREQUEST = _descriptor.Descriptor(
  name='StageSettlementRequest',
  full_name='StageSettlementRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage_id', full_name='StageSettlementRequest.stage_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stage_type', full_name='StageSettlementRequest.stage_type', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='steps', full_name='StageSettlementRequest.steps', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='StageSettlementRequest.result', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_skip', full_name='StageSettlementRequest.is_skip', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=226,
  serialized_end=347,
)


_STAGESWEEPREQUEST = _descriptor.Descriptor(
  name='StageSweepRequest',
  full_name='StageSweepRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage_id', full_name='StageSweepRequest.stage_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='times', full_name='StageSweepRequest.times', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sweep_type', full_name='StageSweepRequest.sweep_type', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=349,
  serialized_end=421,
)


_RESETSTAGEREQUEST = _descriptor.Descriptor(
  name='ResetStageRequest',
  full_name='ResetStageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage_id', full_name='ResetStageRequest.stage_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=423,
  serialized_end=460,
)


_STARAWARDREQUEST = _descriptor.Descriptor(
  name='StarAwardRequest',
  full_name='StarAwardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chapter_id', full_name='StarAwardRequest.chapter_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='award_type', full_name='StarAwardRequest.award_type', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=462,
  serialized_end=520,
)


_UPDATAPLOTCHAPTERREQUEST = _descriptor.Descriptor(
  name='UpdataPlotChapterRequest',
  full_name='UpdataPlotChapterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chapter_id', full_name='UpdataPlotChapterRequest.chapter_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=522,
  serialized_end=568,
)


_OPENSTAGECHESTREQUEST = _descriptor.Descriptor(
  name='OpenStageChestRequest',
  full_name='OpenStageChestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage_id', full_name='OpenStageChestRequest.stage_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=570,
  serialized_end=611,
)

_STAGESETTLEMENTREQUEST.fields_by_name['steps'].message_type = stage_pb2._STEPINFO
DESCRIPTOR.message_types_by_name['StageInfoRequest'] = _STAGEINFOREQUEST
DESCRIPTOR.message_types_by_name['ChapterInfoRequest'] = _CHAPTERINFOREQUEST
DESCRIPTOR.message_types_by_name['StageStartRequest'] = _STAGESTARTREQUEST
DESCRIPTOR.message_types_by_name['StageSettlementRequest'] = _STAGESETTLEMENTREQUEST
DESCRIPTOR.message_types_by_name['StageSweepRequest'] = _STAGESWEEPREQUEST
DESCRIPTOR.message_types_by_name['ResetStageRequest'] = _RESETSTAGEREQUEST
DESCRIPTOR.message_types_by_name['StarAwardRequest'] = _STARAWARDREQUEST
DESCRIPTOR.message_types_by_name['UpdataPlotChapterRequest'] = _UPDATAPLOTCHAPTERREQUEST
DESCRIPTOR.message_types_by_name['OpenStageChestRequest'] = _OPENSTAGECHESTREQUEST

class StageInfoRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STAGEINFOREQUEST

  # @@protoc_insertion_point(class_scope:StageInfoRequest)

class ChapterInfoRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHAPTERINFOREQUEST

  # @@protoc_insertion_point(class_scope:ChapterInfoRequest)

class StageStartRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STAGESTARTREQUEST

  # @@protoc_insertion_point(class_scope:StageStartRequest)

class StageSettlementRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STAGESETTLEMENTREQUEST

  # @@protoc_insertion_point(class_scope:StageSettlementRequest)

class StageSweepRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STAGESWEEPREQUEST

  # @@protoc_insertion_point(class_scope:StageSweepRequest)

class ResetStageRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESETSTAGEREQUEST

  # @@protoc_insertion_point(class_scope:ResetStageRequest)

class StarAwardRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STARAWARDREQUEST

  # @@protoc_insertion_point(class_scope:StarAwardRequest)

class UpdataPlotChapterRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UPDATAPLOTCHAPTERREQUEST

  # @@protoc_insertion_point(class_scope:UpdataPlotChapterRequest)

class OpenStageChestRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OPENSTAGECHESTREQUEST

  # @@protoc_insertion_point(class_scope:OpenStageChestRequest)


# @@protoc_insertion_point(module_scope)
