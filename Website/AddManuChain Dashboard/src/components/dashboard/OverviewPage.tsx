'use client'

import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import {
  Package,
  Clock,
  CheckCircle,
  DollarSign,
  Factory,
  FileBox,
  AlertTriangle,
} from 'lucide-react'
import { orders, printCenters, blueprints, dashboardStats } from '@/lib/static-data'

const statusColors: Record<string, string> = {
  pending: 'bg-slate-100 text-slate-600',
  printing: 'bg-[#0EA5E9]/10 text-[#0EA5E9]',
  quality_check: 'bg-[#F59E0B]/10 text-[#F59E0B]',
  shipped: 'bg-[#14B8A6]/10 text-[#14B8A6]',
  delivered: 'bg-green-100 text-green-600',
}

const statusLabels: Record<string, string> = {
  pending: 'Pending',
  printing: 'Printing',
  quality_check: 'Quality Check',
  shipped: 'Shipped',
  delivered: 'Delivered',
}

export function OverviewPage() {
  const kpis = [
    {
      title: 'Active Orders',
      value: dashboardStats.activeOrders.toString(),
      change: `${dashboardStats.totalOrders} total`,
      icon: Package,
      color: '#0EA5E9',
    },
    {
      title: 'Parts Delivered',
      value: dashboardStats.deliveredParts.toLocaleString(),
      change: 'Total delivered',
      icon: CheckCircle,
      color: '#14B8A6',
    },
    {
      title: 'Avg. Lead Time',
      value: `${dashboardStats.avgLeadTime} days`,
      change: '-33% vs traditional',
      icon: Clock,
      color: '#F59E0B',
    },
    {
      title: 'Cost Savings',
      value: `$${Math.round(dashboardStats.costSavings / 1000)}K`,
      change: 'YTD savings',
      icon: DollarSign,
      color: '#10B981',
    },
  ]

  const recentOrders = orders.slice(0, 5)
  const onlineCenters = printCenters.filter(c => c.status !== 'offline')
  const pendingBlueprints = blueprints.filter(b => b.status === 'pending_review')

  return (
    <div className="p-6 space-y-6">
      {/* KPI Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {kpis.map((kpi, index) => (
          <Card key={index} className="bg-white border-slate-200">
            <CardContent className="p-6">
              <div className="flex items-start justify-between">
                <div>
                  <p className="text-sm text-slate-500 mb-1">{kpi.title}</p>
                  <p className="text-3xl font-bold text-[#0F172A]">{kpi.value}</p>
                  <p className="text-xs text-[#14B8A6] mt-1">{kpi.change}</p>
                </div>
                <div
                  className="w-12 h-12 rounded-lg flex items-center justify-center"
                  style={{ backgroundColor: `${kpi.color}15` }}
                >
                  <kpi.icon className="w-6 h-6" style={{ color: kpi.color }} />
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Main Content Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Recent Orders */}
        <Card className="lg:col-span-2 bg-white border-slate-200">
          <CardHeader>
            <CardTitle className="text-lg font-semibold text-[#0F172A]">Recent Orders</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {recentOrders.map((order) => {
                const center = printCenters.find(c => c.id === order.centerId)
                return (
                  <div
                    key={order.id}
                    className="flex items-center justify-between p-4 bg-slate-50 rounded-lg"
                  >
                    <div className="flex items-center gap-4">
                      <div className="w-10 h-10 rounded-lg bg-[#0F172A]/5 flex items-center justify-center">
                        <Package className="w-5 h-5 text-[#0F172A]" />
                      </div>
                      <div>
                        <p className="font-medium text-[#0F172A]">{order.partName}</p>
                        <p className="text-sm text-slate-500">
                          {order.orderId} • {center?.name || 'Pending assignment'}
                        </p>
                      </div>
                    </div>
                    <div className="flex items-center gap-4">
                      <Badge className={statusColors[order.status]}>
                        {statusLabels[order.status]}
                      </Badge>
                      <span className="text-sm text-slate-500 w-20 text-right">
                        {order.status === 'delivered' 
                          ? 'Delivered' 
                          : order.eta 
                            ? new Date(order.eta).toLocaleDateString()
                            : 'TBD'}
                      </span>
                    </div>
                  </div>
                )
              })}
            </div>
          </CardContent>
        </Card>

        {/* Right Column */}
        <div className="space-y-6">
          {/* Print Center Status */}
          <Card className="bg-white border-slate-200">
            <CardHeader>
              <CardTitle className="text-lg font-semibold text-[#0F172A]">Print Centers</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {printCenters.map((center) => (
                  <div key={center.id} className="flex items-center justify-between">
                    <div className="flex items-center gap-3">
                      <div className={`w-2 h-2 rounded-full ${
                        center.status === 'online' ? 'bg-[#14B8A6]' :
                        center.status === 'busy' ? 'bg-[#F59E0B]' : 'bg-slate-300'
                      }`} />
                      <span className="text-sm text-[#0F172A]">{center.name}</span>
                    </div>
                    <Badge 
                      variant="outline" 
                      className={`${
                        center.status === 'online' ? 'text-[#14B8A6] border-[#14B8A6]' :
                        center.status === 'busy' ? 'text-[#F59E0B] border-[#F59E0B]' : 
                        'text-slate-400 border-slate-400'
                      }`}
                    >
                      {center.status.charAt(0).toUpperCase() + center.status.slice(1)}
                    </Badge>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>

          {/* Quick Stats */}
          <Card className="bg-white border-slate-200">
            <CardHeader>
              <CardTitle className="text-lg font-semibold text-[#0F172A]">Inventory Stats</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <FileBox className="w-4 h-4 text-[#0EA5E9]" />
                    <span className="text-sm text-slate-600">Available Blueprints</span>
                  </div>
                  <span className="font-semibold text-[#0F172A]">{blueprints.length}</span>
                </div>
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <Factory className="w-4 h-4 text-[#14B8A6]" />
                    <span className="text-sm text-slate-600">Online Centers</span>
                  </div>
                  <span className="font-semibold text-[#0F172A]">{onlineCenters.length}</span>
                </div>
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <AlertTriangle className="w-4 h-4 text-[#F59E0B]" />
                    <span className="text-sm text-slate-600">Pending Review</span>
                  </div>
                  <span className="font-semibold text-[#F59E0B]">{pendingBlueprints.length}</span>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  )
}
