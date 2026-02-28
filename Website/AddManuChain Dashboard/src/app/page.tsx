'use client'

// Dashboard for AddManuChain - v2
import { useState } from 'react'
import {
  Sidebar,
  Header,
  OverviewPage,
  RoleDashboard,
  OnboardingTutorial,
  useOnboarding,
  SectionTutorial,
  useSectionTutorial,
  AIAssistant,
  OrdersPage,
  BlueprintsPage,
  CentersPage,
  AnalyticsPage,
  SettingsPage,
  AuditLogPage,
  PartnersPage,
  ShipmentsPage,
  MaterialsPage,
  CertificationsPage,
  AuthoritiesPage,
  CustomerSuccessPage,
  DigitalInventoryPage,
  PrintApprovalPage,
  PhysicalInventoryPage,
  PeerPrintersPage,
  IPLibraryPage,
  LabPage,
} from '@/components/dashboard'

export default function Dashboard() {
  const [activeTab, setActiveTab] = useState('overview')
  const [mobileOpen, setMobileOpen] = useState(false)
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false)
  const [currentRole, setCurrentRole] = useState('admin')
  const { showOnboarding, isLoading, completeOnboarding } = useOnboarding()
  const { tutorialSection, showTutorial, hideTutorial, isVisible: tutorialVisible } = useSectionTutorial(activeTab)

  const getPageTitle = () => {
    switch (activeTab) {
      case 'overview':
        return { title: 'Dashboard Overview', subtitle: 'Welcome back, John' }
      case 'orders':
        return { title: 'Orders', subtitle: 'Manage and track your part orders' }
      case 'print_queue':
        return { title: 'Print Queue', subtitle: 'DRM approval pipeline — OEM & Certification Authority sign-offs' }
      case 'physical_inventory':
        return { title: 'Physical Inventory', subtitle: 'Manage physical spare parts across all sites' }
      case 'digital_inventory':
        return { title: 'Digital Inventory', subtitle: 'AI-driven parts forecasting and onsite readiness' }
      case 'blueprints':
        return { title: 'Blueprint Library', subtitle: 'Manage certified CAD blueprints' }
      case 'centers':
        return { title: 'Print Centers', subtitle: 'Monitor certified AM facilities' }
      case 'peer_printers':
        return { title: 'Peer Printers', subtitle: 'Airbnb-style peer-to-peer 3D printer network' }
      case 'shipments':
        return { title: 'Shipments', subtitle: 'Track delivery logistics' }
      case 'materials':
        return { title: 'Materials Inventory', subtitle: 'Raw material stock management' }
      case 'partners':
        return { title: 'OEM Partners', subtitle: 'Manage partner relationships' }
      case 'analytics':
        return { title: 'Analytics', subtitle: 'Performance insights and reports' }
      case 'audit':
        return { title: 'Audit Logs', subtitle: 'System activity and compliance tracking' }
      case 'certifications':
        return { title: 'Certifications', subtitle: 'Compliance and certification management' }
      case 'authorities':
        return { title: 'Certification Authorities', subtitle: 'Manage relationships with certifying bodies' }
      case 'services':
        return { title: 'Customer Success', subtitle: 'End-to-end service and training management' }
      case 'ip_library':
        return { title: 'IP Library', subtitle: 'OEM intellectual property, licensing & royalty management' }
      case 'lab_portal':
        return { title: 'Lab & Testing Portal', subtitle: 'AM testing requests, equipment scheduling & certification reports' }
      case 'settings':
        return { title: 'Settings', subtitle: 'Manage your account preferences' }
      default:
        return { title: 'Dashboard', subtitle: '' }
    }
  }

  const renderPage = () => {
    switch (activeTab) {
      case 'overview':
        return <RoleDashboard role={currentRole} />
      case 'orders':
        return <OrdersPage role={currentRole} />
      case 'print_queue':
        return <PrintApprovalPage role={currentRole} />
      case 'physical_inventory':
        return <PhysicalInventoryPage role={currentRole} />
      case 'digital_inventory':
        return <DigitalInventoryPage role={currentRole} />
      case 'blueprints':
        return <BlueprintsPage role={currentRole} />
      case 'centers':
        return <CentersPage role={currentRole} />
      case 'peer_printers':
        return <PeerPrintersPage role={currentRole} />
      case 'shipments':
        return <ShipmentsPage role={currentRole} />
      case 'materials':
        return <MaterialsPage role={currentRole} />
      case 'partners':
        return <PartnersPage role={currentRole} />
      case 'analytics':
        return <AnalyticsPage role={currentRole} />
      case 'audit':
        return <AuditLogPage role={currentRole} />
      case 'certifications':
        return <CertificationsPage role={currentRole} />
      case 'authorities':
        return <AuthoritiesPage role={currentRole} />
      case 'services':
        return <CustomerSuccessPage role={currentRole} />
      case 'ip_library':
        return <IPLibraryPage role={currentRole} />
      case 'lab_portal':
        return <LabPage role={currentRole} />
      case 'settings':
        return <SettingsPage role={currentRole} />
      default:
        return <OverviewPage />
    }
  }

  const pageInfo = getPageTitle()

  return (
    <div className="min-h-screen bg-[#F8FAFC]">
      {/* Onboarding Tutorial for first-time users */}
      {!isLoading && showOnboarding && (
        <OnboardingTutorial onComplete={completeOnboarding} />
      )}

      {/* Per-section Tutorial */}
      {!showOnboarding && (
        <SectionTutorial
          sectionId={tutorialSection ?? activeTab}
          visible={tutorialVisible}
          onClose={hideTutorial}
        />
      )}

      {/* Sidebar (mobile controlled) */}
      <Sidebar
        activeTab={activeTab}
        onTabChange={(t) => { setActiveTab(t); setMobileOpen(false); }}
        mobileOpen={mobileOpen}
        onMobileClose={() => setMobileOpen(false)}
        collapsed={sidebarCollapsed}
        onCollapsedChange={setSidebarCollapsed}
        activeRole={currentRole}
        onRoleChange={setCurrentRole}
      />

      {/* Main Content */}
      <div className={`ml-0 transition-all duration-300 ${sidebarCollapsed ? 'md:ml-20' : 'md:ml-64'}`}>
        {/* Header */}
        <Header
          title={pageInfo.title}
          subtitle={pageInfo.subtitle}
          onNavigate={setActiveTab}
          onTutorialClick={() => showTutorial(activeTab)}
          mobileOpen={mobileOpen}
          setMobileOpen={setMobileOpen}
        />

        {/* Page Content */}
        <main className="min-h-[calc(100vh-64px)]">{renderPage()}</main>
      </div>

      {/* AI Assistant floating chat widget */}
      <AIAssistant role={currentRole} />
    </div>
  )
}
