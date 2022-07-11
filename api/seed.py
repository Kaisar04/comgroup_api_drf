from api.models import Employer
from faker import Faker

fake = Faker()

for i in range(10000):
    level1 = Employer(full_name=fake.name(), job_title = "level1", start_date=fake.date(), salary=fake.random_int(1000))
    level1.save()
    level2 = Employer(full_name=fake.name(), job_title = "level2", start_date=fake.date(), salary=fake.random_int(1000), parent=level1)
    level2.save()
    level3 = Employer(full_name=fake.name(), job_title = "level3", start_date=fake.date(), salary=fake.random_int(1000), parent=level2)
    level3.save()
    level4 = Employer(full_name=fake.name(), job_title = "level4", start_date=fake.date(), salary=fake.random_int(1000), parent=level3)
    level4.save()
    level5 = Employer(full_name=fake.name(), job_title = "level5", start_date=fake.date(), salary=fake.random_int(1000), parent=level4)
    level5.save()