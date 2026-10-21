from argparse import ArgumentParser, Namespace
import json
import datetime

def main(): 
    parser = ArgumentParser()
    commands = parser.add_subparsers(dest='command', required=True)

    add_parser = commands.add_parser('add', help='Adds a new task.')
    add_parser.add_argument('description', type=str)

    update_parser = commands.add_parser('update', help='Updates an item from list')
    update_parser.add_argument('id', type=int)
    update_parser.add_argument('description', type=str)

    delete_parser = commands.add_parser('delete', help='Deletes an item from list.')
    delete_parser.add_argument('id', type=int)

    in_progress_parser = commands.add_parser('mark-in-progress', help='Marks an item as in-progress.')
    in_progress_parser.add_argument('id', type=int)

    done_parser = commands.add_parser('mark-done', help='Marks an item as done.')
    done_parser.add_argument('id', type=int)

    list_parser = commands.add_parser('list', help='List all items or lists items by status')
    list_parser.add_argument('status', nargs='?', choices=['todo', 'in-progress', 'done'], default=None)

    args = parser.parse_args()

    if args.command == 'add':
        try:
            with open('tasks.json', 'r', encoding='utf-8') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = []

        now = datetime.datetime.now()

        new_task = {
            "id": len(tasks) + 1, #TODO: implement maybe max(id) + 1
            "description": args.description,
            "status": 'todo',
            "createdAt": f'{now}',
            "updatedAt": f'{now}'
        }
        tasks.append(new_task)
        with open('tasks.json', 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=2)

    elif args.command == 'update':
        try:
            with open('tasks.json', 'r', encoding='utf-8') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            parser.error('tasks.json not found.')

        for task in tasks:
            if task['id'] == args.id: 
                task['description'] = args.description
                task['updatedAt'] = f'{datetime.datetime.now()}'
                print(f"Updated task {args.id}: {task['description']}")
                break
        else:
            parser.error(f'Task {args.id} not found.')

        with open('tasks.json', 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=2)
        
    elif args.command == 'delete':
        try:
            with open('tasks.json', 'r', encoding='utf-8') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            parser.error('tasks.json not found')

        original_count = len(tasks)

        tasks = [task for task in tasks if task['id'] != args.id]

        if len(tasks) == original_count:
            parser.error(f"Error: Task {args.id} not found.")
        else:
            with open('tasks.json', 'w', encoding='utf-8') as file:
                json.dump(tasks, file, indent=2)

            print(f'Task {args.id} deleted.')

    elif args.command == 'mark-in-progress':
        try:
            with open('tasks.json', 'r', encoding='utf-8') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            parser.error('tasks.json not found.')

        for task in tasks:
            if task['id'] == args.id: 
                task['status'] = 'in-progress'
                task['updatedAt'] = f'{datetime.datetime.now()}'
                print(f"Marked {args.id} as {task['status']}")
                break
        else:
            parser.error(f'Task {args.id} not found.')

        with open('tasks.json', 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=2)

    elif args.command == 'mark-done':
        try:
            with open('tasks.json', 'r', encoding='utf-8') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            parser.error('tasks.json not found.')

        for task in tasks:
            if task['id'] == args.id: 
                task['status'] = 'done'
                task['updatedAt'] = f'{datetime.datetime.now()}'
                print(f"Marked {args.id} as {task['status']}")
                break
        else:
            parser.error(f'Task {args.id} not found.')

        with open('tasks.json', 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=2)

    elif args.command == 'list':
        try:
            with open('tasks.json', 'r', encoding='utf-8') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = []
        if len(tasks) == 0:
            print('To-Do list is empty! Congrats!')

        tasks_to_show = tasks

        if args.status is not None:
            tasks_to_show = [
                task for task in tasks
                if task['status'] == args.status
            ]

        for task in tasks_to_show:
            print(f"{task['id']}=>\t[{task['status']}]\t{task['description']}")

if __name__ == '__main__':
    main()