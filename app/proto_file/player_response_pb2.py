# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: player_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
# @@protoc_insertion_point(imports)
from app.proto_file import hero_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='player_response.proto',
  package='',
  serialized_pb='\n\x15player_response.proto\x1a\nhero.proto\"K\n\x0ePlayerResponse\x12\n\n\x02id\x18\x01 \x02(\x03\x12\x10\n\x08nickname\x18\x02 \x02(\t\x12\x1b\n\thero_list\x18\x03 \x03(\x0b\x32\x08.Hero_PB')




_PLAYERRESPONSE = _descriptor.Descriptor(
  name='PlayerResponse',
  full_name='PlayerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PlayerResponse.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='PlayerResponse.nickname', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_list', full_name='PlayerResponse.hero_list', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=37,
  serialized_end=112,
)

_PLAYERRESPONSE.fields_by_name['hero_list'].message_type = hero_pb2._HERO_PB
DESCRIPTOR.message_types_by_name['PlayerResponse'] = _PLAYERRESPONSE

class PlayerResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PLAYERRESPONSE

  # @@protoc_insertion_point(class_scope:PlayerResponse)


# @@protoc_insertion_point(module_scope)