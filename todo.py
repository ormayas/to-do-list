
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Ajouter une tâche."""
        self.tasks.append({
            "title": task,
            "completed": False
        })
        print("✅ Tâche ajoutée avec succès.")

    def display_tasks(self):
        """Afficher toutes les tâches."""
        if not self.tasks:
            print("\n📭 Aucune tâche enregistrée.")
            return

        print("\n========== MES TÂCHES ==========")

        for index, task in enumerate(self.tasks, start=1):
            status = "✔" if task["completed"] else "✘"
            print(f"{index}. [{status}] {task['title']}")

    def complete_task(self, task_number):
        """Marquer une tâche comme terminée."""
        try:
            self.tasks[task_number - 1]["completed"] = True
            print("🎉 Tâche terminée.")
        except IndexError:
            print("❌ Numéro de tâche invalide.")

    def delete_task(self, task_number):
        """Supprimer une tâche."""
        try:
            deleted = self.tasks.pop(task_number - 1)
            print(f"🗑️ '{deleted['title']}' supprimée.")
        except IndexError:
            print("❌ Numéro de tâche invalide.")


def display_menu():
    print("\n" + "=" * 35)
    print("         TO-DO LIST")
    print("=" * 35)
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Marquer une tâche comme terminée")
    print("4. Supprimer une tâche")
    print("5. Quitter")


def main():
    todo = TodoList()

    while True:
        display_menu()

        choice = input("\nVotre choix : ")

        match choice:
            case "1":
                task = input("Nouvelle tâche : ")
                todo.add_task(task)

            case "2":
                todo.display_tasks()

            case "3":
                todo.display_tasks()
                try:
                    number = int(input("\nNuméro de la tâche terminée : "))
                    todo.complete_task(number)
                except ValueError:
                    print("❌ Veuillez entrer un nombre.")

            case "4":
                todo.display_tasks()
                try:
                    number = int(input("\nNuméro de la tâche à supprimer : "))
                    todo.delete_task(number)
                except ValueError:
                    print("❌ Veuillez entrer un nombre.")

            case "5":
                print("\n👋 Merci d'avoir utilisé la To-Do List.")
                break

            case _:
                print("❌ Choix invalide.")


if __name__ == "__main__":
    main()
