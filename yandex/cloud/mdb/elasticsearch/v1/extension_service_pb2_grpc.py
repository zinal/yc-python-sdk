# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.mdb.elasticsearch.v1 import extension_pb2 as yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__pb2
from yandex.cloud.mdb.elasticsearch.v1 import extension_service_pb2 as yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class ExtensionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.mdb.elasticsearch.v1.ExtensionService/Get',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__service__pb2.GetExtensionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__pb2.Extension.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.mdb.elasticsearch.v1.ExtensionService/List',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__service__pb2.ListExtensionsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__service__pb2.ListExtensionsResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.mdb.elasticsearch.v1.ExtensionService/Create',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__service__pb2.CreateExtensionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.mdb.elasticsearch.v1.ExtensionService/Update',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__service__pb2.UpdateExtensionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.mdb.elasticsearch.v1.ExtensionService/Delete',
                request_serializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__service__pb2.DeleteExtensionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class ExtensionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """Returns the specified extension of Elasticsearch cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Returns the list of available extensions for the specified Elasticsearch cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates new extension version.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified extension.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified extension.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExtensionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__service__pb2.GetExtensionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__pb2.Extension.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__service__pb2.ListExtensionsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__service__pb2.ListExtensionsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__service__pb2.CreateExtensionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__service__pb2.UpdateExtensionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__service__pb2.DeleteExtensionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.mdb.elasticsearch.v1.ExtensionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ExtensionService(object):
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.elasticsearch.v1.ExtensionService/Get',
            yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__service__pb2.GetExtensionRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__pb2.Extension.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.elasticsearch.v1.ExtensionService/List',
            yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__service__pb2.ListExtensionsRequest.SerializeToString,
            yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__service__pb2.ListExtensionsResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.elasticsearch.v1.ExtensionService/Create',
            yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__service__pb2.CreateExtensionRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.elasticsearch.v1.ExtensionService/Update',
            yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__service__pb2.UpdateExtensionRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.mdb.elasticsearch.v1.ExtensionService/Delete',
            yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_extension__service__pb2.DeleteExtensionRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
