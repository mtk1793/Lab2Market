'use client'

import { useState } from 'react'
import {
  FlaskConical,
  Microscope,
  Beaker,
  TestTubeDiagonal,
  FileText,
  CheckCircle2,
  Clock,
  AlertTriangle,
  Upload,
  Download,
  Plus,
  Search,
  ChevronDown,
  X,
  BarChart3,
  Shield,
  Layers,
  Thermometer,
  Gauge,
  ClipboardList,
} from 'lucide-react'

// ─── Types ────────────────────────────────────────────────────────────────────

type TestStatus = 'pending' | 'in_progress' | 'passed' | 'failed' | 'review'
type TestType = 'mechanical' | 'chemical' | 'thermal' | 'dimensional' | 'ndt' | 'fatigue'

interface TestRequest {
  id: string
  partName: string
  partNumber: string
  submittedBy: string
  organization: string
  testTypes: TestType[]
  priority: 'standard' | 'expedited' | 'critical'
  status: TestStatus
  submittedDate: string
  dueDate: string
  technician: string
  sampleCount: number
  certRequired: string
}

interface Equipment {
  id: string
  name: string
  type: string
  status: 'available' | 'in_use' | 'maintenance' | 'offline'
  nextAvailable?: string
  currentJob?: string
  utilization: number
}

interface TestReport {
  id: string
  partName: string
  partNumber: string
  testDate: string
  result: 'pass' | 'fail' | 'conditional'
  issuer: string
  certStandard: string
  fileReady: boolean
}

// ─── Mock Data ────────────────────────────────────────────────────────────────

const mockTestRequests: TestRequest[] = [
  {
    id: 'TR-2026-041',
    partName: 'Pump Impeller — Marine Grade',
    partNumber: 'WRT-PI-3300',
    submittedBy: 'Johann Weber',
    organization: 'Wärtsilä Marine OEM',
    testTypes: ['mechanical', 'dimensional', 'ndt'],
    priority: 'critical',
    status: 'in_progress',
    submittedDate: 'Feb 24, 2026',
    dueDate: 'Mar 3, 2026',
    technician: 'Dr. Ahmad Osman',
    sampleCount: 3,
    certRequired: 'DNV GL',
  },
  {
    id: 'TR-2026-038',
    partName: 'Shaft Seal Assembly',
    partNumber: 'RR-SS-770B',
    submittedBy: 'OEM Portal',
    organization: 'Rolls-Royce Power Systems',
    testTypes: ['mechanical', 'thermal', 'fatigue'],
    priority: 'expedited',
    status: 'pending',
    submittedDate: 'Feb 25, 2026',
    dueDate: 'Mar 5, 2026',
    technician: 'Unassigned',
    sampleCount: 5,
    certRequired: "Lloyd's Register",
  },
  {
    id: 'TR-2026-035',
    partName: 'Valve Body — High Pressure',
    partNumber: 'CAT-VB-1120',
    submittedBy: 'PolyUnity NL',
    organization: 'Print Facility',
    testTypes: ['dimensional', 'chemical'],
    priority: 'standard',
    status: 'review',
    submittedDate: 'Feb 20, 2026',
    dueDate: 'Mar 1, 2026',
    technician: 'Li Wei',
    sampleCount: 2,
    certRequired: 'ISO 9001',
  },
  {
    id: 'TR-2026-031',
    partName: 'Heat Exchanger Fin Array',
    partNumber: 'SIE-HEX-550',
    submittedBy: 'Capt. Sarah Leblanc',
    organization: 'Horizon Maritime',
    testTypes: ['thermal', 'dimensional'],
    priority: 'standard',
    status: 'passed',
    submittedDate: 'Feb 15, 2026',
    dueDate: 'Feb 22, 2026',
    technician: 'Dr. Ahmad Osman',
    sampleCount: 4,
    certRequired: 'Bureau Veritas',
  },
  {
    id: 'TR-2026-028',
    partName: 'Rudder Bearing Housing',
    partNumber: 'MAN-RB-800X',
    submittedBy: 'OEM Portal',
    organization: 'MAN Energy Solutions',
    testTypes: ['mechanical', 'ndt', 'fatigue'],
    priority: 'expedited',
    status: 'failed',
    submittedDate: 'Feb 10, 2026',
    dueDate: 'Feb 18, 2026',
    technician: 'Li Wei',
    sampleCount: 3,
    certRequired: 'ClassNK',
  },
]

