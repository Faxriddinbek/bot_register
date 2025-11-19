from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from keyboards.default import phone_number, location
from keyboards.inline import IT_language
from states.register import RegisterState

router = Router() # Router bu dispecherni yordamchisi


@router.message(F.text == "/start")# F.text bu kelgan xabarni anglatadi lekin ishlamidi
async def start_handler(message: Message, state: FSMContext):
    text = "Iltimos tilni tanlang\nPlease select the language."# message => bu foydalanuvchiga yuboriladigon habar
    await message.answer(text=text, reply_markup=IT_language)# answer => nima yuborayotganga qarab type tanlanadi
    await state.set_state(RegisterState.IT_language)


@router.callback_query(RegisterState.IT_language)# callback_query inline button ishlash uchun kerak
async def IT_language_handler(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    registered = data.get("IT_language", [])

    if call.data in registered:
        return await call.message.answer("Bu tildan ro'yhatdan o'tgansiz")

    await state.update_data(IT_language=call.data)
    text = "Iltimos to'liq ismingizni kliriting"
    await call.message.answer(text=text)# call tepadagi messageni (buttonni orqasidagi malumot) olosh uchun kerak
    await state.set_state(RegisterState.full_name)


@router.message(RegisterState.full_name)
async def full_name_handler(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    text = "Iltimos telefon raqamingizni kiriting"
    await message.answer(text=text, reply_markup=phone_number)
    await state.set_state(RegisterState.phone_number)


@router.message(RegisterState.phone_number, F.content_type == ContentType.CONTACT)
async def phone_number_handler(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    text = "Iltimos yoshingizni kiriting"
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(RegisterState.age)


@router.message(RegisterState.age)
async def age_handler(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    text = "Manzilingizni ulshing"
    await message.answer(text=text, reply_markup=location)
    await state.set_state(RegisterState.location)


@router.message(RegisterState.location, F.content_type == ContentType.LOCATION)
async def location_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    print(data)
    await state.update_data(location=message.location)

    registered = data.get("registered_languages", [])
    registered.append(data["IT_language"])

    await state.update_data(registered_languages=registered)
    text = f"Siz {data['IT_language']}ga muvaffaqiyatli ro'yxatdan o'tdingiz\nYana kursga yozilasizmi?"
    await state.set_state(RegisterState.IT_language)
    await message.answer(text=text, reply_markup=IT_language)
