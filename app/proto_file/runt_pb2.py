# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: runt.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='runt.proto',
  package='',
  serialized_pb='\n\nrunt.proto\x1a\x0c\x63ommon.proto\"V\n\x0eRuntSetRequest\x12\x0f\n\x07hero_no\x18\x01 \x02(\x05\x12\x11\n\trunt_type\x18\x02 \x02(\x05\x12\x0f\n\x07runt_po\x18\x03 \x02(\x05\x12\x0f\n\x07runt_no\x18\x04 \x02(\x0c\"/\n\x0fRuntSetResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\"F\n\x0fRuntPickRequest\x12\x0f\n\x07hero_no\x18\x01 \x02(\x05\x12\x11\n\trunt_type\x18\x02 \x02(\x05\x12\x0f\n\x07runt_po\x18\x03 \x01(\x05\"0\n\x10RuntPickResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\"}\n\x10InitRuntResponse\x12\x14\n\x04runt\x18\x01 \x03(\x0b\x32\x06.Runt1\x12\x0e\n\x06stone1\x18\x02 \x02(\x05\x12\x0e\n\x06stone2\x18\x03 \x02(\x05\x12\x1c\n\x0crefresh_runt\x18\x04 \x01(\x0b\x32\x06.Runt1\x12\x15\n\rrefresh_times\x18\x05 \x02(\x05\"f\n\x05Runt1\x12\x0f\n\x07runt_no\x18\x01 \x02(\x0c\x12\x1c\n\tmain_attr\x18\x02 \x03(\x0b\x32\t.RuntAttr\x12\x1d\n\nminor_attr\x18\x03 \x03(\x0b\x32\t.RuntAttr\x12\x0f\n\x07runt_id\x18\x04 \x02(\x05\"b\n\x08RuntAttr\x12\x17\n\x0f\x61ttr_value_type\x18\x01 \x02(\x05\x12\x12\n\nattr_value\x18\x02 \x02(\x02\x12\x16\n\x0e\x61ttr_increment\x18\x03 \x02(\x05\x12\x11\n\tattr_type\x18\x04 \x02(\x05\"Q\n\x13RefreshRuntResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\x1c\n\x0crefresh_runt\x18\x02 \x01(\x0b\x32\x06.Runt1\"&\n\x13RefiningRuntRequest\x12\x0f\n\x07runt_no\x18\x01 \x03(\x0c\"j\n\x14RefiningRuntResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\x0e\n\x06stone1\x18\x02 \x02(\x05\x12\x0e\n\x06stone2\x18\x03 \x02(\x05\x12\x14\n\x04runt\x18\x04 \x03(\x0b\x32\x06.Runt1\"O\n\x11\x42uildRuntResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\x1c\n\x0crefresh_runt\x18\x02 \x01(\x0b\x32\x06.Runt1')




_RUNTSETREQUEST = _descriptor.Descriptor(
  name='RuntSetRequest',
  full_name='RuntSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero_no', full_name='RuntSetRequest.hero_no', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='runt_type', full_name='RuntSetRequest.runt_type', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='runt_po', full_name='RuntSetRequest.runt_po', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='runt_no', full_name='RuntSetRequest.runt_no', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  serialized_start=28,
  serialized_end=114,
)


_RUNTSETRESPONSE = _descriptor.Descriptor(
  name='RuntSetResponse',
  full_name='RuntSetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='RuntSetResponse.res', index=0,
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
  serialized_start=116,
  serialized_end=163,
)


_RUNTPICKREQUEST = _descriptor.Descriptor(
  name='RuntPickRequest',
  full_name='RuntPickRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero_no', full_name='RuntPickRequest.hero_no', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='runt_type', full_name='RuntPickRequest.runt_type', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='runt_po', full_name='RuntPickRequest.runt_po', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=165,
  serialized_end=235,
)


_RUNTPICKRESPONSE = _descriptor.Descriptor(
  name='RuntPickResponse',
  full_name='RuntPickResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='RuntPickResponse.res', index=0,
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
  serialized_start=237,
  serialized_end=285,
)


_INITRUNTRESPONSE = _descriptor.Descriptor(
  name='InitRuntResponse',
  full_name='InitRuntResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='runt', full_name='InitRuntResponse.runt', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stone1', full_name='InitRuntResponse.stone1', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stone2', full_name='InitRuntResponse.stone2', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='refresh_runt', full_name='InitRuntResponse.refresh_runt', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='refresh_times', full_name='InitRuntResponse.refresh_times', index=4,
      number=5, type=5, cpp_type=1, label=2,
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
  serialized_start=287,
  serialized_end=412,
)


_RUNT1 = _descriptor.Descriptor(
  name='Runt1',
  full_name='Runt1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='runt_no', full_name='Runt1.runt_no', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='main_attr', full_name='Runt1.main_attr', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minor_attr', full_name='Runt1.minor_attr', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='runt_id', full_name='Runt1.runt_id', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  serialized_start=414,
  serialized_end=516,
)


