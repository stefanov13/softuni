from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)

        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"
        
        task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        completed_tasks = list(filter(lambda t: t.completed, self.tasks))
        count_completed_tasks = len(completed_tasks)

        for task in completed_tasks:
            self.tasks.remove(task)

        return f"Cleared {count_completed_tasks} tasks."

    def view_section(self):
        output = [f"Section {self.name}:"]

        for t in self.tasks:
            output.append(t.details())

        return '\n'.join(output)

