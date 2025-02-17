from abc import ABC, abstractmethod
from typing import Literal

from pydantic import AliasPath, BaseModel, Field

ClockifyTimeEntryType = Literal["REGULAR", "TIMEOFF", "HOLIDAY"]

class TimeEntryService[T](ABC):
    @abstractmethod
    def get_time_entries(self, start_date: str, end_date: str) -> list[T]:
        raise NotImplementedError

class ClockifyTimeInterval(BaseModel):
    duration: str
    start: str
    end: str


class ClockifyTimeEntry(BaseModel):
    id: str
    description: str
    user_id: str = Field(validation_alias=AliasPath("userId"))
    billable: bool
    task_d: str = Field(validation_alias=AliasPath("taskId"))
    project_id: str = Field(validation_alias=AliasPath("projectId"))
    workspace_id: str = Field(validation_alias=AliasPath("workspaceId"))
    time_interval: ClockifyTimeInterval = Field(validation_alias=AliasPath("timeInterval"))
    type: ClockifyTimeEntryType


class ClockifyTimeEntryService(TimeEntryService[ClockifyTimeEntry]):
    def get_time_entries(self, start_date: str, end_date: str) -> list[ClockifyTimeEntry]:
        pass
