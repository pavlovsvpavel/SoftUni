from abc import abstractmethod, ABC
import time


class AnyManager(ABC):
    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class Workable(ABC):

    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):

    @abstractmethod
    def eat(self):
        pass


class Worker(Workable, Eatable):
    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Workable, Eatable):
    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(Workable):
    def work(self):
        print("I'm a robot. I'm working....")


class WorkManager(AnyManager):
    def set_worker(self, worker):
        if not isinstance(worker, Workable):
            raise AssertionError(f"'{worker.__class__.__name__}' class must be a subclass of {Workable}")

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(AnyManager):
    def set_worker(self, worker):
        if not isinstance(worker, Eatable):
            raise AssertionError(f"'{worker.__class__.__name__}' class must be a subclass of {Eatable}")

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


work_manager = WorkManager()
break_manager = BreakManager()

work_manager.set_worker(Worker())
break_manager.set_worker(Worker())

work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())

work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()

try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()

except AssertionError:
    pass
