from collectors.auth_collector import AuthCollector
from collectors.payment_collector import PaymentCollector
from collectors.storage_collector import StorageCollector
from collectors.notify_collector import NotifyCollector


class AnalyticsService:

    def __init__(self):

        self.auth = AuthCollector()

        self.payment = PaymentCollector()

        self.storage = StorageCollector()

        self.notify = NotifyCollector()

    def overview(self):

        return {

            "auth": self.auth.metrics(),

            "payment": self.payment.metrics(),

            "storage": self.storage.metrics(),

            "notify": self.notify.metrics()

        }
