# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/longhorn/longhorn-instance-manager/pkg/imrpc/disk.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='github.com/longhorn/longhorn-instance-manager/pkg/imrpc/disk.proto',
  package='imrpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nBgithub.com/longhorn/longhorn-instance-manager/pkg/imrpc/disk.proto\x12\x05imrpc\x1a\x1bgoogle/protobuf/empty.proto\"\xb8\x01\n\x04\x44isk\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x12\n\ntotal_size\x18\x05 \x01(\x03\x12\x11\n\tfree_size\x18\x06 \x01(\x03\x12\x14\n\x0ctotal_blocks\x18\x07 \x01(\x03\x12\x13\n\x0b\x66ree_blocks\x18\x08 \x01(\x03\x12\x12\n\nblock_size\x18\t \x01(\x03\x12\x14\n\x0c\x63luster_size\x18\n \x01(\x03\"{\n\x0fReplicaInstance\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x11\n\tdisk_name\x18\x03 \x01(\t\x12\x11\n\tdisk_uuid\x18\x04 \x01(\t\x12\x11\n\tspec_size\x18\x05 \x01(\x04\x12\x13\n\x0b\x61\x63tual_size\x18\x06 \x01(\x04\"\x84\x01\n\x11\x44iskCreateRequest\x12\"\n\tdisk_type\x18\x01 \x01(\x0e\x32\x0f.imrpc.DiskType\x12\x11\n\tdisk_name\x18\x02 \x01(\t\x12\x11\n\tdisk_uuid\x18\x03 \x01(\t\x12\x11\n\tdisk_path\x18\x04 \x01(\t\x12\x12\n\nblock_size\x18\x05 \x01(\x03\"Z\n\x0e\x44iskGetRequest\x12\"\n\tdisk_type\x18\x01 \x01(\x0e\x32\x0f.imrpc.DiskType\x12\x11\n\tdisk_name\x18\x02 \x01(\t\x12\x11\n\tdisk_path\x18\x03 \x01(\t\"]\n\x11\x44iskDeleteRequest\x12\"\n\tdisk_type\x18\x01 \x01(\x0e\x32\x0f.imrpc.DiskType\x12\x11\n\tdisk_name\x18\x02 \x01(\t\x12\x11\n\tdisk_uuid\x18\x03 \x01(\t\"W\n\x1e\x44iskReplicaInstanceListRequest\x12\"\n\tdisk_type\x18\x01 \x01(\x0e\x32\x0f.imrpc.DiskType\x12\x11\n\tdisk_name\x18\x02 \x01(\t\"\xcb\x01\n\x1f\x44iskReplicaInstanceListResponse\x12W\n\x11replica_instances\x18\x01 \x03(\x0b\x32<.imrpc.DiskReplicaInstanceListResponse.ReplicaInstancesEntry\x1aO\n\x15ReplicaInstancesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.imrpc.ReplicaInstance:\x02\x38\x01\"\x8b\x01\n DiskReplicaInstanceDeleteRequest\x12\"\n\tdisk_type\x18\x01 \x01(\x0e\x32\x0f.imrpc.DiskType\x12\x11\n\tdisk_name\x18\x02 \x01(\t\x12\x11\n\tdisk_uuid\x18\x03 \x01(\t\x12\x1d\n\x15replcia_instance_name\x18\x04 \x01(\t\"\xab\x01\n\x13\x44iskVersionResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x11\n\tgitCommit\x18\x02 \x01(\t\x12\x11\n\tbuildDate\x18\x03 \x01(\t\x12,\n$instanceManagerDiskServiceAPIVersion\x18\x04 \x01(\x03\x12/\n\'instanceManagerDiskServiceAPIMinVersion\x18\x05 \x01(\x03*%\n\x08\x44iskType\x12\x0e\n\nfilesystem\x10\x00\x12\t\n\x05\x62lock\x10\x01\x32\xbb\x03\n\x0b\x44iskService\x12\x33\n\nDiskCreate\x12\x18.imrpc.DiskCreateRequest\x1a\x0b.imrpc.Disk\x12>\n\nDiskDelete\x12\x18.imrpc.DiskDeleteRequest\x1a\x16.google.protobuf.Empty\x12-\n\x07\x44iskGet\x12\x15.imrpc.DiskGetRequest\x1a\x0b.imrpc.Disk\x12h\n\x17\x44iskReplicaInstanceList\x12%.imrpc.DiskReplicaInstanceListRequest\x1a&.imrpc.DiskReplicaInstanceListResponse\x12\\\n\x19\x44iskReplicaInstanceDelete\x12\'.imrpc.DiskReplicaInstanceDeleteRequest\x1a\x16.google.protobuf.Empty\x12@\n\nVersionGet\x12\x16.google.protobuf.Empty\x1a\x1a.imrpc.DiskVersionResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_DISKTYPE = _descriptor.EnumDescriptor(
  name='DiskType',
  full_name='imrpc.DiskType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='filesystem', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='block', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1351,
  serialized_end=1388,
)
_sym_db.RegisterEnumDescriptor(_DISKTYPE)

