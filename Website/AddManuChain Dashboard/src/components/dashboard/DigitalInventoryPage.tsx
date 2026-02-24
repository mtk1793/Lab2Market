'use client'

import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import {
  Sparkles,
  Cpu,
  Database,
  Shield,
  Printer,
  Wrench,
  MapPin,
  Factory,
  Layers,
  Activity,
  CheckCircle2,
  ArrowRight,
  Users,
} from 'lucide-react'

const aiCapabilities = [
  {
    title: 'Failure Prediction and Demand Forecasting',
    detail: 'Models learn from maintenance logs, sensor data, and historical orders to predict which parts will fail next.',
  },
  {
    title: 'Risk-Weighted Stocking',
    detail: 'Auto-ranks parts by downtime cost, lead time, and criticality to create a digital safety stock queue.',
  },
  {
    title: 'Capacity-Aware Routing',
    detail: 'Matches jobs to certified centers based on queue depth, materials, and compliance requirements.',
  },
  {
    title: 'Continuous Compliance Checks',
    detail: 'Flags expiring certifications, missing QA steps, and OEM IP restrictions before manufacturing begins.',
  },
]

const aiKpis = [
  {
    label: 'Forecast Accuracy',
    value: '85%+',
    note: 'Critical parts demand',
    icon: Sparkles,
  },
  {
    label: 'Downtime Risk Reduction',
    value: '60-80%',
    note: 'Across priority assets',
    icon: Activity,
  },
  {
    label: 'Routing Match Time',
    value: '< 5 min',
    note: 'Certified capacity match',
    icon: Cpu,
  },
  {
    label: 'Compliance Coverage',
    value: '100%',
    note: 'Automated checks',
    icon: Shield,
  },
]

const deploymentChecklist = [
  { label: 'Site induction approved', status: 'ready' },
  { label: 'Power + ventilation validated', status: 'ready' },
  { label: 'Material batch certification logged', status: 'in_progress' },
  { label: 'QA tooling calibrated', status: 'ready' },
  { label: 'Network + telemetry link verified', status: 'in_progress' },
  { label: 'Onsite safety briefing completed', status: 'ready' },
]

const onsiteCapabilities = [
  {
    title: 'Rapid Emergency Fabrication',
    detail: 'Print critical spares onsite to reduce downtime during offshore incidents or storm windows.',
  },
  {
    title: 'Tooling and Retrofit Production',
    detail: 'Produce jigs, fixtures, brackets, and retrofit parts for fast maintenance turnaround.',
  },
  {
    title: 'In-Situ QA and Inspection',
    detail: 'Capture inspections, dimensional checks, and certificates directly into the digital inventory record.',
  },
  {
    title: 'Material Qualification and Traceability',
    detail: 'Track powder batches, build parameters, and QA outcomes for every part produced onsite.',
  },
  {
    title: 'Remote Operations Sync',
    detail: 'Stream telemetry to the main dashboard for real-time job status and inventory usage updates.',
  },
  {
    title: 'Mobile Print Cell Deployment',
    detail: 'Support containerized or portable printers that can be shipped to yards or platforms on demand.',
  },
  {
    title: 'Operator Enablement and Training',
    detail: 'Provide onsite coaching, SOPs, and QA playbooks to keep production aligned with certification standards.',
  },
  {
    title: 'Reverse Engineering Support',
    detail: 'Capture field measurements and scan data to rebuild legacy parts into certified digital blueprints.',
  },
  {
    title: 'Material Reuse and Waste Tracking',
    detail: 'Track powder reuse ratios and scrap volumes to improve sustainability reporting.',
  },
  {
    title: 'Environmental Control Monitoring',
    detail: 'Monitor humidity, temperature, and vibration for stable onsite print quality.',
  },
]

const platformFeatures = [
  {
    title: 'Digital Blueprint Vault',
    detail: 'Version-controlled CAD files with OEM permissions and certification metadata.',
    icon: Layers,
  },
  {
    title: 'Smart Order Orchestration',
    detail: 'One-click ordering with automated approvals and compliance routing.',
    icon: Factory,
  },
  {
    title: 'Real-Time Inventory Analytics',
    detail: 'Dashboards for stock risk, lead-time savings, and carbon impact.',
    icon: Activity,
  },
  {
    title: 'Secure Audit Trail',
    detail: 'Immutable logs for every blueprint access, print job, and QA sign-off.',
    icon: Shield,
  },
]

