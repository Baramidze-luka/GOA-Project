import json
import os

# JSON ფაილის გზის განსაზღვრა
PathToFileJson = os.path.join(os.path.dirname(__file__), 'UserData.json')

class Account:
    # აქაუნთის შესაქმნელი ფუნქცია რომელიც გამოიძახება როცა Account() ფუნქციას გამოიყენებ
    def __init__(self):
        self.name = None
        self.user = None

    # რეგისტრაციის ფუნქცია, რომელიც იღებს მომხმარებლის სახელს, პაროლს და ელ.ფოსტას
    def SignUp(self, name: str, password: str, e_mail: str) -> str:
        template = {"password": password, "e_mail": e_mail, "data": {
            'Balance': {
            "GOA BANK": 0.0,  # GOA BANK-ის საწყისი ბალანსი
            "TBC BANK": 0.0,  # TBC BANK-ის საწყისი ბალანსი
            "GEO BANK": 0.0,  # GEO BANK-ის საწყისი ბალანსი
            },
            "Cards": {

            },
            "AutoFill": {
                'Cards':[],
                'PersonalData':   [],
            }
        }}  # ეს არის შაბლონი, რომელიც გამოიყენება ახალი მომხმარებლისთვის
        try:
            # ვხსნით UserData.json ფაილს წასაკითხად
            if not os.path.exists(PathToFileJson):
                with open(PathToFileJson, 'w') as file:
                    json.dump({}, file)  # ვქმნით ცარიელ JSON ფაილს თუ ის არ არსებობს

            with open(PathToFileJson, 'r') as file:
                users = json.load(file)  # ვტვირთავთ მომხმარებლების მონაცემებს JSON ფაილიდან
                # ვამოწმებთ, არსებობს თუ არა მომხმარებელი ამ სახელით ან ელ.ფოსტით
                for user in users.values():
                    if user['e_mail'] == e_mail:
                        return "Email Already Exists"  # თუ ელ.ფოსტა უკვე არსებობს, ვაბრუნებთ შესაბამის შეტყობინებას
                if name not in users:
                    users[name] = template  # თუ არ არსებობს, ვქმნით ახალ მომხმარებელს შაბლონის მიხედვით
                    # ვხსნით UserData.json ფაილს ჩასაწერად
                    with open(PathToFileJson, 'w') as file:
                        json.dump(users, file, indent=4)  # ვწერთ განახლებულ მონაცემებს JSON ფაილში
                    self.LogIn(name, password, e_mail)  # ვიძახებთ LogIn ფუნქციას ავტორიზაციისთვის
                    return "Account created successfully"  # ვაბრუნებთ წარმატების შეტყობინებას
                return "Username Already Exists"  # თუ მომხმარებელი უკვე არსებობს, ვაბრუნებთ შესაბამის შეტყობინებას
        except json.JSONDecodeError:
            return "Error decoding JSON data"  # თუ JSON მონაცემების დეკოდირებისას მოხდა შეცდომა, ვაბრუნებთ შეცდომის შეტყობინებას

    # აქაუნთში შესვლა
    def LogIn(self, name: str, password: str, e_mail: str) -> str:
        try:
            # ვხსნით UserData.json ფაილს წასაკითხად
            with open(PathToFileJson, 'r') as file:
                users = json.load(file)  # ვტვირთავთ მომხმარებლების მონაცემებს JSON ფაილიდან
                if name in users:  # ვამოწმებთ, არსებობს თუ არა მომხმარებელი ამ სახელით
                    user = users[name]  # ვიღებთ მომხმარებლის მონაცემებს
                    # ვამოწმებთ, ემთხვევა თუ არა პაროლი და ელ.ფოსტა
                    if user['password'] == password and user['e_mail'] == e_mail:
                        self.name = name  # ვინახავთ მომხმარებლის სახელს
                        self.user = user  # ვინახავთ მომხმარებლის მონაცემებს
                        return "Login successful"  # ვაბრუნებთ წარმატების შეტყობინებას
                return "Incorrect Username or Password"  # თუ მონაცემები არ ემთხვევა, ვაბრუნებთ შეცდომის შეტყობინებას
        except FileNotFoundError:
            return "UserData.json file not found"  # თუ ფაილი არ მოიძებნა, ვაბრუნებთ შესაბამის შეტყობინებას
        except json.JSONDecodeError:
            return "Error decoding JSON data"  # თუ JSON მონაცემების დეკოდირებისას მოხდა შეცდომა, ვაბრუნებთ შეცდომის შეტყობინებას

    # აქაუნთიდან გამოსვლა
    def LogOut(self):
        self.SaveData()
        self.name = None
        self.user = None  # ვანულებთ self-ს, რაც ნიშნავს რომ მომხმარებელი გამოვიდა სისტემიდან
        
    # მონაცემების ჩატვირთვა
    def LoadData(self):
        try:
            # ვხსნით UserData.json ფაილს წასაკითხად
            with open(PathToFileJson, 'r') as file:
                self.user = json.load(file)[self.name]  # ვტვირთავთ მომხმარებლის მონაცემებს JSON ფაილიდან
        except FileNotFoundError:
            self.user = {}  # თუ ფაილი არ მოიძებნა, ვქმნით ცარიელ მონაცემებს
        except json.JSONDecodeError:
            self.user = {}  # თუ JSON მონაცემების დეკოდირებისას მოხდა შეცდომა, ვქმნით ცარიელ მონაცემებს

    # მონაცემების შენახვა
    def SaveData(self):
        try:
            # ვხსნით UserData.json ფაილს წასაკითხად
            with open(PathToFileJson, 'r') as file:
                users = json.load(file)  # ვტვირთავთ მომხმარებლების მონაცემებს JSON ფაილიდან
            # ვამატებთ ან ვაახლებთ მომხმარებლის მონაცემებს
            users[self.name] = self.user
            # ვხსნით UserData.json ფაილს ჩასაწერად
            with open(PathToFileJson, 'w') as file:
                json.dump(users, file, indent=4)  # ვწერთ განახლებულ მონაცემებს JSON ფაილში
        except Exception as e:
            print(f"An error occurred while saving data: {e}")  # თუ მოხდა შეცდომა, ვბეჭდავთ შეცდომის შეტყობინებას

    # ახალი მომხმარებლის დამატება
    def AddUser(self, name: str, password: str, e_mail: str):
        self.SignUp(name, password, e_mail)  # ვიძახებთ SignUp ფუნქციას
        self.SaveData()  # ვიძახებთ SaveData ფუნქციას მონაცემების შესანახად