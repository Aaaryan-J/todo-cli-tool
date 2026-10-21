# Task CLI

A small command-line task manager built with Python. Tasks are stored locally in a JSON file.

## Features

- Add tasks
- Update task descriptions
- Delete tasks
- Mark tasks as in progress or done
- List all tasks
- Filter tasks by status

## Installation

Clone the repository and move into the project directory:

```
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd todo_cli
```

Create and activate a virtual environment if needed:

```
python -m venv myenv
myenv\Scripts\activate
```

Install the project:

```
python -m pip install -e .
```

## Usage

Add a task:

```
task-cli add "Buy groceries"
```

Update a task:

```
task-cli update 1 "Buy groceries and cook dinner"
```

Delete a task:

```
task-cli delete 1
```

Mark a task as in progress:

```
task-cli mark-in-progress 1
```

Mark a task as done:

```
task-cli mark-done 1
```

List all tasks:

```
task-cli list
```

List tasks by status:

```
task-cli list todo
task-cli list in-progress
task-cli list done
```

Tasks are saved in a local `tasks.json` file. This file is ignored by Git because it contains local task data.

## License

This project is for learning and personal use.