DiskType = enum_type_wrapper.EnumTypeWrapper(_DISKTYPE)
filesystem = 0
block = 1



_DISK = _descriptor.Descriptor(
  name='Disk',
  full_name='imrpc.Disk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='imrpc.Disk.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='imrpc.Disk.uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='imrpc.Disk.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='imrpc.Disk.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_size', full_name='imrpc.Disk.total_size', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='free_size', full_name='imrpc.Disk.free_size', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_blocks', full_name='imrpc.Disk.total_blocks', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='free_blocks', full_name='imrpc.Disk.free_blocks', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_size', full_name='imrpc.Disk.block_size', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster_size', full_name='imrpc.Disk.cluster_size', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=107,
  serialized_end=291,
)


_REPLICAINSTANCE = _descriptor.Descriptor(
  name='ReplicaInstance',
  full_name='imrpc.ReplicaInstance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='imrpc.ReplicaInstance.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='imrpc.ReplicaInstance.uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_name', full_name='imrpc.ReplicaInstance.disk_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_uuid', full_name='imrpc.ReplicaInstance.disk_uuid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec_size', full_name='imrpc.ReplicaInstance.spec_size', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actual_size', full_name='imrpc.ReplicaInstance.actual_size', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=293,
  serialized_end=416,
)


_DISKCREATEREQUEST = _descriptor.Descriptor(
  name='DiskCreateRequest',
  full_name='imrpc.DiskCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disk_type', full_name='imrpc.DiskCreateRequest.disk_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_name', full_name='imrpc.DiskCreateRequest.disk_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_uuid', full_name='imrpc.DiskCreateRequest.disk_uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_path', full_name='imrpc.DiskCreateRequest.disk_path', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_size', full_name='imrpc.DiskCreateRequest.block_size', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=419,
  serialized_end=551,
)


_DISKGETREQUEST = _descriptor.Descriptor(
  name='DiskGetRequest',
  full_name='imrpc.DiskGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disk_type', full_name='imrpc.DiskGetRequest.disk_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_name', full_name='imrpc.DiskGetRequest.disk_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_path', full_name='imrpc.DiskGetRequest.disk_path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=553,
  serialized_end=643,
)


_DISKDELETEREQUEST = _descriptor.Descriptor(
  name='DiskDeleteRequest',
  full_name='imrpc.DiskDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disk_type', full_name='imrpc.DiskDeleteRequest.disk_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_name', full_name='imrpc.DiskDeleteRequest.disk_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_uuid', full_name='imrpc.DiskDeleteRequest.disk_uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=645,
  serialized_end=738,
)


_DISKREPLICAINSTANCELISTREQUEST = _descriptor.Descriptor(
  name='DiskReplicaInstanceListRequest',
  full_name='imrpc.DiskReplicaInstanceListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disk_type', full_name='imrpc.DiskReplicaInstanceListRequest.disk_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_name', full_name='imrpc.DiskReplicaInstanceListRequest.disk_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=740,
  serialized_end=827,
)


_DISKREPLICAINSTANCELISTRESPONSE_REPLICAINSTANCESENTRY = _descriptor.Descriptor(
  name='ReplicaInstancesEntry',
  full_name='imrpc.DiskReplicaInstanceListResponse.ReplicaInstancesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='imrpc.DiskReplicaInstanceListResponse.ReplicaInstancesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='imrpc.DiskReplicaInstanceListResponse.ReplicaInstancesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=954,
  serialized_end=1033,
)

_DISKREPLICAINSTANCELISTRESPONSE = _descriptor.Descriptor(
  name='DiskReplicaInstanceListResponse',
  full_name='imrpc.DiskReplicaInstanceListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='replica_instances', full_name='imrpc.DiskReplicaInstanceListResponse.replica_instances', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DISKREPLICAINSTANCELISTRESPONSE_REPLICAINSTANCESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=830,
  serialized_end=1033,
)


_DISKREPLICAINSTANCEDELETEREQUEST = _descriptor.Descriptor(
  name='DiskReplicaInstanceDeleteRequest',
  full_name='imrpc.DiskReplicaInstanceDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disk_type', full_name='imrpc.DiskReplicaInstanceDeleteRequest.disk_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_name', full_name='imrpc.DiskReplicaInstanceDeleteRequest.disk_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disk_uuid', full_name='imrpc.DiskReplicaInstanceDeleteRequest.disk_uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replcia_instance_name', full_name='imrpc.DiskReplicaInstanceDeleteRequest.replcia_instance_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1036,
  serialized_end=1175,
)


