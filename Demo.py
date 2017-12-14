from src.api import Api
from src.permission import Permission
from src.person import Person
from src.project import Project
from src.uplink import Uplink

if __name__=="__main__":
    user=input('\nEnter UserName:')
    password=input('\nEnter Password:')
    pd=Person(user, password)
    print('\n[*]logining...')
    pd.api.login()
    print('\n[+]login done.')
    connection=pd.api

    while True:
        choice=input('\nEnter 1 for add new project:\nEnter 2 for projects list.\n')
        choice=int(choice)
        
        if choice==1:
            project_name=input('\nEnter project name')
            project_description= input('\nEnter project description')
            print('\n[*]making project...')
            pd.make_new_project(project_name, project_description)
            print('\n[+]making project done!')
            
        elif choice==2:
            print('\n[*]getting projects')
            projects=pd.get_projects(page_size=20, page_number=0)
##            print("\n[+] projects are:", pd.projects)
            for index, project in enumerate(projects):
                print(index, ':', project.project_obj['name'])

            choice=input('Enter project number')
            choice=int(choice)

##            print('[+]selected project is', pd.projects[choice])
##             print('[+]selected project content is', pd.projects[choice].project_obj)
            x=input('Enter 1 for  add things\nEnter 2 for get things')
            x=int(x)

            if x==2:
                
                things=pd.projects[choice].get_things(page_number=1, page_size=10, api=connection)
                for index, thing in enumerate(things):
                    print(index, ':', thing.thing_obj['name'])

                thing_choice=int(input('Select thing: '))
                

                z=input('Enter 1 for sensors\nEnter 2 for add sensor')
                z=int(z)

                if z==1:
                    sensors=pd.projects[choice].things[thing_choice].get_sensors(connection)
                    for index, sensor in enumerate(sensors):
                        print(index, ':', sensor.sensor_obj)

            elif x==1:
                thing_name=input('Enter thing_name')
                description=input('Enter description')
                print('\nadding thing.')
                pd.projects[choice].make_new_thing(thing_name, description, api=connection)
                print('adding done')
                
