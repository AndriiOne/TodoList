from django.test import TestCase
from django.urls import reverse

from tasks.models import Tag, Task


class TaskToggleStatusTest(TestCase):
    def test_toggle_marks_undone_task_as_done(self):
        task = Task.objects.create(content="Home Tasks", is_done=False)
        url = reverse("tasks:task-toggle-status", args=[task.id])
        self.client.post(url)
        task.refresh_from_db()
        self.assertTrue(task.is_done)

    def test_toggle_marks_done_task_as_undone(self):
        task = Task.objects.create(content="Home Tasks", is_done=True)
        url = reverse("tasks:task-toggle-status", args=[task.id])
        self.client.post(url)
        task.refresh_from_db()
        self.assertFalse(task.is_done)


class ModelTest(TestCase):
    def test_tasks_str(self):
        task = Task.objects.create(content="Home Tasks", is_done=False)
        self.assertEqual(str(task), "Home Tasks")

    def test_tag_str(self):
        task = Tag.objects.create(name="home")
        self.assertEqual(str(task), "home")


class OrderingTest(TestCase):
    def test_ordering_by_is_done(self):
        task_done = Task.objects.create(content="Work Tasks", is_done=True)
        task_undone = Task.objects.create(content="Home Tasks", is_done=False)
        tasks_from_db = list(Task.objects.all())
        self.assertEqual(tasks_from_db, [task_undone, task_done])