const mockEquipment: Equipment[] = [
  {
    id: 'EQ-001',
    name: 'Instron 5985 UTM',
    type: 'Tensile / Compression',
    status: 'in_use',
    currentJob: 'TR-2026-041',
    utilization: 82,
  },
  {
    id: 'EQ-002',
    name: 'Zeiss CMM Contura',
    type: 'Coordinate Measurement',
    status: 'available',
    utilization: 45,
  },
  {
    id: 'EQ-003',
    name: 'Industrial CT Scanner',
    type: 'Non-Destructive Testing',
    status: 'in_use',
    currentJob: 'TR-2026-038',
    utilization: 91,
  },
  {
    id: 'EQ-004',
    name: 'DSC 3+ Calorimeter',
    type: 'Thermal Analysis',
    status: 'available',
    utilization: 33,
  },
  {
    id: 'EQ-005',
    name: 'SEM / EDS Hitachi SU5000',
    type: 'Surface & Chemical Analysis',
    status: 'maintenance',
    nextAvailable: 'Mar 2, 2026',
    utilization: 0,
  },
  {
    id: 'EQ-006',
    name: 'MTS 810 Fatigue Tester',
    type: 'Fatigue / Cyclic Loading',
    status: 'available',
    utilization: 60,
  },
]

const mockReports: TestReport[] = [
  {
    id: 'RPT-2026-031',
    partName: 'Heat Exchanger Fin Array',
    partNumber: 'SIE-HEX-550',
    testDate: 'Feb 22, 2026',
    result: 'pass',
    issuer: 'Dr. Ahmad Osman',
    certStandard: 'Bureau Veritas',
    fileReady: true,
  },
  {
    id: 'RPT-2026-028',
    partName: 'Rudder Bearing Housing',
    partNumber: 'MAN-RB-800X',
    testDate: 'Feb 18, 2026',
    result: 'fail',
    issuer: 'Li Wei',
    certStandard: 'ClassNK',
    fileReady: true,
  },
  {
    id: 'RPT-2026-025',
    partName: 'Turbocharger Rotor',
    partNumber: 'MAN-TCR-330',
    testDate: 'Feb 12, 2026',
    result: 'conditional',
    issuer: 'Dr. Ahmad Osman',
    certStandard: 'DNV GL',
    fileReady: true,
  },
]

// ─── Helpers ──────────────────────────────────────────────────────────────────

const testTypeLabel: Record<TestType, string> = {
  mechanical: 'Mechanical',
  chemical: 'Chemical',
  thermal: 'Thermal',
  dimensional: 'Dimensional',
  ndt: 'NDT',
  fatigue: 'Fatigue',
}

const testTypeColor: Record<TestType, string> = {
  mechanical: 'bg-blue-100 text-blue-700',
  chemical: 'bg-purple-100 text-purple-700',
  thermal: 'bg-orange-100 text-orange-700',
  dimensional: 'bg-teal-100 text-teal-700',
  ndt: 'bg-pink-100 text-pink-700',
  fatigue: 'bg-red-100 text-red-700',
}

const statusConfig: Record<TestStatus, { label: string; color: string; icon: React.ReactNode }> = {
  pending: {
    label: 'Pending',
    color: 'bg-slate-100 text-slate-600',
    icon: <Clock className="w-3.5 h-3.5" />,
  },
  in_progress: {
    label: 'In Progress',
    color: 'bg-blue-100 text-blue-700',
    icon: <FlaskConical className="w-3.5 h-3.5" />,
  },
  review: {
    label: 'Under Review',
    color: 'bg-amber-100 text-amber-700',
    icon: <AlertTriangle className="w-3.5 h-3.5" />,
  },
  passed: {
    label: 'Passed',
    color: 'bg-green-100 text-green-700',
    icon: <CheckCircle2 className="w-3.5 h-3.5" />,
  },
  failed: {
    label: 'Failed',
    color: 'bg-red-100 text-red-700',
    icon: <X className="w-3.5 h-3.5" />,
  },
}

const eqStatusConfig = {
  available: { label: 'Available', color: 'bg-green-100 text-green-700', dot: 'bg-green-500' },
  in_use: { label: 'In Use', color: 'bg-blue-100 text-blue-700', dot: 'bg-blue-500' },
  maintenance: { label: 'Maintenance', color: 'bg-amber-100 text-amber-700', dot: 'bg-amber-500' },
  offline: { label: 'Offline', color: 'bg-red-100 text-red-700', dot: 'bg-red-500' },
}

