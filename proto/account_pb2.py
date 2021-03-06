# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/account.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/account.proto',
  package='account',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13proto/account.proto\x12\x07\x61\x63\x63ount\"H\n\x14\x43reateAccountRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0f\n\x07\x65n_name\x18\x03 \x01(\t\"\x17\n\x15\x43reateAccountResponse\"/\n\x0cLoginRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x1d\n\rLoginResponse\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"n\n\x14UpdateAccountRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x17\n\x0forigin_password\x18\x02 \x01(\t\x12\x17\n\x0fupdate_password\x18\x03 \x01(\t\x12\x16\n\x0e\x63heck_password\x18\x04 \x01(\t\"\x17\n\x15UpdateAccountResponse2\xe2\x01\n\x07\x41\x63\x63ount\x12I\n\x06signup\x12\x1d.account.CreateAccountRequest\x1a\x1e.account.CreateAccountResponse\"\x00\x12\x39\n\x06signin\x12\x15.account.LoginRequest\x1a\x16.account.LoginResponse\"\x00\x12Q\n\x0eupdate_account\x12\x1d.account.UpdateAccountRequest\x1a\x1e.account.UpdateAccountResponse\"\x00\x62\x06proto3'
)




_CREATEACCOUNTREQUEST = _descriptor.Descriptor(
  name='CreateAccountRequest',
  full_name='account.CreateAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='account.CreateAccountRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='account.CreateAccountRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='en_name', full_name='account.CreateAccountRequest.en_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=104,
)


_CREATEACCOUNTRESPONSE = _descriptor.Descriptor(
  name='CreateAccountResponse',
  full_name='account.CreateAccountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=129,
)


_LOGINREQUEST = _descriptor.Descriptor(
  name='LoginRequest',
  full_name='account.LoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='account.LoginRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='account.LoginRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=178,
)


_LOGINRESPONSE = _descriptor.Descriptor(
  name='LoginResponse',
  full_name='account.LoginResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='account.LoginResponse.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=209,
)


_UPDATEACCOUNTREQUEST = _descriptor.Descriptor(
  name='UpdateAccountRequest',
  full_name='account.UpdateAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='account.UpdateAccountRequest.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='origin_password', full_name='account.UpdateAccountRequest.origin_password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_password', full_name='account.UpdateAccountRequest.update_password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='check_password', full_name='account.UpdateAccountRequest.check_password', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=321,
)


_UPDATEACCOUNTRESPONSE = _descriptor.Descriptor(
  name='UpdateAccountResponse',
  full_name='account.UpdateAccountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=323,
  serialized_end=346,
)

DESCRIPTOR.message_types_by_name['CreateAccountRequest'] = _CREATEACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['CreateAccountResponse'] = _CREATEACCOUNTRESPONSE
DESCRIPTOR.message_types_by_name['LoginRequest'] = _LOGINREQUEST
DESCRIPTOR.message_types_by_name['LoginResponse'] = _LOGINRESPONSE
DESCRIPTOR.message_types_by_name['UpdateAccountRequest'] = _UPDATEACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['UpdateAccountResponse'] = _UPDATEACCOUNTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateAccountRequest = _reflection.GeneratedProtocolMessageType('CreateAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEACCOUNTREQUEST,
  '__module__' : 'proto.account_pb2'
  # @@protoc_insertion_point(class_scope:account.CreateAccountRequest)
  })
_sym_db.RegisterMessage(CreateAccountRequest)

CreateAccountResponse = _reflection.GeneratedProtocolMessageType('CreateAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEACCOUNTRESPONSE,
  '__module__' : 'proto.account_pb2'
  # @@protoc_insertion_point(class_scope:account.CreateAccountResponse)
  })
_sym_db.RegisterMessage(CreateAccountResponse)

LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQUEST,
  '__module__' : 'proto.account_pb2'
  # @@protoc_insertion_point(class_scope:account.LoginRequest)
  })
_sym_db.RegisterMessage(LoginRequest)

LoginResponse = _reflection.GeneratedProtocolMessageType('LoginResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGINRESPONSE,
  '__module__' : 'proto.account_pb2'
  # @@protoc_insertion_point(class_scope:account.LoginResponse)
  })
_sym_db.RegisterMessage(LoginResponse)

UpdateAccountRequest = _reflection.GeneratedProtocolMessageType('UpdateAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEACCOUNTREQUEST,
  '__module__' : 'proto.account_pb2'
  # @@protoc_insertion_point(class_scope:account.UpdateAccountRequest)
  })
_sym_db.RegisterMessage(UpdateAccountRequest)

UpdateAccountResponse = _reflection.GeneratedProtocolMessageType('UpdateAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEACCOUNTRESPONSE,
  '__module__' : 'proto.account_pb2'
  # @@protoc_insertion_point(class_scope:account.UpdateAccountResponse)
  })
_sym_db.RegisterMessage(UpdateAccountResponse)



_ACCOUNT = _descriptor.ServiceDescriptor(
  name='Account',
  full_name='account.Account',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=349,
  serialized_end=575,
  methods=[
  _descriptor.MethodDescriptor(
    name='signup',
    full_name='account.Account.signup',
    index=0,
    containing_service=None,
    input_type=_CREATEACCOUNTREQUEST,
    output_type=_CREATEACCOUNTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='signin',
    full_name='account.Account.signin',
    index=1,
    containing_service=None,
    input_type=_LOGINREQUEST,
    output_type=_LOGINRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='update_account',
    full_name='account.Account.update_account',
    index=2,
    containing_service=None,
    input_type=_UPDATEACCOUNTREQUEST,
    output_type=_UPDATEACCOUNTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ACCOUNT)

DESCRIPTOR.services_by_name['Account'] = _ACCOUNT

# @@protoc_insertion_point(module_scope)
