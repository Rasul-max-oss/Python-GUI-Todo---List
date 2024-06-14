import tkinter as tk

# Создаем окно приложения
root = tk.Tk()
root.title('Список задач')
root.configure(bg='#F5F5DC')  # Устанавливаем цвет фона окна


def add_task():
    task_text = task_entry.get()#получает текст из виджета task_entry
    if task_text:#если текст задачи не пустой
        #добавляет его в конец списка задач tasks_listbox
        tasks_listbox.insert(tk.END, task_text)
        #и очищает поле для ввода задач task_entry.
        task_entry.delete(0, tk.END)


def delete_task():
     selected_task = tasks_listbox.curselection()[0]#выбранный элемент при клике
     tasks_listbox.delete(selected_task)#удаление

# Функция complete_task() для завершения выбранной задачи в списке
def complete_task():
    # Получаем индекс выбранной задачи в списке
    selected_task = tasks_listbox.curselection()
    # Проверяем, была ли выбрана задача
    if selected_task:
        # Получаем индекс выбранной задачи
        index = selected_task[0]
        # Устанавливаем цвет текста для задачи с указанным индексом в зеленый
        tasks_listbox.itemconfig(index, {'fg': 'green'})


def edit_task():
    # Получаем индекс выбранной задачи в списке
    selected_task = tasks_listbox.curselection()
    if selected_task:
        # Получаем индекс выбранной задачи
        index = selected_task[0]

        # Создаем новое окно для редактирования задачи
        edit_window = tk.Toplevel(root)
        edit_window.title('Редактировать задачу')

        # Функция для сохранения изменений и обновления задачи
        def save_edit():
            new_text = edit_entry.get()  # Получаем новый текст задачи из поля ввода
            tasks_listbox.delete(index)  # Удаляем старую задачу из списка
            tasks_listbox.insert(index, new_text)  # Вставляем отредактированную задачу обратно
            edit_window.destroy()  # Закрываем окно редактирования

        # Создаем виджет для ввода нового текста задачи
        edit_entry = tk.Entry(edit_window, width=30)
        edit_entry.pack(pady=10)

        # Кнопка для сохранения изменений
        save_button = tk.Button(edit_window, text='Сохранить', command=save_edit)
        save_button.pack()

# Создаем поле для ввода новой задачи
task_entry = tk.Entry(root, width=30, bg="white", fg="black", font=('Arial', 12))
task_entry.pack(pady=10)

# Создаем список для отображения задач
tasks_listbox = tk.Listbox(root, width=50, bg="white", fg="black", font=('Arial', 12))
tasks_listbox.pack(padx=10, pady=10)

# Создаем кнопку для добавления задачи
add_button = tk.Button(root, text="Добавить задачу", bg="#4CAF50", fg="white",command=add_task)
add_button.pack()

# Создаем кнопку для удаления выбранной задачи из списка
delete_button = tk.Button(root, text='Удалить выбранную задачу', bg="#4CAF50", fg="white",command=delete_task)
delete_button.pack(pady=10)

# Создаем кнопку для отметки задачи как выполненной
mark_button = tk.Button(root, text='Отметить задачу', bg="#4CAF50", fg="white",command=complete_task)
mark_button.pack()

# Создаем кнопку для редактирования выбранной задачи
edit_button = tk.Button(root, text='Редактировать выбранную задачу', bg="#4CAF50", fg="white",command=edit_task)
edit_button.pack()

# Запускаем главный цикл обработки событий окна
root.mainloop()

