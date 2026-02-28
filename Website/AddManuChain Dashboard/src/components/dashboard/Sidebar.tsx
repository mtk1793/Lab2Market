'use client'

import { cn } from '@/lib/utils'
import {
  LayoutDashboard,
  Package,
  FileBox,
  Factory,
  BarChart3,
  Settings,
  Anchor,
  User,
  ChevronLeft,
  ChevronRight,
  ChevronDown,
  FileText,
  Users,
  Truck,
  Boxes,
  Shield,
  GraduationCap,
  Sparkles,
  KeyRound,
  X,
} from 'lucide-react'
import { useState } from 'react'
import { useSession } from 'next-auth/react'

// Define which roles can access which menu items
const rolePermissions: Record<string, string[]> = {
  admin: ['overview', 'orders', 'print_queue', 'digital_inventory', 'physical_inventory', 'blueprints', 'centers', 'peer_printers', 'shipments', 'materials', 'partners', 'services', 'analytics', 'audit', 'certifications', 'authorities', 'settings'],
  customer_admin: ['overview', 'orders', 'digital_inventory', 'physical_inventory', 'blueprints', 'peer_printers', 'shipments', 'materials', 'services', 'analytics', 'settings'],
  operator: ['overview', 'orders', 'digital_inventory', 'physical_inventory', 'blueprints', 'peer_printers', 'shipments', 'settings'],
  oem_partner: ['overview', 'print_queue', 'digital_inventory', 'blueprints', 'peer_printers', 'analytics', 'certifications', 'settings'],
  print_center: ['overview', 'orders', 'digital_inventory', 'physical_inventory', 'blueprints', 'peer_printers', 'shipments', 'materials', 'settings'],
  cert_authority: ['overview', 'print_queue', 'digital_inventory', 'blueprints', 'certifications', 'authorities', 'audit', 'settings'],
}

const menuSections = [
  {
    title: 'Main',
    items: [
      { id: 'overview', label: 'Overview', icon: LayoutDashboard },
      { id: 'orders', label: 'Orders', icon: Package, badge: 3 },
      { id: 'print_queue', label: 'Print Queue', icon: KeyRound, badge: 5 },
    ],
  },
  {
    title: 'Supply Chain',
    items: [
      { id: 'blueprints', label: 'Blueprint Library', icon: FileBox },
      { id: 'digital_inventory', label: 'Digital Inventory', icon: Sparkles },
      { id: 'physical_inventory', label: 'Physical Inventory', icon: Boxes },
      { id: 'centers', label: 'Print Centers', icon: Factory },
      { id: 'peer_printers', label: 'Peer Printers', icon: Users },
      { id: 'shipments', label: 'Shipments', icon: Truck },
      { id: 'materials', label: 'Materials', icon: Boxes },
    ],
  },
  {
    title: 'Partners',
    items: [
      { id: 'partners', label: 'OEM Partners', icon: Users },
      { id: 'services', label: 'Customer Success', icon: GraduationCap },
    ],
  },
  {
    title: 'Insights',
    items: [
      { id: 'analytics', label: 'Analytics', icon: BarChart3 },
      { id: 'audit', label: 'Audit Logs', icon: FileText },
      { id: 'certifications', label: 'Certifications', icon: Shield },
      { id: 'authorities', label: 'Authorities', icon: Shield },
    ],
  },
  {
    title: 'System',
    items: [
      { id: 'settings', label: 'Settings', icon: Settings },
    ],
  },
]

interface SidebarProps {
  activeTab: string
  onTabChange: (tab: string) => void
  mobileOpen?: boolean
  onMobileClose?: () => void
}

