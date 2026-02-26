'use client'

import { useState } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { Progress } from '@/components/ui/progress'
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'
import { Boxes, AlertTriangle, CheckCircle, Clock, TrendingUp, RefreshCw } from 'lucide-react'
import { materials } from '@/lib/static-data'

const statusColors: Record<string, string> = {
  adequate: 'bg-[#14B8A6]/10 text-[#14B8A6]',
  low: 'bg-[#F59E0B]/10 text-[#F59E0B]',
  critical: 'bg-red-100 text-red-600',
}

const statusLabels: Record<string, string> = {
  adequate: 'Adequate',
  low: 'Low Stock',
  critical: 'Critical',
}

export function MaterialsPage() {
  const stats = {
    total: materials.length,
    adequate: materials.filter(m => m.status === 'adequate').length,
    low: materials.filter(m => m.status === 'low').length,
    critical: materials.filter(m => m.status === 'critical').length,
    totalValue: materials.reduce((sum, m) => sum + (m.totalStock * m.unitCost), 0),
  }

  const getStockPercentage = (material: typeof materials[0]) => {
    return Math.min(100, (material.totalStock / material.maxStock) * 100)
  }

  return (
    <div className="p-3 sm:p-6 space-y-4 sm:space-y-6">
      {/* Stats */}
      <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-[#0EA5E9]/10 flex items-center justify-center">
                <Boxes className="w-5 h-5 text-[#0EA5E9]" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">{stats.total}</p>
                <p className="text-sm text-slate-500">Materials</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-[#14B8A6]/10 flex items-center justify-center">
                <CheckCircle className="w-5 h-5 text-[#14B8A6]" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">{stats.adequate}</p>
                <p className="text-sm text-slate-500">Adequate</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-[#F59E0B]/10 flex items-center justify-center">
                <AlertTriangle className="w-5 h-5 text-[#F59E0B]" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">{stats.low}</p>
                <p className="text-sm text-slate-500">Low Stock</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-red-100 flex items-center justify-center">
                <AlertTriangle className="w-5 h-5 text-red-600" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">{stats.critical}</p>
                <p className="text-sm text-slate-500">Critical</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-green-100 flex items-center justify-center">
                <TrendingUp className="w-5 h-5 text-green-600" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">${(stats.totalValue / 1000).toFixed(0)}K</p>
                <p className="text-sm text-slate-500">Total Value</p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Alert Banner */}
      {stats.critical > 0 && (
        <Card className="bg-red-50 border-red-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <AlertTriangle className="w-5 h-5 text-red-600" />
              <div>
                <p className="font-medium text-red-800">
                  {stats.critical} material{stats.critical > 1 ? 's' : ''} at critical stock levels
                </p>
                <p className="text-sm text-red-600">
                  Immediate reorder required: {materials.filter(m => m.status === 'critical').map(m => m.name).join(', ')}
                </p>
              </div>
              <Button className="ml-auto bg-red-600 hover:bg-red-700">
                Create Purchase Order
              </Button>
            </div>
          </CardContent>
        </Card>
      )}

      {/* Materials Table */}
      <Card className="bg-white border-slate-200">
        <CardHeader className="flex flex-row items-center justify-between">
          <CardTitle className="text-lg font-semibold text-[#0F172A]">Material Inventory</CardTitle>
          <Button variant="outline" size="sm">
            <RefreshCw className="w-4 h-4 mr-2" />
            Refresh
          </Button>
        </CardHeader>
        <CardContent className="p-0">
          <Table>
            <TableHeader>
              <TableRow className="bg-slate-50">
                <TableHead className="font-semibold text-[#0F172A]">Material</TableHead>
                <TableHead className="font-semibold text-[#0F172A]">Stock Level</TableHead>
                <TableHead className="font-semibold text-[#0F172A]">Status</TableHead>
                <TableHead className="font-semibold text-[#0F172A]">Distribution</TableHead>
                <TableHead className="font-semibold text-[#0F172A]">Unit Cost</TableHead>
                <TableHead className="font-semibold text-[#0F172A]">Lead Time</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {materials.map((material) => (
                <TableRow key={material.id} className="hover:bg-slate-50">
                  <TableCell>
                    <div>
                      <p className="font-medium text-[#0F172A]">{material.name}</p>
                      <p className="text-xs text-slate-500">{material.category}</p>
                    </div>
                  </TableCell>
                  <TableCell>
                    <div className="w-40">
                      <div className="flex items-center justify-between text-sm mb-1">
                        <span className="font-medium text-[#0F172A]">{material.totalStock} {material.unit}</span>
                        <span className="text-slate-500">max {material.maxStock}</span>
                      </div>
                      <Progress 
                        value={getStockPercentage(material)} 
                        className={`h-2 ${material.status === 'critical' ? '[&>div]:bg-red-500' : material.status === 'low' ? '[&>div]:bg-[#F59E0B]' : ''}`}
                      />
                      <p className="text-xs text-slate-400 mt-1">
                        Min: {material.minStock} • Reorder: {material.reorderPoint}
                      </p>
                    </div>
                  </TableCell>
                  <TableCell>
                    <Badge className={statusColors[material.status]}>
                      {statusLabels[material.status]}
                    </Badge>
                  </TableCell>
                  <TableCell>
                    <div className="space-y-1">
                      {material.centerStocks?.map((stock, idx) => (
                        <div key={idx} className="flex items-center gap-2 text-sm">
                          <span className="text-slate-600">{stock.centerName}:</span>
                          <span className="font-medium text-[#0F172A]">{stock.stock} {material.unit}</span>
                        </div>
                      ))}
                    </div>
                  </TableCell>
                  <TableCell className="font-medium text-[#0F172A]">
                    ${material.unitCost}/{material.unit}
                  </TableCell>
                  <TableCell>
                    <div className="flex items-center gap-1 text-slate-600">
                      <Clock className="w-4 h-4" />
                      {material.leadTime} days
                    </div>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  )
}
