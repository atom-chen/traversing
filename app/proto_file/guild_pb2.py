# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: guild.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='guild.proto',
  package='',
  serialized_pb='\n\x0bguild.proto\x1a\x0c\x63ommon.proto\"\"\n\x12\x43reateGuildRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"3\n\x13\x43reateGuildResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse')




_CREATEGUILDREQUEST = _descriptor.Descriptor(
  name='CreateGuildRequest',
  full_name='CreateGuildRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CreateGuildRequest.name', index=0,
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
  serialized_start=29,
  serialized_end=63,
)


_CREATEGUILDRESPONSE = _descriptor.Descriptor(
  name='CreateGuildResponse',
  full_name='CreateGuildResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='CreateGuildResponse.res', index=0,
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
  serialized_start=65,
  serialized_end=116,
)

_CREATEGUILDRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
DESCRIPTOR.message_types_by_name['CreateGuildRequest'] = _CREATEGUILDREQUEST
DESCRIPTOR.message_types_by_name['CreateGuildResponse'] = _CREATEGUILDRESPONSE

class CreateGuildRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CREATEGUILDREQUEST

  # @@protoc_insertion_point(class_scope:CreateGuildRequest)

class CreateGuildResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CREATEGUILDRESPONSE

  # @@protoc_insertion_point(class_scope:CreateGuildResponse)


# @@protoc_insertion_point(module_scope)
