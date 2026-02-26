'use client'

import { useState } from 'react'
import { Card, CardContent } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { Progress } from '@/components/ui/progress'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Textarea } from '@/components/ui/textarea'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
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
import { Factory, Search, Plus, MapPin, Printer, CheckCircle, Clock, XCircle } from 'lucide-react'
import { toast } from 'sonner'
import { printCenters as initialCenters } from '@/lib/static-data'

const statusColors: Record<string, string> = {
  online: 'bg-[#14B8A6]/10 text-[#14B8A6]',
  busy: 'bg-[#F59E0B]/10 text-[#F59E0B]',
  offline: 'bg-slate-100 text-slate-500',
}

export function CentersPage() {
  const [centers, setCenters] = useState(initialCenters)
  const [searchQuery, setSearchQuery] = useState('')
  const [statusFilter, setStatusFilter] = useState('all')
  const [isCreateOpen, setIsCreateOpen] = useState(false)
  const [isViewOpen, setIsViewOpen] = useState(false)
  const [selectedCenter, setSelectedCenter] = useState<any>(null)
  const [formData, setFormData] = useState({
    name: '',
    location: '',
    certification: '',
    totalPrinters: 1,
    contactName: '',
    contactEmail: '',
  })
  const [onsitePlan, setOnsitePlan] = useState({
    mode: 'onsite',
    location: '',
    accessWindow: '',
    safetyRequirements: '',
    equipmentNeeds: '',
    supportContacts: '',
    notes: '',
  })

  const filteredCenters = centers.filter(center => {
    const matchesSearch = center.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         center.location.toLowerCase().includes(searchQuery.toLowerCase())
    const matchesStatus = statusFilter === 'all' || center.status === statusFilter
    return matchesSearch && matchesStatus
  })

  const stats = {
    total: centers.length,
    online: centers.filter(c => c.status === 'online').length,
    busy: centers.filter(c => c.status === 'busy').length,
    offline: centers.filter(c => c.status === 'offline').length,
    totalCapacity: Math.round(centers.reduce((sum, c) => sum + c.capacity, 0) / centers.length),
  }

  const handleCreateCenter = () => {
    if (!formData.name || !formData.location) {
      toast.error('Name and location are required')
      return
    }

    const newCenterNum = centers.length + 1
    const newCenter = {
      id: `pc-${Date.now()}`,
      centerId: `PC-00${newCenterNum}`,
      name: formData.name,
      location: formData.location,
      status: 'offline',
      certification: formData.certification || 'Pending',
      totalPrinters: formData.totalPrinters,
      activePrinters: 0,
      capacity: 0,
      currentJobs: 0,
      completedToday: 0,
      contactName: formData.contactName,
      contactEmail: formData.contactEmail,
      materials: [],
      specialties: [],
    }

    setCenters([newCenter, ...centers])
    toast.success(`Print center "${formData.name}" created successfully`)
    setIsCreateOpen(false)
    setFormData({ name: '', location: '', certification: '', totalPrinters: 1, contactName: '', contactEmail: '' })
  }

  return (
    <div className="p-3 sm:p-6 space-y-4 sm:space-y-6">
      <Tabs defaultValue="network" className="w-full">
        <TabsList className="bg-white border border-slate-200">
          <TabsTrigger value="network">Network</TabsTrigger>
          <TabsTrigger value="onsite">Onsite Printing</TabsTrigger>
        </TabsList>

        <TabsContent value="network" className="space-y-6">
          {/* Stats */}
          <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-[#0EA5E9]/10 flex items-center justify-center">
                <Factory className="w-5 h-5 text-[#0EA5E9]" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">{stats.total}</p>
                <p className="text-sm text-slate-500">Total Centers</p>
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
                <p className="text-2xl font-bold text-[#0F172A]">{stats.online}</p>
                <p className="text-sm text-slate-500">Online</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-[#F59E0B]/10 flex items-center justify-center">
                <Clock className="w-5 h-5 text-[#F59E0B]" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">{stats.busy}</p>
                <p className="text-sm text-slate-500">Busy</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-slate-100 flex items-center justify-center">
                <XCircle className="w-5 h-5 text-slate-500" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">{stats.offline}</p>
                <p className="text-sm text-slate-500">Offline</p>
              </div>
            </div>
          </CardContent>
        </Card>
        <Card className="bg-white border-slate-200">
          <CardContent className="p-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-purple-100 flex items-center justify-center">
                <Factory className="w-5 h-5 text-purple-600" />
              </div>
              <div>
                <p className="text-2xl font-bold text-[#0F172A]">{stats.totalCapacity}%</p>
                <p className="text-sm text-slate-500">Avg Capacity</p>
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
            placeholder="Search centers..."
            className="pl-10 bg-white border-slate-200"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
        </div>
        <Select value={statusFilter} onValueChange={setStatusFilter}>
          <SelectTrigger className="w-40 bg-white border-slate-200">
            <SelectValue placeholder="Status" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="all">All Status</SelectItem>
            <SelectItem value="online">Online</SelectItem>
            <SelectItem value="busy">Busy</SelectItem>
            <SelectItem value="offline">Offline</SelectItem>
          </SelectContent>
        </Select>
        <Button 
          onClick={() => setIsCreateOpen(true)}
          className="bg-[#0EA5E9] hover:bg-[#0EA5E9]/90 text-white"
        >
          <Plus className="w-4 h-4 mr-2" />
          Add Center
        </Button>
      </div>

      {/* Centers Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {filteredCenters.map((center) => (
          <Card key={center.id} className="bg-white border-slate-200 cursor-pointer hover:shadow-md transition-shadow"
            onClick={() => { setSelectedCenter(center); setIsViewOpen(true) }}>
            <CardContent className="p-4">
              <div className="flex items-start justify-between mb-4">
                <div className="flex items-center gap-3">
                  <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${
                    center.status === 'online' ? 'bg-[#14B8A6]/10' :
                    center.status === 'busy' ? 'bg-[#F59E0B]/10' : 'bg-slate-100'
                  }`}>
                    <Factory className={`w-5 h-5 ${
                      center.status === 'online' ? 'text-[#14B8A6]' :
                      center.status === 'busy' ? 'text-[#F59E0B]' : 'text-slate-500'
                    }`} />
                  </div>
                  <div>
                    <p className="font-semibold text-[#0F172A]">{center.name}</p>
                    <div className="flex items-center gap-1 text-xs text-slate-500">
                      <MapPin className="w-3 h-3" />
                      {center.location}
                    </div>
                  </div>
                </div>
                <Badge className={statusColors[center.status]}>
                  {center.status.charAt(0).toUpperCase() + center.status.slice(1)}
                </Badge>
              </div>

              <div className="space-y-3">
                <div>
                  <div className="flex items-center justify-between text-sm mb-1">
                    <span className="text-slate-500">Capacity</span>
                    <span className="font-medium text-[#0F172A]">{center.capacity}%</span>
                  </div>
                  <Progress value={center.capacity} className="h-2" />
                </div>

                <div className="grid grid-cols-3 gap-2 text-center">
                  <div className="bg-slate-50 rounded p-2">
                    <p className="text-lg font-bold text-[#0F172A]">{center.activePrinters}/{center.totalPrinters}</p>
                    <p className="text-xs text-slate-500">Printers</p>
                  </div>
                  <div className="bg-slate-50 rounded p-2">
                    <p className="text-lg font-bold text-[#0F172A]">{center.currentJobs}</p>
                    <p className="text-xs text-slate-500">Jobs</p>
                  </div>
                  <div className="bg-slate-50 rounded p-2">
                    <p className="text-lg font-bold text-[#14B8A6]">{center.completedToday}</p>
                    <p className="text-xs text-slate-500">Done</p>
                  </div>
                </div>

                <div className="pt-2 border-t border-slate-100">
                  <Badge variant="outline" className="text-xs">{center.certification}</Badge>
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Create Center Dialog */}
      <Dialog open={isCreateOpen} onOpenChange={setIsCreateOpen}>
        <DialogContent className="max-w-md">
          <DialogHeader>
            <DialogTitle>Add Print Center</DialogTitle>
            <DialogDescription>Register a new certified AM facility</DialogDescription>
          </DialogHeader>
          <div className="space-y-4 py-4">
            <div className="space-y-2">
              <Label>Center Name *</Label>
              <Input
                placeholder="e.g., Atlantic XL"
                value={formData.name}
                onChange={(e) => setFormData({ ...formData, name: e.target.value })}
              />
            </div>
            <div className="space-y-2">
              <Label>Location *</Label>
              <Input
                placeholder="e.g., Halifax, NS"
                value={formData.location}
                onChange={(e) => setFormData({ ...formData, location: e.target.value })}
              />
            </div>
            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label>Certification</Label>
                <Select value={formData.certification} onValueChange={(v) => setFormData({ ...formData, certification: v })}>
                  <SelectTrigger>
                    <SelectValue placeholder="Select..." />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="Lloyd's Register">Lloyd's Register</SelectItem>
                    <SelectItem value="DNV GL">DNV GL</SelectItem>
                    <SelectItem value="CSA">CSA</SelectItem>
                    <SelectItem value="Pending">Pending</SelectItem>
                  </SelectContent>
                </Select>
              </div>
              <div className="space-y-2">
                <Label>Total Printers</Label>
                <Input
                  type="number"
                  min={1}
                  value={formData.totalPrinters}
                  onChange={(e) => setFormData({ ...formData, totalPrinters: parseInt(e.target.value) || 1 })}
                />
              </div>
            </div>
            <div className="space-y-2">
              <Label>Contact Name</Label>
              <Input
                placeholder="Contact person"
                value={formData.contactName}
                onChange={(e) => setFormData({ ...formData, contactName: e.target.value })}
              />
            </div>
            <div className="space-y-2">
              <Label>Contact Email</Label>
              <Input
                type="email"
                placeholder="contact@center.com"
                value={formData.contactEmail}
                onChange={(e) => setFormData({ ...formData, contactEmail: e.target.value })}
              />
            </div>
          </div>
          <DialogFooter>
            <Button variant="outline" onClick={() => setIsCreateOpen(false)}>Cancel</Button>
            <Button onClick={handleCreateCenter} className="bg-[#0EA5E9]">Add Center</Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>

      {/* View Center Dialog */}
      <Dialog open={isViewOpen} onOpenChange={setIsViewOpen}>
        <DialogContent className="max-w-lg">
          <DialogHeader>
            <DialogTitle>Center Details</DialogTitle>
          </DialogHeader>
          {selectedCenter && (
            <div className="space-y-4 py-4">
              <div className="flex items-center gap-4 p-4 bg-slate-50 rounded-lg">
                <div className={`w-12 h-12 rounded-lg flex items-center justify-center ${
                  selectedCenter.status === 'online' ? 'bg-[#14B8A6]/10' :
                  selectedCenter.status === 'busy' ? 'bg-[#F59E0B]/10' : 'bg-slate-100'
                }`}>
                  <Factory className={`w-6 h-6 ${
                    selectedCenter.status === 'online' ? 'text-[#14B8A6]' :
                    selectedCenter.status === 'busy' ? 'text-[#F59E0B]' : 'text-slate-500'
                  }`} />
                </div>
                <div>
                  <p className="font-semibold text-[#0F172A]">{selectedCenter.name}</p>
                  <p className="text-sm text-slate-500">{selectedCenter.centerId} • {selectedCenter.location}</p>
                </div>
                <Badge className={statusColors[selectedCenter.status]} style={{ marginLeft: 'auto' }}>
                  {selectedCenter.status.charAt(0).toUpperCase() + selectedCenter.status.slice(1)}
                </Badge>
              </div>
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <Label className="text-slate-500">Certification</Label>
                  <p><Badge variant="outline">{selectedCenter.certification}</Badge></p>
                </div>
                <div>
                  <Label className="text-slate-500">Capacity</Label>
                  <p className="font-medium">{selectedCenter.capacity}%</p>
                </div>
                <div>
                  <Label className="text-slate-500">Active Printers</Label>
                  <p className="font-medium">{selectedCenter.activePrinters}/{selectedCenter.totalPrinters}</p>
                </div>
                <div>
                  <Label className="text-slate-500">Current Jobs</Label>
                  <p className="font-medium">{selectedCenter.currentJobs}</p>
                </div>
              </div>
              <div className="grid grid-cols-2 gap-4 pt-2 border-t">
                <div>
                  <Label className="text-slate-500">Contact</Label>
                  <p className="font-medium">{selectedCenter.contactName}</p>
                  <p className="text-sm text-slate-500">{selectedCenter.contactEmail}</p>
                </div>
                <div>
                  <Label className="text-slate-500">Completed Today</Label>
                  <p className="text-2xl font-bold text-[#14B8A6]">{selectedCenter.completedToday}</p>
                </div>
              </div>
              {selectedCenter.materials?.length > 0 && (
                <div>
                  <Label className="text-slate-500">Materials</Label>
                  <div className="flex flex-wrap gap-1 mt-1">
                    {selectedCenter.materials.map((m: string, i: number) => (
                      <Badge key={i} variant="secondary" className="text-xs">{m}</Badge>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}
        </DialogContent>
      </Dialog>
        </TabsContent>

        <TabsContent value="onsite" className="space-y-6">
          <Card className="bg-white border-slate-200">
            <CardContent className="p-6 space-y-4">
              <div>
                <h3 className="text-lg font-semibold text-[#0F172A]">Onsite Printing Engagement</h3>
                <p className="text-sm text-slate-500">
                  Define onsite requirements for rapid deployment, inspection, and certification workflows.
                </p>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="space-y-2">
                  <Label>Engagement Mode</Label>
                  <Select
                    value={onsitePlan.mode}
                    onValueChange={(value) => setOnsitePlan({ ...onsitePlan, mode: value })}
                  >
                    <SelectTrigger className="bg-white">
                      <SelectValue placeholder="Select mode" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="onsite">Onsite</SelectItem>
                      <SelectItem value="virtual">Virtual</SelectItem>
                      <SelectItem value="hybrid">Hybrid</SelectItem>
                    </SelectContent>
                  </Select>
                </div>
                <div className="space-y-2">
                  <Label>Site Location</Label>
                  <Input
                    placeholder="Platform, shipyard, or facility"
                    value={onsitePlan.location}
                    onChange={(e) => setOnsitePlan({ ...onsitePlan, location: e.target.value })}
                  />
                </div>
                <div className="space-y-2">
                  <Label>Access Window</Label>
                  <Input
                    placeholder="e.g., 2-week offshore window"
                    value={onsitePlan.accessWindow}
                    onChange={(e) => setOnsitePlan({ ...onsitePlan, accessWindow: e.target.value })}
                  />
                </div>
                <div className="space-y-2">
                  <Label>Support Contacts</Label>
                  <Input
                    placeholder="Operations lead or HSE contact"
                    value={onsitePlan.supportContacts}
                    onChange={(e) => setOnsitePlan({ ...onsitePlan, supportContacts: e.target.value })}
                  />
                </div>
                <div className="space-y-2 md:col-span-2">
                  <Label>Safety Requirements</Label>
                  <Textarea
                    rows={3}
                    placeholder="Induction, certifications, PPE, safety protocols"
                    value={onsitePlan.safetyRequirements}
                    onChange={(e) => setOnsitePlan({ ...onsitePlan, safetyRequirements: e.target.value })}
                  />
                </div>
                <div className="space-y-2 md:col-span-2">
                  <Label>Equipment & Facility Needs</Label>
                  <Textarea
                    rows={3}
                    placeholder="Power, ventilation, QA tools, storage, network access"
                    value={onsitePlan.equipmentNeeds}
                    onChange={(e) => setOnsitePlan({ ...onsitePlan, equipmentNeeds: e.target.value })}
                  />
                </div>
                <div className="space-y-2 md:col-span-2">
                  <Label>Notes</Label>
                  <Textarea
                    rows={3}
                    placeholder="Additional onsite coordination notes"
                    value={onsitePlan.notes}
                    onChange={(e) => setOnsitePlan({ ...onsitePlan, notes: e.target.value })}
                  />
                </div>
              </div>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  )
}
