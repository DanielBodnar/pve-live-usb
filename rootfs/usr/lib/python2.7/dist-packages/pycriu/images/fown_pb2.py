# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fown.proto

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
  name='fown.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\nfown.proto\"V\n\nfown_entry\x12\x0b\n\x03uid\x18\x01 \x02(\r\x12\x0c\n\x04\x65uid\x18\x02 \x02(\r\x12\x0e\n\x06signum\x18\x03 \x02(\r\x12\x10\n\x08pid_type\x18\x04 \x02(\r\x12\x0b\n\x03pid\x18\x05 \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FOWN_ENTRY = _descriptor.Descriptor(
  name='fown_entry',
  full_name='fown_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='fown_entry.uid', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='euid', full_name='fown_entry.euid', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signum', full_name='fown_entry.signum', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pid_type', full_name='fown_entry.pid_type', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pid', full_name='fown_entry.pid', index=4,
      number=5, type=13, cpp_type=3, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=100,
)

DESCRIPTOR.message_types_by_name['fown_entry'] = _FOWN_ENTRY

fown_entry = _reflection.GeneratedProtocolMessageType('fown_entry', (_message.Message,), dict(
  DESCRIPTOR = _FOWN_ENTRY,
  __module__ = 'fown_pb2'
  # @@protoc_insertion_point(class_scope:fown_entry)
  ))
_sym_db.RegisterMessage(fown_entry)


# @@protoc_insertion_point(module_scope)
