# Turrant.ai Website & Blog

AI-powered document collection platform website with integrated blog system. Built with FastAPI backend and static HTML frontend.

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

- **Backend**: FastAPI (Python)
- **Database**: Supabase (PostgreSQL)
- **Frontend**: HTML, Tailwind CSS (CDN), Vanilla JavaScript
- **Rich Text Editor**: Quill.js
- **Icons**: Lucide Icons
- **Fonts**: Plus Jakarta Sans (Google Fonts)

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
│   ├── finance.html         # Industry pages...
│   ├── images/              # Static images
│   ├── logos/               # Company logos
│   └── steps/               # How it works images
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not in git)
└── README.md
```

## Setup

### 1. Clone Repository

```bash
git clone https://github.com/sahil511ji/sahil-ver2.git
cd sahil-ver2
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Create a `.env` file in the root directory:

```env
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_ANON_KEY=your-anon-key-here
```

### 4. Supabase Setup

Create the following tables in your Supabase project:

#### `blog_posts` table
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

#### `blog_categories` table
```sql
CREATE TABLE blog_categories (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name TEXT NOT NULL,
  slug TEXT UNIQUE NOT NULL,
  description TEXT
);
```

#### Row Level Security (RLS)
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

### 5. Run Development Server

```bash
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

Visit: http://localhost:8000

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

### Railway / Render
```bash
# Start command
python -m uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

### Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## License

Proprietary - Turrant.ai
