# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inherit.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='inherit.proto',
  package='',
  serialized_pb='\n\rinherit.proto\x1a\x0c\x63ommon.proto\"6\n\x14InheritRefineRequest\x12\x0e\n\x06origin\x18\x01 \x02(\x05\x12\x0e\n\x06target\x18\x02 \x02(\x05\"9\n\x17InheritEquipmentRequest\x12\x0e\n\x06origin\x18\x01 \x02(\t\x12\x0e\n\x06target\x18\x02 \x02(\t\"6\n\x14InheritUnparaRequest\x12\x0e\n\x06origin\x18\x01 \x02(\x05\x12\x0e\n\x06target\x18\x02 \x02(\x05')




_INHERITREFINEREQUEST = _descriptor.Descriptor(
  name='InheritRefineRequest',
  full_name='InheritRefineRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin', full_name='InheritRefineRequest.origin', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='InheritRefineRequest.target', index=1,
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
  serialized_start=31,
  serialized_end=85,
)


_INHERITEQUIPMENTREQUEST = _descriptor.Descriptor(
  name='InheritEquipmentRequest',
  full_name='InheritEquipmentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin', full_name='InheritEquipmentRequest.origin', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='InheritEquipmentRequest.target', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=87,
  serialized_end=144,
)


_INHERITUNPARAREQUEST = _descriptor.Descriptor(
  name='InheritUnparaRequest',
  full_name='InheritUnparaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin', full_name='InheritUnparaRequest.origin', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='InheritUnparaRequest.target', index=1,
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
  serialized_start=146,
  serialized_end=200,
)

DESCRIPTOR.message_types_by_name['InheritRefineRequest'] = _INHERITREFINEREQUEST
DESCRIPTOR.message_types_by_name['InheritEquipmentRequest'] = _INHERITEQUIPMENTREQUEST
DESCRIPTOR.message_types_by_name['InheritUnparaRequest'] = _INHERITUNPARAREQUEST

class InheritRefineRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INHERITREFINEREQUEST

  # @@protoc_insertion_point(class_scope:InheritRefineRequest)

class InheritEquipmentRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INHERITEQUIPMENTREQUEST

  # @@protoc_insertion_point(class_scope:InheritEquipmentRequest)

class InheritUnparaRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INHERITUNPARAREQUEST

  # @@protoc_insertion_point(class_scope:InheritUnparaRequest)


# @@protoc_insertion_point(module_scope)