const priorityBadge = {
  critical: 'bg-red-100 text-red-700 border border-red-200',
  expedited: 'bg-amber-100 text-amber-700 border border-amber-200',
  standard: 'bg-slate-100 text-slate-600 border border-slate-200',
}

// ─── Main Component ───────────────────────────────────────────────────────────

export function LabPage({ role = 'admin' }: { role?: string }) {
  const [activeTab, setActiveTab] = useState<'requests' | 'equipment' | 'reports'>('requests')
  const [searchQuery, setSearchQuery] = useState('')
  const [filterStatus, setFilterStatus] = useState<string>('all')
  const [showNewTestDialog, setShowNewTestDialog] = useState(false)
  const [showReportDialog, setShowReportDialog] = useState<TestReport | null>(null)

  // Stats
  const total = mockTestRequests.length
  const inProgress = mockTestRequests.filter(r => r.status === 'in_progress').length
  const pendingCount = mockTestRequests.filter(r => r.status === 'pending').length
  const passedCount = mockTestRequests.filter(r => r.status === 'passed').length
  const eqAvailable = mockEquipment.filter(e => e.status === 'available').length

  const filteredRequests = mockTestRequests.filter(r => {
    const matchSearch =
      !searchQuery ||
      r.partName.toLowerCase().includes(searchQuery.toLowerCase()) ||
      r.partNumber.toLowerCase().includes(searchQuery.toLowerCase()) ||
      r.organization.toLowerCase().includes(searchQuery.toLowerCase())
    const matchStatus = filterStatus === 'all' || r.status === filterStatus
    return matchSearch && matchStatus
  })

  return (
    <div className="p-6 max-w-[1400px] mx-auto space-y-6">

      {/* ── Header Banner ───────────────────────────────────────────────── */}
      <div className="rounded-xl bg-gradient-to-r from-emerald-900 via-teal-800 to-emerald-900 p-6 text-white">
        <div className="flex items-center gap-3 mb-2">
          <div className="p-2 bg-white/10 rounded-lg">
            <FlaskConical className="w-6 h-6" />
          </div>
          <div>
            <h2 className="text-xl font-bold">Lab & Testing Portal</h2>
            <p className="text-emerald-200 text-sm">Additive Manufacturing Test Facility — Dalhousie University</p>
          </div>
        </div>
        <div className="mt-4 grid grid-cols-2 md:grid-cols-4 gap-3">
          {[
            { label: 'Active Tests', value: inProgress, icon: <FlaskConical className="w-4 h-4" />, color: 'text-blue-200' },
            { label: 'Pending Requests', value: pendingCount, icon: <Clock className="w-4 h-4" />, color: 'text-amber-200' },
            { label: 'Passed This Month', value: passedCount, icon: <CheckCircle2 className="w-4 h-4" />, color: 'text-green-200' },
            { label: 'Equipment Available', value: `${eqAvailable}/${mockEquipment.length}`, icon: <Gauge className="w-4 h-4" />, color: 'text-purple-200' },
          ].map(stat => (
            <div key={stat.label} className="bg-white/10 rounded-lg p-3">
              <div className={`flex items-center gap-1.5 text-xs mb-1 ${stat.color}`}>
                {stat.icon}
                <span>{stat.label}</span>
              </div>
              <p className="text-2xl font-bold">{stat.value}</p>
            </div>
          ))}
        </div>
      </div>

      {/* ── Tabs ────────────────────────────────────────────────────────── */}
      <div className="flex items-center gap-1 bg-slate-100 p-1 rounded-lg w-fit">
        {[
          { key: 'requests', label: 'Test Requests', icon: <ClipboardList className="w-4 h-4" /> },
          { key: 'equipment', label: 'Equipment', icon: <Gauge className="w-4 h-4" /> },
          { key: 'reports', label: 'Test Reports', icon: <FileText className="w-4 h-4" /> },
        ].map(tab => (
          <button
            key={tab.key}
            onClick={() => setActiveTab(tab.key as typeof activeTab)}
            className={`flex items-center gap-2 px-4 py-2 rounded-md text-sm font-medium transition-all ${
              activeTab === tab.key
                ? 'bg-white text-emerald-700 shadow-sm'
                : 'text-slate-500 hover:text-slate-700'
            }`}
          >
            {tab.icon}
            {tab.label}
            {tab.key === 'requests' && pendingCount > 0 && (
              <span className="bg-amber-500 text-white text-xs rounded-full px-1.5 py-0.5 leading-none">
                {pendingCount}
              </span>
            )}
          </button>
        ))}
      </div>

      {/* ── Test Requests Tab ────────────────────────────────────────────── */}
      {activeTab === 'requests' && (
        <div className="space-y-4">
          {/* Toolbar */}
          <div className="flex flex-col sm:flex-row gap-3 items-start sm:items-center justify-between">
            <div className="flex gap-2 flex-wrap">
              <div className="relative">
                <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
                <input
                  type="text"
                  placeholder="Search part / org..."
                  value={searchQuery}
                  onChange={e => setSearchQuery(e.target.value)}
                  className="pl-9 pr-4 py-2 text-sm border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-400 w-56"
                />
              </div>
              <select
                value={filterStatus}
                onChange={e => setFilterStatus(e.target.value)}
                className="px-3 py-2 text-sm border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-400"
              >
                <option value="all">All Statuses</option>
                <option value="pending">Pending</option>
                <option value="in_progress">In Progress</option>
                <option value="review">Under Review</option>
                <option value="passed">Passed</option>
                <option value="failed">Failed</option>
              </select>
            </div>
            <button
              onClick={() => setShowNewTestDialog(true)}
              className="flex items-center gap-2 px-4 py-2 bg-emerald-600 text-white text-sm rounded-lg hover:bg-emerald-700 transition-colors"
            >
              <Plus className="w-4 h-4" />
              New Test Request
            </button>
          </div>

          {/* Request Cards */}
          <div className="space-y-3">
            {filteredRequests.map(req => {
              const st = statusConfig[req.status]
              return (
                <div key={req.id} className="bg-white border border-slate-100 rounded-xl p-5 hover:shadow-md transition-shadow">
                  <div className="flex flex-col lg:flex-row lg:items-start justify-between gap-4">
                    {/* Left */}
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center gap-2 flex-wrap mb-1">
                        <span className="text-xs font-mono text-slate-400">{req.id}</span>
                        <span className={`inline-flex items-center gap-1 text-xs font-medium px-2 py-0.5 rounded-full ${st.color}`}>
                          {st.icon} {st.label}
                        </span>
                        <span className={`text-xs px-2 py-0.5 rounded-full font-medium capitalize ${priorityBadge[req.priority]}`}>
                          {req.priority}
                        </span>
                      </div>
                      <h3 className="font-semibold text-slate-800 text-base">{req.partName}</h3>
                      <p className="text-sm text-slate-500 mb-2">
                        <span className="font-mono">{req.partNumber}</span> · {req.organization}
                        {' '}· Submitted by <span className="font-medium">{req.submittedBy}</span>
                      </p>
                      {/* Test type badges */}
                      <div className="flex flex-wrap gap-1.5 mb-2">
                        {req.testTypes.map(t => (
                          <span key={t} className={`text-xs px-2 py-0.5 rounded-full font-medium ${testTypeColor[t]}`}>
                            {testTypeLabel[t]}
                          </span>
                        ))}
                      </div>
                      <div className="flex gap-4 text-xs text-slate-500 flex-wrap">
                        <span>Samples: <strong>{req.sampleCount}</strong></span>
                        <span>Cert: <strong>{req.certRequired}</strong></span>
                        <span>Technician: <strong>{req.technician}</strong></span>
                      </div>
                    </div>
                    {/* Right — dates */}
                    <div className="flex flex-col gap-1 text-xs text-slate-500 text-right shrink-0">
                      <span>Submitted: <strong className="text-slate-700">{req.submittedDate}</strong></span>
                      <span>Due: <strong className="text-slate-700">{req.dueDate}</strong></span>
                      <div className="flex gap-2 mt-2 justify-end">
                        {req.status === 'pending' && (
                          <button className="px-3 py-1.5 text-xs bg-emerald-50 text-emerald-700 border border-emerald-200 rounded-lg hover:bg-emerald-100 transition-colors">
                            Assign & Start
                          </button>
                        )}
                        {req.status === 'in_progress' && (
                          <button className="px-3 py-1.5 text-xs bg-blue-50 text-blue-700 border border-blue-200 rounded-lg hover:bg-blue-100 transition-colors">
                            Log Results
                          </button>
                        )}
                        {req.status === 'review' && (
                          <button className="px-3 py-1.5 text-xs bg-amber-50 text-amber-700 border border-amber-200 rounded-lg hover:bg-amber-100 transition-colors">
                            Finalize Report
                          </button>
                        )}
                        {(req.status === 'passed' || req.status === 'failed') && (
                          <button className="px-3 py-1.5 text-xs bg-slate-50 text-slate-600 border border-slate-200 rounded-lg hover:bg-slate-100 transition-colors">
                            View Report
                          </button>
                        )}
                      </div>
                    </div>
                  </div>
                </div>
              )
            })}
            {filteredRequests.length === 0 && (
              <div className="text-center py-12 text-slate-400">
                <FlaskConical className="w-10 h-10 mx-auto mb-2 opacity-30" />
                <p>No test requests match your filters.</p>
              </div>
            )}
          </div>
        </div>
      )}

      {/* ── Equipment Tab ────────────────────────────────────────────────── */}
      {activeTab === 'equipment' && (
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
          {mockEquipment.map(eq => {
            const st = eqStatusConfig[eq.status]
            return (
              <div key={eq.id} className="bg-white border border-slate-100 rounded-xl p-5 hover:shadow-md transition-shadow">
                <div className="flex items-start justify-between mb-3">
                  <div className="p-2 bg-emerald-50 rounded-lg">
                    <Microscope className="w-5 h-5 text-emerald-700" />
                  </div>
                  <span className={`inline-flex items-center gap-1.5 text-xs font-medium px-2.5 py-1 rounded-full ${st.color}`}>
                    <span className={`w-1.5 h-1.5 rounded-full ${st.dot}`} />
                    {st.label}
                  </span>
                </div>
                <h3 className="font-semibold text-slate-800 mb-1">{eq.name}</h3>
                <p className="text-xs text-slate-500 mb-3">{eq.type}</p>

                {/* Utilization bar */}
                <div className="mb-3">
                  <div className="flex justify-between text-xs text-slate-500 mb-1">
                    <span>Monthly utilization</span>
                    <span className="font-medium">{eq.utilization}%</span>
                  </div>
                  <div className="h-1.5 bg-slate-100 rounded-full overflow-hidden">
                    <div
                      className={`h-full rounded-full transition-all ${
                        eq.utilization > 80 ? 'bg-red-400' :
                        eq.utilization > 60 ? 'bg-amber-400' : 'bg-emerald-500'
                      }`}
                      style={{ width: `${eq.utilization}%` }}
                    />
                  </div>
                </div>

                {eq.currentJob && (
                  <p className="text-xs text-blue-600 font-medium">
                    Current job: {eq.currentJob}
                  </p>
                )}
                {eq.nextAvailable && (
                  <p className="text-xs text-amber-600 font-medium">
                    Next available: {eq.nextAvailable}
                  </p>
                )}
                {eq.status === 'available' && (
                  <button className="mt-3 w-full py-1.5 text-xs bg-emerald-50 text-emerald-700 border border-emerald-200 rounded-lg hover:bg-emerald-100 transition-colors">
                    Reserve Equipment
                  </button>
                )}
              </div>
            )
          })}
        </div>
      )}

      {/* ── Reports Tab ──────────────────────────────────────────────────── */}
      {activeTab === 'reports' && (
        <div className="space-y-3">
          <div className="flex items-center justify-between mb-2">
            <p className="text-sm text-slate-500">
              {mockReports.length} completed test reports
            </p>
            <button className="flex items-center gap-2 px-3 py-1.5 text-xs bg-white border border-slate-200 rounded-lg hover:bg-slate-50 transition-colors">
              <Upload className="w-3.5 h-3.5" />
              Upload Raw Data
            </button>
          </div>
          {mockReports.map(rpt => (
            <div key={rpt.id} className="bg-white border border-slate-100 rounded-xl p-5 flex items-center justify-between">
              <div className="flex items-center gap-4">
                <div className={`p-2 rounded-lg ${
                  rpt.result === 'pass' ? 'bg-green-50' :
                  rpt.result === 'fail' ? 'bg-red-50' : 'bg-amber-50'
                }`}>
                  {rpt.result === 'pass' && <CheckCircle2 className="w-5 h-5 text-green-600" />}
                  {rpt.result === 'fail' && <X className="w-5 h-5 text-red-600" />}
                  {rpt.result === 'conditional' && <AlertTriangle className="w-5 h-5 text-amber-600" />}
                </div>
                <div>
                  <div className="flex items-center gap-2 mb-0.5">
                    <span className="text-xs font-mono text-slate-400">{rpt.id}</span>
                    <span className={`text-xs font-semibold px-2 py-0.5 rounded-full ${
                      rpt.result === 'pass' ? 'bg-green-100 text-green-700' :
                      rpt.result === 'fail' ? 'bg-red-100 text-red-700' :
                      'bg-amber-100 text-amber-700'
                    }`}>
                      {rpt.result === 'pass' ? 'PASS' : rpt.result === 'fail' ? 'FAIL' : 'CONDITIONAL'}
                    </span>
                  </div>
                  <h3 className="font-semibold text-slate-800">{rpt.partName}</h3>
                  <p className="text-xs text-slate-500">
                    {rpt.partNumber} · {rpt.certStandard} · Issued by {rpt.issuer} · {rpt.testDate}
                  </p>
                </div>
              </div>
              <div className="flex gap-2">
                <button
                  onClick={() => setShowReportDialog(rpt)}
                  className="px-3 py-1.5 text-xs bg-slate-50 text-slate-600 border border-slate-200 rounded-lg hover:bg-slate-100 transition-colors"
                >
                  Preview
                </button>
                {rpt.fileReady && (
                  <button className="flex items-center gap-1.5 px-3 py-1.5 text-xs bg-emerald-50 text-emerald-700 border border-emerald-200 rounded-lg hover:bg-emerald-100 transition-colors">
                    <Download className="w-3.5 h-3.5" />
                    PDF
                  </button>
                )}
              </div>
            </div>
          ))}
        </div>
      )}

      {/* ── New Test Request Dialog ───────────────────────────────────────── */}
      {showNewTestDialog && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-2xl shadow-2xl w-full max-w-lg max-h-[90vh] overflow-y-auto">
            <div className="flex items-center justify-between p-6 border-b border-slate-100">
              <div className="flex items-center gap-3">
                <div className="p-2 bg-emerald-50 rounded-lg">
                  <FlaskConical className="w-5 h-5 text-emerald-600" />
                </div>
                <div>
                  <h3 className="font-semibold text-slate-800">New Test Request</h3>
                  <p className="text-xs text-slate-500">Submit a part sample for AM testing & certification</p>
                </div>
              </div>
              <button onClick={() => setShowNewTestDialog(false)} className="text-slate-400 hover:text-slate-600">
                <X className="w-5 h-5" />
              </button>
            </div>
            <div className="p-6 space-y-4">
              <div>
                <label className="block text-xs font-medium text-slate-600 mb-1.5">Part Name</label>
                <input type="text" placeholder="e.g. Pump Impeller — Marine Grade" className="w-full px-3 py-2 text-sm border border-slate-200 rounded-lg focus:ring-2 focus:ring-emerald-400 outline-none" />
              </div>
              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block text-xs font-medium text-slate-600 mb-1.5">Part Number</label>
                  <input type="text" placeholder="OEM part number" className="w-full px-3 py-2 text-sm border border-slate-200 rounded-lg focus:ring-2 focus:ring-emerald-400 outline-none" />
                </div>
                <div>
                  <label className="block text-xs font-medium text-slate-600 mb-1.5">Sample Count</label>
                  <input type="number" min={1} defaultValue={1} className="w-full px-3 py-2 text-sm border border-slate-200 rounded-lg focus:ring-2 focus:ring-emerald-400 outline-none" />
                </div>
              </div>
              <div>
                <label className="block text-xs font-medium text-slate-600 mb-1.5">Test Types Required</label>
                <div className="flex flex-wrap gap-2">
                  {(Object.keys(testTypeLabel) as TestType[]).map(t => (
                    <label key={t} className="flex items-center gap-1.5 cursor-pointer">
                      <input type="checkbox" className="rounded text-emerald-600" />
                      <span className={`text-xs px-2 py-0.5 rounded-full cursor-pointer ${testTypeColor[t]}`}>
                        {testTypeLabel[t]}
                      </span>
                    </label>
                  ))}
                </div>
              </div>
              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block text-xs font-medium text-slate-600 mb-1.5">Priority</label>
                  <select className="w-full px-3 py-2 text-sm border border-slate-200 rounded-lg focus:ring-2 focus:ring-emerald-400 outline-none">
                    <option value="standard">Standard</option>
                    <option value="expedited">Expedited</option>
                    <option value="critical">Critical</option>
                  </select>
                </div>
                <div>
                  <label className="block text-xs font-medium text-slate-600 mb-1.5">Cert Standard</label>
                  <select className="w-full px-3 py-2 text-sm border border-slate-200 rounded-lg focus:ring-2 focus:ring-emerald-400 outline-none">
                    <option>DNV GL</option>
                    <option>Lloyd&apos;s Register</option>
                    <option>Bureau Veritas</option>
                    <option>ClassNK</option>
                    <option>ABS</option>
                    <option>ISO 9001</option>
                  </select>
                </div>
              </div>
              <div>
                <label className="block text-xs font-medium text-slate-600 mb-1.5">Upload Sample Data / Blueprint</label>
                <div className="border-2 border-dashed border-slate-200 rounded-xl p-4 text-center text-sm text-slate-400 hover:border-emerald-300 transition-colors cursor-pointer">
                  <Upload className="w-6 h-6 mx-auto mb-1 opacity-40" />
                  <p>Drag & drop or click to upload</p>
                  <p className="text-xs mt-0.5">.pdf, .step, .stl, .xlsx</p>
                </div>
              </div>
              <div>
                <label className="block text-xs font-medium text-slate-600 mb-1.5">Notes</label>
                <textarea rows={3} placeholder="Special handling requirements, material grade, printing parameters..." className="w-full px-3 py-2 text-sm border border-slate-200 rounded-lg focus:ring-2 focus:ring-emerald-400 outline-none resize-none" />
              </div>
            </div>
            <div className="flex gap-3 p-6 pt-0">
              <button onClick={() => setShowNewTestDialog(false)} className="flex-1 py-2.5 border border-slate-200 text-slate-600 text-sm rounded-lg hover:bg-slate-50 transition-colors">
                Cancel
              </button>
              <button onClick={() => setShowNewTestDialog(false)} className="flex-1 py-2.5 bg-emerald-600 text-white text-sm rounded-lg hover:bg-emerald-700 transition-colors font-medium">
                Submit Request
              </button>
            </div>
          </div>
        </div>
      )}

      {/* ── Report Preview Dialog ─────────────────────────────────────────── */}
      {showReportDialog && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-2xl shadow-2xl w-full max-w-md">
            <div className="flex items-center justify-between p-6 border-b border-slate-100">
              <h3 className="font-semibold text-slate-800">Test Report: {showReportDialog.id}</h3>
              <button onClick={() => setShowReportDialog(null)} className="text-slate-400 hover:text-slate-600">
                <X className="w-5 h-5" />
              </button>
            </div>
            <div className="p-6 space-y-3 text-sm">
              <div className="flex justify-between">
                <span className="text-slate-500">Part Name</span>
                <span className="font-medium text-slate-800">{showReportDialog.partName}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-500">Part Number</span>
                <span className="font-mono text-slate-700">{showReportDialog.partNumber}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-500">Test Date</span>
                <span className="text-slate-700">{showReportDialog.testDate}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-500">Cert Standard</span>
                <span className="text-slate-700">{showReportDialog.certStandard}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-500">Issuing Technician</span>
                <span className="text-slate-700">{showReportDialog.issuer}</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-slate-500">Result</span>
                <span className={`font-bold px-3 py-1 rounded-full text-sm ${
                  showReportDialog.result === 'pass' ? 'bg-green-100 text-green-700' :
                  showReportDialog.result === 'fail' ? 'bg-red-100 text-red-700' :
                  'bg-amber-100 text-amber-700'
                }`}>
                  {showReportDialog.result.toUpperCase()}
                </span>
              </div>
            </div>
            <div className="flex gap-3 p-6 pt-0">
              <button onClick={() => setShowReportDialog(null)} className="flex-1 py-2.5 border border-slate-200 text-slate-600 text-sm rounded-lg hover:bg-slate-50">
                Close
              </button>
              <button className="flex-1 flex items-center justify-center gap-2 py-2.5 bg-emerald-600 text-white text-sm rounded-lg hover:bg-emerald-700 font-medium">
                <Download className="w-4 h-4" />
                Download PDF
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
