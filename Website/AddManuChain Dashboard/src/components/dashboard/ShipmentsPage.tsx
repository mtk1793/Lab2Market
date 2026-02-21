'use client'

import { useState } from 'react'
import { Card, CardContent } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { Input } from '@/components/ui/input'
import { Progress } from '@/components/ui/progress'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'
import { Truck, Search, Filter, RefreshCw, MapPin, Clock, CheckCircle, Package, AlertCircle, ArrowRight } from 'lucide-react'
import { shipments, orders } from '@/lib/static-data'

const statusColors: Record<string, string> = {
  preparing: 'bg-slate-100 text-slate-600',
  in_transit: 'bg-[#0EA5E9]/10 text-[#0EA5E9]',
  out_for_delivery: 'bg-[#F59E0B]/10 text-[#F59E0B]',
  delivered: 'bg-green-100 text-green-600',
  delayed: 'bg-red-100 text-red-600',
}

const statusLabels: Record<string, string> = {
  preparing: 'Preparing',
  in_transit: 'In Transit',
  out_for_delivery: 'Out for Delivery',
  delivered: 'Delivered',
  delayed: 'Delayed',
}

const statusIcons: Record<string, any> = {
  preparing: Package,
  in_transit: Truck,
  out_for_delivery: ArrowRight,
  delivered: CheckCircle,
  delayed: AlertCircle,
}

export function ShipmentsPage() {
  const [searchQuery, setSearchQuery] = useState('')
  const [statusFilter, setStatusFilter] = useState('all')

  const filteredShipments = shipments.filter(shipment => {
    const matchesSearch = shipment.trackingId.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         shipment.destination.toLowerCase().includes(searchQuery.toLowerCase())
    const matchesStatus = statusFilter === 'all' || shipment.status === statusFilter
    return matchesSearch && matchesStatus
  })

  const stats = {
    total: shipments.length,
    inTransit: shipments.filter(s => s.status === 'in_transit' || s.status === 'out_for_delivery').length,
    delivered: shipments.filter(s => s.status === 'delivered').length,
    delayed: shipments.filter(s => s.status === 'delayed').length,
  }

  const getOrderInfo = (orderId: string) => {
    return orders.find(o => o.id === orderId)
  }

  return (
    <div className="p-6 space-y-6">
      {/* Stats */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-[#0EA5E9]/10 flex items-center justify-center">
                <Truck className="w-5 h-5 text-[#0EA5E9]" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">{stats.total}</p>
                <p className="text-sm text-slate-500">Total Shipments</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-[#F59E0B]/10 flex items-center justify-center">
                <ArrowRight className="w-5 h-5 text-[#F59E0B]" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">{stats.inTransit}</p>
                <p className="text-sm text-slate-500">In Transit</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-green-100 flex items-center justify-center">
                <CheckCircle className="w-5 h-5 text-green-600" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">{stats.delivered}</p>
                <p className="text-sm text-slate-500">Delivered</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-red-100 flex items-center justify-center">
                <AlertCircle className="w-5 h-5 text-red-600" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">{stats.delayed}</p>
                <p className="text-sm text-slate-500">Delayed</p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Filters */}
      <div className="flex flex-col sm:flex-row gap-4">
        <div className="relative flex-1">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-slate-400" />
          <Input
            placeholder="Search by tracking ID, destination..."
            className="pl-10 bg-white border-slate-200"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
        </div>
        <Select value={statusFilter} onValueChange={setStatusFilter}>
          <SelectTrigger className="w-44 bg-white border-slate-200">
            <Filter className="w-4 h-4 mr-2" />
            <SelectValue placeholder="Status" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="all">All Status</SelectItem>
            <SelectItem value="preparing">Preparing</SelectItem>
            <SelectItem value="in_transit">In Transit</SelectItem>
            <SelectItem value="out_for_delivery">Out for Delivery</SelectItem>
            <SelectItem value="delivered">Delivered</SelectItem>
            <SelectItem value="delayed">Delayed</SelectItem>
          </SelectContent>
        </Select>
        <Button variant="outline">
          <RefreshCw className="w-4 h-4 mr-2" />
          Refresh
        </Button>
      </div>

      {/* Shipments Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        {filteredShipments.map((shipment) => {
          const StatusIcon = statusIcons[shipment.status] || Truck
          const order = getOrderInfo(shipment.orderId)
          return (
            <Card key={shipment.id} className="bg-white border-slate-200">
              <CardContent className="p-4">
                {/* Header */}
                <div className="flex items-start justify-between mb-4">
                  <div>
                    <div className="flex items-center gap-2 mb-1">
                      <span className="font-mono text-sm font-medium text-[#0EA5E9]">{shipment.trackingId}</span>
                    </div>
                    <p className="font-medium text-[#0F172A]">{order?.partName || 'Unknown Part'}</p>
                    <p className="text-xs text-slate-500">{order?.orderId}</p>
                  </div>
                  <Badge className={statusColors[shipment.status]}>
                    <StatusIcon className="w-3 h-3 mr-1" />
                    {statusLabels[shipment.status]}
                  </Badge>
                </div>

                {/* Route */}
                <div className="flex items-center gap-2 mb-4">
                  <div className="flex-1">
                    <div className="flex items-center gap-2 text-sm">
                      <MapPin className="w-4 h-4 text-[#14B8A6]" />
                      <span className="text-slate-600 truncate">{shipment.origin}</span>
                    </div>
                  </div>
                  <ArrowRight className="w-4 h-4 text-slate-300 flex-shrink-0" />
                  <div className="flex-1">
                    <div className="flex items-center gap-2 text-sm">
                      <MapPin className="w-4 h-4 text-[#F59E0B]" />
                      <span className="text-slate-600 truncate">{shipment.destination}</span>
                    </div>
                  </div>
                </div>

                {/* Progress */}
                <div className="mb-4">
                  <div className="flex items-center justify-between text-sm mb-1">
                    <span className="text-slate-500">{shipment.distance.toLocaleString()} km</span>
                    <span className="text-slate-500">{shipment.progress}% complete</span>
                  </div>
                  <Progress value={shipment.progress} className="h-2" />
                </div>

                {/* Footer */}
                <div className="flex items-center justify-between pt-3 border-t border-slate-100">
                  <div className="flex items-center gap-4 text-sm text-slate-500">
                    <div className="flex items-center gap-1">
                      <Truck className="w-4 h-4" />
                      {shipment.carrier}
                    </div>
                    <div className="flex items-center gap-1">
                      <Clock className="w-4 h-4" />
                      {shipment.status === 'delivered' 
                        ? `Delivered ${shipment.actualDelivery ? new Date(shipment.actualDelivery).toLocaleDateString() : ''}`
                        : `ETA: ${new Date(shipment.estimatedDelivery).toLocaleDateString()}`
                      }
                    </div>
                  </div>
                  <Button variant="ghost" size="sm">
                    Track
                  </Button>
                </div>
              </CardContent>
            </Card>
          )
        })}
      </div>
    </div>
  )
}
