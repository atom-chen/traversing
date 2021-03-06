# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: player_request.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='player_request.proto',
  package='',
  serialized_pb='\n\x14player_request.proto\"#\n\x12PlayerLoginRequest\x12\r\n\x05token\x18\x01 \x02(\t\"\'\n\x13\x43reatePlayerRequest\x12\x10\n\x08nickname\x18\x01 \x01(\t\"S\n\x16NewbeeGuideStepRequest\x12\x0f\n\x07step_id\x18\x01 \x02(\x05\x12\x11\n\tcommon_id\x18\x02 \x01(\t\x12\x15\n\rsub_common_id\x18\x03 \x01(\t\"$\n\x11\x43hangeHeadRequest\x12\x0f\n\x07hero_id\x18\x01 \x02(\x05\"\"\n\x11\x43hangeBattleSpeed\x12\r\n\x05speed\x18\x01 \x02(\x05\"$\n\x10\x43hangeStageStory\x12\x10\n\x08story_id\x18\x01 \x02(\x05')




_PLAYERLOGINREQUEST = _descriptor.Descriptor(
  name='PlayerLoginRequest',
  full_name='PlayerLoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='PlayerLoginRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=24,
  serialized_end=59,
)


_CREATEPLAYERREQUEST = _descriptor.Descriptor(
  name='CreatePlayerRequest',
  full_name='CreatePlayerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nickname', full_name='CreatePlayerRequest.nickname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=61,
  serialized_end=100,
)


_NEWBEEGUIDESTEPREQUEST = _descriptor.Descriptor(
  name='NewbeeGuideStepRequest',
  full_name='NewbeeGuideStepRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step_id', full_name='NewbeeGuideStepRequest.step_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='common_id', full_name='NewbeeGuideStepRequest.common_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sub_common_id', full_name='NewbeeGuideStepRequest.sub_common_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=102,
  serialized_end=185,
)


_CHANGEHEADREQUEST = _descriptor.Descriptor(
  name='ChangeHeadRequest',
  full_name='ChangeHeadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero_id', full_name='ChangeHeadRequest.hero_id', index=0,
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
  serialized_start=187,
  serialized_end=223,
)


_CHANGEBATTLESPEED = _descriptor.Descriptor(
  name='ChangeBattleSpeed',
  full_name='ChangeBattleSpeed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='speed', full_name='ChangeBattleSpeed.speed', index=0,
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
  serialized_start=225,
  serialized_end=259,
)


_CHANGESTAGESTORY = _descriptor.Descriptor(
  name='ChangeStageStory',
  full_name='ChangeStageStory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='story_id', full_name='ChangeStageStory.story_id', index=0,
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
  serialized_start=261,
  serialized_end=297,
)

DESCRIPTOR.message_types_by_name['PlayerLoginRequest'] = _PLAYERLOGINREQUEST
DESCRIPTOR.message_types_by_name['CreatePlayerRequest'] = _CREATEPLAYERREQUEST
DESCRIPTOR.message_types_by_name['NewbeeGuideStepRequest'] = _NEWBEEGUIDESTEPREQUEST
DESCRIPTOR.message_types_by_name['ChangeHeadRequest'] = _CHANGEHEADREQUEST
DESCRIPTOR.message_types_by_name['ChangeBattleSpeed'] = _CHANGEBATTLESPEED
DESCRIPTOR.message_types_by_name['ChangeStageStory'] = _CHANGESTAGESTORY

class PlayerLoginRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PLAYERLOGINREQUEST

  # @@protoc_insertion_point(class_scope:PlayerLoginRequest)

class CreatePlayerRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CREATEPLAYERREQUEST

  # @@protoc_insertion_point(class_scope:CreatePlayerRequest)

class NewbeeGuideStepRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NEWBEEGUIDESTEPREQUEST

  # @@protoc_insertion_point(class_scope:NewbeeGuideStepRequest)

class ChangeHeadRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHANGEHEADREQUEST

  # @@protoc_insertion_point(class_scope:ChangeHeadRequest)

class ChangeBattleSpeed(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHANGEBATTLESPEED

  # @@protoc_insertion_point(class_scope:ChangeBattleSpeed)

class ChangeStageStory(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHANGESTAGESTORY

  # @@protoc_insertion_point(class_scope:ChangeStageStory)


# @@protoc_insertion_point(module_scope)
