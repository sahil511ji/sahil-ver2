# Turrant.ai Website & Blog

AI-powered document collection platform website with integrated blog system. Built with FastAPI backend and static HTML frontend.

## Quick Start (Docker - Recommended)

**This is the easiest way to run the project - works on any machine!**

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/sahil511ji/sahil-ver2.git
cd sahil-ver2

# 2. Create .env file from example
cp .env.example .env

# 3. Edit .env and add your Supabase credentials
# SUPABASE_URL=https://your-project.supabase.co
# SUPABASE_ANON_KEY=your-key-here

# 4. Run with Docker
docker-compose up --build

# 5. Open browser
# http://localhost:8000
```

That's it! The app runs exactly the same on any machine.

---

## Alternative: Manual Setup (Without Docker)

### Prerequisites
- Python 3.11+
- pip

### Steps

```bash
# 1. Clone repository
git clone https://github.com/sahil511ji/sahil-ver2.git
cd sahil-ver2

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
cp .env.example .env
# Edit .env with your Supabase credentials

# 5. Run server
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload

# 6. Open http://localhost:8000
```

---

## Features

### Website
- **Landing Page** - Main marketing website for Turrant.ai
- **Industry Pages** - Finance, Insurance, HR, Travel, Logistics, Education
- **Clean URLs** - `/blog/my-post` instead of `blog-post.html?slug=my-post`

### Blog System
- **Blog Listing** - Published posts with search and category filtering
- **Blog Posts** - Individual post pages with full content and social sharing
- **Admin Panel** - Create, edit, delete posts with rich text editor

### Admin Features
- Email/password authentication via Supabase Auth
- Rich text editor (Quill.js)
- Image upload with auto-compression
- Category and tag management
- SEO fields (meta title, description)
- Publish/draft and featured toggles

## Tech Stack

- **Backend**: FastAPI (Python 3.11)
- **Database**: Supabase (PostgreSQL)
- **Frontend**: HTML, Tailwind CSS (CDN), Vanilla JavaScript
- **Containerization**: Docker
- **Rich Text Editor**: Quill.js
- **Icons**: Lucide Icons

## Project Structure

```
├── backend/
│   ├── main.py              # FastAPI app entry point
│   ├── config.py            # Environment configuration
│   ├── routes/
│   │   ├── pages.py         # Static page routes
│   │   ├── blog.py          # Blog routes & API
│   │   └── admin.py         # Admin routes & API
│   └── services/
│       └── supabase.py      # Supabase client
├── frontend/
│   ├── index.html           # Homepage
│   ├── blog.html            # Blog listing
│   ├── blog-post.html       # Individual post
│   ├── blog-admin.html      # Admin panel
│   └── images/              # Static assets
├── Dockerfile               # Docker image definition
├── docker-compose.yml       # Docker compose config
├── requirements.txt         # Python dependencies
├── .env.example             # Environment template
└── README.md
```

## Environment Variables

Create a `.env` file with:

| Variable | Description | Example |
|----------|-------------|---------|
| `SUPABASE_URL` | Your Supabase project URL | `https://abc123.supabase.co` |
| `SUPABASE_ANON_KEY` | Your Supabase anon key | `eyJhbGciOiJIUzI1...` |

Get these from: **Supabase Dashboard → Project Settings → API**

## Supabase Setup

Create these tables in your Supabase project:

### `blog_posts` table
```sql
CREATE TABLE blog_posts (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  slug TEXT UNIQUE NOT NULL,
  title TEXT NOT NULL,
  excerpt TEXT,
  content TEXT,
  featured_image TEXT,
  card_color TEXT DEFAULT 'teal',
  author TEXT DEFAULT 'Turrant Team',
  category TEXT,
  tags JSONB DEFAULT '[]',
  meta_title TEXT,
  meta_description TEXT,
  published BOOLEAN DEFAULT false,
  featured BOOLEAN DEFAULT false,
  published_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

### `blog_categories` table
```sql
CREATE TABLE blog_categories (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name TEXT NOT NULL,
  slug TEXT UNIQUE NOT NULL,
  description TEXT
);
```

### Row Level Security (RLS)
```sql
ALTER TABLE blog_posts ENABLE ROW LEVEL SECURITY;
ALTER TABLE blog_categories ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Public can read published posts" ON blog_posts
  FOR SELECT USING (published = true);

CREATE POLICY "Public can read categories" ON blog_categories
  FOR SELECT USING (true);

CREATE POLICY "Auth users can manage posts" ON blog_posts
  FOR ALL USING (auth.role() = 'authenticated');
```

## URL Routes

| URL | Description |
|-----|-------------|
| `/` | Homepage |
| `/blog` | Blog listing |
| `/blog/{slug}` | Individual blog post |
| `/admin` | Admin panel |
| `/finance` | Finance industry page |
| `/insurance` | Insurance industry page |
| `/hr` | HR industry page |
| `/travel` | Travel industry page |
| `/logistics` | Logistics industry page |
| `/education` | Education industry page |

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/posts` | Get all published posts |
| GET | `/api/posts/{slug}` | Get single post by slug |
| GET | `/api/categories` | Get all categories |
| GET | `/api/admin/posts` | Get all posts (admin) |
| POST | `/api/admin/posts` | Create new post |
| PUT | `/api/admin/posts/{id}` | Update post |
| DELETE | `/api/admin/posts/{id}` | Delete post |

## Deployment

### Docker (Recommended)
```bash
docker-compose up -d
```

### Railway / Render
Set these:
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`

### Environment Variables
Make sure to set `SUPABASE_URL` and `SUPABASE_ANON_KEY` in your deployment platform.

## Troubleshooting

### "Module not found" errors
```bash
# Use Docker instead - it handles all dependencies
docker-compose up --build
```

### Port already in use
```bash
# Change port in docker-compose.yml or run:
docker-compose down
docker-compose up
```

### Supabase connection errors
- Check your `.env` file has correct credentials
- Make sure SUPABASE_ANON_KEY starts with `eyJ...`

## License

Proprietary - Turrant.ai
