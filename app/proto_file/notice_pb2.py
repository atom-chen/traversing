# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: notice.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='notice.proto',
  package='',
  serialized_pb='\n\x0cnotice.proto\"\x86\x01\n\x0eNoticeResponse\x12\x11\n\tnotice_id\x18\x01 \x01(\x05\x12\x13\n\x0bplayer_name\x18\x02 \x01(\t\x12\x0f\n\x07hero_no\x18\x03 \x01(\x05\x12\x18\n\x10hero_break_level\x18\x04 \x01(\x05\x12\x14\n\x0c\x65quipment_no\x18\x05 \x01(\x05\x12\x0b\n\x03msg\x18\x06 \x01(\t')




_NOTICERESPONSE = _descriptor.Descriptor(
  name='NoticeResponse',
  full_name='NoticeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='notice_id', full_name='NoticeResponse.notice_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_name', full_name='NoticeResponse.player_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_no', full_name='NoticeResponse.hero_no', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_break_level', full_name='NoticeResponse.hero_break_level', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equipment_no', full_name='NoticeResponse.equipment_no', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='NoticeResponse.msg', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=17,
  serialized_end=151,
)

DESCRIPTOR.message_types_by_name['NoticeResponse'] = _NOTICERESPONSE

class NoticeResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NOTICERESPONSE

  # @@protoc_insertion_point(class_scope:NoticeResponse)


# @@protoc_insertion_point(module_scope)
