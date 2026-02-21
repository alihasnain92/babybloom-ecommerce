# 🌸 BabyBloom — Django E-Commerce Backend

A complete e-commerce backend for a newborn baby clothing and care items store, built with Django 5.

---

## 🚀 Tech Stack

| Tool | Purpose |
|---|---|
| Django 5.2 | Web framework |
| SQLite | Development database |
| PostgreSQL | Production database (Railway) |
| Cloudinary | Image storage |
| Gunicorn | Production WSGI server |
| Bootstrap 5 | Frontend styling |

---

## 📁 Project Structure

```
babybloom/
├── babybloom/          # Project config (settings, urls, wsgi)
├── users/              # Auth: signup, login, logout + CustomUser model
├── store/              # Category & Product models + shop views
├── cart/               # Cart & CartItem models + cart views
├── orders/             # Order, OrderItem, ShippingAddress + checkout
├── contact/            # ContactMessage model + contact form
├── templates/          # HTML templates (Bootstrap 5)
├── static/             # CSS / JS assets
├── media/              # Local image uploads (dev only)
├── .env                # Secret keys (never push to GitHub!)
├── requirements.txt
└── manage.py
```

---

## ⚙️ Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/babybloom.git
cd babybloom

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env and fill in your SECRET_KEY and Cloudinary credentials

# 5. Run migrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. (Optional) Seed sample data
python seed_data.py

# 8. Start development server
python manage.py runserver
```

---

## 🔑 Environment Variables (`.env`)

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

# Production only (Railway PostgreSQL):
# DATABASE_URL=postgresql://...
```

---

## 🌐 API Endpoints

| Method | URL | Description | Auth |
|---|---|---|---|
| GET/POST | `/signup/` | Register new user | No |
| GET/POST | `/login/` | Login | No |
| GET | `/logout/` | Logout | No |
| GET | `/` | Homepage | No |
| GET | `/shop/` | All products | No |
| GET | `/shop/category/<id>/` | Products by category | No |
| GET | `/shop/product/<id>/` | Product detail | No |
| GET | `/cart/` | View cart | ✅ Yes |
| POST | `/cart/add/<id>/` | Add to cart | ✅ Yes |
| POST | `/cart/update/<id>/` | Update quantity | ✅ Yes |
| POST | `/cart/remove/<id>/` | Remove item | ✅ Yes |
| GET/POST | `/checkout/` | Place order | ✅ Yes |
| GET | `/order/confirmation/<id>/` | Order success | ✅ Yes |
| GET | `/orders/` | Order history | ✅ Yes |
| GET | `/orders/<id>/` | Order detail | ✅ Yes |
| GET/POST | `/contact/` | Contact form | No |
| GET | `/admin/` | Django admin | Staff only |

---

## 🗄️ Database Models

| Model | App | Key Fields |
|---|---|---|
| CustomUser | users | email (unique), phone, created_at |
| Category | store | name, image |
| Product | store | category (FK), name, price, stock_quantity |
| Cart | cart | user (OneToOne) |
| CartItem | cart | cart (FK), product (FK), quantity |
| Order | orders | user (FK), total_price, status |
| OrderItem | orders | order (FK), product (FK), price (snapshot!) |
| ShippingAddress | orders | order (OneToOne), full_name, address, city |
| ContactMessage | contact | name, email, message |

---

## 🚢 Deploy on Railway

1. Push this repo to GitHub
2. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Add PostgreSQL plugin inside Railway
4. Add all environment variables from `.env`
5. Add `DATABASE_URL` from Railway's PostgreSQL plugin
6. Set start command: `python manage.py migrate && gunicorn babybloom.wsgi`
7. Railway gives you a free live URL ✅

---

## 🔒 Security Notes

- Never commit `.env` to GitHub (it's in `.gitignore`)
- Set `DEBUG=False` in production
- Change `ALLOWED_HOSTS` to your Railway domain before deploying
- Enable Cloudinary storage in production by uncommenting `DEFAULT_FILE_STORAGE`

---

*BabyBloom — Newborn Baby Store | Built with Django 🌸*
