# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cdkey.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cdkey.proto',
  package='',
  serialized_pb='\n\x0b\x63\x64key.proto\x1a\x0c\x63ommon.proto\"\x1d\n\x0c\x43\x64keyRequest\x12\r\n\x05\x63\x64key\x18\x01 \x02(\t\"S\n\rCdkeyResqonse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12$\n\x04gain\x18\x02 \x01(\x0b\x32\x16.GameResourcesResponse')




_CDKEYREQUEST = _descriptor.Descriptor(
  name='CdkeyRequest',
  full_name='CdkeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cdkey', full_name='CdkeyRequest.cdkey', index=0,
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
  serialized_start=29,
  serialized_end=58,
)


_CDKEYRESQONSE = _descriptor.Descriptor(
  name='CdkeyResqonse',
  full_name='CdkeyResqonse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='CdkeyResqonse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gain', full_name='CdkeyResqonse.gain', index=1,
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
  serialized_start=60,
  serialized_end=143,
)

_CDKEYRESQONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_CDKEYRESQONSE.fields_by_name['gain'].message_type = common_pb2._GAMERESOURCESRESPONSE
DESCRIPTOR.message_types_by_name['CdkeyRequest'] = _CDKEYREQUEST
DESCRIPTOR.message_types_by_name['CdkeyResqonse'] = _CDKEYRESQONSE

class CdkeyRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDKEYREQUEST

  # @@protoc_insertion_point(class_scope:CdkeyRequest)

class CdkeyResqonse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDKEYRESQONSE

  # @@protoc_insertion_point(class_scope:CdkeyResqonse)


# @@protoc_insertion_point(module_scope)
