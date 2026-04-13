from aiogram.fsm.state import StatesGroup, State


class RegisterState(StatesGroup):# bu quyidagi steatelarga tushuradi
    language = State()
    full_name = State()
    phone_number = State()
    age = State()
    location = State()