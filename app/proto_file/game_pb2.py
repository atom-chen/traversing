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
  serialized_pb='\n\ngame.proto\x1a\x0c\x63ommon.proto\"\xf6\x03\n\x10GameLoginRequest\x12\r\n\x05token\x18\x01 \x02(\t\x12\x0f\n\x07plat_id\x18\x02 \x01(\x05\x12\x16\n\x0e\x63lient_version\x18\x03 \x01(\t\x12\x17\n\x0fsystem_software\x18\x04 \x01(\t\x12\x17\n\x0fsystem_hardware\x18\x05 \x01(\t\x12\x14\n\x0ctelecom_oper\x18\x06 \x01(\t\x12\x0f\n\x07network\x18\x07 \x01(\t\x12\x14\n\x0cscreen_width\x18\x08 \x01(\x05\x12\x14\n\x0cscreen_hight\x18\t \x01(\x05\x12\x0f\n\x07\x64\x65nsity\x18\n \x01(\x02\x12\x15\n\rlogin_channel\x18\x0b \x01(\x05\x12\x0b\n\x03mac\x18\x0c \x01(\t\x12\x14\n\x0c\x63pu_hardware\x18\r \x01(\t\x12\x0e\n\x06memory\x18\x0e \x01(\x05\x12\x11\n\tgl_render\x18\x0f \x01(\t\x12\x12\n\ngl_version\x18\x10 \x01(\t\x12\x11\n\tdevice_id\x18\x11 \x01(\t\x12\x10\n\x08platform\x18\x12 \x01(\x05\x12\x0f\n\x07open_id\x18\x13 \x01(\t\x12\x10\n\x08open_key\x18\x14 \x01(\t\x12\x11\n\tpay_token\x18\x15 \x01(\t\x12\r\n\x05\x61ppid\x18\x16 \x01(\t\x12\x0e\n\x06\x61ppkey\x18\x1a \x01(\t\x12\n\n\x02pf\x18\x17 \x01(\t\x12\r\n\x05pfkey\x18\x18 \x01(\t\x12\x0e\n\x06zoneid\x18\x19 \x01(\t\"\xd2\x05\n\x11GameLoginResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x10\n\x08nickname\x18\x03 \x01(\t\x12\r\n\x05level\x18\x04 \x01(\x05\x12\x0b\n\x03\x65xp\x18\x05 \x01(\x05\x12\x10\n\x08\x66inances\x18\x06 \x03(\x05\x12\x11\n\tfine_hero\x18\x07 \x01(\x05\x12\x16\n\x0e\x65xcellent_hero\x18\x08 \x01(\x05\x12\x16\n\x0e\x66ine_equipment\x18\t \x01(\x05\x12\x1b\n\x13\x65xcellent_equipment\x18\n \x01(\x05\x12\x11\n\tpvp_times\x18\x0b \x01(\x05\x12\x19\n\x11pvp_refresh_count\x18\x0c \x01(\x05\x12\x11\n\tvip_level\x18\r \x01(\x05\x12\x13\n\x0bserver_time\x18\x0e \x01(\x05\x12\x10\n\x08guild_id\x18\x0f \x01(\x05\x12\x14\n\x0c\x63ombat_power\x18\x10 \x01(\x02\x12\x17\n\x0fnewbee_guide_id\x18\x11 \x01(\x05\x12\x15\n\rregister_time\x18\x18 \x01(\x05\x12\x19\n\x11get_stamina_times\x18\x12 \x01(\x05\x12\x19\n\x11\x62uy_stamina_times\x18\x13 \x01(\x05\x12\x1e\n\x16last_gain_stamina_time\x18\x14 \x01(\x05\x12\x1f\n\x17soul_shop_refresh_times\x18\x15 \x01(\x05\x12\x0c\n\x04head\x18\x16 \x03(\x05\x12\x10\n\x08now_head\x18\x17 \x01(\x05\x12\x1a\n\x12\x66irst_recharge_ids\x18\x19 \x03(\x05\x12\x0b\n\x03gag\x18\x1a \x01(\x05\x12\x0f\n\x07\x63losure\x18\x1b \x01(\x05\x12\x10\n\x08recharge\x18\x1c \x01(\x05\x12\x15\n\rtomorrow_gift\x18\x1d \x01(\x05\x12\x14\n\x0c\x62\x61ttle_speed\x18\x1e \x01(\x05\x12\x17\n\x0f\x66ine_hero_times\x18\x1f \x01(\x05\x12\x1c\n\x14\x65xcellent_hero_times\x18  \x01(\x05\"(\n\x11HeartBeatResponse\x12\x13\n\x0bserver_time\x18\x01 \x01(\x05\"+\n\x12StaminaOperRequest\x12\x15\n\rresource_type\x18\x01 \x01(\x05')




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
    _descriptor.FieldDescriptor(
      name='plat_id', full_name='GameLoginRequest.plat_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_version', full_name='GameLoginRequest.client_version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='system_software', full_name='GameLoginRequest.system_software', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='system_hardware', full_name='GameLoginRequest.system_hardware', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='telecom_oper', full_name='GameLoginRequest.telecom_oper', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='network', full_name='GameLoginRequest.network', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='screen_width', full_name='GameLoginRequest.screen_width', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='screen_hight', full_name='GameLoginRequest.screen_hight', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='density', full_name='GameLoginRequest.density', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='login_channel', full_name='GameLoginRequest.login_channel', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mac', full_name='GameLoginRequest.mac', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu_hardware', full_name='GameLoginRequest.cpu_hardware', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memory', full_name='GameLoginRequest.memory', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gl_render', full_name='GameLoginRequest.gl_render', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gl_version', full_name='GameLoginRequest.gl_version', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_id', full_name='GameLoginRequest.device_id', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='platform', full_name='GameLoginRequest.platform', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open_id', full_name='GameLoginRequest.open_id', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open_key', full_name='GameLoginRequest.open_key', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pay_token', full_name='GameLoginRequest.pay_token', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appid', full_name='GameLoginRequest.appid', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appkey', full_name='GameLoginRequest.appkey', index=22,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pf', full_name='GameLoginRequest.pf', index=23,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pfkey', full_name='GameLoginRequest.pfkey', index=24,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='zoneid', full_name='GameLoginRequest.zoneid', index=25,
      number=25, type=9, cpp_type=9, label=1,
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
  serialized_end=531,
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
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
      name='register_time', full_name='GameLoginResponse.register_time', index=17,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_stamina_times', full_name='GameLoginResponse.get_stamina_times', index=18,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buy_stamina_times', full_name='GameLoginResponse.buy_stamina_times', index=19,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_gain_stamina_time', full_name='GameLoginResponse.last_gain_stamina_time', index=20,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='soul_shop_refresh_times', full_name='GameLoginResponse.soul_shop_refresh_times', index=21,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='head', full_name='GameLoginResponse.head', index=22,
      number=22, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='now_head', full_name='GameLoginResponse.now_head', index=23,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first_recharge_ids', full_name='GameLoginResponse.first_recharge_ids', index=24,
      number=25, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gag', full_name='GameLoginResponse.gag', index=25,
      number=26, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='closure', full_name='GameLoginResponse.closure', index=26,
      number=27, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recharge', full_name='GameLoginResponse.recharge', index=27,
      number=28, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tomorrow_gift', full_name='GameLoginResponse.tomorrow_gift', index=28,
      number=29, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_speed', full_name='GameLoginResponse.battle_speed', index=29,
      number=30, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fine_hero_times', full_name='GameLoginResponse.fine_hero_times', index=30,
      number=31, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='excellent_hero_times', full_name='GameLoginResponse.excellent_hero_times', index=31,
      number=32, type=5, cpp_type=1, label=1,
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
  serialized_start=534,
  serialized_end=1256,
)


