import random
from queue import Queue

class Printer:

    def __init__(self,ppm: int):
        self._page_rate = ppm
        self._current_task = None
        self._remaining_time = 0

    def tick(self):
        if self._current_task != None:
            self._remaining_time -= 1
            if self._remaining_time <= 0:
                self._current_task = None

    def busy(self) -> bool:
        return True if self._current_task != None else False

    def start(self,new_task):
        self._current_task = new_task
        self._remaining_time = new_task.num_pages * 60 / self._page_rate


class Task:

    def __init__(self,time: float):
        self._timestamp = time
        self._num_pages = random.randrange(1,21)

    @property
    def time_stamp(self) -> float:
        return self._timestamp

    @property
    def num_pages(self) -> int:
        return self._num_pages

    def wait_time(self,current_time: float) -> float:
        return current_time - self.time_stamp


def simulation(num_seconds: float,pages_per_minute: int):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task():              #adds a new printing task after every 3 minutes
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.isempty()):
            #checks if printer is not busy and the queue is not empty
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start(next_task)

        lab_printer.tick()
    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average wait time is %6.2f secs %3d tasks remaining"%(average_wait,print_queue._size))


def new_print_task():
    return True if random.randrange(1,181) == 180 else False  #returns true if the time is 180 seconds


for i in range(10):
    simulation(3600,2)