# AddManuChain Dashboard
**Digital Inventory Platform for Offshore Oil & Gas**

🚀 **On-demand, certified metal parts in days, not weeks**

[![Next.js](https://img.shields.io/badge/Next.js-16-black)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue)](https://typescriptlang.org/)
[![Prisma](https://img.shields.io/badge/Prisma-6-2D3748)](https://prisma.io/)
[![NextAuth.js](https://img.shields.io/badge/NextAuth.js-4-purple)](https://next-auth.js.org/)

---

## 📖 Overview

AddManuChain is Alma-Tech's flagship platform that transforms offshore supply chains by replacing physical "just-in-case" inventories with digital "just-on-time" manufacturing. When a critical part fails at sea, every hour costs $50,000–$100,000. Our platform connects OEM blueprint owners, certified 3D printing centers, and offshore operators to deliver DNV/Lloyd's Register certified parts in 3-5 days instead of 21+ days.

### 🎯 Key Value Propositions

- **81% Lead Time Reduction** - From 21 days to 4 days average
- **81% Warehouse Cost Savings** - $450K → $85K annually
- **Design Flexibility** - 15+ custom iterations vs 1-2 traditional
- **Environmental Impact** - Significant CO₂ reduction through local manufacturing
- **End-to-End Service** - Full implementation support (Assessment → Training → Maintenance)

---

## ✨ Features

### 🔧 Core Operations
- **Digital Blueprint Library** - Certified CAD files with OEM attribution
- **On-Demand Ordering** - Real-time order placement and tracking
- **Print Center Network** - Certified facility management and capacity monitoring
- **Shipment Tracking** - End-to-end logistics visibility

### 🤝 Ecosystem Management
- **OEM Partnerships** - Blueprint IP licensing and revenue tracking
- **Certification Authorities** - Regulatory body relationship management (DNV, Lloyd's Register, ABS)
- **Customer Success** - 5-phase implementation tracking (Assessment → Adoption → Integration → Training → Maintenance)
- **Training Management** - Onboarding, safety, and advanced operations training

### 📊 Analytics & Insights
- **Comparative Analytics** - Just-on-Time vs Just-in-Case metrics
- **ROI Dashboard** - Cost savings, lead time reduction, design flexibility
- **Environmental Impact** - CO₂ saved, miles avoided, waste reduction
- **Business Intelligence** - KPIs, trends, forecasting

### 🔒 Security & Compliance
- **Role-Based Access Control** - 6 user roles (Admin, Customer Admin, Operator, OEM Partner, Print Center, Cert Authority)
- **Authentication** - NextAuth.js with credential-based login
- **Audit Logs** - Complete activity tracking for compliance
- **Data Encryption** - Sensitive data protection

---

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ ([Download](https://nodejs.org/))
- npm or yarn package manager
- Git ([Download](https://git-scm.com/))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/addmanuchain.git
cd "AddManuChain Dashboard"
```

2. **Install dependencies**
```bash
npm install
```

3. **Setup environment variables**
```bash
cp .env.example .env
```

Edit `.env` and add:
```bash
DATABASE_URL="file:./dev.db"
NEXTAUTH_URL="http://localhost:3000"
NEXTAUTH_SECRET="generate-with-openssl-rand-base64-32"
```

Generate secret:
```bash
# Mac/Linux
openssl rand -base64 32

# Windows PowerShell
[Convert]::ToBase64String((1..32 | ForEach-Object { Get-Random -Maximum 256 }))
```

4. **Initialize database**
```bash
npx prisma db push
npx tsx prisma/seed.ts
```

5. **Start development server**
```bash
npm run dev
```

6. **Open browser**
Navigate to `http://localhost:3000`

### Demo Credentials

| Role | Email | Password |
|------|-------|----------|
| **Admin** | admin@almatech.com | admin123 |
| **Operator** | operator@statoil.com | operator123 |
| **Partner** | partner@oem.com | partner123 |

⚠️ **Change these before production!**

---

## 🏗️ Tech Stack

### Frontend
- **Next.js 16** - React framework with App Router
- **TypeScript 5** - Type-safe development
- **Tailwind CSS 4** - Utility-first styling
- **shadcn/ui** - High-quality component library
- **Recharts** - Data visualization
- **Framer Motion** - Animations

### Backend
- **Next.js API Routes** - RESTful API
- **Prisma ORM** - Type-safe database access
- **SQLite** (dev) / **PostgreSQL** (prod) - Database
- **NextAuth.js** - Authentication
- **bcryptjs** - Password hashing

### DevOps
- **Vercel** - Deployment platform (recommended)
- **Sentry** - Error tracking
- **Vercel Analytics** - Performance monitoring

---

## 📁 Project Structure

```
src/
├── app/
│   ├── api/              # API routes
│   │   ├── auth/         # NextAuth endpoints
│   │   ├── orders/       # Order CRUD
│   │   ├── blueprints/   # Blueprint management
│   │   ├── authorities/  # Certification authorities
│   │   └── ...
│   ├── login/            # Login page
│   ├── page.tsx          # Dashboard home
│   └── layout.tsx        # Root layout
├── components/
│   ├── dashboard/        # Dashboard pages
│   │   ├── OverviewPage.tsx
│   │   ├── OrdersPage.tsx
│   │   ├── BlueprintsPage.tsx
│   │   ├── AuthoritiesPage.tsx
│   │   ├── CustomerSuccessPage.tsx
│   │   ├── AnalyticsPage.tsx
│   │   └── ...
│   └── ui/               # shadcn/ui components
├── hooks/
│   └── use-dashboard.ts  # Custom React hooks with SWR
├── lib/
│   ├── auth.ts           # NextAuth configuration
│   └── utils.ts          # Utility functions
└── types/
    └── next-auth.d.ts    # TypeScript type extensions

prisma/
├── schema.prisma         # Database schema
└── seed.ts               # Seed data

public/                   # Static assets
```

---

## 🗄️ Database Schema

### Core Models
- **User** - Authentication and user management
- **Blueprint** - Digital part library
- **Order** - Part orders and tracking
- **PrintCenter** - Certified facilities
- **Shipment** - Logistics tracking

### Partner & Certification
- **Partner** - OEM relationships
- **Certification** - Compliance documents
- **CertificationAuthority** - Regulatory bodies
- **CertificationRequest** - Approval workflow

### Customer Success
- **CustomerEngagement** - Implementation tracking
- **TrainingSession** - Training management
- **ComparativeMetrics** - ROI analytics
- **EnvironmentalImpact** - Sustainability tracking

### Supporting Models
- **Material** - Raw material inventory
- **AuditLog** - Activity tracking
- **CustomizationRequest** - Design modifications

[View Full Schema](prisma/schema.prisma)

---

## 🔐 Authentication & Authorization

### User Roles

| Role | Permissions | Use Case |
|------|-------------|----------|
| **admin** | Full system access | Platform management |
| **customer_admin** | Company-wide access | Operations manager |
| **operator** | Place orders, track status | Rig technician |
| **oem_partner** | Manage blueprints | IP owner |
| **print_center** | Update job status | Facility operator |
| **cert_authority** | Review certifications | Regulatory body |

### Protected Routes

All routes except `/login` and `/api/auth/*` require authentication. Middleware automatically redirects unauthenticated users.

```typescript
// src/middleware.ts
export { default } from 'next-auth/middleware'
```

---

## 📚 Documentation

Comprehensive guides available:

- **[Deployment Guide](DEPLOYMENT.md)** - Production deployment (Vercel, Railway, Self-hosted)
- **[User Guide](USER_GUIDE.md)** - Feature documentation and workflows
- **[Monitoring Guide](MONITORING.md)** - Sentry, analytics, and logging

---

## 🛠️ Development

### Available Scripts

```bash
# Development
npm run dev          # Start dev server on port 3000

# Build
npm run build        # Production build
npm run start        # Start production server

# Database
npm run db:push      # Sync Prisma schema to database
npm run db:migrate   # Create migration
npm run db:reset     # Reset database (WARNING: deletes data)

# Code Quality
npm run lint         # Run ESLint
```

### Database Management

```bash
# View database in browser
npx prisma studio

# Generate Prisma Client after schema changes
npx prisma generate

# Seed database with demo data
npx tsx prisma/seed.ts
```

---

## 🚀 Deployment

### Option 1: Vercel (Recommended)

1. Push code to GitHub
2. Import project in [Vercel](https://vercel.com)
3. Set environment variables:
   - `DATABASE_URL`
   - `NEXTAUTH_URL`
   - `NEXTAUTH_SECRET`
4. Deploy!

**Database:** Use PlanetScale (MySQL) or Supabase (PostgreSQL)

[Full Deployment Guide →](DEPLOYMENT.md)

### Option 2: Railway

1. Sign up at [Railway](https://railway.app)
2. Deploy from GitHub
3. Add PostgreSQL service
4. Configure environment variables
5. Automatic deployments on push

### Option 3: Self-Hosted

Requirements: Ubuntu 22.04, Node.js 18+, PM2, Nginx

```bash
npm run build
pm2 start npm --name "addmanuchain" -- start
```

[Detailed Instructions →](DEPLOYMENT.md#option-3-self-hosted-vpscloud)

---

## 📊 Key Metrics (Example Data)

Based on seed data and pilot deployments:

| Metric | Traditional OEM | AddManuChain | Improvement |
|--------|----------------|--------------|-------------|
| **Lead Time** | 21 days | 4 days | **81% faster** |
| **Warehouse Costs** | $450K/year | $85K/year | **81% savings** |
| **Design Iterations** | 1-2 | 15+ | **13x flexibility** |
| **Repair Rate** | 0% | 65% | **Waste reduction** |
| **CO₂ Emissions** | Baseline | -1,247 kg | **Environmental** |

---

## 🤝 Contributing

### Development Workflow

1. Create feature branch: `git checkout -b feature/your-feature`
2. Make changes and test locally
3. Run linter: `npm run lint`
4. Commit: `git commit -m "feat: your feature description"`
5. Push: `git push origin feature/your-feature`
6. Create Pull Request

### Code Style

- Follow TypeScript best practices
- Use Prettier for formatting (configured in project)
- Write meaningful commit messages (Conventional Commits)
- Add comments for complex logic

---

## 🐛 Troubleshooting

### Common Issues

**"Prisma Client not found"**
```bash
npx prisma generate
```

**"NextAuth session undefined"**
- Check `NEXTAUTH_URL` and `NEXTAUTH_SECRET` in `.env`
- Restart dev server

**Build fails**
- Clear `.next` folder: `rm -rf .next`
- Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`

**Database errors**
```bash
npx prisma db push --force-reset
npx tsx prisma/seed.ts
```

[More Troubleshooting →](USER_GUIDE.md#troubleshooting)

---

## 📞 Support

- **Email:** support@addmanuchain.com
- **Documentation:** [docs.addmanuchain.com](https://docs.addmanuchain.com)
- **Issues:** [GitHub Issues](https://github.com/yourusername/addmanuchain/issues)

---

## 📄 License

Copyright © 2026 Alma-Tech. All rights reserved.

This is proprietary software. Unauthorized copying, distribution, or modification is prohibited.

---

## 🙏 Acknowledgments

**Founders:**
- Alireza Vahedi Nemani (CEO) - PhD Candidate, Materials Engineering, Dalhousie University
- Mahya Ghaffari (CTO) - PhD Candidate, Materials Engineering, Dalhousie University

**Advisors:**
- Dr. Ali Nasiri - Assistant Professor & Canada Research Chair, Ocean Engineering, Dalhousie
- Harsimran Malhi - Business Advisor, 7 years at Halliburton, Oxford MBA

**Supported By:**
- Emera IdeaHub
- CleanTech Commons
- Lab2Market Program

---

**Version:** 1.0.0  
**Last Updated:** February 23, 2026  
**Status:** MVP Ready for Pilot Launch

---

## 🎯 Roadmap

### Q2 2026
- [ ] Mobile-responsive improvements
- [ ] Bulk blueprint upload
- [ ] Enhanced reporting (PDF/Excel export)
- [ ] Email notifications

### Q3 2026
- [ ] Real-time printer status (IoT integration)
- [ ] Predictive analytics
- [ ] ERP/PLM API integrations
- [ ] Multi-language support

### Q4 2026
- [ ] AI-based quality control
- [ ] Dynamic pricing engine
- [ ] White-label options
- [ ] Marketplace features

---

**🚀 Ready to revolutionize offshore supply chains!**
- **🔐 Auth Included** - NextAuth.js for secure authentication flows
- **📊 Data Visualization** - Charts, tables, and drag-and-drop functionality
- **🌍 i18n Ready** - Multi-language support with Next Intl
- **🚀 Production Ready** - Optimized build and deployment settings
- **🤖 AI-Friendly** - Structured codebase perfect for AI assistance

## 🚀 Quick Start

```bash
# Install dependencies
bun install

# Start development server
bun run dev

# Build for production
bun run build

# Start production server
bun start
```

Open [http://localhost:3000](http://localhost:3000) to see your application running.

## 🤖 Powered by Z.ai

This scaffold is optimized for use with [Z.ai](https://chat.z.ai) - your AI assistant for:

- **💻 Code Generation** - Generate components, pages, and features instantly
- **🎨 UI Development** - Create beautiful interfaces with AI assistance  
- **🔧 Bug Fixing** - Identify and resolve issues with intelligent suggestions
- **📝 Documentation** - Auto-generate comprehensive documentation
- **🚀 Optimization** - Performance improvements and best practices

Ready to build something amazing? Start chatting with Z.ai at [chat.z.ai](https://chat.z.ai) and experience the future of AI-powered development!

## 📁 Project Structure

```
src/
├── app/                 # Next.js App Router pages
├── components/          # Reusable React components
│   └── ui/             # shadcn/ui components
├── hooks/              # Custom React hooks
└── lib/                # Utility functions and configurations
```

## 🎨 Available Features & Components

This scaffold includes a comprehensive set of modern web development tools:

### 🧩 UI Components (shadcn/ui)
- **Layout**: Card, Separator, Aspect Ratio, Resizable Panels
- **Forms**: Input, Textarea, Select, Checkbox, Radio Group, Switch
- **Feedback**: Alert, Toast (Sonner), Progress, Skeleton
- **Navigation**: Breadcrumb, Menubar, Navigation Menu, Pagination
- **Overlay**: Dialog, Sheet, Popover, Tooltip, Hover Card
- **Data Display**: Badge, Avatar, Calendar

### 📊 Advanced Data Features
- **Tables**: Powerful data tables with sorting, filtering, pagination (TanStack Table)
- **Charts**: Beautiful visualizations with Recharts
- **Forms**: Type-safe forms with React Hook Form + Zod validation

### 🎨 Interactive Features
- **Animations**: Smooth micro-interactions with Framer Motion
- **Drag & Drop**: Modern drag-and-drop functionality with DND Kit
- **Theme Switching**: Built-in dark/light mode support

### 🔐 Backend Integration
- **Authentication**: Ready-to-use auth flows with NextAuth.js
- **Database**: Type-safe database operations with Prisma
- **API Client**: HTTP requests with Fetch + TanStack Query
- **State Management**: Simple and scalable with Zustand

### 🌍 Production Features
- **Internationalization**: Multi-language support with Next Intl
- **Image Optimization**: Automatic image processing with Sharp
- **Type Safety**: End-to-end TypeScript with Zod validation
- **Essential Hooks**: 100+ useful React hooks with ReactUse for common patterns

## 🤝 Get Started with Z.ai

1. **Clone this scaffold** to jumpstart your project
2. **Visit [chat.z.ai](https://chat.z.ai)** to access your AI coding assistant
3. **Start building** with intelligent code generation and assistance
4. **Deploy with confidence** using the production-ready setup

---

Built with ❤️ for the developer community. Supercharged by [Z.ai](https://chat.z.ai) 🚀