_HEARTBEATRESPONSE = _descriptor.Descriptor(
  name='HeartBeatResponse',
  full_name='HeartBeatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_time', full_name='HeartBeatResponse.server_time', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=1258,
  serialized_end=1298,
)


_STAMINAOPERREQUEST = _descriptor.Descriptor(
  name='StaminaOperRequest',
  full_name='StaminaOperRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_type', full_name='StaminaOperRequest.resource_type', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=1300,
  serialized_end=1343,
)

_GAMELOGINRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
DESCRIPTOR.message_types_by_name['GameLoginRequest'] = _GAMELOGINREQUEST
DESCRIPTOR.message_types_by_name['GameLoginResponse'] = _GAMELOGINRESPONSE
DESCRIPTOR.message_types_by_name['HeartBeatResponse'] = _HEARTBEATRESPONSE
DESCRIPTOR.message_types_by_name['StaminaOperRequest'] = _STAMINAOPERREQUEST

class GameLoginRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GAMELOGINREQUEST

  # @@protoc_insertion_point(class_scope:GameLoginRequest)

class GameLoginResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GAMELOGINRESPONSE

  # @@protoc_insertion_point(class_scope:GameLoginResponse)

class HeartBeatResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEARTBEATRESPONSE

  # @@protoc_insertion_point(class_scope:HeartBeatResponse)

class StaminaOperRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STAMINAOPERREQUEST

  # @@protoc_insertion_point(class_scope:StaminaOperRequest)


# @@protoc_insertion_point(module_scope)
