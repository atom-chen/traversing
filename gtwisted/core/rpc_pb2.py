# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rpc.proto',
  package='',
  serialized_pb='\n\trpc.proto\"\xf3\x03\n\x0bRPCProtocol\x12\x0f\n\x07msgType\x18\x01 \x02(\x0c\x12\x0b\n\x03key\x18\x02 \x02(\x0c\x12\x0c\n\x04name\x18\x03 \x02(\x0c\x12&\n\x06result\x18\x04 \x01(\x0b\x32\x16.RPCProtocol.Parameter\x12*\n\nparameters\x18\x05 \x03(\x0b\x32\x16.RPCProtocol.Parameter\x1a\xe3\x02\n\tParameter\x12\x14\n\x0cpython_param\x18\x01 \x01(\x0c\x12\x13\n\x0bproto_param\x18\x02 \x01(\x0c\x12\x14\n\x0cstring_param\x18\x03 \x01(\t\x12\x11\n\tint_param\x18\x04 \x01(\x11\x12\x12\n\nuint_param\x18\x05 \x01(\r\x12\x13\n\x0bint64_param\x18\x06 \x01(\x12\x12\x14\n\x0cuint64_param\x18\x07 \x01(\x04\x12\x12\n\nbool_param\x18\x08 \x01(\x08\x12\x13\n\x0b\x66loat_param\x18\t \x01(\x02\x12\x14\n\x0c\x64ouble_param\x18\n \x01(\x01\x12\x0f\n\x07is_null\x18\x0b \x01(\x08\x12&\n\x06tuples\x18\x0c \x03(\x0b\x32\x16.RPCProtocol.Parameter\x12$\n\x04list\x18\r \x03(\x0b\x32\x16.RPCProtocol.Parameter\x12\x11\n\tnull_list\x18\x0e \x01(\x08\x12\x12\n\nnull_tuple\x18\x0f \x01(\x08')




_RPCPROTOCOL_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='RPCProtocol.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='python_param', full_name='RPCProtocol.Parameter.python_param', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proto_param', full_name='RPCProtocol.Parameter.proto_param', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_param', full_name='RPCProtocol.Parameter.string_param', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int_param', full_name='RPCProtocol.Parameter.int_param', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uint_param', full_name='RPCProtocol.Parameter.uint_param', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int64_param', full_name='RPCProtocol.Parameter.int64_param', index=5,
      number=6, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uint64_param', full_name='RPCProtocol.Parameter.uint64_param', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bool_param', full_name='RPCProtocol.Parameter.bool_param', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_param', full_name='RPCProtocol.Parameter.float_param', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='double_param', full_name='RPCProtocol.Parameter.double_param', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_null', full_name='RPCProtocol.Parameter.is_null', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tuples', full_name='RPCProtocol.Parameter.tuples', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='list', full_name='RPCProtocol.Parameter.list', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='null_list', full_name='RPCProtocol.Parameter.null_list', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='null_tuple', full_name='RPCProtocol.Parameter.null_tuple', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=158,
  serialized_end=513,
)

_RPCPROTOCOL = _descriptor.Descriptor(
  name='RPCProtocol',
  full_name='RPCProtocol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgType', full_name='RPCProtocol.msgType', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='RPCProtocol.key', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='RPCProtocol.name', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='RPCProtocol.result', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='RPCProtocol.parameters', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RPCPROTOCOL_PARAMETER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=14,
  serialized_end=513,
)

_RPCPROTOCOL_PARAMETER.fields_by_name['tuples'].message_type = _RPCPROTOCOL_PARAMETER
_RPCPROTOCOL_PARAMETER.fields_by_name['list'].message_type = _RPCPROTOCOL_PARAMETER
_RPCPROTOCOL_PARAMETER.containing_type = _RPCPROTOCOL;
_RPCPROTOCOL.fields_by_name['result'].message_type = _RPCPROTOCOL_PARAMETER
_RPCPROTOCOL.fields_by_name['parameters'].message_type = _RPCPROTOCOL_PARAMETER
DESCRIPTOR.message_types_by_name['RPCProtocol'] = _RPCPROTOCOL

class RPCProtocol(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Parameter(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _RPCPROTOCOL_PARAMETER

    # @@protoc_insertion_point(class_scope:RPCProtocol.Parameter)
  DESCRIPTOR = _RPCPROTOCOL

  # @@protoc_insertion_point(class_scope:RPCProtocol)


# @@protoc_insertion_point(module_scope)
