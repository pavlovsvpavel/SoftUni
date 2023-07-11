from abc import ABC, abstractmethod


class AnyWorker(ABC):

    @staticmethod
    @abstractmethod
    def work():
        pass


class Worker(AnyWorker):

    @staticmethod
    def work():
        print("I'm working!!")


class SuperWorker(AnyWorker):

    @staticmethod
    def work():
        print("I work very hard!!!")


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker_type):
        if not isinstance(worker_type, AnyWorker):
            raise AssertionError(f"'{worker_type.__class__.__name__}' class must be a subclass of {AnyWorker}")

        self.worker = worker_type

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = Worker()
manager = Manager()
super_worker = SuperWorker()

try:
    manager.set_worker(worker)
    manager.manage()

    manager.set_worker(super_worker)
    manager.manage()

except AssertionError as error:
    print(f"Manager fails to support....\n", error)
