# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class NDArray(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ndarray = ... # type: builtin___bytes

    def __init__(self,
        *,
        ndarray : typing___Optional[builtin___bytes] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> NDArray: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> NDArray: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"ndarray"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"ndarray",b"ndarray"]) -> None: ...

class Weights(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def weights(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[NDArray]: ...

    def __init__(self,
        *,
        weights : typing___Optional[typing___Iterable[NDArray]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Weights: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Weights: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"weights"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"weights",b"weights"]) -> None: ...

class ClientInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    gpu = ... # type: builtin___bool

    def __init__(self,
        *,
        gpu : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ClientInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ClientInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"gpu"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"gpu",b"gpu"]) -> None: ...

class ClientRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Connect(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def info(self) -> ClientInfo: ...

        def __init__(self,
            *,
            info : typing___Optional[ClientInfo] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ClientRequest.Connect: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ClientRequest.Connect: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"info"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"info"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"info",b"info"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"info",b"info"]) -> None: ...

    class WeightUpdate(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        num_examples = ... # type: builtin___int

        @property
        def weights(self) -> Weights: ...

        def __init__(self,
            *,
            weights : typing___Optional[Weights] = None,
            num_examples : typing___Optional[builtin___int] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ClientRequest.WeightUpdate: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ClientRequest.WeightUpdate: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"weights"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"num_examples",u"weights"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"weights",b"weights"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"num_examples",b"num_examples",u"weights",b"weights"]) -> None: ...


    @property
    def connect(self) -> ClientRequest.Connect: ...

    @property
    def weight_update(self) -> ClientRequest.WeightUpdate: ...

    def __init__(self,
        *,
        connect : typing___Optional[ClientRequest.Connect] = None,
        weight_update : typing___Optional[ClientRequest.WeightUpdate] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ClientRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ClientRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"connect",u"report",u"weight_update"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"connect",u"report",u"weight_update"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"connect",b"connect",u"report",b"report",u"weight_update",b"weight_update"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"connect",b"connect",u"report",b"report",u"weight_update",b"weight_update"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"report",b"report"]) -> typing_extensions___Literal["connect","weight_update"]: ...

class ServerResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Reconnect(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        seconds = ... # type: builtin___int

        def __init__(self,
            *,
            seconds : typing___Optional[builtin___int] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ServerResponse.Reconnect: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ServerResponse.Reconnect: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"seconds"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"seconds",b"seconds"]) -> None: ...

    class Train(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        epochs = ... # type: builtin___int

        @property
        def weights(self) -> Weights: ...

        def __init__(self,
            *,
            weights : typing___Optional[Weights] = None,
            epochs : typing___Optional[builtin___int] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ServerResponse.Train: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ServerResponse.Train: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"weights"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"epochs",u"weights"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"weights",b"weights"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"epochs",b"epochs",u"weights",b"weights"]) -> None: ...


    @property
    def reconnect(self) -> ServerResponse.Reconnect: ...

    @property
    def train(self) -> ServerResponse.Train: ...

    def __init__(self,
        *,
        reconnect : typing___Optional[ServerResponse.Reconnect] = None,
        train : typing___Optional[ServerResponse.Train] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ServerResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ServerResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"instruction",u"reconnect",u"train"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"instruction",u"reconnect",u"train"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"instruction",b"instruction",u"reconnect",b"reconnect",u"train",b"train"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"instruction",b"instruction",u"reconnect",b"reconnect",u"train",b"train"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"instruction",b"instruction"]) -> typing_extensions___Literal["reconnect","train"]: ...