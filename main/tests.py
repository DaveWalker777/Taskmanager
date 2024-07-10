# myapp/tests/test_models.py
import pytest
from django.utils import timezone
from main.models import Theme, Task

@pytest.fixture
def theme():
    return Theme.objects.create(title="Учеба")

@pytest.fixture
def task(theme):
    return Task.objects.create(
        theme=theme,
        title="Математика",
        task="Решить примеры",
        date=timezone.now().date(),
        time=timezone.now().time()
    )

@pytest.mark.django_db
def test_theme_creation(theme):
    assert theme.title == "Учеба"
    assert str(theme) == "Учеба"

@pytest.mark.django_db
def test_task_creation(task):
    assert task.title == "Математика"
    assert task.task == "Решить примеры"
    assert str(task) == "Математика"
    assert task.theme.title == "Учеба"

@pytest.mark.django_db
def test_task_link_to_theme(theme, task):
    assert task in theme.tasks.all()