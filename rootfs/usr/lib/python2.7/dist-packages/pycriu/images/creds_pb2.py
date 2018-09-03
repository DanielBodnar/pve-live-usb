# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: creds.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='creds.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0b\x63reds.proto\"\xf7\x01\n\x0b\x63reds_entry\x12\x0b\n\x03uid\x18\x01 \x02(\r\x12\x0b\n\x03gid\x18\x02 \x02(\r\x12\x0c\n\x04\x65uid\x18\x03 \x02(\r\x12\x0c\n\x04\x65gid\x18\x04 \x02(\r\x12\x0c\n\x04suid\x18\x05 \x02(\r\x12\x0c\n\x04sgid\x18\x06 \x02(\r\x12\r\n\x05\x66suid\x18\x07 \x02(\r\x12\r\n\x05\x66sgid\x18\x08 \x02(\r\x12\x0f\n\x07\x63\x61p_inh\x18\t \x03(\r\x12\x0f\n\x07\x63\x61p_prm\x18\n \x03(\r\x12\x0f\n\x07\x63\x61p_eff\x18\x0b \x03(\r\x12\x0f\n\x07\x63\x61p_bnd\x18\x0c \x03(\r\x12\x0f\n\x07secbits\x18\r \x02(\r\x12\x0e\n\x06groups\x18\x0e \x03(\r\x12\x13\n\x0blsm_profile\x18\x0f \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CREDS_ENTRY = _descriptor.Descriptor(
  name='creds_entry',
  full_name='creds_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='creds_entry.uid', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gid', full_name='creds_entry.gid', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='euid', full_name='creds_entry.euid', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egid', full_name='creds_entry.egid', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='suid', full_name='creds_entry.suid', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sgid', full_name='creds_entry.sgid', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fsuid', full_name='creds_entry.fsuid', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fsgid', full_name='creds_entry.fsgid', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cap_inh', full_name='creds_entry.cap_inh', index=8,
      number=9, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cap_prm', full_name='creds_entry.cap_prm', index=9,
      number=10, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cap_eff', full_name='creds_entry.cap_eff', index=10,
      number=11, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cap_bnd', full_name='creds_entry.cap_bnd', index=11,
      number=12, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='secbits', full_name='creds_entry.secbits', index=12,
      number=13, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='groups', full_name='creds_entry.groups', index=13,
      number=14, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lsm_profile', full_name='creds_entry.lsm_profile', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=263,
)

DESCRIPTOR.message_types_by_name['creds_entry'] = _CREDS_ENTRY

creds_entry = _reflection.GeneratedProtocolMessageType('creds_entry', (_message.Message,), dict(
  DESCRIPTOR = _CREDS_ENTRY,
  __module__ = 'creds_pb2'
  # @@protoc_insertion_point(class_scope:creds_entry)
  ))
_sym_db.RegisterMessage(creds_entry)


# @@protoc_insertion_point(module_scope)
