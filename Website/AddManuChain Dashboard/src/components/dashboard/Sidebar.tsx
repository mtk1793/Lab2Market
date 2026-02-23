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
  FileText,
  Users,
  Truck,
  Boxes,
  Shield,
  GraduationCap,
} from 'lucide-react'
import { useState } from 'react'

const menuSections = [
  {
    title: 'Main',
    items: [
      { id: 'overview', label: 'Overview', icon: LayoutDashboard },
      { id: 'orders', label: 'Orders', icon: Package, badge: 3 },
    ],
  },
  {
    title: 'Supply Chain',
    items: [
      { id: 'blueprints', label: 'Blueprint Library', icon: FileBox },
      { id: 'centers', label: 'Print Centers', icon: Factory },
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
}

export function Sidebar({ activeTab, onTabChange }: SidebarProps) {
  const [collapsed, setCollapsed] = useState(false)

  return (
    <aside
      className={cn(
        'fixed left-0 top-0 z-40 h-screen bg-[#0F172A] border-r border-slate-800 transition-all duration-300 flex flex-col',
        collapsed ? 'w-20' : 'w-64'
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
        <button
          onClick={() => setCollapsed(!collapsed)}
          className={cn(
            'text-slate-400 hover:text-white transition-colors',
            collapsed && 'hidden'
          )}
        >
          <ChevronLeft className="w-5 h-5" />
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

      {/* Navigation - Scrollable */}
      <nav className="flex-1 overflow-y-auto px-3 py-4 space-y-6">
        {menuSections.map((section, sectionIdx) => (
          <div key={sectionIdx}>
            {!collapsed && (
              <h3 className="px-3 mb-2 text-xs font-semibold text-slate-500 uppercase tracking-wider">
                {section.title}
              </h3>
            )}
            <div className="space-y-1">
              {section.items.map((item) => (
                <button
                  key={item.id}
                  onClick={() => onTabChange(item.id)}
                  className={cn(
                    'w-full flex items-center gap-3 px-3 py-2.5 rounded-lg transition-all',
                    activeTab === item.id
                      ? 'bg-[#0EA5E9]/20 text-[#0EA5E9]'
                      : 'text-slate-400 hover:text-white hover:bg-slate-800'
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
          </div>
        ))}
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
  )
}
