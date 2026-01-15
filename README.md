
# 📝 Django Blog (Forms-based)

Bu loyiha Django framework yordamida **blog tizimi** yaratish uchun ishlab chiqilgan.
Postlar **Django forms.Form** orqali boshqariladi va **maʼlumotlar fayl (posts.txt)** orqali saqlanadi (model ishlatilmagan).

---

## 🚀 Asosiy imkoniyatlar

- 🆕 Post yaratish (Create)
- 📖 Postlar ro‘yxati (List)
- 🔍 Status bo‘yicha filter (All / Published / Unpublished)
- 📄 Bitta postni ko‘rish (Detail)
- ✏️ Postni tahrirlash (Edit)
- 🗑️ Postni o‘chirish (Delete)
- 🟢 Publish / Draft holati
- 🕒 Created time va **Last edited time**
- 🔑 Slug orqali URL
- 🎨 CSS bilan bezatilgan UI

---

## 🛠 Texnologiyalar

- Python 3.12
- Django 5.2
- HTML5
- CSS3
- Django Forms (`forms.Form`)
- JSON / TXT file storage

---

## 📂 Loyiha tuzilishi (Asosiylari)

```

lesson66-django-blog/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│
├── web/
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── posts.html
│   ├── post_detail.html
│   ├── create_post.html
│   ├── post_created.html
│   ├── update_post.html
│   ├── post_updated.html
│
├── static/css/
│           └── style.css
│
├── posts.txt
├── manage.py
└── README.md

````

---

## 🧾 Post maʼlumotlari formati (posts.txt)

```json
{
  "id": "uuid",
  "title": "Post title",
  "slug": "post-slug",
  "content": "Post content",
  "is_published": true,
  "created_at": "YYYY-MM-DD HH:MM",
  "updated_at": "YYYY-MM-DD HH:MM"
}
````

---

## ⚙️ O‘rnatish va ishga tushirish

### 1️⃣ Virtual muhit yaratish

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 2️⃣ Django o‘rnatish

```bash
pip install django
```

### 3️⃣ Serverni ishga tushirish

```bash
python manage.py runserver
```

Brauzerda oching:

```
http://127.0.0.1:8000/
```

---

## 📌 Muhim eslatmalar

* Loyiha **model ishlatmaydi**
* Barcha maʼlumotlar `posts.txt` faylda saqlanadi
* Sluglar **unique** bo‘lishi uchun uuid qisqa ko‘rinishi bilan yaratiladi
* Delete faqat **POST** so‘rov orqali amalga oshadi (xavfsizlik uchun)

---

## 👨‍💻 Muallif:

# **Mehroj Saparov**

## ✅ Xulosa

Ushbu loyiha Django formalar bilan ishlash, CRUD amallarini tushunish va
model bo‘lmagan holatda maʼlumot saqlashni o‘rganish uchun mo‘ljallangan.

---

