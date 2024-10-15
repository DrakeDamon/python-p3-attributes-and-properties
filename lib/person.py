#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name='Guido', job='Sales'):
        self.set_name(name)
        self.set_job(job)

    # Getter and Setter for Name
    def get_name(self):
        return self._name

    def set_name(self, name):
        '''Name must be string between 1 and 25 characters in length'''
        if isinstance(name, str) and 1 <= len(name) <= 25:
            
            self._name = name.title()
        else:
            print(
                "Name must be string between 1 and 25 characters."
            )

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs." )

# Usage
    name = property(get_name, set_name)
    job = property(get_job, set_job)