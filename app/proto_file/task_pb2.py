# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='task.proto',
  package='',
  serialized_pb='\n\ntask.proto\x1a\x0c\x63ommon.proto\"F\n\x04Task\x12\x0b\n\x03tid\x18\x01 \x02(\x05\x12!\n\tcondition\x18\x02 \x03(\x0b\x32\x0e.TaskCondition\x12\x0e\n\x06status\x18\x03 \x02(\x05\"E\n\rTaskCondition\x12\x14\n\x0c\x63ondition_no\x18\x01 \x02(\x05\x12\x0f\n\x07\x63urrent\x18\x02 \x01(\x05\x12\r\n\x05state\x18\x03 \x01(\x05\"\x1f\n\x0fTaskInfoRequest\x12\x0c\n\x04sort\x18\x01 \x02(\x05\"(\n\x10TaskInfoResponse\x12\x14\n\x05tasks\x18\x01 \x03(\x0b\x32\x05.Task\" \n\x11TaskRewardRequest\x12\x0b\n\x03tid\x18\x01 \x02(\x05\"e\n\x12TaskRewardResponse\x12\x0b\n\x03tid\x18\x01 \x01(\x05\x12$\n\x04gain\x18\x02 \x01(\x0b\x32\x16.GameResourcesResponse\x12\x1c\n\x03res\x18\x03 \x02(\x0b\x32\x0f.CommonResponse')




_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tid', full_name='Task.tid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition', full_name='Task.condition', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='Task.status', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=28,
  serialized_end=98,
)


_TASKCONDITION = _descriptor.Descriptor(
  name='TaskCondition',
  full_name='TaskCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='condition_no', full_name='TaskCondition.condition_no', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current', full_name='TaskCondition.current', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='TaskCondition.state', index=2,
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
  serialized_start=100,
  serialized_end=169,
)


_TASKINFOREQUEST = _descriptor.Descriptor(
  name='TaskInfoRequest',
  full_name='TaskInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sort', full_name='TaskInfoRequest.sort', index=0,
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
  serialized_start=171,
  serialized_end=202,
)


_TASKINFORESPONSE = _descriptor.Descriptor(
  name='TaskInfoResponse',
  full_name='TaskInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tasks', full_name='TaskInfoResponse.tasks', index=0,
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
  serialized_start=204,
  serialized_end=244,
)


_TASKREWARDREQUEST = _descriptor.Descriptor(
  name='TaskRewardRequest',
  full_name='TaskRewardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tid', full_name='TaskRewardRequest.tid', index=0,
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
  serialized_start=246,
  serialized_end=278,
)


_TASKREWARDRESPONSE = _descriptor.Descriptor(
  name='TaskRewardResponse',
  full_name='TaskRewardResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tid', full_name='TaskRewardResponse.tid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gain', full_name='TaskRewardResponse.gain', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='res', full_name='TaskRewardResponse.res', index=2,
      number=3, type=11, cpp_type=10, label=2,
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
  serialized_start=280,
  serialized_end=381,
)

_TASK.fields_by_name['condition'].message_type = _TASKCONDITION
_TASKINFORESPONSE.fields_by_name['tasks'].message_type = _TASK
_TASKREWARDRESPONSE.fields_by_name['gain'].message_type = common_pb2._GAMERESOURCESRESPONSE
_TASKREWARDRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['TaskCondition'] = _TASKCONDITION
DESCRIPTOR.message_types_by_name['TaskInfoRequest'] = _TASKINFOREQUEST
DESCRIPTOR.message_types_by_name['TaskInfoResponse'] = _TASKINFORESPONSE
DESCRIPTOR.message_types_by_name['TaskRewardRequest'] = _TASKREWARDREQUEST
DESCRIPTOR.message_types_by_name['TaskRewardResponse'] = _TASKREWARDRESPONSE

class Task(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASK

  # @@protoc_insertion_point(class_scope:Task)

class TaskCondition(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASKCONDITION

  # @@protoc_insertion_point(class_scope:TaskCondition)

class TaskInfoRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASKINFOREQUEST

  # @@protoc_insertion_point(class_scope:TaskInfoRequest)

class TaskInfoResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASKINFORESPONSE

  # @@protoc_insertion_point(class_scope:TaskInfoResponse)

class TaskRewardRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASKREWARDREQUEST

  # @@protoc_insertion_point(class_scope:TaskRewardRequest)

class TaskRewardResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASKREWARDRESPONSE

  # @@protoc_insertion_point(class_scope:TaskRewardResponse)


# @@protoc_insertion_point(module_scope)
