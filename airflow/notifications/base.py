
import logging

class BaseNotificationHandler():

    def on_task_start(self, context):
        pass

    def on_task_finish(self, context):
        pass

    def on_sla_miss(self, context):
        pass

