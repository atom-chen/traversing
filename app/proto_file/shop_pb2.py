# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shop.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='shop.proto',
  package='',
  serialized_pb='\n\nshop.proto\"\x19\n\x0bShopRequest\x12\n\n\x02id\x18\x01 \x02(\x05')




_SHOPREQUEST = _descriptor.Descriptor(
  name='ShopRequest',
  full_name='ShopRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ShopRequest.id', index=0,
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
  serialized_start=14,
  serialized_end=39,
)

DESCRIPTOR.message_types_by_name['ShopRequest'] = _SHOPREQUEST

class ShopRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SHOPREQUEST

  # @@protoc_insertion_point(class_scope:ShopRequest)


# @@protoc_insertion_point(module_scope)