_DISKVERSIONRESPONSE = _descriptor.Descriptor(
  name='DiskVersionResponse',
  full_name='imrpc.DiskVersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='imrpc.DiskVersionResponse.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gitCommit', full_name='imrpc.DiskVersionResponse.gitCommit', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buildDate', full_name='imrpc.DiskVersionResponse.buildDate', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceManagerDiskServiceAPIVersion', full_name='imrpc.DiskVersionResponse.instanceManagerDiskServiceAPIVersion', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceManagerDiskServiceAPIMinVersion', full_name='imrpc.DiskVersionResponse.instanceManagerDiskServiceAPIMinVersion', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1178,
  serialized_end=1349,
)

_DISKCREATEREQUEST.fields_by_name['disk_type'].enum_type = _DISKTYPE
_DISKGETREQUEST.fields_by_name['disk_type'].enum_type = _DISKTYPE
_DISKDELETEREQUEST.fields_by_name['disk_type'].enum_type = _DISKTYPE
_DISKREPLICAINSTANCELISTREQUEST.fields_by_name['disk_type'].enum_type = _DISKTYPE
_DISKREPLICAINSTANCELISTRESPONSE_REPLICAINSTANCESENTRY.fields_by_name['value'].message_type = _REPLICAINSTANCE
_DISKREPLICAINSTANCELISTRESPONSE_REPLICAINSTANCESENTRY.containing_type = _DISKREPLICAINSTANCELISTRESPONSE
_DISKREPLICAINSTANCELISTRESPONSE.fields_by_name['replica_instances'].message_type = _DISKREPLICAINSTANCELISTRESPONSE_REPLICAINSTANCESENTRY
_DISKREPLICAINSTANCEDELETEREQUEST.fields_by_name['disk_type'].enum_type = _DISKTYPE
DESCRIPTOR.message_types_by_name['Disk'] = _DISK
DESCRIPTOR.message_types_by_name['ReplicaInstance'] = _REPLICAINSTANCE
DESCRIPTOR.message_types_by_name['DiskCreateRequest'] = _DISKCREATEREQUEST
DESCRIPTOR.message_types_by_name['DiskGetRequest'] = _DISKGETREQUEST
DESCRIPTOR.message_types_by_name['DiskDeleteRequest'] = _DISKDELETEREQUEST
DESCRIPTOR.message_types_by_name['DiskReplicaInstanceListRequest'] = _DISKREPLICAINSTANCELISTREQUEST
DESCRIPTOR.message_types_by_name['DiskReplicaInstanceListResponse'] = _DISKREPLICAINSTANCELISTRESPONSE
DESCRIPTOR.message_types_by_name['DiskReplicaInstanceDeleteRequest'] = _DISKREPLICAINSTANCEDELETEREQUEST
DESCRIPTOR.message_types_by_name['DiskVersionResponse'] = _DISKVERSIONRESPONSE
DESCRIPTOR.enum_types_by_name['DiskType'] = _DISKTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Disk = _reflection.GeneratedProtocolMessageType('Disk', (_message.Message,), {
  'DESCRIPTOR' : _DISK,
  '__module__' : 'github.com.longhorn.longhorn_instance_manager.pkg.imrpc.disk_pb2'
  # @@protoc_insertion_point(class_scope:imrpc.Disk)
  })
_sym_db.RegisterMessage(Disk)

ReplicaInstance = _reflection.GeneratedProtocolMessageType('ReplicaInstance', (_message.Message,), {
  'DESCRIPTOR' : _REPLICAINSTANCE,
  '__module__' : 'github.com.longhorn.longhorn_instance_manager.pkg.imrpc.disk_pb2'
  # @@protoc_insertion_point(class_scope:imrpc.ReplicaInstance)
  })
_sym_db.RegisterMessage(ReplicaInstance)

DiskCreateRequest = _reflection.GeneratedProtocolMessageType('DiskCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _DISKCREATEREQUEST,
  '__module__' : 'github.com.longhorn.longhorn_instance_manager.pkg.imrpc.disk_pb2'
  # @@protoc_insertion_point(class_scope:imrpc.DiskCreateRequest)
  })
_sym_db.RegisterMessage(DiskCreateRequest)

DiskGetRequest = _reflection.GeneratedProtocolMessageType('DiskGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _DISKGETREQUEST,
  '__module__' : 'github.com.longhorn.longhorn_instance_manager.pkg.imrpc.disk_pb2'
  # @@protoc_insertion_point(class_scope:imrpc.DiskGetRequest)
  })
_sym_db.RegisterMessage(DiskGetRequest)

