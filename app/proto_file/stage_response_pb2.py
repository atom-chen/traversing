# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stage_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import stage_pb2
import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stage_response.proto',
  package='',
  serialized_pb='\n\x14stage_response.proto\x1a\x0bstage.proto\x1a\x0c\x63ommon.proto\"^\n\x11StageInfoResponse\x12\x15\n\x05stage\x18\x01 \x03(\x0b\x32\x06.Stage\x12\x19\n\x11\x65lite_stage_times\x18\x02 \x02(\x05\x12\x17\n\x0f\x61\x63t_stage_times\x18\x03 \x02(\x05\"7\n\x13\x43hapterInfoResponse\x12 \n\x0bstage_award\x18\x01 \x03(\x0b\x32\x0b.StageAward\"\xdd\x02\n\x12StageStartResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\x10\n\x08\x64rop_num\x18\x02 \x01(\x05\x12\x18\n\x03red\x18\x04 \x03(\x0b\x32\x0b.BattleUnit\x12\x1d\n\x04\x62lue\x18\x05 \x03(\x0b\x32\x0f.BattleUnitGrop\x12\x1b\n\x06\x66riend\x18\x06 \x01(\x0b\x32\x0b.BattleUnit\x12\x12\n\nhero_unpar\x18\x07 \x01(\x05\x12\x18\n\x10hero_unpar_level\x18\x08 \x01(\x05\x12\x15\n\rmonster_unpar\x18\t \x01(\x05\x12\x1c\n\x07replace\x18\n \x01(\x0b\x32\x0b.BattleUnit\x12\x12\n\nreplace_no\x18\x0b \x01(\x05\x12\x1a\n\x05\x61wake\x18\x0c \x03(\x0b\x32\x0b.BattleUnit\x12\x10\n\x08\x61wake_no\x18\r \x03(\x05\x12\r\n\x05seed1\x18\x0e \x01(\x05\x12\r\n\x05seed2\x18\x0f \x01(\x05\"^\n\x17StageSettlementResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12%\n\x05\x64rops\x18\x02 \x01(\x0b\x32\x16.GameResourcesResponse\",\n\x11\x46ormationResponse\x12\x17\n\x06lineup\x18\x01 \x03(\x0b\x32\x07.LineUp\"4\n\x14UnparalleledResponse\x12\x1c\n\x05unpar\x18\x01 \x03(\x0b\x32\r.Unparalleled\"Y\n\x12StageSweepResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12%\n\x05\x64rops\x18\x02 \x03(\x0b\x32\x16.GameResourcesResponse\"2\n\x12ResetStageResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse')




_STAGEINFORESPONSE = _descriptor.Descriptor(
  name='StageInfoResponse',
  full_name='StageInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage', full_name='StageInfoResponse.stage', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='elite_stage_times', full_name='StageInfoResponse.elite_stage_times', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='act_stage_times', full_name='StageInfoResponse.act_stage_times', index=2,
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
  serialized_start=51,
  serialized_end=145,
)


_CHAPTERINFORESPONSE = _descriptor.Descriptor(
  name='ChapterInfoResponse',
  full_name='ChapterInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage_award', full_name='ChapterInfoResponse.stage_award', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=147,
  serialized_end=202,
)


_STAGESTARTRESPONSE = _descriptor.Descriptor(
  name='StageStartResponse',
  full_name='StageStartResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='StageStartResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop_num', full_name='StageStartResponse.drop_num', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='red', full_name='StageStartResponse.red', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blue', full_name='StageStartResponse.blue', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friend', full_name='StageStartResponse.friend', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_unpar', full_name='StageStartResponse.hero_unpar', index=5,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_unpar_level', full_name='StageStartResponse.hero_unpar_level', index=6,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='monster_unpar', full_name='StageStartResponse.monster_unpar', index=7,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='replace', full_name='StageStartResponse.replace', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='replace_no', full_name='StageStartResponse.replace_no', index=9,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='awake', full_name='StageStartResponse.awake', index=10,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='awake_no', full_name='StageStartResponse.awake_no', index=11,
      number=13, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seed1', full_name='StageStartResponse.seed1', index=12,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seed2', full_name='StageStartResponse.seed2', index=13,
      number=15, type=5, cpp_type=1, label=1,
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
  serialized_start=205,
  serialized_end=554,
)


_STAGESETTLEMENTRESPONSE = _descriptor.Descriptor(
  name='StageSettlementResponse',
  full_name='StageSettlementResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='StageSettlementResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drops', full_name='StageSettlementResponse.drops', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=556,
  serialized_end=650,
)


