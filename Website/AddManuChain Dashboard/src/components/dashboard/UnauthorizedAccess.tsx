'use client'

import { ShieldAlert } from 'lucide-react'
import { useSession } from 'next-auth/react'
import { getRoleDisplayName } from '@/lib/permissions'

interface UnauthorizedAccessProps {
  requiredRoles?: string[]
  message?: string
}

export function UnauthorizedAccess({ requiredRoles, message }: UnauthorizedAccessProps) {
  const { data: session } = useSession()
  const userRole = session?.user?.role

  return (
    <div className="flex items-center justify-center min-h-[600px]">
      <div className="text-center max-w-md px-6">
        <div className="inline-flex items-center justify-center w-20 h-20 rounded-full bg-red-500/10 mb-6">
          <ShieldAlert className="w-10 h-10 text-red-500" />
        </div>
        
        <h2 className="text-2xl font-bold text-white mb-3">
          Access Denied
        </h2>
        
        <p className="text-slate-400 mb-6">
          {message || "You don't have permission to access this page."}
        </p>
        
        {userRole && (
          <div className="bg-slate-800/50 rounded-lg p-4 mb-4">
            <p className="text-sm text-slate-400 mb-2">Your current role:</p>
            <p className="text-white font-medium">
              {getRoleDisplayName(userRole as any)}
            </p>
          </div>
        )}
        
        {requiredRoles && requiredRoles.length > 0 && (
          <div className="bg-slate-800/50 rounded-lg p-4">
            <p className="text-sm text-slate-400 mb-2">Required role(s):</p>
            <p className="text-white font-medium">
              {requiredRoles.join(', ')}
            </p>
          </div>
        )}
        
        <p className="text-sm text-slate-500 mt-6">
          Contact your administrator if you believe you should have access.
        </p>
      </div>
    </div>
  )
}