const warehouseProfiles = [
  {
    key: 'operator',
    label: 'Operator',
    industry: 'Offshore Oil & Gas',
    highlights: [
      { label: 'Critical Parts Queue', value: '148 items' },
      { label: 'Assets Covered', value: '12 rigs' },
      { label: 'Avg. Response SLA', value: '36 hrs' },
      { label: 'Onsite Printers', value: '4 mobile cells' },
    ],
    notes: 'Focus on uptime protection, emergency spares, and rapid offshore response.',
  },
  {
    key: 'oem',
    label: 'OEM Partner',
    industry: 'Marine Propulsion',
    highlights: [
      { label: 'Certified Blueprints', value: '320 files' },
      { label: 'IP Licenses Active', value: '48 agreements' },
      { label: 'Quality Alerts', value: '2 open' },
      { label: 'Preferred Centers', value: '9 partners' },
    ],
    notes: 'Focus on IP governance, certification compliance, and royalty tracking.',
  },
  {
    key: 'print',
    label: 'Print Center',
    industry: 'Certified AM Network',
    highlights: [
      { label: 'Queued Jobs', value: '26 builds' },
      { label: 'Material SKUs', value: '18 batches' },
      { label: 'Utilization', value: '82%' },
      { label: 'QA Pass Rate', value: '97%' },
    ],
    notes: 'Focus on capacity, material availability, and compliance readiness.',
  },
  {
    key: 'authority',
    label: 'Cert Authority',
    industry: 'Regulatory Compliance',
    highlights: [
      { label: 'Audits Scheduled', value: '6' },
      { label: 'Cert Renewals', value: '14 pending' },
      { label: 'Inspection Logs', value: '1,240' },
      { label: 'Nonconformities', value: '3 open' },
    ],
    notes: 'Focus on inspection traceability, renewals, and compliance evidence.',
  },
]

