# Production Deployment Guide
## AddManuChain Dashboard

This guide walks you through deploying the AddManuChain Dashboard to production.

---

## 📋 Pre-Deployment Checklist

### 1. Environment Variables
Create production environment variables based on `.env.example`:

```bash
# Required Variables
DATABASE_URL="your-production-database-url"
NEXTAUTH_URL="https://your-domain.com"
NEXTAUTH_SECRET="generate-with-openssl-rand-base64-32"
```

### 2. Database Setup

**For Development (SQLite):**
```bash
DATABASE_URL="file:./dev.db"
```

**For Production (PostgreSQL recommended):**
```bash
# Example with PlanetScale (recommended for Prisma)
DATABASE_URL="mysql://user:password@host/database?ssl={"rejectUnauthorized":true}"

# Example with Supabase
DATABASE_URL="postgresql://postgres:password@db.xxx.supabase.co:5432/postgres"

# Example with Railway
DATABASE_URL="postgresql://user:password@containers-us-west-xxx.railway.app:5432/railway"
```

### 3. Generate NextAuth Secret
```bash
# On Mac/Linux
openssl rand -base64 32

# On Windows PowerShell
[Convert]::ToBase64String((1..32 | ForEach-Object { Get-Random -Maximum 256 }))
```

---

## 🚀 Deployment Options

### Option 1: Vercel (Recommended)

**Why Vercel?**
- Zero-config deployment for Next.js
- Automatic HTTPS and CDN
- Preview deployments for each push
- Free tier available

**Steps:**

1. **Install Vercel CLI**
```bash
npm install -g vercel
```

2. **Login to Vercel**
```bash
vercel login
```

3. **Deploy**
```bash
cd "Website/AddManuChain Dashboard"
vercel
```

4. **Set Environment Variables** (via Vercel Dashboard)
   - Go to: Project Settings → Environment Variables
   - Add:
     - `DATABASE_URL`
     - `NEXTAUTH_URL` (use your Vercel URL)
     - `NEXTAUTH_SECRET`

