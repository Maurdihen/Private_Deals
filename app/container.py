from app.service.students_serv import StudentServ
from setup_db import db

from app.dao.fathers_dao import FatherDao
from app.service.fathers_serv import FatherServ
from app.dao.mothers_dao import MotherDao
from app.service.mothers_serv import MotherServ
from app.dao.students_dao import StudentDao
from app.service.students_serv import StudentServ

father_dao = FatherDao(db.session)
father_serv = FatherServ(father_dao)

mother_dao = MotherDao(db.session)
mother_serv = MotherServ(mother_dao)

student_dao = StudentDao(db.session)
student_serv = StudentServ(student_dao)