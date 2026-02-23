# Monitoring & Analytics Setup Guide
## AddManuChain Dashboard

This guide covers error tracking, performance monitoring, and analytics configuration.

---

## 📊 Overview

The AddManuChain Dashboard includes:
1. **Sentry** - Error tracking and performance monitoring
2. **Vercel Analytics** - Web vitals and user analytics (if deployed on Vercel)
3. **Custom Logging** - Application-level logging
4. **Audit Logs** - User activity tracking (built-in)

---

## 🚨 Sentry - Error Tracking

### Why Sentry?
- **Real-time error alerts** - Get notified immediately when errors occur
- **Stack traces with context** - See exactly what went wrong
- **Performance monitoring** - Track slow API calls and page loads
- **Session replay** - Watch user sessions leading to errors
- **Release tracking** - Compare error rates across deployments

### Setup Instructions

#### 1. Create Sentry Account
1. Go to [sentry.io](https://sentry.io) and sign up
2. Create a new project → Select "Next.js"
3. Copy your **DSN** (e.g., `https://xxxxx@o123456.ingest.sentry.io/123456`)

#### 2. Configure Environment Variables

Add to `.env` or `.env.production`:
```bash
SENTRY_DSN="your-sentry-dsn-from-step-1"
SENTRY_ORG="your-organization-slug"
SENTRY_PROJECT="your-project-name"
```

For development (optional):
```bash
SENTRY_DEV_ENABLED="true"  # Set to "true" to enable Sentry in development
```

#### 3. Configuration Files

The following files are already created:
- ✅ `sentry.client.config.ts` - Client-side error tracking
- ✅ `sentry.server.config.ts` - Server-side error tracking
- ✅ `sentry.edge.config.ts` - Edge runtime error tracking

#### 4. Update Next.js Config (if needed)

If Next.js doesn't automatically detect Sentry:

```typescript
// next.config.ts
import { withSentryConfig } from '@sentry/nextjs'

const nextConfig = {
  // Your existing config
}

export default withSentryConfig(nextConfig, {
  silent: true,
  org: process.env.SENTRY_ORG,
  project: process.env.SENTRY_PROJECT,
})
```

#### 5. Test Sentry

Add a test error button (remove after testing):

```tsx
// src/app/page.tsx
<button onClick={() => { throw new Error('Sentry Test Error') }}>
  Test Sentry
</button>
```

Click the button and check your Sentry dashboard for the error.

---

### Using Sentry in Your Code

#### Automatic Error Capture
Most unhandled errors are captured automatically. No code changes needed!

#### Manual Error Capture

```typescript
import * as Sentry from '@sentry/nextjs'

try {
  // Your code
} catch (error) {
  Sentry.captureException(error)
  // Handle error
}
```

#### Add Context to Errors

```typescript
Sentry.setUser({
  id: user.id,
  email: user.email,
  role: user.role,
  company: user.company,
})

Sentry.setTag('feature', 'blueprint-upload')
Sentry.setTag('priority', 'high')

Sentry.addBreadcrumb({
  message: 'User uploaded blueprint',
  category: 'action',
  level: 'info',
})
```

#### Performance Monitoring

```typescript
import * as Sentry from '@sentry/nextjs'

// Measure database query performance
const transaction = Sentry.startTransaction({
  op: 'database.query',
  name: 'Fetch Orders',
})

const orders = await prisma.order.findMany()

transaction.finish()
```

#### API Route Error Handling

```typescript
// src/app/api/orders/route.ts
import * as Sentry from '@sentry/nextjs'

export async function GET(request: Request) {
  try {
    const orders = await prisma.order.findMany()
    return Response.json(orders)
  } catch (error) {
    Sentry.captureException(error, {
      tags: {
        api: 'orders',
        method: 'GET',
      },
    })
    return Response.json({ error: 'Failed to fetch orders' }, { status: 500 })
  }
}
```

---

### Sentry Alerts

#### Configure Alerts in Sentry Dashboard

1. **Project Settings** → **Alerts** → **Create Alert Rule**
2. **Alert Types:**
   - **Error Count** - Trigger when error frequency exceeds threshold
   - **Issue Frequency** - Alert on specific error patterns
   - **Performance Degradation** - Slow API calls or page loads

3. **Notification Channels:**
   - Email
   - Slack
   - PagerDuty (for critical issues)
   - Webhooks

#### Recommended Alert Rules

**Critical Errors:**
- Trigger: 10+ errors in 1 minute
- Notify: Slack + Email
- Action: Immediate investigation

**Authentication Failures:**
- Trigger: 50+ failed logins in 5 minutes
- Notify: Security team
- Action: Potential security incident

**API Degradation:**
- Trigger: API response time > 3 seconds
- Notify: DevOps team
- Action: Performance investigation

---

## 📈 Vercel Analytics (if deployed on Vercel)

### Automatic Setup (No Configuration Needed!)

When deployed on Vercel, analytics are automatically enabled:
- **Web Vitals** - Core Web Vitals (LCP, FID, CLS)
- **User Analytics** - Page views, unique visitors
- **Audience** - Geographic distribution, devices, browsers

### View Analytics

1. Go to [vercel.com](https://vercel.com)
2. Select your project
3. Click **Analytics** tab

### Key Metrics to Monitor

- **Total Visitors** - Unique users per day/week/month
- **Page Views** - Most visited pages
- **Web Vitals Score** - Performance rating (aim for 90+)
- **Top Pages** - Orders, Blueprints, Analytics
- **Error Rate** - 4xx/5xx responses

---

## 📝 Application Logging

### Console Logging (Development)

Standard console methods work:
```typescript
console.log('Info message')
console.warn('Warning message')
console.error('Error message')
```

### Structured Logging (Production)

For production, use a structured logger:

```typescript
// src/lib/logger.ts
export const logger = {
  info: (message: string, meta?: any) => {
    console.log(JSON.stringify({ level: 'info', message, ...meta, timestamp: new Date().toISOString() }))
  },
  warn: (message: string, meta?: any) => {
    console.warn(JSON.stringify({ level: 'warn', message, ...meta, timestamp: new Date().toISOString() }))
  },
  error: (message: string, error?: any, meta?: any) => {
    console.error(JSON.stringify({ 
      level: 'error', 
      message, 
      error: error?.message, 
      stack: error?.stack,
      ...meta, 
      timestamp: new Date().toISOString() 
    }))
  },
}

// Usage
import { logger } from '@/lib/logger'

logger.info('Order created', { orderId: 'ORD-123', userId: 'user-456' })
logger.error('Database connection failed', error, { retry: 3 })
```

### View Logs

**Vercel:**
```bash
vercel logs --follow
```

**Self-hosted (PM2):**
```bash
pm2 logs addmanuchain
```

**Docker:**
```bash
docker logs -f container-name
```

---

## 🔍 Built-in Audit Logs

The dashboard includes comprehensive audit logging:

### What's Logged
- Order creation and status changes
- Blueprint uploads and modifications
- User authentication events
- Configuration changes
- Certification approvals

### Accessing Audit Logs

**Via Dashboard:**
1. Navigate to **Audit Logs** page
2. Filter by:
   - Order ID
   - User
   - Action type
   - Date range

**Via Database:**
```sql
SELECT * FROM AuditLog 
WHERE action = 'order_created' 
AND createdAt > datetime('now', '-7 days')
ORDER BY createdAt DESC;
```

**Via API:**
```typescript
const logs = await prisma.auditLog.findMany({
  where: {
    orderId: 'ORD-123',
  },
  orderBy: {
    createdAt: 'desc',
  },
})
```

### Audit Log Retention

- **Development:** 30 days
- **Production:** 365 days (adjust based on compliance requirements)

Configure retention in database cleanup job:
```typescript
// Delete logs older than 365 days
await prisma.auditLog.deleteMany({
  where: {
    createdAt: {
      lt: new Date(Date.now() - 365 * 24 * 60 * 60 * 1000)
    }
  }
})
```

---

## 🎯 Custom Metrics

### Application-Specific Metrics

Track key business metrics:

```typescript
// src/lib/metrics.ts
import * as Sentry from '@sentry/nextjs'

export const trackOrderPlaced = (order: Order) => {
  Sentry.addBreadcrumb({
    message: 'Order placed',
    category: 'business',
    level: 'info',
    data: {
      orderId: order.orderId,
      priority: order.priority,
      value: calculateOrderValue(order),
    },
  })
}

export const trackLeadTime = (orderId: string, days: number) => {
  // Send to analytics
  console.log(JSON.stringify({
    metric: 'lead_time',
    orderId,
    days,
    timestamp: new Date().toISOString(),
  }))
}
```

### KPIs to Monitor

- **Order Volume** - Orders per day/week
- **Lead Time** - Average time from order to delivery
- **Error Rate** - Failed orders / total orders
- **Certification Approval Time** - Days to approval
- **User Activity** - Daily/weekly active users
- **Cost Savings** - Tracked vs traditional supply
- **Customer Health Scores** - Average across customers

---

## 🚨 Incident Response

### When Sentry Alerts Fire

1. **Acknowledge** - Confirm you've seen the alert
2. **Assess Severity:**
   - **P0 Critical** - Production down, users blocked
   - **P1 High** - Major feature broken
   - **P2 Medium** - Minor feature affected
   - **P3 Low** - Cosmetic issue
3. **Investigate** - Use Sentry stack traces and session replay
4. **Fix** - Deploy hotfix if critical
5. **Post-Mortem** - Document what happened and how to prevent

### Escalation Path

- **P0:** Immediate notification to on-call engineer
- **P1:** Notify team via Slack within 15 minutes
- **P2:** Create ticket, address in next sprint
- **P3:** Add to backlog

---

## 📊 Analytics Dashboard

### Creating Custom Analytics Page

Example: Track blueprint popularity

```typescript
// src/app/analytics-admin/page.tsx
'use client'

import { useEffect, useState } from 'react'

export default function AnalyticsAdmin() {
  const [stats, setStats] = useState(null)
  
  useEffect(() => {
    fetch('/api/analytics/blueprints')
      .then(res => res.json())
      .then(setStats)
  }, [])
  
  return (
    <div>
      <h1>Blueprint Analytics</h1>
      {stats?.topBlueprints.map(bp => (
        <div key={bp.id}>
          {bp.name}: {bp.printCount} prints
        </div>
      ))}
    </div>
  )
}
```

### API Route for Analytics

```typescript
// src/app/api/analytics/blueprints/route.ts
export async function GET() {
  const topBlueprints = await prisma.blueprint.findMany({
    orderBy: { printCount: 'desc' },
    take: 10,
  })
  
  return Response.json({ topBlueprints })
}
```

---

## 🔐 Privacy & Compliance

### GDPR Compliance

- **User Data Sanitization:** Remove PII from Sentry errors
- **Data Retention:** Configure retention policies
- **Right to be Forgotten:** Ability to delete user data

### Sensitive Data Filtering

Already configured in `sentry.server.config.ts`:
```typescript
beforeSend(event) {
  // Remove sensitive headers
  delete event.request?.cookies
  delete event.request?.headers?.['authorization']
  return event
}
```

---

## ✅ Monitoring Checklist

### Initial Setup
- [ ] Sentry account created
- [ ] DSN configured in environment variables
- [ ] Test error sent and received in Sentry
- [ ] Alert rules configured
- [ ] Notification channels set up (Slack, email)
- [ ] Team invited to Sentry project

### Ongoing Monitoring
- [ ] Check Sentry dashboard daily
- [ ] Review error trends weekly
- [ ] Monitor performance metrics
- [ ] Audit log retention policy enforced
- [ ] Monthly analytics review meeting

### Production Checklist
- [ ] Sentry configured for production environment
- [ ] Vercel Analytics enabled (if applicable)
- [ ] Log aggregation configured
- [ ] Uptime monitoring set up (UptimeRobot, Pingdom)
- [ ] Incident response plan documented
- [ ] On-call rotation established

---

## 📞 Support

**Sentry Support:**
- Docs: [docs.sentry.io](https://docs.sentry.io)
- Community: [forum.sentry.io](https://forum.sentry.io)

**Vercel Support:**
- Docs: [vercel.com/docs](https://vercel.com/docs)
- Support: support@vercel.com

---

**Document Version:** 1.0  
**Last Updated:** February 23, 2026  
**Maintained By:** DevOps Team
