from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime, timezone
from app.db.db import Base

class JobApplicationStatusHistory(Base):
    __tablename__ = "job_application_status_history"

    id = Column(Integer, primary_key=True)
    application_id = Column(Integer, ForeignKey("job_applications.id"))
    old_status = Column(String)
    new_status = Column(String)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_by = Column(Integer, ForeignKey("users.id"))