_RUNTATTR = _descriptor.Descriptor(
  name='RuntAttr',
  full_name='RuntAttr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attr_value_type', full_name='RuntAttr.attr_value_type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attr_value', full_name='RuntAttr.attr_value', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attr_increment', full_name='RuntAttr.attr_increment', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attr_type', full_name='RuntAttr.attr_type', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  serialized_start=518,
  serialized_end=616,
)


_REFRESHRUNTRESPONSE = _descriptor.Descriptor(
  name='RefreshRuntResponse',
  full_name='RefreshRuntResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='RefreshRuntResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='refresh_runt', full_name='RefreshRuntResponse.refresh_runt', index=1,
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
  serialized_start=618,
  serialized_end=699,
)


_REFININGRUNTREQUEST = _descriptor.Descriptor(
  name='RefiningRuntRequest',
  full_name='RefiningRuntRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='runt_no', full_name='RefiningRuntRequest.runt_no', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  serialized_start=701,
  serialized_end=739,
)


_REFININGRUNTRESPONSE = _descriptor.Descriptor(
  name='RefiningRuntResponse',
  full_name='RefiningRuntResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='RefiningRuntResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stone1', full_name='RefiningRuntResponse.stone1', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stone2', full_name='RefiningRuntResponse.stone2', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='runt', full_name='RefiningRuntResponse.runt', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=741,
  serialized_end=847,
)


_BUILDRUNTRESPONSE = _descriptor.Descriptor(
  name='BuildRuntResponse',
  full_name='BuildRuntResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='BuildRuntResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='refresh_runt', full_name='BuildRuntResponse.refresh_runt', index=1,
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
  serialized_start=849,
  serialized_end=928,
)

_RUNTSETRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_RUNTPICKRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_INITRUNTRESPONSE.fields_by_name['runt'].message_type = _RUNT1
_INITRUNTRESPONSE.fields_by_name['refresh_runt'].message_type = _RUNT1
_RUNT1.fields_by_name['main_attr'].message_type = _RUNTATTR
_RUNT1.fields_by_name['minor_attr'].message_type = _RUNTATTR
_REFRESHRUNTRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_REFRESHRUNTRESPONSE.fields_by_name['refresh_runt'].message_type = _RUNT1
_REFININGRUNTRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_REFININGRUNTRESPONSE.fields_by_name['runt'].message_type = _RUNT1
_BUILDRUNTRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
_BUILDRUNTRESPONSE.fields_by_name['refresh_runt'].message_type = _RUNT1
DESCRIPTOR.message_types_by_name['RuntSetRequest'] = _RUNTSETREQUEST
DESCRIPTOR.message_types_by_name['RuntSetResponse'] = _RUNTSETRESPONSE
DESCRIPTOR.message_types_by_name['RuntPickRequest'] = _RUNTPICKREQUEST
DESCRIPTOR.message_types_by_name['RuntPickResponse'] = _RUNTPICKRESPONSE
DESCRIPTOR.message_types_by_name['InitRuntResponse'] = _INITRUNTRESPONSE
DESCRIPTOR.message_types_by_name['Runt1'] = _RUNT1
DESCRIPTOR.message_types_by_name['RuntAttr'] = _RUNTATTR
DESCRIPTOR.message_types_by_name['RefreshRuntResponse'] = _REFRESHRUNTRESPONSE
DESCRIPTOR.message_types_by_name['RefiningRuntRequest'] = _REFININGRUNTREQUEST
DESCRIPTOR.message_types_by_name['RefiningRuntResponse'] = _REFININGRUNTRESPONSE
DESCRIPTOR.message_types_by_name['BuildRuntResponse'] = _BUILDRUNTRESPONSE

class RuntSetRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RUNTSETREQUEST

  # @@protoc_insertion_point(class_scope:RuntSetRequest)

class RuntSetResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RUNTSETRESPONSE

  # @@protoc_insertion_point(class_scope:RuntSetResponse)

class RuntPickRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RUNTPICKREQUEST

  # @@protoc_insertion_point(class_scope:RuntPickRequest)

class RuntPickResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RUNTPICKRESPONSE

  # @@protoc_insertion_point(class_scope:RuntPickResponse)

class InitRuntResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INITRUNTRESPONSE

  # @@protoc_insertion_point(class_scope:InitRuntResponse)

class Runt1(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RUNT1

  # @@protoc_insertion_point(class_scope:Runt1)

class RuntAttr(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RUNTATTR

  # @@protoc_insertion_point(class_scope:RuntAttr)

class RefreshRuntResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REFRESHRUNTRESPONSE

  # @@protoc_insertion_point(class_scope:RefreshRuntResponse)

class RefiningRuntRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REFININGRUNTREQUEST

  # @@protoc_insertion_point(class_scope:RefiningRuntRequest)

class RefiningRuntResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REFININGRUNTRESPONSE

  # @@protoc_insertion_point(class_scope:RefiningRuntResponse)

class BuildRuntResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BUILDRUNTRESPONSE

  # @@protoc_insertion_point(class_scope:BuildRuntResponse)


# @@protoc_insertion_point(module_scope)
