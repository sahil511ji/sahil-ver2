# Turrant.ai Blog

A blog system for Turrant.ai built with static HTML, Tailwind CSS, and Supabase as the backend.

## Features

- **Blog Listing** (`blog.html`) - Displays published blog posts with search and category filtering
- **Blog Post** (`blog-post.html`) - Individual blog post page with full content, social sharing
- **Blog Admin** (`blog-admin.html`) - Admin panel for managing blog posts

### Admin Features
- Email/password authentication via Supabase Auth
- Create, edit, and delete blog posts
- Rich text editor (Quill.js)
- Image upload with auto-compression
- Category and tag management
- SEO fields (meta title, description)
- Publish/draft and featured toggles

## Tech Stack

- **Frontend**: HTML, Tailwind CSS (CDN), Vanilla JavaScript
- **Backend**: Supabase (PostgreSQL, Auth, Storage)
- **Rich Text Editor**: Quill.js
- **Icons**: Lucide Icons
- **Fonts**: Plus Jakarta Sans (Google Fonts)

## Setup

### 1. Supabase Configuration

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
-- Enable RLS
ALTER TABLE blog_posts ENABLE ROW LEVEL SECURITY;
ALTER TABLE blog_categories ENABLE ROW LEVEL SECURITY;

-- Public read access for published posts
CREATE POLICY "Public can read published posts" ON blog_posts
  FOR SELECT USING (published = true);

-- Public read access for categories
CREATE POLICY "Public can read categories" ON blog_categories
  FOR SELECT USING (true);

-- Authenticated users can manage posts
CREATE POLICY "Auth users can manage posts" ON blog_posts
  FOR ALL USING (auth.role() = 'authenticated');

-- Authenticated users can manage categories
CREATE POLICY "Auth users can manage categories" ON blog_categories
  FOR ALL USING (auth.role() = 'authenticated');
```

#### Storage Bucket
1. Create a bucket named `blog-images`
2. Set it to **Public**
3. Add policy for authenticated uploads

### 2. Update Credentials

Update the Supabase credentials in these files:
- `blog.html`
- `blog-post.html`
- `blog-admin.html`

```javascript
const SUPABASE_URL = 'YOUR_SUPABASE_URL';
const SUPABASE_ANON_KEY = 'YOUR_SUPABASE_ANON_KEY';
```

### 3. Local Development

```bash
# Install serve (if not installed)
npm install

# Start local server
npm start
```

Visit:
- Blog: http://localhost:3000/blog.html
- Admin: http://localhost:3000/blog-admin.html

## File Structure

```
├── blog.html           # Blog listing page
├── blog-post.html      # Individual blog post page
├── blog-admin.html     # Admin panel
├── index.html          # Main website
├── images/             # Static images
├── package.json        # npm scripts
├── railway.json        # Railway deployment config
└── README.md
```

## Deployment

### Railway
The project is configured for Railway deployment. Push to main branch to auto-deploy.

### Other Platforms
Since this is a static site, it can be deployed to:
- Netlify
- Vercel
- GitHub Pages
- Any static file hosting

## Brand Colors

- Primary (Teal): `#003a37`
- Accent (Green): `#16A085`
- Light Green: `#10b981`

## License

Proprietary - Turrant.ai
