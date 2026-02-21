'use client'

import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Bell, Search, Plus } from 'lucide-react'

interface HeaderProps {
  title: string
  subtitle?: string
  action?: {
    label: string
    onClick: () => void
  }
}

export function Header({ title, subtitle, action }: HeaderProps) {
  return (
    <header className="sticky top-0 z-30 bg-[#F8FAFC] border-b border-slate-200">
      <div className="flex items-center justify-between h-16 px-6">
        {/* Title */}
        <div>
          <h1 className="text-xl font-bold text-[#0F172A]">{title}</h1>
          {subtitle && <p className="text-sm text-slate-500">{subtitle}</p>}
        </div>

        {/* Actions */}
        <div className="flex items-center gap-4">
          {/* Search */}
          <div className="relative hidden md:block">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-slate-400" />
            <Input
              placeholder="Search parts, orders..."
              className="w-64 pl-10 bg-white border-slate-200"
            />
          </div>

          {/* Notifications */}
          <Button variant="ghost" size="icon" className="relative">
            <Bell className="w-5 h-5 text-slate-600" />
            <span className="absolute top-1 right-1 w-2 h-2 bg-[#F59E0B] rounded-full" />
          </Button>

          {/* Primary Action */}
          {action && (
            <Button
              onClick={action.onClick}
              className="bg-[#0EA5E9] hover:bg-[#0EA5E9]/90 text-white"
            >
              <Plus className="w-4 h-4 mr-2" />
              {action.label}
            </Button>
          )}
        </div>
      </div>
    </header>
  )
}
