# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='game.proto',
  package='',
  serialized_pb='\n\ngame.proto\x1a\x0c\x63ommon.proto\"!\n\x10GameLoginRequest\x12\r\n\x05token\x18\x01 \x02(\t\"\xeb\x03\n\x11GameLoginResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x10\n\x08nickname\x18\x03 \x01(\t\x12\r\n\x05level\x18\x04 \x01(\x05\x12\x0b\n\x03\x65xp\x18\x05 \x01(\x05\x12\x10\n\x08\x66inances\x18\x06 \x03(\x05\x12\x11\n\tfine_hero\x18\x07 \x01(\x05\x12\x16\n\x0e\x65xcellent_hero\x18\x08 \x01(\x05\x12\x16\n\x0e\x66ine_equipment\x18\t \x01(\x05\x12\x1b\n\x13\x65xcellent_equipment\x18\n \x01(\x05\x12\x11\n\tpvp_times\x18\x0b \x01(\x05\x12\x19\n\x11pvp_refresh_count\x18\x0c \x01(\x05\x12\x11\n\tvip_level\x18\r \x01(\x05\x12\x13\n\x0bserver_time\x18\x0e \x01(\x05\x12\x10\n\x08guild_id\x18\x0f \x01(\x0c\x12\x14\n\x0c\x63ombat_power\x18\x10 \x01(\x02\x12\x17\n\x0fnewbee_guide_id\x18\x11 \x01(\x05\x12\x19\n\x11get_stamina_times\x18\x12 \x01(\x05\x12\x19\n\x11\x62uy_stamina_times\x18\x13 \x01(\x05\x12\x1e\n\x16last_gain_stamina_time\x18\x14 \x01(\x05\x12\x1f\n\x17soul_shop_refresh_times\x18\x15 \x01(\x05')




_GAMELOGINREQUEST = _descriptor.Descriptor(
  name='GameLoginRequest',
  full_name='GameLoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='GameLoginRequest.token', index=0,
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
  serialized_start=28,
  serialized_end=61,
)


_GAMELOGINRESPONSE = _descriptor.Descriptor(
  name='GameLoginResponse',
  full_name='GameLoginResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='GameLoginResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='GameLoginResponse.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='GameLoginResponse.nickname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='GameLoginResponse.level', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp', full_name='GameLoginResponse.exp', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='finances', full_name='GameLoginResponse.finances', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fine_hero', full_name='GameLoginResponse.fine_hero', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='excellent_hero', full_name='GameLoginResponse.excellent_hero', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fine_equipment', full_name='GameLoginResponse.fine_equipment', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='excellent_equipment', full_name='GameLoginResponse.excellent_equipment', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pvp_times', full_name='GameLoginResponse.pvp_times', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pvp_refresh_count', full_name='GameLoginResponse.pvp_refresh_count', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vip_level', full_name='GameLoginResponse.vip_level', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_time', full_name='GameLoginResponse.server_time', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guild_id', full_name='GameLoginResponse.guild_id', index=14,
      number=15, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combat_power', full_name='GameLoginResponse.combat_power', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='newbee_guide_id', full_name='GameLoginResponse.newbee_guide_id', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_stamina_times', full_name='GameLoginResponse.get_stamina_times', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buy_stamina_times', full_name='GameLoginResponse.buy_stamina_times', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_gain_stamina_time', full_name='GameLoginResponse.last_gain_stamina_time', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='soul_shop_refresh_times', full_name='GameLoginResponse.soul_shop_refresh_times', index=20,
      number=21, type=5, cpp_type=1, label=1,
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
  serialized_start=64,
  serialized_end=555,
)

_GAMELOGINRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
DESCRIPTOR.message_types_by_name['GameLoginRequest'] = _GAMELOGINREQUEST
DESCRIPTOR.message_types_by_name['GameLoginResponse'] = _GAMELOGINRESPONSE

class GameLoginRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GAMELOGINREQUEST

  # @@protoc_insertion_point(class_scope:GameLoginRequest)

class GameLoginResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GAMELOGINRESPONSE

  # @@protoc_insertion_point(class_scope:GameLoginResponse)


# @@protoc_insertion_point(module_scope)
