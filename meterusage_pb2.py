# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meterusage.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10meterusage.proto\x12\nmeterusage\"\x13\n\x11MeterUsageRequest\"4\n\x10MeterUsageRecord\x12\x0c\n\x04time\x18\x01 \x01(\t\x12\x12\n\nmeterusage\x18\x02 \x01(\x01\"C\n\x12MeterUsageResponse\x12-\n\x07records\x18\x01 \x03(\x0b\x32\x1c.meterusage.MeterUsageRecord2e\n\x11MeterUsageService\x12P\n\rGetMeterUsage\x12\x1d.meterusage.MeterUsageRequest\x1a\x1e.meterusage.MeterUsageResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meterusage_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_METERUSAGEREQUEST']._serialized_start=32
  _globals['_METERUSAGEREQUEST']._serialized_end=51
  _globals['_METERUSAGERECORD']._serialized_start=53
  _globals['_METERUSAGERECORD']._serialized_end=105
  _globals['_METERUSAGERESPONSE']._serialized_start=107
  _globals['_METERUSAGERESPONSE']._serialized_end=174
  _globals['_METERUSAGESERVICE']._serialized_start=176
  _globals['_METERUSAGESERVICE']._serialized_end=277
# @@protoc_insertion_point(module_scope)