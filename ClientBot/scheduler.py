from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sched import scheduler


class Scheduler:
    def __init__(self) -> None:
        self.scheduler = AsyncIOScheduler()
