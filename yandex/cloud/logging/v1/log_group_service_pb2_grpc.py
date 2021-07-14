# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.logging.v1 import log_group_pb2 as yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__pb2
from yandex.cloud.logging.v1 import log_group_service_pb2 as yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class LogGroupServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.logging.v1.LogGroupService/Get',
                request_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.GetLogGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__pb2.LogGroup.FromString,
                )
        self.GetDefault = channel.unary_unary(
                '/yandex.cloud.logging.v1.LogGroupService/GetDefault',
                request_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.GetDefaultLogGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__pb2.LogGroup.FromString,
                )
        self.Stats = channel.unary_unary(
                '/yandex.cloud.logging.v1.LogGroupService/Stats',
                request_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.GetLogGroupStatsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.GetLogGroupStatsResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.logging.v1.LogGroupService/List',
                request_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.ListLogGroupsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.ListLogGroupsResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.logging.v1.LogGroupService/Create',
                request_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.CreateLogGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.logging.v1.LogGroupService/Update',
                request_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.UpdateLogGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.logging.v1.LogGroupService/Delete',
                request_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.DeleteLogGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListResources = channel.unary_unary(
                '/yandex.cloud.logging.v1.LogGroupService/ListResources',
                request_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.ListResourcesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.ListResourcesResponse.FromString,
                )
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.logging.v1.LogGroupService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.ListOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.ListOperationsResponse.FromString,
                )
        self.ListAccessBindings = channel.unary_unary(
                '/yandex.cloud.logging.v1.LogGroupService/ListAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
                )
        self.SetAccessBindings = channel.unary_unary(
                '/yandex.cloud.logging.v1.LogGroupService/SetAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.UpdateAccessBindings = channel.unary_unary(
                '/yandex.cloud.logging.v1.LogGroupService/UpdateAccessBindings',
                request_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class LogGroupServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDefault(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stats(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListResources(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAccessBindings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAccessBindings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAccessBindings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LogGroupServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.GetLogGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__pb2.LogGroup.SerializeToString,
            ),
            'GetDefault': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDefault,
                    request_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.GetDefaultLogGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__pb2.LogGroup.SerializeToString,
            ),
            'Stats': grpc.unary_unary_rpc_method_handler(
                    servicer.Stats,
                    request_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.GetLogGroupStatsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.GetLogGroupStatsResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.ListLogGroupsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.ListLogGroupsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.CreateLogGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.UpdateLogGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.DeleteLogGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListResources': grpc.unary_unary_rpc_method_handler(
                    servicer.ListResources,
                    request_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.ListResourcesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.ListResourcesResponse.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.ListOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.ListOperationsResponse.SerializeToString,
            ),
            'ListAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.SerializeToString,
            ),
            'SetAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.logging.v1.LogGroupService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LogGroupService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.logging.v1.LogGroupService/Get',
            yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.GetLogGroupRequest.SerializeToString,
            yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__pb2.LogGroup.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDefault(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.logging.v1.LogGroupService/GetDefault',
            yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.GetDefaultLogGroupRequest.SerializeToString,
            yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__pb2.LogGroup.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.logging.v1.LogGroupService/Stats',
            yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.GetLogGroupStatsRequest.SerializeToString,
            yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.GetLogGroupStatsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.logging.v1.LogGroupService/List',
            yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.ListLogGroupsRequest.SerializeToString,
            yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.ListLogGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.logging.v1.LogGroupService/Create',
            yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.CreateLogGroupRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.logging.v1.LogGroupService/Update',
            yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.UpdateLogGroupRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.logging.v1.LogGroupService/Delete',
            yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.DeleteLogGroupRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListResources(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.logging.v1.LogGroupService/ListResources',
            yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.ListResourcesRequest.SerializeToString,
            yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.ListResourcesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.logging.v1.LogGroupService/ListOperations',
            yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.ListOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_logging_dot_v1_dot_log__group__service__pb2.ListOperationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.logging.v1.LogGroupService/ListAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.logging.v1.LogGroupService/SetAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.SetAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.logging.v1.LogGroupService/UpdateAccessBindings',
            yandex_dot_cloud_dot_access_dot_access__pb2.UpdateAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