export function Sidebar({ activeTab, onTabChange, mobileOpen, onMobileClose }: SidebarProps) {
  const [collapsed, setCollapsed] = useState(false)
  const { data: session } = useSession()

  // Which section titles are expanded — all open by default
  const [openSections, setOpenSections] = useState<Record<string, boolean>>(
    Object.fromEntries(menuSections.map(s => [s.title, true]))
  )

  const toggleSection = (title: string) => {
    setOpenSections(prev => ({ ...prev, [title]: !prev[title] }))
  }

  // Role-based item filtering
  const role = (session?.user as { role?: string })?.role ?? 'admin'
  const allowed = rolePermissions[role] ?? rolePermissions.admin

  return (
    <>
      {/* backdrop when mobile menu open */}
      {mobileOpen && (
        <div
          className="fixed inset-0 bg-black/50 z-20 md:hidden"
          onClick={onMobileClose}
        />
      )}
      <aside
        className={cn(
          'fixed left-0 top-0 z-40 h-full bg-[#0F172A] border-r border-slate-800 transition-all duration-300 flex flex-col',
          collapsed ? 'w-20' : 'w-64',
          mobileOpen ? 'block' : 'hidden',
          'md:block'
        )}
      >
      {/* Logo */}
      <div className="flex items-center justify-between h-16 px-4 border-b border-slate-800 flex-shrink-0">
        <div className={cn('flex items-center gap-2', collapsed && 'hidden')}>
          <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-[#0EA5E9] to-[#14B8A6] flex items-center justify-center">
            <Anchor className="w-5 h-5 text-white" />
          </div>
          <span className="text-lg font-bold text-white">
            AddManu<span className="text-[#0EA5E9]">Chain</span>
          </span>
        </div>
        {collapsed && (
          <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-[#0EA5E9] to-[#14B8A6] flex items-center justify-center mx-auto">
            <Anchor className="w-5 h-5 text-white" />
          </div>
        )}
        {/* Collapse button — desktop only */}
        <button
          onClick={() => setCollapsed(!collapsed)}
          className={cn(
            'hidden md:flex items-center justify-center text-slate-400 hover:text-white transition-colors',
            collapsed && 'md:hidden'
          )}
        >
          <ChevronLeft className="w-5 h-5" />
        </button>
        {/* Close button — mobile only */}
        <button
          onClick={onMobileClose}
          className="md:hidden flex items-center justify-center text-slate-400 hover:text-white transition-colors"
          aria-label="Close menu"
        >
          <X className="w-5 h-5" />
        </button>
        {collapsed && (
          <button
            onClick={() => setCollapsed(false)}
            className="absolute right-2 top-6 text-slate-400 hover:text-white transition-colors"
          >
            <ChevronRight className="w-5 h-5" />
          </button>
        )}
      </div>

      {/* Navigation — scrollable */}
      <nav className="flex-1 min-h-0 overflow-y-auto px-3 py-4 space-y-1 scrollbar-thin scrollbar-thumb-slate-700 scrollbar-track-transparent">
        {menuSections.map((section) => {
          const visibleItems = section.items.filter(item => allowed.includes(item.id))
          if (visibleItems.length === 0) return null
          const isOpen = openSections[section.title] ?? true

          return (
            <div key={section.title} className="mb-1">
              {/* Section header — clickable to collapse, hidden in icon-only mode */}
              {!collapsed && (
                <button
                  onClick={() => toggleSection(section.title)}
                  className="w-full flex items-center justify-between px-3 py-1.5 mb-1 rounded-md group hover:bg-slate-800/60 transition-colors"
                >
                  <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider group-hover:text-slate-400 transition-colors">
                    {section.title}
                  </span>
                  <ChevronDown
                    className={cn(
                      'w-3.5 h-3.5 text-slate-600 group-hover:text-slate-400 transition-all duration-200',
                      !isOpen && '-rotate-90'
                    )}
                  />
                </button>
              )}

              {/* Section items */}
              <div
                className={cn(
                  'space-y-0.5 overflow-hidden transition-all duration-200',
                  !collapsed && !isOpen ? 'max-h-0 opacity-0' : 'max-h-[600px] opacity-100'
                )}
              >
                {visibleItems.map((item) => (
                  <button
                    key={item.id}
                    onClick={() => {
                      onTabChange(item.id)
                      onMobileClose?.()
                    }}
                    title={collapsed ? item.label : undefined}
                    className={cn(
                      'w-full flex items-center gap-3 px-3 py-2.5 rounded-lg transition-all',
                      activeTab === item.id
                        ? 'bg-[#0EA5E9]/20 text-[#0EA5E9]'
                        : 'text-slate-400 hover:text-white hover:bg-slate-800',
                      collapsed && 'justify-center px-0'
                    )}
                  >
                    <item.icon className="w-5 h-5 flex-shrink-0" />
                    {!collapsed && (
                      <>
                        <span className="flex-1 text-left text-sm font-medium">{item.label}</span>
                        {item.badge && (
                          <span className="px-2 py-0.5 text-xs font-medium bg-[#F59E0B] text-white rounded-full">
                            {item.badge}
                          </span>
                        )}
                      </>
                    )}
                  </button>
                ))}
              </div>

              {/* Divider between sections in collapsed mode */}
              {collapsed && <div className="w-8 h-px bg-slate-800 mx-auto my-2" />}
            </div>
          )
        })}
      </nav>

      {/* User Section */}
      <div className="border-t border-slate-800 p-3 flex-shrink-0">
        <div
          className={cn(
            'flex items-center gap-3 px-3 py-2 rounded-lg bg-slate-800/50',
            collapsed && 'justify-center'
          )}
        >
          <div className="w-8 h-8 rounded-full bg-[#14B8A6] flex items-center justify-center flex-shrink-0">
            <User className="w-4 h-4 text-white" />
          </div>
          {!collapsed && (
            <div className="flex-1 min-w-0">
              <p className="text-sm font-medium text-white truncate">John Operator</p>
              <p className="text-xs text-slate-400 truncate">Horizon Maritime</p>
            </div>
          )}
        </div>
      </div>
    </aside>
  </>
  )
}