export function DigitalInventoryPage() {
  return (
    <div className="p-6 space-y-6">
      <Card className="bg-white border-slate-200">
        <CardContent className="p-6">
          <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
            <div>
              <div className="flex items-center gap-2 text-sm text-slate-500">
                <Sparkles className="w-4 h-4 text-[#0EA5E9]" />
                Digital Inventory Command Center
              </div>
              <h2 className="text-2xl font-bold text-[#0F172A] mt-1">AI-Driven Digital Inventory</h2>
              <p className="text-slate-600 mt-2 max-w-2xl">
                Centralize certified blueprints, predictive demand signals, and onsite printer capabilities to deliver
                mission-critical parts in days, not weeks.
              </p>
            </div>
            <div className="flex flex-wrap gap-2">
              <Badge className="bg-[#0EA5E9]/10 text-[#0EA5E9]">AI Routing</Badge>
              <Badge className="bg-[#14B8A6]/10 text-[#14B8A6]">Onsite Printers</Badge>
              <Badge className="bg-[#F59E0B]/10 text-[#F59E0B]">Certified Network</Badge>
            </div>
          </div>
        </CardContent>
      </Card>

      <Tabs defaultValue="ai" className="w-full">
        <TabsList className="bg-white border border-slate-200">
          <TabsTrigger value="ai">AI Engine</TabsTrigger>
          <TabsTrigger value="onsite">Inside Printers</TabsTrigger>
          <TabsTrigger value="features">Platform Features</TabsTrigger>
        </TabsList>

        <TabsContent value="ai" className="space-y-4">
          <Card className="bg-white border-slate-200">
            <CardHeader>
              <CardTitle className="text-lg font-semibold text-[#0F172A]">AI Engine Overview</CardTitle>
            </CardHeader>
            <CardContent className="grid grid-cols-1 lg:grid-cols-2 gap-4">
              <div className="rounded-xl border border-slate-200 bg-slate-50 p-4">
                <div className="flex items-center gap-2">
                  <Cpu className="w-4 h-4 text-[#0EA5E9]" />
                  <p className="font-semibold text-[#0F172A]">Prediction Pipeline</p>
                </div>
                <p className="text-sm text-slate-600 mt-2">
                  Ingests equipment telemetry, failure reports, and purchase history to predict demand spikes.
                </p>
              </div>
              <div className="rounded-xl border border-slate-200 bg-slate-50 p-4">
                <div className="flex items-center gap-2">
                  <Database className="w-4 h-4 text-[#14B8A6]" />
                  <p className="font-semibold text-[#0F172A]">Digital Safety Stock</p>
                </div>
                <p className="text-sm text-slate-600 mt-2">
                  Maintains a virtual inventory queue that triggers prints only when risk thresholds are met.
                </p>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-white border-slate-200">
            <CardHeader>
              <CardTitle className="text-lg font-semibold text-[#0F172A]">AI Performance KPIs</CardTitle>
            </CardHeader>
            <CardContent className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              {aiKpis.map((kpi) => (
                <div key={kpi.label} className="rounded-xl border border-slate-200 bg-slate-50 p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-xs text-slate-500">{kpi.label}</p>
                      <p className="text-2xl font-bold text-[#0F172A]">{kpi.value}</p>
                      <p className="text-xs text-slate-500 mt-1">{kpi.note}</p>
                    </div>
                    <div className="w-10 h-10 rounded-lg bg-white border border-slate-200 flex items-center justify-center">
                      <kpi.icon className="w-5 h-5 text-[#0EA5E9]" />
                    </div>
                  </div>
                </div>
              ))}
            </CardContent>
          </Card>

          <Card className="bg-white border-slate-200">
            <CardHeader>
              <CardTitle className="text-lg font-semibold text-[#0F172A]">AI Workflow</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-3">
                <div className="flex-1 rounded-xl border border-slate-200 bg-slate-50 p-3 text-center">
                  <p className="text-xs text-slate-500">Signal Ingest</p>
                  <p className="text-sm font-semibold text-[#0F172A]">Telemetry + Logs</p>
                </div>
                <ArrowRight className="w-4 h-4 text-slate-400 hidden lg:block" />
                <div className="flex-1 rounded-xl border border-slate-200 bg-slate-50 p-3 text-center">
                  <p className="text-xs text-slate-500">Modeling</p>
                  <p className="text-sm font-semibold text-[#0F172A]">Predict Failures</p>
                </div>
                <ArrowRight className="w-4 h-4 text-slate-400 hidden lg:block" />
                <div className="flex-1 rounded-xl border border-slate-200 bg-slate-50 p-3 text-center">
                  <p className="text-xs text-slate-500">Prioritize</p>
                  <p className="text-sm font-semibold text-[#0F172A]">Risk Queue</p>
                </div>
                <ArrowRight className="w-4 h-4 text-slate-400 hidden lg:block" />
                <div className="flex-1 rounded-xl border border-slate-200 bg-slate-50 p-3 text-center">
                  <p className="text-xs text-slate-500">Route</p>
                  <p className="text-sm font-semibold text-[#0F172A]">Certified Match</p>
                </div>
                <ArrowRight className="w-4 h-4 text-slate-400 hidden lg:block" />
                <div className="flex-1 rounded-xl border border-slate-200 bg-slate-50 p-3 text-center">
                  <p className="text-xs text-slate-500">Verify</p>
                  <p className="text-sm font-semibold text-[#0F172A]">QA + Audit</p>
                </div>
              </div>
              <div className="mt-3 text-xs text-slate-500">
                Workflow output feeds the digital inventory dashboard and triggers onsite printer readiness when required.
              </div>
            </CardContent>
          </Card>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {aiCapabilities.map((item) => (
              <Card key={item.title} className="bg-white border-slate-200">
                <CardContent className="p-4 space-y-2">
                  <div className="flex items-center gap-2">
                    <CheckCircle2 className="w-4 h-4 text-[#14B8A6]" />
                    <p className="font-semibold text-[#0F172A]">{item.title}</p>
                  </div>
                  <p className="text-sm text-slate-600">{item.detail}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </TabsContent>

        <TabsContent value="onsite" className="space-y-4">
          <Card className="bg-white border-slate-200">
            <CardHeader>
              <CardTitle className="text-lg font-semibold text-[#0F172A]">Field Deployment Checklist</CardTitle>
            </CardHeader>
            <CardContent className="grid grid-cols-1 md:grid-cols-2 gap-3">
              {deploymentChecklist.map((item) => (
                <div key={item.label} className="flex items-center justify-between rounded-xl border border-slate-200 bg-slate-50 p-3">
                  <div className="flex items-center gap-2">
                    <CheckCircle2 className="w-4 h-4 text-[#14B8A6]" />
                    <span className="text-sm text-slate-700">{item.label}</span>
                  </div>
                  <Badge className={item.status === 'ready' ? 'bg-[#14B8A6]/10 text-[#14B8A6]' : 'bg-[#F59E0B]/10 text-[#F59E0B]'}>
                    {item.status === 'ready' ? 'Ready' : 'In Progress'}
                  </Badge>
                </div>
              ))}
            </CardContent>
          </Card>

          <Card className="bg-white border-slate-200">
            <CardHeader>
              <CardTitle className="text-lg font-semibold text-[#0F172A]">Inside Printers and Onsite Operations</CardTitle>
            </CardHeader>
            <CardContent className="grid grid-cols-1 lg:grid-cols-2 gap-4">
              <div className="rounded-xl border border-slate-200 bg-slate-50 p-4">
                <div className="flex items-center gap-2">
                  <Printer className="w-4 h-4 text-[#0EA5E9]" />
                  <p className="font-semibold text-[#0F172A]">Printer Deployment Zones</p>
                </div>
                <p className="text-sm text-slate-600 mt-2">
                  Shipyards, offshore platforms, and fabrication yards can host mobile print cells with secure
                  access to certified blueprints.
                </p>
              </div>
              <div className="rounded-xl border border-slate-200 bg-slate-50 p-4">
                <div className="flex items-center gap-2">
                  <MapPin className="w-4 h-4 text-[#F59E0B]" />
                  <p className="font-semibold text-[#0F172A]">Logistics and Access</p>
                </div>
                <p className="text-sm text-slate-600 mt-2">
                  Track access windows, safety approvals, and equipment staging for every onsite engagement.
                </p>
              </div>
            </CardContent>
          </Card>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {onsiteCapabilities.map((item) => (
              <Card key={item.title} className="bg-white border-slate-200">
                <CardContent className="p-4 space-y-2">
                  <div className="flex items-center gap-2">
                    <Wrench className="w-4 h-4 text-[#0EA5E9]" />
                    <p className="font-semibold text-[#0F172A]">{item.title}</p>
                  </div>
                  <p className="text-sm text-slate-600">{item.detail}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </TabsContent>

        <TabsContent value="features" className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {platformFeatures.map((item) => (
              <Card key={item.title} className="bg-white border-slate-200">
                <CardContent className="p-4 space-y-2">
                  <div className="flex items-center gap-2">
                    <item.icon className="w-4 h-4 text-[#14B8A6]" />
                    <p className="font-semibold text-[#0F172A]">{item.title}</p>
                  </div>
                  <p className="text-sm text-slate-600">{item.detail}</p>
                </CardContent>
              </Card>
            ))}
          </div>

          <Card className="bg-white border-slate-200">
            <CardHeader>
              <CardTitle className="text-lg font-semibold text-[#0F172A]">Digital Inventory Warehouse Profiles</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <Tabs defaultValue="operator" className="w-full">
                <TabsList className="bg-slate-50 border border-slate-200">
                  {warehouseProfiles.map((profile) => (
                    <TabsTrigger key={profile.key} value={profile.key}>{profile.label}</TabsTrigger>
                  ))}
                </TabsList>
                {warehouseProfiles.map((profile) => (
                  <TabsContent key={profile.key} value={profile.key} className="space-y-4">
                    <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-3">
                      <div>
                        <div className="flex items-center gap-2 text-sm text-slate-500">
                          <Users className="w-4 h-4 text-[#0EA5E9]" />
                          {profile.label} Warehouse
                        </div>
                        <h4 className="text-lg font-semibold text-[#0F172A]">{profile.industry}</h4>
                        <p className="text-sm text-slate-600 mt-1">{profile.notes}</p>
                      </div>
                      <Badge className="bg-[#0EA5E9]/10 text-[#0EA5E9]">Active Profile</Badge>
                    </div>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                      {profile.highlights.map((item) => (
                        <div key={item.label} className="rounded-xl border border-slate-200 bg-slate-50 p-3">
                          <p className="text-xs text-slate-500">{item.label}</p>
                          <p className="text-lg font-semibold text-[#0F172A]">{item.value}</p>
                        </div>
                      ))}
                    </div>
                  </TabsContent>
                ))}
              </Tabs>
            </CardContent>
          </Card>

          <Card className="bg-white border-slate-200">
            <CardHeader>
              <CardTitle className="text-lg font-semibold text-[#0F172A]">Inventory Workflow</CardTitle>
            </CardHeader>
            <CardContent className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="rounded-xl border border-slate-200 bg-slate-50 p-4">
                <div className="flex items-center gap-2">
                  <Sparkles className="w-4 h-4 text-[#0EA5E9]" />
                  <p className="font-semibold text-[#0F172A]">Predict</p>
                </div>
                <p className="text-sm text-slate-600 mt-2">
                  AI monitors risk signals and builds a prioritized digital stock queue.
                </p>
              </div>
              <div className="rounded-xl border border-slate-200 bg-slate-50 p-4">
                <div className="flex items-center gap-2">
                  <Factory className="w-4 h-4 text-[#14B8A6]" />
                  <p className="font-semibold text-[#0F172A]">Print</p>
                </div>
                <p className="text-sm text-slate-600 mt-2">
                  Certified centers or onsite printers execute the build with full QA traceability.
                </p>
              </div>
              <div className="rounded-xl border border-slate-200 bg-slate-50 p-4">
                <div className="flex items-center gap-2">
                  <Shield className="w-4 h-4 text-[#0F172A]" />
                  <p className="font-semibold text-[#0F172A]">Verify</p>
                </div>
                <p className="text-sm text-slate-600 mt-2">
                  Inspection data and certifications sync back into the digital inventory record.
                </p>
              </div>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  )
}