DiskDeleteRequest = _reflection.GeneratedProtocolMessageType('DiskDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DISKDELETEREQUEST,
  '__module__' : 'github.com.longhorn.longhorn_instance_manager.pkg.imrpc.disk_pb2'
  # @@protoc_insertion_point(class_scope:imrpc.DiskDeleteRequest)
  })
_sym_db.RegisterMessage(DiskDeleteRequest)

DiskReplicaInstanceListRequest = _reflection.GeneratedProtocolMessageType('DiskReplicaInstanceListRequest', (_message.Message,), {
  'DESCRIPTOR' : _DISKREPLICAINSTANCELISTREQUEST,
  '__module__' : 'github.com.longhorn.longhorn_instance_manager.pkg.imrpc.disk_pb2'
  # @@protoc_insertion_point(class_scope:imrpc.DiskReplicaInstanceListRequest)
  })
_sym_db.RegisterMessage(DiskReplicaInstanceListRequest)

DiskReplicaInstanceListResponse = _reflection.GeneratedProtocolMessageType('DiskReplicaInstanceListResponse', (_message.Message,), {

  'ReplicaInstancesEntry' : _reflection.GeneratedProtocolMessageType('ReplicaInstancesEntry', (_message.Message,), {
    'DESCRIPTOR' : _DISKREPLICAINSTANCELISTRESPONSE_REPLICAINSTANCESENTRY,
    '__module__' : 'github.com.longhorn.longhorn_instance_manager.pkg.imrpc.disk_pb2'
    # @@protoc_insertion_point(class_scope:imrpc.DiskReplicaInstanceListResponse.ReplicaInstancesEntry)
    })
  ,
  'DESCRIPTOR' : _DISKREPLICAINSTANCELISTRESPONSE,
  '__module__' : 'github.com.longhorn.longhorn_instance_manager.pkg.imrpc.disk_pb2'
  # @@protoc_insertion_point(class_scope:imrpc.DiskReplicaInstanceListResponse)
  })
_sym_db.RegisterMessage(DiskReplicaInstanceListResponse)
_sym_db.RegisterMessage(DiskReplicaInstanceListResponse.ReplicaInstancesEntry)

DiskReplicaInstanceDeleteRequest = _reflection.GeneratedProtocolMessageType('DiskReplicaInstanceDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DISKREPLICAINSTANCEDELETEREQUEST,
  '__module__' : 'github.com.longhorn.longhorn_instance_manager.pkg.imrpc.disk_pb2'
  # @@protoc_insertion_point(class_scope:imrpc.DiskReplicaInstanceDeleteRequest)
  })
_sym_db.RegisterMessage(DiskReplicaInstanceDeleteRequest)

DiskVersionResponse = _reflection.GeneratedProtocolMessageType('DiskVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _DISKVERSIONRESPONSE,
  '__module__' : 'github.com.longhorn.longhorn_instance_manager.pkg.imrpc.disk_pb2'
  # @@protoc_insertion_point(class_scope:imrpc.DiskVersionResponse)
  })
_sym_db.RegisterMessage(DiskVersionResponse)


_DISKREPLICAINSTANCELISTRESPONSE_REPLICAINSTANCESENTRY._options = None

_DISKSERVICE = _descriptor.ServiceDescriptor(
  name='DiskService',
  full_name='imrpc.DiskService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1391,
  serialized_end=1834,
  methods=[
  _descriptor.MethodDescriptor(
    name='DiskCreate',
    full_name='imrpc.DiskService.DiskCreate',
    index=0,
    containing_service=None,
    input_type=_DISKCREATEREQUEST,
    output_type=_DISK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DiskDelete',
    full_name='imrpc.DiskService.DiskDelete',
    index=1,
    containing_service=None,
    input_type=_DISKDELETEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DiskGet',
    full_name='imrpc.DiskService.DiskGet',
    index=2,
    containing_service=None,
    input_type=_DISKGETREQUEST,
    output_type=_DISK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DiskReplicaInstanceList',
    full_name='imrpc.DiskService.DiskReplicaInstanceList',
    index=3,
    containing_service=None,
    input_type=_DISKREPLICAINSTANCELISTREQUEST,
    output_type=_DISKREPLICAINSTANCELISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DiskReplicaInstanceDelete',
    full_name='imrpc.DiskService.DiskReplicaInstanceDelete',
    index=4,
    containing_service=None,
    input_type=_DISKREPLICAINSTANCEDELETEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='VersionGet',
    full_name='imrpc.DiskService.VersionGet',
    index=5,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_DISKVERSIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DISKSERVICE)

DESCRIPTOR.services_by_name['DiskService'] = _DISKSERVICE

# @@protoc_insertion_point(module_scope)