5. **Setup Production Database**
   
   **Option A: PlanetScale (MySQL, Free Tier)**
   - Sign up at [planetscale.com](https://planetscale.com)
   - Create database
   - Get connection string
   - Update `schema.prisma` datasource to `mysql`
   
   **Option B: Supabase (PostgreSQL, Free Tier)**
   - Sign up at [supabase.com](https://supabase.com)
   - Create project
   - Get database URL from Project Settings → Database
   - Update `schema.prisma` datasource to `postgresql`

6. **Run Database Migrations**
```bash
# After setting DATABASE_URL environment variable
npx prisma db push
```

7. **Seed Production Database** (optional)
```bash
npx tsx prisma/seed.ts
```

8. **Deploy Again**
```bash
vercel --prod
```

---

### Option 2: Railway

**Why Railway?**
- Simple deployment
- Built-in PostgreSQL database
- Generous free tier

**Steps:**

1. **Sign up at [railway.app](https://railway.app)**

2. **Create New Project** → Deploy from GitHub

3. **Add PostgreSQL Service**
   - Add Service → Database → PostgreSQL
   - Railway automatically creates `DATABASE_URL`

4. **Configure Environment Variables**
   - Add `NEXTAUTH_URL` (Railway provides this)
   - Add `NEXTAUTH_SECRET`

5. **Deploy automatically** (connected to GitHub)

---

### Option 3: Self-Hosted (VPS/Cloud)

**Requirements:**
- Ubuntu 22.04 or similar
- Node.js 18+
- PM2 for process management
- Nginx for reverse proxy

**Steps:**

1. **Setup Server**
```bash
# Install Node.js 18
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install PM2
sudo npm install -g pm2

# Install Nginx
sudo apt install nginx
```

2. **Clone Repository**
```bash
git clone https://github.com/yourusername/addmanuchain.git
cd addmanuchain
npm install
```

3. **Build for Production**
```bash
npm run build
```

4. **Setup Environment Variables**
```bash
nano .env.production
# Add your production variables
```

5. **Start with PM2**
```bash
pm2 start npm --name "addmanuchain" -- start
pm2 save
pm2 startup
```

6. **Configure Nginx**
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

7. **Setup SSL with Let's Encrypt**
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

---

## 🗄️ Database Migration Strategy

### From SQLite (Dev) to PostgreSQL/MySQL (Prod)

1. **Update Prisma Schema**
```prisma
datasource db {
  provider = "postgresql"  // or "mysql"
  url      = env("DATABASE_URL")
}
```

2. **Generate New Migration**
```bash
npx prisma migrate dev --name init
```

3. **Apply to Production**
```bash
npx prisma migrate deploy
```

4. **Seed Production Data**
```bash
npx tsx prisma/seed.ts
```

---

## 🔒 Security Checklist

- [ ] Use strong `NEXTAUTH_SECRET` (32+ characters)
- [ ] Enable HTTPS (automatic with Vercel/Railway)
- [ ] Set secure `DATABASE_URL` with SSL
- [ ] Configure CORS if needed
- [ ] Enable rate limiting for API routes
- [ ] Review user roles and permissions
- [ ] Configure backup strategy for database
- [ ] Set up monitoring (Sentry, Vercel Analytics)

---

## 📊 Post-Deployment Setup

### 1. Create Admin User

After deployment, create your first admin user via seed script or directly in database:

```bash
# Using Prisma Studio
npx prisma studio

# Or via seed script (already included)
```

### 2. Test Authentication

- Visit `/login`
- Use demo credentials or create new user
- Verify role-based access

### 3. Configure Monitoring

**Sentry (Error Tracking):**
```bash
npm install @sentry/nextjs
```

Then add to `.env`:
```
SENTRY_DSN="your-sentry-dsn"
```

**Vercel Analytics:**
- Enabled automatically on Vercel

---

## 🔄 Update Strategy

### For Vercel/Railway (Auto-Deploy)
1. Push to `main` branch
2. Automatic build and deploy
3. Zero downtime

### For Self-Hosted
```bash
git pull origin main
npm install
npm run build
pm2 restart addmanuchain
```

---

## 📈 Performance Optimization

1. **Enable Edge Runtime** (optional)
```typescript
// src/app/api/*/route.ts
export const runtime = 'edge'
```

2. **Configure Caching**
```typescript
// next.config.ts
export default {
  images: {
    domains: ['your-cdn.com'],
  },
}
```

3. **Database Connection Pooling**
```prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
  directUrl = env("DIRECT_DATABASE_URL")
}
```

---

## 🆘 Troubleshooting

### Issue: "Invalid `prisma.user.findUnique()` invocation"
**Solution:** Run database migrations
```bash
npx prisma db push
```

### Issue: "NextAuth session undefined"
**Solution:** Check `NEXTAUTH_URL` and `NEXTAUTH_SECRET` are set correctly

### Issue: Build fails on Vercel
**Solution:** Check logs for missing environment variables

### Issue: Database connection timeout
**Solution:** Verify `DATABASE_URL` format and database is accessible from deployment platform

---

## 📞 Support

For deployment issues:
- Check logs: `vercel logs` or `pm2 logs addmanuchain`
- Verify environment variables
- Review Prisma migrations: `npx prisma migrate status`

---

## 🎉 Success Checklist

After deployment, verify:
- [ ] Website loads at production URL
- [ ] Login page accessible
- [ ] Can authenticate with demo credentials
- [ ] Dashboard loads all pages
- [ ] API routes respond correctly
- [ ] Database queries work
- [ ] Role-based access functions properly
- [ ] HTTPS is enabled
- [ ] Error monitoring is active

---

**Deployment Date:** _____________  
**Deployed By:** _____________  
**Production URL:** _____________  
**Database Provider:** _____________
