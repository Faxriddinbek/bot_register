# Telegram Bot Registration System - Loyiha Ma'lumotlari

## 📋 Loyiha Tavsifi (Project Description)

Bu loyiha **Telegram bot** yordamida foydalanuvchilarni ro'yxatdan o'tkazish tizimidir. Bot ikki tilli (O'zbek va Ingliz) qo'llab-quvvatlaydi va foydalanuvchilardan ma'lumotlarni to'plash va ma'lumotlar bazasida saqlash imkoniyatini beradi.

## 🛠️ Ishlatilgan Texnologiyalar (Technologies Used)

### Backend Framework & Libraries
- **Python 3.x** - Asosiy dasturlash tili
- **Aiogram 3.22.0** - Asinxron Telegram Bot API framework
- **Asyncio** - Asinxron dasturlash uchun

### Database & ORM
- **PostgreSQL** - Relatsion ma'lumotlar bazasi
- **SQLAlchemy 1.4.50** - ORM (Object-Relational Mapping)
- **Alembic 1.12.1** - Database migration tool
- **Databases 0.8.0** - Asinxron database kutubxonasi
- **AsyncPG 0.29.0** - PostgreSQL uchun asinxron driver
- **Psycopg2-binary 2.9.9** - PostgreSQL adapter

### Configuration & Environment
- **Python-dotenv 1.0.0** - Environment variables boshqarish
- **Environs 8.0.0** - Environment variables validation
- **Pydantic 2.11.10** - Data validation va settings management

### HTTP & Networking
- **Aiohttp 3.12.15** - Asinxron HTTP client/server
- **Aiofiles 24.1.0** - Asinxron fayl operatsiyalari

### Utilities
- **Openpyxl 3.0.10** - Excel fayllar bilan ishlash
- **Babel 2.9.1** - Internationalization support
- **Marshmallow 3.20.1** - Object serialization/deserialization

## 🏗️ Loyiha Arxitekturasi (Project Architecture)

### Asosiy Komponentlar:

1. **Main Entry Point** (`main.py`)
   - Bot initialization
   - Dispatcher setup
   - Startup/shutdown handlers
   - Router registration

2. **Core Module** (`core/`)
   - `config.py` - Environment variables va konfiguratsiya
   - `database_settings.py` - Database connection va setup
   - `models.py` - SQLAlchemy database modellar

3. **Handlers** (`handlers/`)
   - `register.py` - Foydalanuvchi ro'yxatdan o'tish logikasi
   - `settings.py` - Bot sozlamalari va qo'shimcha funksiyalar

4. **States** (`states/`)
   - `register.py` - FSM (Finite State Machine) states ro'yxatdan o'tish uchun

5. **Keyboards** (`keyboards/`)
   - `default.py` - Standart klaviatura tugmalari
   - `inline.py` - Inline keyboard tugmalari

6. **Utils** (`utils/`)
   - `db_commands/user.py` - Database CRUD operatsiyalari
   - `set_default_commands.py` - Bot default buyruqlarini sozlash

7. **Filters** (`filters/`)
   - `admin.py` - Admin filtrlari

8. **Migrations** (`alembic/`)
   - Database schema versiyalari va migration fayllari

## ⚙️ Asosiy Funksiyalar (Key Features)

1. **Ikki tilli qo'llab-quvvatlash** (O'zbek/Ingliz)
2. **Foydalanuvchi ro'yxatdan o'tish**:
   - Til tanlash
   - To'liq ism kiritish
   - Telefon raqami (contact yoki text)
   - Yosh kiritish
3. **Ma'lumotlar bazasida saqlash** (PostgreSQL)
4. **FSM (Finite State Machine)** - Multi-step form to'ldirish
5. **Inline va Reply keyboardlar**
6. **Fayl yuklash va yuborish funksiyalari**
7. **Database migrations** (Alembic)

## 📊 Database Schema

**Users Table:**
- `id` (Integer, Primary Key)
- `full_name` (String)
- `language` (String)
- `age` (SmallInteger)
- `chat_id` (BigInteger)
- `phone_number` (String)
- `created_at` (DateTime, Timezone-aware)
- `updated_at` (DateTime, Timezone-aware)

## 🔧 Texnik Ko'nikmalar (Technical Skills Demonstrated)

### Backend Development
- ✅ Asinxron dasturlash (Async/Await)
- ✅ RESTful API prinsiplari
- ✅ Database design va modeling
- ✅ ORM ishlatish (SQLAlchemy)
- ✅ Database migrations (Alembic)

### Telegram Bot Development
- ✅ Aiogram framework
- ✅ FSM (Finite State Machine) implementation
- ✅ Message handlers va callback handlers
- ✅ Keyboard management (Inline va Reply)
- ✅ File handling

### Database
- ✅ PostgreSQL
- ✅ Database connection pooling
- ✅ CRUD operations
- ✅ Query optimization

### Code Organization
- ✅ Modular architecture
- ✅ Separation of concerns
- ✅ Clean code principles
- ✅ Environment configuration

## 📝 Intervyu uchun Tushuntirishlar (Interview Talking Points)

### 1. Nima uchun Aiogram tanlangan?
- Asinxron ishlaydi, yuqori performance
- Modern Python async/await syntax
- Keng funksional imkoniyatlar
- Yaxshi dokumentatsiya

### 2. Database qanday ishlaydi?
- PostgreSQL - reliable va scalable
- SQLAlchemy ORM - code readability va maintainability
- Alembic - version control database schema uchun
- AsyncPG - yuqori performance asinxron operatsiyalar uchun

### 3. FSM qanday ishlatilgan?
- Multi-step form to'ldirish uchun
- User state management
- Conversation flow control

### 4. Loyiha strukturasini qanday tashkil qildingiz?
- Modular approach - har bir komponent alohida
- Separation of concerns - handlers, models, utils alohida
- Scalability - yangi funksiyalar qo'shish oson

## 🚀 Key Achievements

- ✅ To'liq funksional Telegram bot
- ✅ Ikki tilli qo'llab-quvvatlash
- ✅ Database integration
- ✅ Clean va maintainable code structure
- ✅ Production-ready architecture

## 📚 O'rganilgan Texnologiyalar (Technologies Learned)

1. **Aiogram 3.x** - Modern Telegram Bot framework
2. **Async Python** - Asyncio, async/await patterns
3. **PostgreSQL** - Relational database management
4. **SQLAlchemy** - ORM va database abstraction
5. **Alembic** - Database version control
6. **FSM** - State management patterns
7. **Environment Configuration** - Secure config management

---

## 💼 Resume uchun Qisqa Tavsif (Short Description for Resume)

**Telegram Bot Registration System** - Python, Aiogram 3.x, PostgreSQL, SQLAlchemy, Alembic ishlatgan ikki tilli (O'zbek/Ingliz) Telegram bot loyihasi. Foydalanuvchilarni ro'yxatdan o'tkazish, ma'lumotlarni to'plash va PostgreSQL ma'lumotlar bazasida saqlash funksiyalarini amalga oshirgan. Asinxron dasturlash, FSM (Finite State Machine), database migrations va modular arxitektura qo'llangan.

**Technologies:** Python, Aiogram, PostgreSQL, SQLAlchemy, Alembic, AsyncIO, Asyncio, Pydantic, Aiohttp
