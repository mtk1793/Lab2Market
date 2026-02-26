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
import { FileBox, Search, Filter, Plus, Eye, Edit, Trash2, Package, Layers, Building } from 'lucide-react'
import { toast } from 'sonner'
import { blueprints as initialBlueprints } from '@/lib/static-data'

const statusColors: Record<string, string> = {
  active: 'bg-[#14B8A6]/10 text-[#14B8A6]',
  pending_review: 'bg-[#F59E0B]/10 text-[#F59E0B]',
  inactive: 'bg-slate-100 text-slate-500',
}

const statusLabels: Record<string, string> = {
  active: 'Active',
  pending_review: 'Pending Review',
  inactive: 'Inactive',
}

export function BlueprintsPage() {
  const [blueprints, setBlueprints] = useState(initialBlueprints)
  const [searchQuery, setSearchQuery] = useState('')
  const [statusFilter, setStatusFilter] = useState('all')
  const [categoryFilter, setCategoryFilter] = useState('all')
  const [isViewOpen, setIsViewOpen] = useState(false)
  const [selectedBlueprint, setSelectedBlueprint] = useState<any>(null)

  const categories = [...new Set(blueprints.map(b => b.category))]

  const filteredBlueprints = blueprints.filter(bp => {
    const matchesSearch = bp.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         bp.blueprintId.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         bp.oem.toLowerCase().includes(searchQuery.toLowerCase())
    const matchesStatus = statusFilter === 'all' || bp.status === statusFilter
    const matchesCategory = categoryFilter === 'all' || bp.category === categoryFilter
    return matchesSearch && matchesStatus && matchesCategory
  })

  const stats = {
    total: blueprints.length,
    active: blueprints.filter(b => b.status === 'active').length,
    pendingReview: blueprints.filter(b => b.status === 'pending_review').length,
    totalPrints: blueprints.reduce((sum, b) => sum + b.printCount, 0),
  }

  return (
    <div className="p-3 sm:p-6 space-y-4 sm:space-y-6">
      {/* Stats */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-[#0EA5E9]/10 flex items-center justify-center">
                <FileBox className="w-5 h-5 text-[#0EA5E9]" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">{stats.total}</p>
                <p className="text-sm text-slate-500">Total Blueprints</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-[#14B8A6]/10 flex items-center justify-center">
                <Layers className="w-5 h-5 text-[#14B8A6]" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">{stats.active}</p>
                <p className="text-sm text-slate-500">Active</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-[#F59E0B]/10 flex items-center justify-center">
                <FileBox className="w-5 h-5 text-[#F59E0B]" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">{stats.pendingReview}</p>
                <p className="text-sm text-slate-500">Pending Review</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-purple-100 flex items-center justify-center">
                <Package className="w-5 h-5 text-purple-600" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">{stats.totalPrints}</p>
                <p className="text-sm text-slate-500">Total Prints</p>
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
            placeholder="Search blueprints..."
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
            <SelectItem value="active">Active</SelectItem>
            <SelectItem value="pending_review">Pending Review</SelectItem>
            <SelectItem value="inactive">Inactive</SelectItem>
          </SelectContent>
        </Select>
        <Select value={categoryFilter} onValueChange={setCategoryFilter}>
          <SelectTrigger className="w-40 bg-white border-slate-200">
            <SelectValue placeholder="Category" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="all">All Categories</SelectItem>
            {categories.map((cat) => (
              <SelectItem key={cat} value={cat}>{cat}</SelectItem>
            ))}
          </SelectContent>
        </Select>
      </div>

      {/* Blueprints Table */}
      <Card className="bg-white border-slate-200">
        <CardContent className="p-0">
          <Table>
            <TableHeader>
              <TableRow className="bg-slate-50">
                <TableHead className="font-semibold text-[#0F172A]">Blueprint</TableHead>
                <TableHead className="font-semibold text-[#0F172A]">Category</TableHead>
                <TableHead className="font-semibold text-[#0F172A]">Material</TableHead>
                <TableHead className="font-semibold text-[#0F172A]">OEM</TableHead>
                <TableHead className="font-semibold text-[#0F172A]">Certification</TableHead>
                <TableHead className="font-semibold text-[#0F172A]">Status</TableHead>
                <TableHead className="font-semibold text-[#0F172A]">Prints</TableHead>
                <TableHead className="font-semibold text-[#0F172A]">Actions</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {filteredBlueprints.map((blueprint) => (
                <TableRow key={blueprint.id} className="hover:bg-slate-50">
                  <TableCell>
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 rounded-lg bg-[#0F172A] flex items-center justify-center">
                        <FileBox className="w-5 h-5 text-white" />
                      </div>
                      <div>
                        <p className="font-mono text-sm text-[#0EA5E9]">{blueprint.blueprintId}</p>
                        <p className="font-medium text-[#0F172A]">{blueprint.name}</p>
                      </div>
                    </div>
                  </TableCell>
                  <TableCell className="text-slate-600">{blueprint.category}</TableCell>
                  <TableCell className="text-slate-600">{blueprint.material}</TableCell>
                  <TableCell className="text-slate-600">{blueprint.oem}</TableCell>
                  <TableCell>
                    <Badge variant="outline" className="text-xs">{blueprint.certification}</Badge>
                  </TableCell>
                  <TableCell>
                    <Badge className={statusColors[blueprint.status]}>
                      {statusLabels[blueprint.status]}
                    </Badge>
                  </TableCell>
                  <TableCell className="font-medium text-[#0F172A]">{blueprint.printCount}</TableCell>
                  <TableCell>
                    <Button
                      variant="ghost"
                      size="icon"
                      className="h-8 w-8"
                      onClick={() => {
                        setSelectedBlueprint(blueprint)
                        setIsViewOpen(true)
                      }}
                    >
                      <Eye className="w-4 h-4" />
                    </Button>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>

      {/* View Blueprint Dialog */}
      <Dialog open={isViewOpen} onOpenChange={setIsViewOpen}>
        <DialogContent className="max-w-lg">
          <DialogHeader>
            <DialogTitle>Blueprint Details</DialogTitle>
          </DialogHeader>
          {selectedBlueprint && (
            <div className="space-y-4 py-4">
              <div className="flex items-center gap-4 p-4 bg-slate-50 rounded-lg">
                <div className="w-12 h-12 rounded-lg bg-[#0F172A] flex items-center justify-center">
                  <FileBox className="w-6 h-6 text-white" />
                </div>
                <div>
                  <p className="font-mono text-sm text-[#0EA5E9]">{selectedBlueprint.blueprintId}</p>
                  <p className="font-semibold text-[#0F172A]">{selectedBlueprint.name}</p>
                </div>
              </div>
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <Label className="text-slate-500">Category</Label>
                  <p className="font-medium">{selectedBlueprint.category}</p>
                </div>
                <div>
                  <Label className="text-slate-500">Material</Label>
                  <p className="font-medium">{selectedBlueprint.material}</p>
                </div>
                <div>
                  <Label className="text-slate-500">OEM</Label>
                  <p className="font-medium">{selectedBlueprint.oem}</p>
                </div>
                <div>
                  <Label className="text-slate-500">Certification</Label>
                  <p className="font-medium">{selectedBlueprint.certification}</p>
                </div>
                <div>
                  <Label className="text-slate-500">Status</Label>
                  <p><Badge className={statusColors[selectedBlueprint.status]}>{statusLabels[selectedBlueprint.status]}</Badge></p>
                </div>
                <div>
                  <Label className="text-slate-500">Print Count</Label>
                  <p className="font-medium">{selectedBlueprint.printCount}</p>
                </div>
              </div>
              {selectedBlueprint.description && (
                <div>
                  <Label className="text-slate-500">Description</Label>
                  <p className="text-sm bg-slate-50 p-3 rounded-lg">{selectedBlueprint.description}</p>
                </div>
              )}
            </div>
          )}
        </DialogContent>
      </Dialog>
    </div>
  )
}
