# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: item.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='item.proto',
  package='',
  serialized_pb='\n\nitem.proto\"+\n\x06ItemPB\x12\x0f\n\x07item_no\x18\x01 \x02(\x05\x12\x10\n\x08item_num\x18\x02 \x02(\x05\"&\n\rItemsResponse\x12\x15\n\x04item\x18\x01 \x03(\x0b\x32\x07.ItemPB')




_ITEMPB = _descriptor.Descriptor(
  name='ItemPB',
  full_name='ItemPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_no', full_name='ItemPB.item_no', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_num', full_name='ItemPB.item_num', index=1,
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
  serialized_start=14,
  serialized_end=57,
)


_ITEMSRESPONSE = _descriptor.Descriptor(
  name='ItemsResponse',
  full_name='ItemsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='ItemsResponse.item', index=0,
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
  serialized_start=59,
  serialized_end=97,
)

_ITEMSRESPONSE.fields_by_name['item'].message_type = _ITEMPB
DESCRIPTOR.message_types_by_name['ItemPB'] = _ITEMPB
DESCRIPTOR.message_types_by_name['ItemsResponse'] = _ITEMSRESPONSE

class ItemPB(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEMPB

  # @@protoc_insertion_point(class_scope:ItemPB)

class ItemsResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEMSRESPONSE

  # @@protoc_insertion_point(class_scope:ItemsResponse)


# @@protoc_insertion_point(module_scope)
