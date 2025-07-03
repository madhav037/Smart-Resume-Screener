from enum import Enum

class UserRole(str, Enum):
    candidate = "candidate"
    recruiter = "recruiter"
    admin = "admin"

class EmploymentType(str, Enum):
    full_time = "full-time"
    part_time = "part-time"
    contract = "contract"
    internship = "internship"

class ApplicationStatus(str, Enum):
    applied = "applied"
    shortlisted = "shortlisted"
    rejected = "rejected"
    withdrawn = "withdrawn"

class CompanySize(str, Enum):
    small = "small"
    medium = "medium"
    large = "large"
