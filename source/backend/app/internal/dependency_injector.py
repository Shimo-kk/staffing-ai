from injector import Injector, Module, singleton
from app.internal.application.interface.service.log_service import ILogService
from app.internal.application.interface.service.slack_service import ISlackService
from app.internal.application.provider.log_provider import ILogProvider
from app.internal.application.provider.notification_provider import (
    INotificationProveider,
)
from app.internal.infrastructure.service.log_service import LogService
from app.internal.infrastructure.service.slack_service import SlackService
from app.internal.application.provider.log_provider import LogProvider
from app.internal.application.provider.notification_provider import (
    NotificationProvider,
)


class DependencyModule(Module):
    def __init__(self):
        pass

    def configure(self, binder):
        # サービス
        binder.bind(ILogService, to=LogService, scope=singleton)
        binder.bind(ISlackService, to=SlackService, scope=singleton)

        # プロバイダ
        binder.bind(ILogProvider, to=LogProvider, scope=singleton)
        binder.bind(INotificationProveider, to=NotificationProvider, scope=singleton)


dependency_injector: Injector = Injector([DependencyModule()])
