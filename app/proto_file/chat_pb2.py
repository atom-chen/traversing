# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chat.proto',
  package='',
  serialized_pb='\n\nchat.proto\".\n\x0e\x43hatObjectInfo\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x10\n\x08nickname\x18\x02 \x01(\t\"4\n\x12LoginToChatRequest\x12\x1e\n\x05owner\x18\x01 \x02(\x0b\x32\x0f.ChatObjectInfo\"x\n\x14\x43hatConectingRequest\x12\x1e\n\x05owner\x18\x01 \x02(\x0b\x32\x0f.ChatObjectInfo\x12\x0f\n\x07\x63hannel\x18\x02 \x02(\x05\x12\x0f\n\x07\x63ontent\x18\x03 \x02(\t\x12\x1e\n\x05other\x18\x04 \x01(\x0b\x32\x0f.ChatObjectInfo\"/\n\x0c\x43hatResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"W\n\x13\x63hatMessageResponse\x12\x0f\n\x07\x63hannel\x18\x01 \x02(\x05\x12\x1e\n\x05owner\x18\x02 \x02(\x0b\x32\x0f.ChatObjectInfo\x12\x0f\n\x07\x63ontent\x18\x05 \x02(\t')




_CHATOBJECTINFO = _descriptor.Descriptor(
  name='ChatObjectInfo',
  full_name='ChatObjectInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ChatObjectInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='ChatObjectInfo.nickname', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=14,
  serialized_end=60,
)


_LOGINTOCHATREQUEST = _descriptor.Descriptor(
  name='LoginToChatRequest',
  full_name='LoginToChatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='LoginToChatRequest.owner', index=0,
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
  serialized_start=62,
  serialized_end=114,
)


_CHATCONECTINGREQUEST = _descriptor.Descriptor(
  name='ChatConectingRequest',
  full_name='ChatConectingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='ChatConectingRequest.owner', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='ChatConectingRequest.channel', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='ChatConectingRequest.content', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='other', full_name='ChatConectingRequest.other', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=116,
  serialized_end=236,
)


_CHATRESPONSE = _descriptor.Descriptor(
  name='ChatResponse',
  full_name='ChatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='ChatResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='ChatResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=238,
  serialized_end=285,
)


_CHATMESSAGERESPONSE = _descriptor.Descriptor(
  name='chatMessageResponse',
  full_name='chatMessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='chatMessageResponse.channel', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='owner', full_name='chatMessageResponse.owner', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='chatMessageResponse.content', index=2,
      number=5, type=9, cpp_type=9, label=2,
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
  serialized_start=287,
  serialized_end=374,
)

_LOGINTOCHATREQUEST.fields_by_name['owner'].message_type = _CHATOBJECTINFO
_CHATCONECTINGREQUEST.fields_by_name['owner'].message_type = _CHATOBJECTINFO
_CHATCONECTINGREQUEST.fields_by_name['other'].message_type = _CHATOBJECTINFO
_CHATMESSAGERESPONSE.fields_by_name['owner'].message_type = _CHATOBJECTINFO
DESCRIPTOR.message_types_by_name['ChatObjectInfo'] = _CHATOBJECTINFO
DESCRIPTOR.message_types_by_name['LoginToChatRequest'] = _LOGINTOCHATREQUEST
DESCRIPTOR.message_types_by_name['ChatConectingRequest'] = _CHATCONECTINGREQUEST
DESCRIPTOR.message_types_by_name['ChatResponse'] = _CHATRESPONSE
DESCRIPTOR.message_types_by_name['chatMessageResponse'] = _CHATMESSAGERESPONSE

class ChatObjectInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHATOBJECTINFO

  # @@protoc_insertion_point(class_scope:ChatObjectInfo)

class LoginToChatRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGINTOCHATREQUEST

  # @@protoc_insertion_point(class_scope:LoginToChatRequest)

class ChatConectingRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHATCONECTINGREQUEST

  # @@protoc_insertion_point(class_scope:ChatConectingRequest)

class ChatResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHATRESPONSE

  # @@protoc_insertion_point(class_scope:ChatResponse)

class chatMessageResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHATMESSAGERESPONSE

  # @@protoc_insertion_point(class_scope:chatMessageResponse)


# @@protoc_insertion_point(module_scope)