import pytest
import json
from task_manager import load_tasks, save_tasks, display_tasks, add_task, update_task, delete_task

@pytest.fixture
def mock_tasks():
    """Fixture for mock tasks."""
    return [
        {"title": "Task 1", "completed": False},
        {"title": "Task 2", "completed": True}
    ]

@pytest.fixture
def mock_task_manager(mock_tasks, tmpdir):
    """Fixture for mocking task manager behavior."""
    # Mock the file path to use a temporary directory
    tasks_file = tmpdir.join("tasks.json")
    tasks_file.write(json.dumps(mock_tasks))
    return str(tasks_file)

def test_load_tasks(mock_task_manager):
    """Test loading tasks from the file."""
    tasks = load_tasks(mock_task_manager)
    assert len(tasks) == 2
    assert tasks[0]["title"] == "Task 1"
    assert tasks[1]["completed"] is True

def test_save_tasks(mock_task_manager):
    """Test saving tasks to the file."""
    tasks = load_tasks(mock_task_manager)
    tasks.append({"title": "Task 3", "completed": False})
    save_tasks(tasks, mock_task_manager)
    
    tasks = load_tasks(mock_task_manager)
    assert len(tasks) == 3
    assert tasks[2]["title"] == "Task 3"

def test_display_tasks(mock_task_manager, capsys):
    """Test displaying tasks."""
    tasks = load_tasks(mock_task_manager)
    display_tasks(tasks)
    
    captured = capsys.readouterr()
    assert "Task 1 - Pending" in captured.out
    assert "Task 2 - Completed" in captured.out

def test_add_task(mock_task_manager, capsys):
    """Test adding a task."""
    tasks = load_tasks(mock_task_manager)
    add_task(tasks, "Task 3")
    
    assert len(tasks) == 3
    assert tasks[2]["title"] == "Task 3"
    assert tasks[2]["completed"] is False
    
def test_update_task(mock_task_manager):
    """Test updating a task status."""
    tasks = load_tasks(mock_task_manager)
    update_task(tasks, 1)
    
    assert tasks[0]["completed"] is True

def test_delete_task(mock_task_manager):
    """Test deleting a task."""
    tasks = load_tasks(mock_task_manager)
    delete_task(tasks, 1)
    
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Task 2"
