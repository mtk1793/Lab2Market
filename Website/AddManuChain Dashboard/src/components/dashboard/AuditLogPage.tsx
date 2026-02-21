'use client'

import { useState } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'
import { FileText, Filter, RefreshCw, Package, Edit, Clock, CheckCircle } from 'lucide-react'
import { auditLogs } from '@/lib/static-data'

const actionColors: Record<string, string> = {
  ORDER_CREATED: 'bg-[#0EA5E9]/10 text-[#0EA5E9]',
  ORDER_UPDATED: 'bg-[#F59E0B]/10 text-[#F59E0B]',
  ORDER_DELETED: 'bg-red-100 text-red-600',
}

const actionLabels: Record<string, string> = {
  ORDER_CREATED: 'Order Created',
  ORDER_UPDATED: 'Status Updated',
  ORDER_DELETED: 'Order Deleted',
}

const actionIcons: Record<string, any> = {
  ORDER_CREATED: Package,
  ORDER_UPDATED: Edit,
  ORDER_DELETED: Package,
}

export function AuditLogPage() {
  const [actionFilter, setActionFilter] = useState('all')

  const filteredLogs = auditLogs.filter(log => {
    return actionFilter === 'all' || log.action === actionFilter
  })

  const stats = {
    total: auditLogs.length,
    created: auditLogs.filter(l => l.action === 'ORDER_CREATED').length,
    updated: auditLogs.filter(l => l.action === 'ORDER_UPDATED').length,
  }

  return (
    <div className="p-6 space-y-6">
      {/* Stats */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-[#0EA5E9]/10 flex items-center justify-center">
                <FileText className="w-5 h-5 text-[#0EA5E9]" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">{stats.total}</p>
                <p className="text-sm text-slate-500">Total Logs</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-[#14B8A6]/10 flex items-center justify-center">
                <Package className="w-5 h-5 text-[#14B8A6]" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">{stats.created}</p>
                <p className="text-sm text-slate-500">Orders Created</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-[#F59E0B]/10 flex items-center justify-center">
                <Edit className="w-5 h-5 text-[#F59E0B]" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">{stats.updated}</p>
                <p className="text-sm text-slate-500">Status Updates</p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Filters */}
      <div className="flex gap-4">
        <Select value={actionFilter} onValueChange={setActionFilter}>
          <SelectTrigger className="w-44 bg-white border-slate-200">
            <Filter className="w-4 h-4 mr-2" />
            <SelectValue placeholder="Action Type" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="all">All Actions</SelectItem>
            <SelectItem value="ORDER_CREATED">Order Created</SelectItem>
            <SelectItem value="ORDER_UPDATED">Status Updated</SelectItem>
          </SelectContent>
        </Select>
        <Button variant="outline">
          <RefreshCw className="w-4 h-4 mr-2" />
          Refresh
        </Button>
      </div>

      {/* Audit Logs List */}
      <Card className="bg-white border-slate-200">
        <CardHeader>
          <CardTitle className="text-lg font-semibold text-[#0F172A]">Activity Log</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {filteredLogs.map((log) => {
              const ActionIcon = actionIcons[log.action] || FileText
              return (
                <div
                  key={log.id}
                  className="flex items-start gap-4 p-4 bg-slate-50 rounded-lg"
                >
                  <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${
                    log.action === 'ORDER_CREATED' ? 'bg-[#0EA5E9]/10' :
                    log.action === 'ORDER_UPDATED' ? 'bg-[#F59E0B]/10' : 'bg-slate-200'
                  }`}>
                    <ActionIcon className={`w-5 h-5 ${
                      log.action === 'ORDER_CREATED' ? 'text-[#0EA5E9]' :
                      log.action === 'ORDER_UPDATED' ? 'text-[#F59E0B]' : 'text-slate-500'
                    }`} />
                  </div>
                  <div className="flex-1">
                    <div className="flex items-center gap-2 mb-1">
                      <Badge className={actionColors[log.action]}>
                        {actionLabels[log.action]}
                      </Badge>
                      <span className="font-mono text-sm text-[#0EA5E9]">{log.order?.orderId}</span>
                    </div>
                    <p className="text-sm text-[#0F172A]">{log.details}</p>
                    <div className="flex items-center gap-4 mt-2 text-xs text-slate-500">
                      <div className="flex items-center gap-1">
                        <Clock className="w-3 h-3" />
                        {new Date(log.createdAt).toLocaleString()}
                      </div>
                      {log.order && (
                        <div className="flex items-center gap-1">
                          <Package className="w-3 h-3" />
                          {log.order.partName}
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              )
            })}
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