_FORMATIONRESPONSE = _descriptor.Descriptor(
  name='FormationResponse',
  full_name='FormationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lineup', full_name='FormationResponse.lineup', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=652,
  serialized_end=696,
)


_UNPARALLELEDRESPONSE = _descriptor.Descriptor(
  name='UnparalleledResponse',
  full_name='UnparalleledResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unpar', full_name='UnparalleledResponse.unpar', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=698,
  serialized_end=750,
)


_STAGESWEEPRESPONSE = _descriptor.Descriptor(
  name='StageSweepResponse',
  full_name='StageSweepResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='StageSweepResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drops', full_name='StageSweepResponse.drops', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=752,
  serialized_end=841,
)


_RESETSTAGERESPONSE = _descriptor.Descriptor(
  name='ResetStageResponse',
  full_name='ResetStageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='ResetStageResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=843,
  serialized_end=893,
)

_STAGEINFORESPONSE.fields_by_name['stage'].message_type = stage_pb2._STAGE
_CHAPTERINFORESPONSE.fields_by_name['stage_award'].message_type = stage_pb2._STAGEAWARD
_STAGESTARTRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_STAGESTARTRESPONSE.fields_by_name['red'].message_type = stage_pb2._BATTLEUNIT
_STAGESTARTRESPONSE.fields_by_name['blue'].message_type = stage_pb2._BATTLEUNITGROP
_STAGESTARTRESPONSE.fields_by_name['friend'].message_type = stage_pb2._BATTLEUNIT
_STAGESTARTRESPONSE.fields_by_name['replace'].message_type = stage_pb2._BATTLEUNIT
_STAGESTARTRESPONSE.fields_by_name['awake'].message_type = stage_pb2._BATTLEUNIT
_STAGESETTLEMENTRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_STAGESETTLEMENTRESPONSE.fields_by_name['drops'].message_type = common_pb2._GAMERESOURCESRESPONSE
_FORMATIONRESPONSE.fields_by_name['lineup'].message_type = stage_pb2._LINEUP
_UNPARALLELEDRESPONSE.fields_by_name['unpar'].message_type = stage_pb2._UNPARALLELED
_STAGESWEEPRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_STAGESWEEPRESPONSE.fields_by_name['drops'].message_type = common_pb2._GAMERESOURCESRESPONSE
_RESETSTAGERESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
DESCRIPTOR.message_types_by_name['StageInfoResponse'] = _STAGEINFORESPONSE
DESCRIPTOR.message_types_by_name['ChapterInfoResponse'] = _CHAPTERINFORESPONSE
DESCRIPTOR.message_types_by_name['StageStartResponse'] = _STAGESTARTRESPONSE
DESCRIPTOR.message_types_by_name['StageSettlementResponse'] = _STAGESETTLEMENTRESPONSE
DESCRIPTOR.message_types_by_name['FormationResponse'] = _FORMATIONRESPONSE
DESCRIPTOR.message_types_by_name['UnparalleledResponse'] = _UNPARALLELEDRESPONSE
DESCRIPTOR.message_types_by_name['StageSweepResponse'] = _STAGESWEEPRESPONSE
DESCRIPTOR.message_types_by_name['ResetStageResponse'] = _RESETSTAGERESPONSE

class StageInfoResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STAGEINFORESPONSE

  # @@protoc_insertion_point(class_scope:StageInfoResponse)

class ChapterInfoResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHAPTERINFORESPONSE

  # @@protoc_insertion_point(class_scope:ChapterInfoResponse)

class StageStartResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STAGESTARTRESPONSE

  # @@protoc_insertion_point(class_scope:StageStartResponse)

class StageSettlementResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STAGESETTLEMENTRESPONSE

  # @@protoc_insertion_point(class_scope:StageSettlementResponse)

class FormationResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FORMATIONRESPONSE

  # @@protoc_insertion_point(class_scope:FormationResponse)

class UnparalleledResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UNPARALLELEDRESPONSE

  # @@protoc_insertion_point(class_scope:UnparalleledResponse)

class StageSweepResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STAGESWEEPRESPONSE

  # @@protoc_insertion_point(class_scope:StageSweepResponse)

class ResetStageResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESETSTAGERESPONSE

  # @@protoc_insertion_point(class_scope:ResetStageResponse)


# @@protoc_insertion_point(module_scope)
