# Role-Based Access Control (RBAC) Implementation

## Overview

The application now implements comprehensive role-based access control, ensuring each user type sees only the features they're authorized to access.

## What Changed

### 1. **Sidebar Navigation** (`src/components/dashboard/Sidebar.tsx`)
- Added dynamic menu filtering based on user role
- Each role now sees only the menu items they're permitted to access
- User section displays the logged-in user's name and company from their session

### 2. **Permission System** (`src/lib/permissions.ts`)
- Created centralized permission management
- Defines which roles can access which pages
- Includes helper functions for checking permissions
- Supports action-based permissions (e.g., who can create orders, approve blueprints)

### 3. **Unauthorized Access Component** (`src/components/dashboard/UnauthorizedAccess.tsx`)
- Professional "Access Denied" screen
- Shows user's current role and required permissions
- Provides clear feedback when users try to access restricted pages

### 4. **Page-Level Protection**
- **AuthoritiesPage**: Only accessible by admins and certification authorities
- **PartnersPage**: Only accessible by admins
- **AuditLogPage**: Only accessible by admins and certification authorities

## Role Permissions Matrix

| Page | Admin | Customer Admin | Operator | OEM Partner | Print Center | Cert Authority |
|------|-------|----------------|----------|-------------|--------------|----------------|
| Overview | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Orders | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ |
| Blueprint Library | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Print Centers | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Shipments | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ |
| Materials | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ |
| OEM Partners | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Customer Success | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Analytics | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ |
| Audit Logs | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Certifications | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Authorities | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Settings | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## Testing the Implementation

### Test Accounts

```
1. Platform Admin
   Email: admin@almatech.com
   Password: admin123
   Expected: See all menu items

2. Rig Operator
   Email: operator@statoil.com
   Password: operator123
   Expected: See Overview, Orders, Blueprint Library, Shipments, Settings only

3. OEM Partner
   Email: partner@oem.com
   Password: partner123
   Expected: See Overview, Blueprint Library, Analytics, Certifications, Settings only
```

### Testing Steps

1. **Log out** (if currently logged in)
2. **Log in as Operator** (`operator@statoil.com`)
   - Notice the sidebar only shows 5 menu items
   - Try navigating to each visible menu item
   - The header should show "Rig Operator" with your role badge

3. **Log out and log in as OEM Partner** (`partner@oem.com`)
   - Notice different menu items appear
   - Try clicking "Authorities" - you should NOT see this option
   - Navigate to Certifications - this should work

4. **Log out and log in as Admin** (`admin@almatech.com`)
   - Notice ALL menu items are visible
   - Navigate to "Authorities" - this should work
   - Navigate to "OEM Partners" - this should work

5. **Direct URL Access Test**
   - While logged in as Operator, manually navigate to a restricted page by changing the URL
   - The system should show the "Access Denied" screen

## What Each Role Sees

### 🔴 **Platform Admin** (Full Access)
- **Main**: Overview, Orders
- **Supply Chain**: Blueprint Library, Print Centers, Shipments, Materials
- **Partners**: OEM Partners, Customer Success
- **Insights**: Analytics, Audit Logs, Certifications, Authorities
- **System**: Settings

### 👔 **Customer Admin** (Management)
- **Main**: Overview, Orders
- **Supply Chain**: Blueprint Library, Shipments, Materials
- **Partners**: Customer Success
- **Insights**: Analytics
- **System**: Settings

### 🔧 **Operator** (Field Personnel)
- **Main**: Overview, Orders
- **Supply Chain**: Blueprint Library, Shipments
- **System**: Settings

### 🏭 **OEM Partner** (Blueprint Owners)
- **Main**: Overview
- **Supply Chain**: Blueprint Library
- **Insights**: Analytics, Certifications
- **System**: Settings

### 🖨️ **Print Center** (Manufacturing)
- **Main**: Overview, Orders
- **Supply Chain**: Blueprint Library, Shipments, Materials
- **System**: Settings

### 🛡️ **Certification Authority** (Compliance)
- **Main**: Overview
- **Supply Chain**: Blueprint Library
- **Insights**: Audit Logs, Certifications, Authorities
- **System**: Settings

## Next Steps for Production

1. **API Endpoint Protection**: Add role checks to all API routes using the permission system
2. **Fine-Grained Permissions**: Implement feature-level restrictions (e.g., operators can view but not edit)
3. **Permission Groups**: Allow custom permission groups beyond the 6 base roles
4. **Audit Logging**: Log all permission checks for compliance
5. **UI Feedback**: Show tooltips explaining why certain actions are disabled

## Technical Implementation Details

### Authorization Flow

```
User Login → Create Session with Role → 
Page Load → Check hasPageAccess() → 
Display UI or UnauthorizedAccess Component
```

### Adding New Protected Pages

```typescript
// In your page component
import { useSession } from 'next-auth/react'
import { hasPageAccess, UserRole } from '@/lib/permissions'
import { UnauthorizedAccess } from './UnauthorizedAccess'

export function MyProtectedPage() {
  const { data: session } = useSession()
  const userRole = session?.user?.role as UserRole
  
  if (!hasPageAccess(userRole, 'my_page_id')) {
    return <UnauthorizedAccess requiredRoles={['Platform Admin']} />
  }
  
  // Rest of your component...
}
```

### Updating Role Permissions

Edit `src/lib/permissions.ts` to modify the `rolePermissions` mapping:

```typescript
export const rolePermissions: Record<string, string[]> = {
  admin: ['overview', 'orders', ...], // Add/remove page IDs
  operator: ['overview', 'orders', 'blueprints'],
  // etc.
}
```

## Security Notes

- ⚠️ **Client-side protection is not enough**: Always validate permissions on the API server
- 🔒 **Session security**: Ensure NEXTAUTH_SECRET is strong in production
- 📝 **Audit trail**: Consider logging all access attempts for compliance
- 🔄 **Role changes**: Users need to log out/in for role changes to take effect

## Questions?

See:
- [USER_GUIDE.md](./USER_GUIDE.md) for end-user documentation
- [DEPLOYMENT.md](./DEPLOYMENT.md) for production deployment
- [MONITORING.md](./MONITORING.md) for error tracking
