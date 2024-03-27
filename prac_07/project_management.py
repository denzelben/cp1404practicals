import datetime
from operator import itemgetter
from prac_07.project import Project
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- " \
       "(A)dd new project\n- (U)pdate project\n- (Q)uit"
FILENAME = "projects.txt"

projects = []
finished_projects = []
unfinished_projects = []

def main():
    print("Welcome to Pythonic Project Management")
    print("Loaded 5 projects from projects.txt")
    in_file = open(FILENAME, "r")
    choice = get_choice().upper()
    while choice != "Q":
        if choice == "D":
            projects.sort(key=itemgetter(2), reverse=False)
            update_project_list()
            print("Incomplete Projects:")
            print_incomplete_projects()
            print("Complete Projects:")
            print_completed_projects()

        elif choice == "U":
            for i in range(len(projects)):
                print(f"{i} {Project(projects[i][0], projects[i][1], projects[i][2], projects[i][3], projects[i][4])}")
            try:
                project_choice = int(input("Project Choice: "))
                print_project_detail(projects, project_choice)
                new_percentage = int(input("New Percentage: "))
                projects[project_choice][4] = new_percentage
                new_priority = int(input("New priority: "))
                projects[project_choice][2] = new_priority
            except ValueError:
                print("Value Error")

        elif choice == "A":
            print("Let's add a new project")
            try:
                get_new_project()
            except ValueError:
                print("Value Error")

        elif choice == "F":
            try:
                start_date = input("Show projects that start after date (dd/mm/yy): ")
                pairs = start_date.split("/")
                integer_date = [int(pair) for pair in pairs]
                convert_date = datetime.date(integer_date[2], integer_date[1], integer_date[0])
                filtered_projects = [project for project in projects if project[1] >= convert_date]
                filtered_projects.sort(key=itemgetter(1))
                for i in range(len(filtered_projects)):
                    print_project_detail(filtered_projects, i)
            except ValueError:
                print("Enter a valid date!")

        elif choice == "s":
            rewrite_file = input(f"Would you like to save to {FILENAME}").lower()
            if "yes" in rewrite_file:
                save_project()

        elif choice == "l":
            load_file()

        else:
            print("Invalid Input")

        choice = get_choice()

    save_changes = input(f"Would you like to save to {FILENAME}? ").lower()
    if "yes" in save_changes:
        save_project()
    print("Thank you for using custom-built project management software.")


def get_choice():
    """Get choice"""
    print(MENU)
    choice = input(">>> ").lower()
    return choice


def get_new_project():
    """Add a new valid project."""
    new_project_name = input("Name: ")
    new_project_date = input("Start date (dd/mm/yy): ")
    pairs = new_project_date.split("/")
    integer_date = [int(pair) for pair in pairs]
    convert_date = datetime.date(integer_date[2], integer_date[1], integer_date[0])
    new_project_date = convert_date
    new_priority = int(input("Priority: "))
    new_cost_estimate = float(input("Cost estimate: $"))
    new_percent_complete = int(input("Percent complete: "))
    projects.append([new_project_name, new_project_date, new_priority, new_cost_estimate,
                     new_percent_complete])


def print_completed_projects():
    """Print completed projects."""
    for completed_project in completed_projects:
        print(
            f"\t{Project(completed_project[0], completed_project[1], completed_project[2], completed_project[3], completed_project[4])}")


def print_incomplete_projects():
    """Print incomplete projects."""
    for incomplete_project in incomplete_projects:
        print(
            f"\t{Project(incomplete_project[0], incomplete_project[1], incomplete_project[2], incomplete_project[3], incomplete_project[4])}")


def update_project_list():
    """Update completion percentage."""
    for project in projects:
        if project[4] == 100:
            if project not in finished_projects:
                finished_projects.append(project)
            if project in unfinished_projects:
                unfinished_projects.remove(project)
        else:
            if project not in unfinished_projects:
                unfinished_projects.append(project)
            if project in finished_projects:
                unfinished_projects.remove(project)


def save_project():
    """Save project to FILENAME."""
    with open(FILENAME, "w") as out_file:
        print(f"Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            formatted_date = project[1].strftime("%d/%m/%Y")
            print(f"{project[0]}\t{formatted_date}\t{project[2]}\t{project[3]}\t{project[4]}",
                  file=out_file)


def print_project_detail(filtered_projects, i):
    """Print project detail."""
    print(
        f"{Project(filtered_projects[i][0], filtered_projects[i][1], filtered_projects[i][2], filtered_projects[i][3], filtered_projects[i][4])}")


def load_file():
    """Load project details from FILENAME."""
    in_file = open(FILENAME, "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(f"\t")
        pairs = parts[1].split("/")
        integer_date = [int(pair) for pair in pairs]
        convert_date = datetime.date(integer_date[2], integer_date[1], integer_date[0])
        parts[1] = convert_date  # Ignore python warning
        parts[2] = int(parts[2])  # Ignore python warning
        parts[3] = float(parts[3])  # Ignore python warning
        parts[4] = int(parts[4])  # Ignore python warning
        projects.append(parts)  # Ignore python warning
    in_file.close()
    return in_file


main()