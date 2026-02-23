/**
 * Role-based permission utilities
 */

export type UserRole = 'admin' | 'customer_admin' | 'operator' | 'oem_partner' | 'print_center' | 'cert_authority'

// Define which roles can access which pages
export const pagePermissions: Record<string, UserRole[]> = {
  overview: ['admin', 'customer_admin', 'operator', 'oem_partner', 'print_center', 'cert_authority'],
  orders: ['admin', 'customer_admin', 'operator', 'print_center'],
  blueprints: ['admin', 'customer_admin', 'operator', 'oem_partner', 'print_center', 'cert_authority'],
  centers: ['admin'],
  shipments: ['admin', 'customer_admin', 'operator', 'print_center'],
  materials: ['admin', 'customer_admin', 'print_center'],
  partners: ['admin'],
  services: ['admin', 'customer_admin'],
  analytics: ['admin', 'customer_admin', 'oem_partner'],
  audit: ['admin', 'cert_authority'],
  certifications: ['admin', 'oem_partner', 'cert_authority'],
  authorities: ['admin', 'cert_authority'],
  settings: ['admin', 'customer_admin', 'operator', 'oem_partner', 'print_center', 'cert_authority'],
}

/**
 * Check if a user has permission to access a specific page
 */
export function hasPageAccess(userRole: UserRole | undefined, pageId: string): boolean {
  if (!userRole) return false
  if (userRole === 'admin') return true // Admin has access to everything
  
  const allowedRoles = pagePermissions[pageId]
  if (!allowedRoles) return false
  
  return allowedRoles.includes(userRole)
}

/**
 * Check if a user can perform a specific action
 */
export const actionPermissions = {
  createOrder: ['admin', 'customer_admin', 'operator'],
  approveOrder: ['admin', 'customer_admin'],
  uploadBlueprint: ['admin', 'oem_partner'],
  approveBlueprint: ['admin', 'cert_authority'],
  manageUsers: ['admin', 'customer_admin'],
  viewAllOrders: ['admin'],
  manageCertAuthorities: ['admin'],
  updateShipmentStatus: ['admin', 'print_center'],
  viewAnalytics: ['admin', 'customer_admin', 'oem_partner'],
} as const

export type Action = keyof typeof actionPermissions

/**
 * Check if a user can perform a specific action
 */
export function canPerformAction(userRole: UserRole | undefined, action: Action): boolean {
  if (!userRole) return false
  if (userRole === 'admin') return true
  
  return actionPermissions[action].includes(userRole as any)
}

/**
 * Get a user-friendly role name
 */
export function getRoleDisplayName(role: UserRole): string {
  const roleNames: Record<UserRole, string> = {
    admin: 'Platform Admin',
    customer_admin: 'Customer Admin',
    operator: 'Operator',
    oem_partner: 'OEM Partner',
    print_center: 'Print Center',
    cert_authority: 'Certification Authority',
  }
  
  return roleNames[role] || role
}
