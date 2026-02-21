'use client'

import { useState } from 'react'
import { Card, CardContent } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Textarea } from '@/components/ui/textarea'
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'
import { Package, Search, Filter, Plus, Eye, Edit, Trash2, ArrowRight, Clock, CheckCircle, AlertCircle } from 'lucide-react'
import { toast } from 'sonner'
import { orders as initialOrders, blueprints, printCenters, users } from '@/lib/static-data'

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

const priorityColors: Record<string, string> = {
  low: 'bg-slate-100 text-slate-500',
  medium: 'bg-[#F59E0B]/10 text-[#F59E0B]',
  high: 'bg-red-100 text-red-600',
}

const statusFlow = ['pending', 'printing', 'quality_check', 'shipped', 'delivered']

export function OrdersPage() {
  const [orders, setOrders] = useState(initialOrders)
  const [searchQuery, setSearchQuery] = useState('')
  const [statusFilter, setStatusFilter] = useState('all')
  const [priorityFilter, setPriorityFilter] = useState('all')
  const [isCreateOpen, setIsCreateOpen] = useState(false)
  const [isViewOpen, setIsViewOpen] = useState(false)
  const [isEditOpen, setIsEditOpen] = useState(false)
  const [selectedOrder, setSelectedOrder] = useState<any>(null)

  const [formData, setFormData] = useState({
    partName: '',
    status: 'pending',
    priority: 'medium',
    quantity: 1,
    notes: '',
    blueprintId: '',
    centerId: '',
  })

  const filteredOrders = orders.filter(order => {
    const matchesSearch = order.partName.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         order.orderId.toLowerCase().includes(searchQuery.toLowerCase())
    const matchesStatus = statusFilter === 'all' || order.status === statusFilter
    const matchesPriority = priorityFilter === 'all' || order.priority === priorityFilter
    return matchesSearch && matchesStatus && matchesPriority
  })

  const stats = {
    total: orders.length,
    pending: orders.filter(o => o.status === 'pending').length,
    printing: orders.filter(o => o.status === 'printing').length,
    qualityCheck: orders.filter(o => o.status === 'quality_check').length,
    shipped: orders.filter(o => o.status === 'shipped').length,
    delivered: orders.filter(o => o.status === 'delivered').length,
  }

  const handleCreateOrder = () => {
    if (!formData.partName) {
      toast.error('Part name is required')
      return
    }

    const newOrderNum = Math.max(...orders.map(o => parseInt(o.orderId.split('-')[1]))) + 1
    const newOrder = {
      id: `ord-${Date.now()}`,
      orderId: `ORD-${newOrderNum}`,
      partName: formData.partName,
      status: formData.status,
      priority: formData.priority,
      quantity: formData.quantity,
      eta: new Date(Date.now() + 5 * 24 * 60 * 60 * 1000).toISOString(),
      requesterId: 'user-1',
      blueprintId: formData.blueprintId || null,
      centerId: formData.centerId || null,
      notes: formData.notes || null,
      createdAt: new Date().toISOString(),
    }

    setOrders([newOrder, ...orders])
    toast.success(`Order ${newOrder.orderId} created successfully`)
    setIsCreateOpen(false)
    setFormData({ partName: '', status: 'pending', priority: 'medium', quantity: 1, notes: '', blueprintId: '', centerId: '' })
  }

  const handleDeleteOrder = (orderId: string) => {
    if (!confirm('Are you sure you want to delete this order?')) return
    setOrders(orders.filter(o => o.id !== orderId))
    toast.success('Order deleted')
  }

  const handleAdvanceStatus = (order: any) => {
    const currentIndex = statusFlow.indexOf(order.status)
    if (currentIndex < statusFlow.length - 1) {
      const newStatus = statusFlow[currentIndex + 1]
      setOrders(orders.map(o => o.id === order.id ? { ...o, status: newStatus } : o))
      toast.success(`Order ${order.orderId} advanced to ${statusLabels[newStatus]}`)
    }
  }

  const handleUpdateOrder = () => {
    if (!selectedOrder) return
    setOrders(orders.map(o => o.id === selectedOrder.id ? selectedOrder : o))
    toast.success(`Order ${selectedOrder.orderId} updated`)
    setIsEditOpen(false)
  }

  return (
    <div className="p-6 space-y-6">
      {/* Stats */}
      <div className="grid grid-cols-2 md:grid-cols-6 gap-4">
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4 text-center">
            <p className="text-2xl font-bold text-[#0F172A]">{stats.total}</p>
            <p className="text-xs text-slate-500">Total Orders</p>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4 text-center">
            <p className="text-2xl font-bold text-slate-600">{stats.pending}</p>
            <p className="text-xs text-slate-500">Pending</p>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4 text-center">
            <p className="text-2xl font-bold text-[#0EA5E9]">{stats.printing}</p>
            <p className="text-xs text-slate-500">Printing</p>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4 text-center">
            <p className="text-2xl font-bold text-[#F59E0B]">{stats.qualityCheck}</p>
            <p className="text-xs text-slate-500">Quality Check</p>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4 text-center">
            <p className="text-2xl font-bold text-[#14B8A6]">{stats.shipped}</p>
            <p className="text-xs text-slate-500">Shipped</p>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4 text-center">
            <p className="text-2xl font-bold text-green-600">{stats.delivered}</p>
            <p className="text-xs text-slate-500">Delivered</p>
          </CardContent>
        </Card>
      </div>

      {/* Filters */}
      <div className="flex flex-col sm:flex-row gap-4">
        <div className="relative flex-1">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-slate-400" />
          <Input
            placeholder="Search orders..."
            className="pl-10 bg-white border-slate-200"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
        </div>
        <Select value={statusFilter} onValueChange={setStatusFilter}>
          <SelectTrigger className="w-40 bg-white border-slate-200">
            <Filter className="w-4 h-4 mr-2" />
            <SelectValue placeholder="Status" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="all">All Status</SelectItem>
            {statusFlow.map((status) => (
              <SelectItem key={status} value={status}>{statusLabels[status]}</SelectItem>
            ))}
          </SelectContent>
        </Select>
        <Select value={priorityFilter} onValueChange={setPriorityFilter}>
          <SelectTrigger className="w-36 bg-white border-slate-200">
            <SelectValue placeholder="Priority" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="all">All Priority</SelectItem>
            <SelectItem value="low">Low</SelectItem>
            <SelectItem value="medium">Medium</SelectItem>
            <SelectItem value="high">High</SelectItem>
          </SelectContent>
        </Select>
        <Button 
          onClick={() => setIsCreateOpen(true)}
          className="bg-[#0EA5E9] hover:bg-[#0EA5E9]/90 text-white"
        >
          <Plus className="w-4 h-4 mr-2" />
          New Order
        </Button>
      </div>

      {/* Orders Table */}
      <Card className="bg-white border-slate-200">
        <CardContent className="p-0">
          <Table>
            <TableHeader>
              <TableRow className="bg-slate-50">
                <TableHead className="font-semibold text-[#0F172A]">Order</TableHead>
                <TableHead className="font-semibold text-[#0F172A]">Part Name</TableHead>
                <TableHead className="font-semibold text-[#0F172A]">Status</TableHead>
                <TableHead className="font-semibold text-[#0F172A]">Priority</TableHead>
                <TableHead className="font-semibold text-[#0F172A]">Qty</TableHead>
                <TableHead className="font-semibold text-[#0F172A]">ETA</TableHead>
                <TableHead className="font-semibold text-[#0F172A]">Actions</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {filteredOrders.map((order) => {
                const blueprint = blueprints.find(b => b.id === order.blueprintId)
                const center = printCenters.find(c => c.id === order.centerId)
                const requester = users.find(u => u.id === order.requesterId)
                
                return (
                  <TableRow key={order.id} className="hover:bg-slate-50">
                    <TableCell>
                      <span className="font-mono text-sm font-medium text-[#0EA5E9]">{order.orderId}</span>
                    </TableCell>
                    <TableCell>
                      <div>
                        <p className="font-medium text-[#0F172A]">{order.partName}</p>
                        {blueprint && (
                          <p className="text-xs text-slate-500">{blueprint.blueprintId}</p>
                        )}
                      </div>
                    </TableCell>
                    <TableCell>
                      <Badge className={statusColors[order.status]}>
                        {statusLabels[order.status]}
                      </Badge>
                    </TableCell>
                    <TableCell>
                      <Badge className={priorityColors[order.priority]}>
                        {order.priority.charAt(0).toUpperCase() + order.priority.slice(1)}
                      </Badge>
                    </TableCell>
                    <TableCell className="text-[#0F172A]">{order.quantity}</TableCell>
                    <TableCell className="text-slate-500">
                      {order.status === 'delivered' ? 'Delivered' : order.eta ? new Date(order.eta).toLocaleDateString() : 'TBD'}
                    </TableCell>
                    <TableCell>
                      <div className="flex items-center gap-1">
                        <Button
                          variant="ghost"
                          size="icon"
                          className="h-8 w-8"
                          onClick={() => {
                            setSelectedOrder({ ...order, blueprint, center, requester })
                            setIsViewOpen(true)
                          }}
                        >
                          <Eye className="w-4 h-4" />
                        </Button>
                        <Button
                          variant="ghost"
                          size="icon"
                          className="h-8 w-8"
                          onClick={() => {
                            setSelectedOrder({ ...order, blueprint, center, requester })
                            setIsEditOpen(true)
                          }}
                        >
                          <Edit className="w-4 h-4" />
                        </Button>
                        {order.status !== 'delivered' && (
                          <Button
                            variant="ghost"
                            size="icon"
                            className="h-8 w-8 text-[#14B8A6]"
                            onClick={() => handleAdvanceStatus(order)}
                            title="Advance status"
                          >
                            <ArrowRight className="w-4 h-4" />
                          </Button>
                        )}
                        <Button
                          variant="ghost"
                          size="icon"
                          className="h-8 w-8 text-red-500"
                          onClick={() => handleDeleteOrder(order.id)}
                        >
                          <Trash2 className="w-4 h-4" />
                        </Button>
                      </div>
                    </TableCell>
                  </TableRow>
                )
              })}
            </TableBody>
          </Table>
        </CardContent>
      </Card>

      {/* Create Order Dialog */}
      <Dialog open={isCreateOpen} onOpenChange={setIsCreateOpen}>
        <DialogContent className="max-w-md">
          <DialogHeader>
            <DialogTitle>Create New Order</DialogTitle>
            <DialogDescription>Submit a new part order</DialogDescription>
          </DialogHeader>
          <div className="space-y-4 py-4">
            <div className="space-y-2">
              <Label>Part Name *</Label>
              <Input
                placeholder="e.g., Hydraulic Valve Body"
                value={formData.partName}
                onChange={(e) => setFormData({ ...formData, partName: e.target.value })}
              />
            </div>
            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label>Priority</Label>
                <Select value={formData.priority} onValueChange={(v) => setFormData({ ...formData, priority: v })}>
                  <SelectTrigger>
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="low">Low</SelectItem>
                    <SelectItem value="medium">Medium</SelectItem>
                    <SelectItem value="high">High</SelectItem>
                  </SelectContent>
                </Select>
              </div>
              <div className="space-y-2">
                <Label>Quantity</Label>
                <Input
                  type="number"
                  min={1}
                  value={formData.quantity}
                  onChange={(e) => setFormData({ ...formData, quantity: parseInt(e.target.value) || 1 })}
                />
              </div>
            </div>
            <div className="space-y-2">
              <Label>Blueprint (Optional)</Label>
              <Select value={formData.blueprintId} onValueChange={(v) => setFormData({ ...formData, blueprintId: v })}>
                <SelectTrigger>
                  <SelectValue placeholder="Select blueprint" />
                </SelectTrigger>
                <SelectContent>
                  {blueprints.filter(b => b.status === 'active').map((bp) => (
                    <SelectItem key={bp.id} value={bp.id}>{bp.blueprintId} - {bp.name}</SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
            <div className="space-y-2">
              <Label>Print Center (Optional)</Label>
              <Select value={formData.centerId} onValueChange={(v) => setFormData({ ...formData, centerId: v })}>
                <SelectTrigger>
                  <SelectValue placeholder="Select center" />
                </SelectTrigger>
                <SelectContent>
                  {printCenters.filter(c => c.status !== 'offline').map((center) => (
                    <SelectItem key={center.id} value={center.id}>{center.name}</SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
            <div className="space-y-2">
              <Label>Notes</Label>
              <Textarea
                placeholder="Additional instructions..."
                value={formData.notes}
                onChange={(e) => setFormData({ ...formData, notes: e.target.value })}
              />
            </div>
          </div>
          <DialogFooter>
            <Button variant="outline" onClick={() => setIsCreateOpen(false)}>Cancel</Button>
            <Button onClick={handleCreateOrder} className="bg-[#0EA5E9]">Create Order</Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>

      {/* View Order Dialog */}
      <Dialog open={isViewOpen} onOpenChange={setIsViewOpen}>
        <DialogContent className="max-w-lg">
          <DialogHeader>
            <DialogTitle>Order Details</DialogTitle>
          </DialogHeader>
          {selectedOrder && (
            <div className="space-y-4 py-4">
              <div className="flex items-center justify-between p-4 bg-slate-50 rounded-lg">
                <div>
                  <p className="font-mono text-lg font-bold text-[#0EA5E9]">{selectedOrder.orderId}</p>
                  <p className="text-sm text-slate-500">{selectedOrder.partName}</p>
                </div>
                <Badge className={statusColors[selectedOrder.status]}>
                  {statusLabels[selectedOrder.status]}
                </Badge>
              </div>
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <Label className="text-slate-500">Priority</Label>
                  <p><Badge className={priorityColors[selectedOrder.priority]}>{selectedOrder.priority}</Badge></p>
                </div>
                <div>
                  <Label className="text-slate-500">Quantity</Label>
                  <p className="font-medium">{selectedOrder.quantity}</p>
                </div>
                <div>
                  <Label className="text-slate-500">Requester</Label>
                  <p className="font-medium">{selectedOrder.requester?.name || 'Unknown'}</p>
                </div>
                <div>
                  <Label className="text-slate-500">ETA</Label>
                  <p className="font-medium">{selectedOrder.eta ? new Date(selectedOrder.eta).toLocaleDateString() : 'TBD'}</p>
                </div>
              </div>
              {selectedOrder.blueprint && (
                <div>
                  <Label className="text-slate-500">Blueprint</Label>
                  <p className="font-medium">{selectedOrder.blueprint.blueprintId} - {selectedOrder.blueprint.name}</p>
                </div>
              )}
              {selectedOrder.center && (
                <div>
                  <Label className="text-slate-500">Print Center</Label>
                  <p className="font-medium">{selectedOrder.center.name} ({selectedOrder.center.location})</p>
                </div>
              )}
              {selectedOrder.notes && (
                <div>
                  <Label className="text-slate-500">Notes</Label>
                  <p className="text-sm bg-slate-50 p-3 rounded-lg">{selectedOrder.notes}</p>
                </div>
              )}
            </div>
          )}
        </DialogContent>
      </Dialog>

      {/* Edit Order Dialog */}
      <Dialog open={isEditOpen} onOpenChange={setIsEditOpen}>
        <DialogContent className="max-w-md">
          <DialogHeader>
            <DialogTitle>Edit Order</DialogTitle>
          </DialogHeader>
          {selectedOrder && (
            <div className="space-y-4 py-4">
              <div className="space-y-2">
                <Label>Status</Label>
                <Select
                  value={selectedOrder.status}
                  onValueChange={(v) => setSelectedOrder({ ...selectedOrder, status: v })}
                >
                  <SelectTrigger>
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    {statusFlow.map((status) => (
                      <SelectItem key={status} value={status}>{statusLabels[status]}</SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>
              <div className="space-y-2">
                <Label>Priority</Label>
                <Select
                  value={selectedOrder.priority}
                  onValueChange={(v) => setSelectedOrder({ ...selectedOrder, priority: v })}
                >
                  <SelectTrigger>
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="low">Low</SelectItem>
                    <SelectItem value="medium">Medium</SelectItem>
                    <SelectItem value="high">High</SelectItem>
                  </SelectContent>
                </Select>
              </div>
              <div className="space-y-2">
                <Label>Notes</Label>
                <Textarea
                  value={selectedOrder.notes || ''}
                  onChange={(e) => setSelectedOrder({ ...selectedOrder, notes: e.target.value })}
                />
              </div>
            </div>
          )}
          <DialogFooter>
            <Button variant="outline" onClick={() => setIsEditOpen(false)}>Cancel</Button>
            <Button onClick={handleUpdateOrder} className="bg-[#0EA5E9]">Save Changes</Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </div>
  )
}
